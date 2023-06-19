import streamlit as st
import altair
import pandas as pd
from sympy import simplify,re
from sympy.abc import t
from Mid2 import solve_normally

st.title("Решатель дифференциальных уравнений")
st.subheader("Введите уравнение:")
eq = st.text_input("Вводите в LaTeX формате")
counter = 0
counter2 = 0
followup = []
for symbol in eq:
    if symbol == '\\':
        followup.append(eq[counter2 + 1:counter2 + 3])
        counter += 1
    counter2 += 1
followup.append('sq')
followup.append('ex')
degree = 1
eq2 = eq.replace("\\frac{d^2y}{dt^2}","ddf(tttttt)").replace("\\frac{dy}{dt}","df(tttttt)").replace("{","(").replace("}",")").replace("lambda","paskhalochka").replace("Lambda","PASKHALOCHKA").replace('e^','exp').replace('tau','STHONE').replace('theta','STHTWO').replace('beta','bbbbb').replace('gamma','ggggg').replace('zeta','zzzzz')
if eq2.find('ddf(tttttt)')>=0:
    degree = 2
eq3 = eq2.replace('\\','').replace("y","f(tttttt)").split("=")
if eq!='':
    st.subheader("Вы ввели:")
    st.latex(eq)
    res = solve_normally('f','tttttt',eq3[0],eq3[1],degree).replace("PASKHALOCHKA","Lambda").replace("paskhalochka","lambda").replace('**','^').replace('tau','y(0)').replace('theta','\\frac{dy}{dt}(0)').replace('STHONE','tau').replace('STHTWO','theta').replace('bbbbb','beta').replace('ggggg','gamma').replace('zzzzz','zeta')
    for item in followup:
        for j in range(len(res)-1,0,-1):
            if res[j:j+2]==item and res[j-1]!='\\':
                res = res[0:j]+'\\'+res[j:len(res)+1]

    st.subheader("Решение:")
    st.latex(res.replace('tttttt','t'))
    varis = []
    do_not_touch = 'sqrtexpsincostancotanctantgarctgtttttt'
    res2 = '%'+res.replace("\\","").replace('y(0)','yin').replace('frac{dy}{dt}(0)','dydtin').replace("^","**").split('=')[1]
    coun = 1
    letter = ''
    for i in range(1,len(res2)-1):
        if res2[i].isalpha() and not(res2[i-1].isalpha()):
            letter = res2[i]
            while letter.isalpha():
                letter = res2[i:i+coun]
                coun+=1
            letter = letter[0:len(letter)-1]
            if do_not_touch.find(letter)<0:
                varis.append(letter)
                do_not_touch=do_not_touch+letter
        letter = ''
        coun = 1
    nums = []
    sl = []
    st.subheader("Задайте переменные")
    for j in range(len(varis)):
        sl.append(1)
        sl[j] = st.slider('$'+varis[j].replace('yin','y(0)').replace('dydtin','\\frac{dy}{dt}(0)')+'$',min_value=-100)
        nums.append(float(sl[j]))
    for k in range(len(varis)):
        res2 = res2.replace('%','').replace(varis[k],str(nums[k]))
    t0 = st.slider("Начальное время",max_value=50)
    t1 = st.slider('Конечное время',min_value=5)
    tlist = []
    ylist = []
    trr = float(t0)
    res3 = res2.replace('tttttt', 't')
    res4 = simplify(res3)
    for gh in range(101):
        sol = float(re(res4.subs(t,trr)))
        tlist.append(trr)
        ylist.append(sol)
        trr = trr+((float(t1)-float(t0))/100)
    for_graph = {'t':tlist,'y':ylist}
    data = pd.DataFrame(for_graph)
    graph_spec = altair.Chart(data).mark_line(interpolate="monotone").encode(
        x = "t",
        y = "y"
    )
    graph = st.altair_chart(graph_spec,use_container_width=True)



