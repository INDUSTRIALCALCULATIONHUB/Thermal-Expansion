import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Thermal Expansion Calculator",
    page_icon="📏",
    layout="centered"
)

# Initialize Session State
if "material" not in st.session_state:
    st.session_state.material = "Select Material"

if "length" not in st.session_state:
    st.session_state.length = ""

if "delta_temp" not in st.session_state:
    st.session_state.delta_temp = ""

if "result" not in st.session_state:
    st.session_state.result = None

# Reset Function
def reset_form():
    st.session_state.material = "Select Material"
    st.session_state.length = ""
    st.session_state.delta_temp = ""
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

# Inputs
st.selectbox(
    "Material",
    ["Select Material"] + list(coefficients.keys()),
    key="material"
)

st.text_input(
    "Length (mm)",
    placeholder="Enter Length in mm",
    key="length"
)

st.text_input(
    "Temperature Difference (°C)",
    placeholder="Enter Temperature Difference",
    key="delta_temp"
)

# Buttons
col1, col2 = st.columns(2)

with col1:
    calculate = st.button("Calculate")

with col2:
    st.button("Reset", on_click=reset_form)

# Calculate
if calculate:

    if st.session_state.material == "Select Material":
        st.error("Please select a material.")

    elif (
        st.session_state.length.strip() == ""
        or st.session_state.delta_temp.strip() == ""
    ):
        st.error("Please enter all required values.")

    else:
        try:
            length_value = float(st.session_state.length)
            delta_temp_value = float(st.session_state.delta_temp)

            alpha = coefficients[st.session_state.material]

            expansion = (
                alpha
                * length_value
                * delta_temp_value
            )

            st.session_state.result = {
                "material": st.session_state.material,
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
    st.write(
        f"**Temperature Difference:** "
        f"{result['delta_temp']:.2f} °C"
    )
    st.write(
        f"**Thermal Expansion:** "
        f"{result['expansion']:.2f} mm"
    )