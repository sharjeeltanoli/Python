import streamlit as st
st.title("Unit Converter")

#Distance Fuctionality
def distance(from_unit, to_unit, value):
    unit = {"Meter": 1, "Kilometer": 1000, "Feet": 0.3048, "Miles": 1609.34}
    result = value * unit[from_unit] / unit[to_unit]
    return result

#Temperature Fuctionality
def temperature(from_unit, to_unit, value):
     if from_unit == to_unit:  # Handling same unit conversion
        return value
     elif from_unit == "Celsius" and to_unit == "Fahrenheit":
         result = (value * 9/5) + 32
     elif from_unit == "Celsius" and to_unit == "Kelvin":
         result = value + 273.15
     elif from_unit == "Fahrenheit" and to_unit == "Celsius":
         result = (value - 32) * 5/9
     elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
         result = (value - 32) * 5/9 + 273.15
     elif from_unit == "Kelvin" and to_unit == "Celsius":
         result = value - 273.15
     elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
         result = (value - 273.15) * 9/5 + 32
     return result

#Weight Fuctionality
def weight(from_unit, to_unit, value):
    unit = {"Gram": 1, "Kilogram": 1000, "Pound": 453.592, "Ounce": 28.3495}
    result = value * unit[from_unit] / unit[to_unit]
    return result

#Pressure Fuctionality
def pressure(from_unit, to_unit, value):
    unit = {"Pascal": 1, "Bar": 100000, "Atmosphere": 101325, "Torr": 133.322}
    result = value * unit[from_unit] / unit[to_unit]
    return result

#Time Fuctionality
def time(from_unit, to_unit, value):
    unit = {"Milisecond": 1, "Second": 1000, "Minute": 60000, "Hour": 3600000, "Day": 86400000, "Week": 604800000, "Month": 2628000000, "Year": 31540000000}
    result = value * unit[from_unit] / unit[to_unit]
    return result


#Main Code
category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure", "Time"])

if category == "Distance":
    from_unit = st.selectbox("From", ["Meter", "Kilometer", "Feet", "Miles"])
    to_unit = st.selectbox("To", ["Meter", "Kilometer", "Feet", "Miles"])    
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = distance(from_unit, to_unit, value)   
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = temperature(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", ["Gram", "Kilogram", "Pound", "Ounce"])
    to_unit = st.selectbox("To", ["Gram", "Kilogram", "Pound", "Ounce"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = weight(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Pressure":
    from_unit = st.selectbox("From", ["Pascal", "Bar", "Atmosphere", "Torr"])
    to_unit = st.selectbox("To", ["Pascal", "Bar", "Atmosphere", "Torr"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = pressure(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Time":
    from_unit = st.selectbox("From", ["Milisecond", "Second", "Minute", "Hour", "Day", "Week", "Month", "Year"])
    to_unit = st.selectbox("To", ["Milisecond", "Second", "Minute", "Hour", "Day", "Week", "Month", "Year"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = time(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
