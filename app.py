import streamlit as st

st.title("2205A21055. -PS6.")

def Tran_Eff(Rated_VA, CL, FCL, K, PF):
    output_power = K * Rated_VA * PF
    input_power = K * Rated_VA * PF + CL + K**2 * FCL
    Eff = (output_power / input_power) * 100  
    CUL = K**2 * FCL  
    return Eff, CUL


def main():
    st.title("Transformer Efficiency and Copper Losses Calculator")
    Rated_VA = st.number_input("Enter Rated Power (VA)", min_value=1, step=1)
    CL = st.number_input("Enter Core Losses (CL) in Watts", min_value=0, step=1)
    FCL = st.number_input("Enter Full Load Copper Losses (FCL) in Watts", min_value=0, step=1)
    K = st.number_input("Enter Loading on Transformer (K)", min_value=0.0, max_value=1.0, step=0.01)
    PF = st.number_input("Enter Power Factor (PF)", min_value=0.0, max_value=1.0, step=0.01)
    
   
col1, col2 = st.columns(2) 
    
    
with col1:
       
        st.write("### Inputs")
        Rated_VA = st.number_input("Rated Power (VA)", min_value=1, step=1)
        CL = st.number_input("Core Losses (CL) in Watts", min_value=0, step=1)
        FCL = st.number_input("Full Load Copper Losses (FCL) in Watts", min_value=0, step=1)
        K = st.number_input("Loading on Transformer (K)", min_value=0.0, max_value=1.0, step=0.01)
        PF = st.number_input("Power Factor (PF)", min_value=0.0, max_value=1.0, step=0.01)
        
   
with col2:
    
    if st.button("Calculate Efficiency and Copper Losses"):
        Eff, CUL = Tran_Eff(Rated_VA, CL, FCL, K, PF)
        st.write("### Results")
        st.write(f"*Transformer Efficiency:* {Eff:.2f}%")
        st.write(f"*Copper Losses at K load factor:* {CUL:.2f} W")
