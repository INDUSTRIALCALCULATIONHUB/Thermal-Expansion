import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Thermal Expansion Calculator",
    page_icon="📏",
    layout="centered"
)

st.title("📏 Thermal Expansion Calculator")

# Material Database
coefficients = {
    "Steel": 11.2e-6,
    "Stainless Steel": 17.3e-6,
    "Aluminium": 23.0e-6,
    "Cast Iron": 10.8e-6,
    "Copper": 16.5e-6
}

# Initialize Session State
if "material" not in st.session_state:
    st.session_state.material = "Select Material"

if "length" not in st.session_state:
    st.session_state.length = ""

if "delta_temp" not in st.session_state:
    st.session_state.delta_temp = ""

# Inputs
material = st.selectbox(
    "Material",
    options=["Select Material"] + list(coefficients.keys()),
    key="material"
)

length = st.text_input(
    "Length (mm)",
    placeholder="Enter Length in mm",
    key="length"
)

delta_temp = st.text_input(
    "Temperature Difference (°C)",
    placeholder="Enter Temperature Difference",
    key="delta_temp"
)

# Buttons
col1, col2 = st.columns(2)

with col1:
    calculate = st.button("Calculate")

with col2:
    reset = st.button("Reset")

# Reset Logic
if reset:
    st.session_state.material = "Select Material"
    st.session_state.length = ""
    st.session_state.delta_temp = ""
    st.rerun()

# Calculate Logic
if calculate:

    if material == "Select Material":
        st.error("Please select a material.")

    elif length.strip() == "" or delta_temp.strip() == "":
        st.error("Please enter all input values.")

    else:
        try:
            length_value = float(length)
            delta_temp_value = float(delta_temp)

            alpha = coefficients[material]

            expansion = (
                alpha
                * length_value
                * delta_temp_value
            )

            st.subheader("Result")

            st.write(f"**Material:** {material}")
            st.write(f"**Length:** {length_value:,.2f} mm")
            st.write(
                f"**Temperature Difference:** "
                f"{delta_temp_value:,.2f} °C"
            )
            st.write(
                f"**Thermal Expansion:** "
                f"{expansion:.2f} mm"
            )

        except ValueError:
            st.error(
                "Please enter valid numeric values."
            )