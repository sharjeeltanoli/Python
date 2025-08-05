import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Trade Calculator", page_icon="📈")

st.title("📈 Leverage Trade Calculator")
st.markdown("Enter your trade details below. Calculates position size, required capital, exposure, and optional profit.")

st.divider()

# --- Input Fields in Form ---
with st.form("trade_form"):
    col1, col2 = st.columns(2)

    with col1:
        direction = st.selectbox("Trade Direction", ["long", "short"])
        entry_price = st.number_input("Entry Price", min_value=0.0001, format="%.4f")
        stop_loss = st.number_input("Stop Loss Price", min_value=0.0001, format="%.4f")
        take_profit = st.number_input("Take Profit Price (optional)", min_value=0.0000, format="%.4f", value=0.0000)

    with col2:
        risk_amount = st.number_input("Risk Amount ($)", min_value=0.01, format="%.2f")
        leverage = st.number_input("Leverage (e.g. 10, 20, 50)", min_value=1, step=1)

    # ✅ Submit button inside form
    submitted = st.form_submit_button("🔍 Calculate")

# --- Calculation Logic ---
def calculate_trade(entry, sl, risk, lev, direction, tp=None):
    if direction == "long" and sl >= entry:
        raise ValueError("For a long trade, Stop Loss must be below Entry Price.")
    if direction == "short" and sl <= entry:
        raise ValueError("For a short trade, Stop Loss must be above Entry Price.")
    if entry == sl:
        raise ValueError("Entry and Stop Loss cannot be the same.")

    price_diff = abs(entry - sl)
    position_size = risk / price_diff
    notional_value = position_size * entry
    required_margin = notional_value / lev
    total_exposure = notional_value

    # Optional TP calculations
    reward = None
    rrr = None
    profit = None

    if tp and tp > 0:
        if direction == "long" and tp <= entry:
            raise ValueError("Take Profit must be above entry for a long trade.")
        if direction == "short" and tp >= entry:
            raise ValueError("Take Profit must be below entry for a short trade.")
        reward = abs(tp - entry) * position_size
        rrr = reward / risk
        profit = reward

    return position_size, required_margin, total_exposure, reward, rrr, profit

# --- Display Results ---
if submitted:
    try:
        size, margin, exposure, reward, rrr, profit = calculate_trade(
            entry_price, stop_loss, risk_amount, leverage, direction, take_profit
        )

        st.success("✅ Calculation Successful")

        st.markdown(f"""
        ### 📊 Trade Metrics:
        - 🔢 **Position Size**: `{size:.4f}` units
        - 💼 **Required Capital (Margin)**: `${margin:.2f}`
        - 💥 **Total Exposure (Trade Value)**: `${exposure:.2f}`
        - ⚖️ **Leverage Used**: `{leverage}x`
        """)

        if take_profit > 0:
            st.markdown(f"""
            ### 🎯 Profit Target:
            - 📈 **Take Profit Price**: `{take_profit}`
            - 💰 **Potential Profit**: `${profit:.2f}`
            - 🧮 **Risk–Reward Ratio (RRR)**: `{rrr:.2f}`
            """)

    except Exception as e:
        st.error(f"❌ Error: {e}")
