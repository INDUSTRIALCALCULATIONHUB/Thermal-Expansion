import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Thermal Expansion Calculator",
    page_icon="⚙️",
    layout="centered"
)

# Session State Initialization
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

# Material Database
coefficients = {
    "Aluminium 5083": 23.8e-6,
    "Aluminium 6061": 23.6e-6,
    "Brass": 19.0e-6,
    "Bronze": 18.0e-6,
    "Carbon Steel (ASTM A36)": 12.0e-6,
    "Carbon Steel (ASTM A106 Gr.B)": 11.7e-6,
    "Carbon Steel (Structural)": 11.2e-6,
    "Cast Iron (Grey)": 10.8e-6,
    "Concrete": 12.0e-6,
    "Copper": 16.5e-6,
    "Ductile Iron": 11.5e-6,
    "FRP (Glass Fiber Reinforced Plastic)": 10.0e-6,
    "Glass": 9.0e-6,
    "HDPE": 120.0e-6,
    "Mild Steel": 12.0e-6,
    "Nickel": 13.0e-6,
    "PTFE (Teflon)": 120.0e-6,
    "PVC": 52.0e-6,
    "Reinforced Concrete": 11.0e-6,
    "Rubber Lining": 80.0e-6,
    "Stainless Steel 304": 17.3e-6,
    "Stainless Steel 310": 14.4e-6,
    "Stainless Steel 316": 16.0e-6,
    "Titanium": 8.6e-6
}

# Header
st.title("⚙️ Thermal Expansion Calculator")

st.markdown(
    """
    Calculate linear thermal expansion of commonly used
    industrial engineering materials.
    """
)

# Material Selection
st.selectbox(
    "Material",
    ["Select Material"] + sorted(coefficients.keys()),
    key="material"
)

# Length Input
st.text_input(
    "Length (mm)",
    placeholder="Enter Length in mm",
    key="length"
)

# Temperature Difference Input
st.text_input(
    "Temperature Difference (°C)",
    placeholder="Enter Temperature Difference",
    key="delta_temp"
)

# Buttons
col1, col2 = st.columns(2)

with col1:
    calculate = st.button(
        "Calculate",
        use_container_width=True
    )

with col2:
    st.button(
        "Reset",
        on_click=reset_form,
        use_container_width=True
    )

# Calculation Logic
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

            alpha = coefficients[
                st.session_state.material
            ]

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
            st.error(
                "Please enter valid numeric values."
            )

# Display Result
if st.session_state.result is not None:

    result = st.session_state.result

    st.markdown("---")

    st.subheader("Result")

    st.write(
        f"**Material:** {result['material']}"
    )

    st.write(
        f"**Length:** "
        f"{result['length']:,.2f} mm"
    )

    st.write(
        f"**Temperature Difference:** "
        f"{result['delta_temp']:,.2f} °C"
    )

    st.success(
        f"Thermal Expansion = "
        f"{result['expansion']:.3f} mm"
    )

# Footer
st.markdown("---")
st.caption("Industrial Calculation Hub")