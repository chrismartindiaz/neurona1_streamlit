import streamlit as st
import pandas as pd

# INSERTAR IMAGEN

st.image('./src/neurona.jpg')

st.title('¡Hola neurona!')

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
   st.header("Una neurona con una entrada y un peso")
   st.text('Peso')
   w0 = st.slider('Peso',0.00,5.00, label_visibility="collapsed", key=11)

   st.text('Introduzca un valor de entrada')
   x0 = st.number_input('Introduzca el valor de la entrada:', label_visibility="collapsed", key=12)

   if st.button('Calcular salida', type='primary'):
      result = x0 * w0
      st.text(f"La salida de la neurona es {result}")


with tab2:

   col1, col2 = st.columns(2)

   with col1:
      st.markdown('Peso w<sub>0</sub>:', unsafe_allow_html=True)
      w0 = st.slider('Peso w0',0.00,5.00, label_visibility="collapsed", key=21)

      st.markdown('Entrada x<sub>0</sub>:', unsafe_allow_html=True)
      x0 = st.number_input('Introduzca el valor de la entrada:', label_visibility="collapsed", key=22)
   
   with col2:
      st.markdown('Peso w<sub>1</sub>:', unsafe_allow_html=True)
      w1 = st.slider('Peso w1',0.00,5.00, label_visibility="collapsed", key = 23)

      st.markdown('Peso x<sub>1</sub>:', unsafe_allow_html=True)
      x1 = st.number_input('Introduzca el valor de la entrada:', label_visibility="collapsed", key = 24)

   if st.button('Calcular salida', type='primary', key=2):
      result2 = x0 * w0 + w1 * w1
      st.text(f"La salida de la neurona es {result2}")

with tab3:

   col1, col2, col3 = st.columns(3)

   with col1:
      st.markdown('Peso w<sub>0</sub>:', unsafe_allow_html=True)
      w0 = st.slider('Peso w0',0.00,5.00, label_visibility="collapsed", key=31)

      st.markdown('Peso x<sub>0</sub>:', unsafe_allow_html=True)
      x0 = st.number_input('Introduzca el valor de la entrada:', label_visibility="collapsed", key=32)
   
   with col2:
      st.markdown('Peso w<sub>1</sub>:', unsafe_allow_html=True)
      w1 = st.slider('Peso w1',0.00,5.00, label_visibility="collapsed", key = 33)

      st.markdown('Peso x<sub>1</sub>:', unsafe_allow_html=True)
      x1 = st.number_input('Introduzca el valor de la entrada:', label_visibility="collapsed", key = 34)
   
   with col3:
      st.markdown('Peso w<sub>2</sub>:', unsafe_allow_html=True)
      w2 = st.slider('Peso w2',0.00,5.00, label_visibility="collapsed")

      st.markdown('Peso x<sub>2</sub>:', unsafe_allow_html=True)
      x2 = st.number_input('Introduzca el valor de la entrada:', label_visibility="collapsed")

   st.text('Introduzca el valor del sesgo')
   b = st.number_input('Introduzca el valor del sesgo', label_visibility="collapsed")

   if st.button('Calcular salida', type='primary', key=3):
      result3 = x0 * w0 + w1 * w1 + x2 * w2 + b
      st.text(f"La salida de la neurona es {result3}")

