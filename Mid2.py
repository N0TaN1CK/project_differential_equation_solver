import sympy
from sympy import Function, Eq, simplify, dsolve, Derivative, sin, cos, exp, checkodesol, Equality
from sympy.abc import x

f = Function('f')
func = str(input('function: ') or 'f')
vari = str(input('variable: ') or 'x')
lst = str(input('left part: ') or '0')
rst = str(input('right part: ') or '0')
#st = 'ddf(x) - df(x) + exp(x)'
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
print(lst, '=', rst)
leq = simplify(lst)
req = simplify(rst)
eq1 = Eq(leq - req,0)
result = dsolve(eq1,f(x))# Solve the ODE
#print(result)
#print(type(result))
#print(type(lst))
if hasattr(result,'lhs'):
    endstr = str(result.lhs) + '=' + str(result.rhs)
    endstr = endstr.replace('f', func)
    endstr = endstr.replace('x', vari)
    endstr = endstr.replace('e' + vari + 'p', 'exp')
    endstr = endstr.replace('e' + func + 'p', 'exp')
    print(endstr)
else:
    for i in range (0,len(result)):
        endstr = str(result.lhs) + '=' + str(result.rhs)
        endstr = endstr.replace('f', func)
        endstr = endstr.replace('x', vari)
        endstr = endstr.replace('e'+vari+'p','exp')
        endstr = endstr.replace('e' + func + 'p', 'exp')
        print(endstr)
