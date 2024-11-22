import streamlit as st

def DELTA_STAR(R12, R23, R31):
    denominator = R12 + R23 + R31
    R1 = (R12 * R31) / denominator
    R2 = (R12 * R23) / denominator
    R3 = (R31 * R23) / denominator
    
    return R1, R2, R3


st.title("2305A21L34-PS5")
st.title("Calculate the Resistance values of Star and Delta Connection")


R12 = st.number_input("Enter R12 (Resistance between 1 and 2 in Ohms)", min_value=0.0, step=0.1)
R23 = st.number_input("Enter R23 (Resistance between 2 and 3 in Ohms)", min_value=0.0, step=0.1)
R31 = st.number_input("Enter R31 (Resistance between 3 and 1 in Ohms)", min_value=0.0, step=0.1)


if st.button("Calculate STAR Resistances"):
    if R12 > 0 and R23 > 0 and R31 > 0:
        R1, R2, R3 = DELTA_STAR(R12, R23, R31)
        # Convert the values to kilo-ohms by dividing by 1000
        R1_kohms = R1 / 1000
        R2_kohms = R2 / 1000
        R3_kohms = R3 / 1000
        
        st.write(f"R1 (Star) = {R1_kohms:.3f} kΩ")
        st.write(f"R2 (Star) = {R2_kohms:.3f} kΩ")
        st.write(f"R3 (Star) = {R3_kohms:.3f} kΩ")
    else:
        st.error("Please enter valid positive resistance values.")
