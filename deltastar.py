import streamlit as st


def DELTA_STAR(R12, R23, R31):
    denominator = R12 + R23 + R31
    R1 = (R12 * R31) / denominator
    R2 = (R12 * R23) / denominator
    R3 = (R31 * R23) / denominator
    
    return R1, R2, R3


st.title("Delta to Star Resistance Conversion")


R12 = st.number_input("Enter R12 (Resistance between 1 and 2)", min_value=0.0, step=0.1)
R23 = st.number_input("Enter R23 (Resistance between 2 and 3)", min_value=0.0, step=0.1)
R31 = st.number_input("Enter R31 (Resistance between 3 and 1)", min_value=0.0, step=0.1)


if st.button("Calculate STAR Resistances"):
    if R12 > 0 and R23 > 0 and R31 > 0:
        R1, R2, R3 = DELTA_STAR(R12, R23, R31)
        st.write(f"R1 (Star) = {R1:.2f} Ohms")
        st.write(f"R2 (Star) = {R2:.2f} Ohms")
        st.write(f"R3 (Star) = {R3:.2f} Ohms")
    else:
        st.error("Please enter valid positive resistance values.")
