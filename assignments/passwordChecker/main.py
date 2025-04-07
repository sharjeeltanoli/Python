import streamlit as st
import re

# Web app title and icon
st.set_page_config(page_title="Password Checker", page_icon="🔒")

# Header Section
st.markdown("""
    <div style="text-align: center;"> 
        <h1 style="font-size: 3rem;">🔒 Password Strength Checker</h1>
        <p style="font-size: 1.3rem;">Check how strong your password is 💪</p>
        <p style="font-size: 1rem;">
            Our tool analyzes the strength of your password based on length, use of symbols, numbers, and uppercase letters.
        </p>
    </div>
""", unsafe_allow_html=True)

# Section for Password Input
st.header("🔑 Enter Password")
password = st.text_input("Enter your password", type="password", placeholder="Type your password here")

# Password Strength Criteria
score = 0
feedback = []

# Section for Password Analysis
if password:
    st.header("👁‍🗨 Password Analysis")

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    # for adding Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one **lowercase letter**.")

    # for adding Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one **uppercase letter**.")

    # for adding Digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one **number**.")

    # for adding Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Use at least one **special character** (e.g: , !, @, #, etc.)")

    # Overall Strength Result
    st.subheader("📊 Result")
    if score == 5:
        st.success("✅ Your password is **Strong**! 🔐")
    elif score >= 3:
        st.warning("⚠️ Your password is **Moderate**. Consider improving it.")
    else:
        st.error("❌ Your password is **Weak**. Please follow the suggestions below.")

    # Show Suggestions
    if feedback:
        st.subheader("💡 Suggestions to Improve Your Password")
        for suggestion in feedback:
            st.write(suggestion)

else:
    st.info("ℹ️ Please enter a password above to check its strength.")
