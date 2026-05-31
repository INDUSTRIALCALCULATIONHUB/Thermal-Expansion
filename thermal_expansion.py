import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Thermal Expansion Calculator",
    page_icon="📏",
    layout="centered"
)

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

# Material Selection
material = st.selectbox(
    "Material",
    options=["Select Material"] + list(coefficients.keys()),
    index=0
)

# Length Input
length = st.text_input(
    "Length (mm)",
    placeholder="Enter Length in mm"
)

# Temperature Input
delta_temp = st.text_input(
    "Temperature Difference (°C)",
    placeholder="Enter Temperature Difference"
)

# Calculate Automatically
if (
    material != "Select Material"
    and length.strip() != ""
    and delta_temp.strip() != ""
):
    try:
        length = float(length)
        delta_temp = float(delta_temp)

        alpha = coefficients[material]
        expansion = alpha * length * delta_temp

        st.subheader("Result")

        st.write(f"**Material:** {material}")
        st.write(f"**Length:** {length:,.2f} mm")
        st.write(f"**Temperature Difference:** {delta_temp:,.2f} °C")
        st.write(f"**Thermal Expansion:** {expansion:.2f} mm")

    except ValueError:
        st.error("Please enter valid numeric values.")