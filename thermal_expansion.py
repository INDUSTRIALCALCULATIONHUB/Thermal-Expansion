import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Thermal Expansion Calculator",
    page_icon="📏",
    layout="centered"
)

# Initialize Session State
if "result" not in st.session_state:
    st.session_state.result = None

# Title
st.title("📏 Thermal Expansion Calculator")

# Material Database
coefficients = {
    "Steel": 11.2e-6,
    "Stainless Steel": 17.3e-6,
    "Aluminium": 23.0e-6,
    "Cast Iron": 10.8e-6,
    "Copper": 16.5e-6
}

# Input Fields
material = st.selectbox(
    "Material",
    ["Select Material"] + list(coefficients.keys())
)

length = st.text_input(
    "Length (mm)",
    value="",
    placeholder="Enter Length in mm"
)

delta_temp = st.text_input(
    "Temperature Difference (°C)",
    value="",
    placeholder="Enter Temperature Difference"
)

# Buttons
col1, col2 = st.columns(2)

with col1:
    calculate = st.button("Calculate")

with col2:
    reset = st.button("Reset")

# Reset Logic
if reset:
    st.session_state.clear()
    st.rerun()

# Calculate Logic
if calculate:

    if material == "Select Material":
        st.error("Please select a material.")

    elif length.strip() == "" or delta_temp.strip() == "":
        st.error("Please enter all required values.")

    else:
        try:
            length_value = float(length)
            delta_temp_value = float(delta_temp)

            alpha = coefficients[material]

            expansion = alpha * length_value * delta_temp_value

            st.session_state.result = {
                "material": material,
                "length": length_value,
                "delta_temp": delta_temp_value,
                "expansion": expansion
            }

        except ValueError:
            st.error("Please enter valid numeric values.")

# Display Result
if st.session_state.result is not None:

    result = st.session_state.result

    st.subheader("Result")

    st.write(f"**Material:** {result['material']}")
    st.write(f"**Length:** {result['length']:.2f} mm")
    st.write(f"**Temperature Difference:** {result['delta_temp']:.2f} °C")
    st.write(f"**Thermal Expansion:** {result['expansion']:.2f} mm")