import streamlit as st

st.title("📏 Unit Converter")
st.markdown("🔄 Convert units quickly and easily!")


value = st.number_input("Enter the value to convert")
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

st.markdown("""<style>
    .stTextInput, .stNumberInput input{
        border-radius: 10px;
        padding: 10px;
        background-color: #f4f1f1;
        color: black;  /* Set font color to black */
    }
    .stButton button {
        border-radius: 10px;
        background-color: #00244c;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border: none;
    }
    .stButton button:hover {
        background-color: #0056b3;
        color:#fff;
    }
    .stSuccess {
        background-color: #e6ffed;
        color: #155724;
        padding: 10px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    .st.markdown{
        background-color: B88E2F;
        color: #155724;
        padding: 10px
    }
    </style>
    """, unsafe_allow_html=True)


def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
            
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
    
    return 0  # Default return if no conversion is selected
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Miles to Kilometers","Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

if st.button("♾️ Convert Now", use_container_width=True):
    result = convert_units(category, value, unit)
    st.success(f"✅ The result is **{result:.2f}**")


st.markdown("---")
st.markdown("<p style='text-align:center;'>🚀 Developed by <b>Abdul Haseeb Shaikh</b></p>", unsafe_allow_html=True)