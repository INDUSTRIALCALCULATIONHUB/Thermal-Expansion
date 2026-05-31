if "result" not in st.session_state:
    st.session_state.result = None

# Calculate
if calculate:
    alpha = coefficients[material]
    expansion = alpha * float(length) * float(delta_temp)

    st.session_state.result = {
        "material": material,
        "length": float(length),
        "delta_temp": float(delta_temp),
        "expansion": expansion
    }

# Reset
if reset:
    st.session_state.clear()
    st.rerun()

# Display Result
if st.session_state.get("result"):

    result = st.session_state.result

    st.subheader("Result")

    st.write(f"**Material:** {result['material']}")
    st.write(f"**Length:** {result['length']:.2f} mm")
    st.write(f"**Temperature Difference:** {result['delta_temp']:.2f} °C")
    st.write(f"**Thermal Expansion:** {result['expansion']:.2f} mm")