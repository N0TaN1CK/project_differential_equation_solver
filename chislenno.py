from scipy.integrate import solve_ivp as solve
import numpy

def parse_equation(equation_input):
    is_second_degree = equation_input.find("d^2")
    if equation_input.find('dy/dt')<0:
        help = equation_input.split('dt^2')
        equation_input = help[0]+'dt^2 + 0.0 * dy/dt'+help[1]
    if equation_input.find(' y ')<0 and equation_input.find('dy/dt')>=0:
        help = equation_input.split('dy/dt')
        equation_input = help[0]+'dy/dt + 0.0 * y '+help[1]
    elif equation_input.find(' y ')<0 and equation_input.find('dy/dt')<0:
        help = equation_input.split('dt^2')
        equation_input = help[0] + 'dt^2 + 0.0 * y ' + help[1]
    stage_one = equation_input.split()
    stage_two = []
    for thing in stage_one:
        if thing.find('.')>=0:
            stage_two.append(numpy.float64(thing))
        else:
            stage_two.append(thing)
    for stuff in stage_two:
        if stuff == '*':
            stage_two.pop(stage_two.index(stuff))
        if stuff == '-':
            stage_two[stage_two.index(stuff)+1] = -1.0*stage_two[stage_two.index(stuff)+1]
            stage_two.pop(stage_two.index(stuff))
        if stuff == '+':
            stage_two.pop(stage_two.index(stuff))
    return [stage_two,is_second_degree]


def solve_equation(equation_parsed,user_input_t1,user_input_t2,user_input_dy,user_input_y):
    if equation_parsed[1]>=0:
        t_span = [user_input_t1,user_input_t2]
        y0 = [user_input_dy,user_input_y]
        def helper(t,y):
            return([((equation_parsed[0][7]-equation_parsed[0][2]*y[0]-equation_parsed[0][4]*y[1])/equation_parsed[0][0]),y[0]])
        solution = solve(helper,t_span,y0)
        return([solution.t,solution.y])
    else:
        t_span = [user_input_t1, user_input_t2]
        y0 = [user_input_y]
        def helper(t,y):
            return(((equation_parsed[0][5]-equation_parsed[0][2]*y[0])/equation_parsed[0][0]))
        solution = solve(helper,t_span,y0)
        return([solution.t,solution.y])



