import streamlit as st
import numpy as np
import pandas as pd

st.title("Решатель дифференциальных уравнений")
st.subheader("Введите уравнение:")
st.text_input("", key="input")
st.subheader("Введенное уравнение:")
st.latex(st.session_state.input)
st.subheader("Решение:")
st.write("Здесь потом будет решение")
st.subheader("График решений:")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.write("Рандомный график с сайта стримлита")
