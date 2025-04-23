import streamlit as st

def converts_units(value , unit_from , unit_to):
    conversions = {
        "meter_kilometer" : 0.001,
        "kilometer_meter" : 1,
        "gram_kilogram" : 0.001,
        "kilogram_gram" : 1000
    }

    key = f"{unit_from}_{unit_to}" #Generate a key based on the input and output units

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"
    
st.title("Unit Converter")

value = st.number_input("Enter the Value:", min_value=1 , step=1)

unit_from = st.selectbox("Convert From:", ["meter" , "kilometer" , "gram" , "kilogram"])

unit_to = st.selectbox("Convert To:", ["meter" , "kilometer" , "gram" , "kilogram"])

if st.button("Convert"):
    result = converts_units(value , unit_from , unit_to)
    st.write(f"Converted Value: {result}")