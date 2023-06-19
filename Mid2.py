import sympy
from sympy import Function, Eq, simplify, dsolve, Derivative, sin, cos, exp, checkodesol, Equality
from sympy.abc import x,tau,theta

def solve_normally(func,vari,lst,rst,deg):
    f = Function('f')
    if func != 'f':
        lst = lst.replace(func,'f')
        rst = rst.replace(func, 'f')
    if vari != 'x':
        lst = lst.replace(vari, 'x')
        rst = rst.replace(vari,'x')
    lst = lst.replace('ddf(x)', 'f(x).diff(x,2)')
    lst = lst.replace('df(x)','f(x).diff(x)')
    rst = rst.replace('ddf(x)', 'f(x).diff(x,2)')
    rst = rst.replace('df(x)','f(x).diff(x)')
    leq = simplify(lst)
    req = simplify(rst)
    eq1 = Eq(leq - req,0)
    if deg == 2:
        result = dsolve(eq1,f(x),ics={f(0):tau, f(x).diff(x).subs(x,0):theta})
    else:
        result = dsolve(eq1, f(x), ics={f(0): tau})
    if hasattr(result,'lhs'):
        endstr = str(result.lhs) + '=' + str(result.rhs)
        endstr = endstr.replace('f', func)
        endstr = endstr.replace('x', vari)
        endstr = endstr.replace('e' + vari + 'p', 'exp')
        endstr = endstr.replace('e' + func + 'p', 'exp')
        return (endstr)
    else:
        for i in range (0,len(result)):
            endstr = str(result.lhs) + '=' + str(result.rhs)
            endstr = endstr.replace('f', func)
            endstr = endstr.replace('x', vari)
            endstr = endstr.replace('e'+vari+'p','exp')
            endstr = endstr.replace('e' + func + 'p', 'exp')
            return (endstr)
