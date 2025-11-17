import streamlit as st
st.title('calculadora simple con streamlit')
valor1=st.number_input('Ingrese el primer valor:', min_value=0.0, value =10.0)
valor2=st.number_input('Ingrese el segundo valor:', min_value=0.0, value =5.0)
valor3=st.number_input('Ingrese el tercer valor:', min_value=0.0, value =11.0)
st.write('...') # separador visual
suma=valor1 + valor2 + valor3
if st.button('Calcular Suma'):
    st.success(f'El resultado de la suma es: **{suma}**')

st.subheader('Valores ingresados')
st.write(f'Primer valor: **{valor1}**')
st.write(f'Segundo valor: ***{valor2}*')
st.write(f'Tercer valor: ***{valor3}*')