import streamlit as st
import numpy
import altair
import pandas as pd
from scipy.integrate import solve_ivp as solve
from chislenno import solve_equation
from chislenno import parse_equation

st.title("Решатель дифференциальных уравнений")
want_solution = st.checkbox('с решением')
if want_solution:
     st.subheader("Введите уравнение:")
     st.text_input("", key="input")
     st.subheader("Введенное уравнение:")
     st.latex(st.session_state.input)
     st.subheader("Решение:")
     st.write("Здесь потом будет решение")
else:
     st.subheader("Введите уравнение:")
     eq = st.text_input("пример правильной записи: 4.7 * d^2y/dt^2 - 33.5 * dy/dt + 43.7 y  = 77.8")
     st.subheader("Введите начальное значение y")
     yst = st.text_input("",key="inputy")
     st.subheader("Введите начальное значение dy/dt")
     dydtst = st.text_input("", key="inputdydt")
     st.subheader("Введите начало временного промежутка")
     t1st = st.text_input("", key="inputt1")
     st.subheader("Введите конец временного промежутка")
     t2st = st.text_input("", key="inputt2")
     ready = st.button("решить")
     if ready:
          yy = numpy.float64(yst)
          dydt = numpy.float64(dydtst)
          t1 = numpy.float64(t1st)
          t2 = numpy.float64(t2st)
          eqpar = parse_equation(eq)
          sol = solve_equation(eqpar,t1,t2,dydt,yy)
          i = 0
          if eqpar[1]>=0:
               i+=1
          for_graph = {'t':list(sol[0]),'y':list(sol[1][i])}
          data = pd.DataFrame(for_graph)
          graph_spec = altair.Chart(data).mark_line(interpolate="monotone").encode(
               x = "t",
               y = "y"
          )
          graph = st.altair_chart(graph_spec,use_container_width=True)



