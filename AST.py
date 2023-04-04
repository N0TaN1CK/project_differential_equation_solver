class Node:
    def __init__(self, op: ..., children: list['Node']):
        self.op = op
        self.children = children

    def __repr__(self):
        return f'Node with operation {self.op} and [{", ".join(map(str, self.children))}]'

    def assign(self, var_name: str, value: int | float):
        new_children = []
        for child in self.children:
            new_children.append(child.assign(var_name, value))
        return Node(self.op, new_children)

    def diff(self):
        return Node('d',[self])

    def Seekdiff(self):
        pnode = self
        if pnode.op == 'd':
            return pnode
        else:
            for N in self.children:
                N.Seekdiff()
    def integrate(self):
        for Ch in self.children:
            Ch = IntNode(Ch.Seekdiff().children[0],Ch)
            return self

class ValueNode(Node):
    def __init__(self, value: int | float):
        super().__init__(None, [])
        self.value = value

    def __repr__(self):
        return f'Value {self.value}'

    def assign(self, var_name: str, value: int | float):
        return self


class VariableNode(Node):
    def __init__(self, var_name: str):
        super().__init__(None, [])
        self.var_name = var_name

    def __repr__(self):
        return f'Variable {self.var_name}'

    def assign(self, var_name: str, value: int | float):
        if self.var_name == var_name:
            return ValueNode(value)
        return self


class BinaryOperation(Node):
    def __init__(self, op: ..., left_child: Node, right_child: Node):
        super().__init__(op, [left_child, right_child])

    @property
    def left_child(self):
        return self.children[0]

    @property
    def right_child(self):
        return self.children[1]

    def __repr__(self):
        return f'({self.children[0]}) {self.op} ({self.children[1]})'

    def assign(self, var_name: str, value: int | float):
        return BinaryOperation(
            self.op,
            self.left_child.assign(var_name, value),
            self.right_child.assign(var_name, value)
        )


# class IntegrationNode(Node):
#    def __int__(self, int_act, int_var: Node, child: Node):
#        super().__init__(int_act, [int_var, child])
#        self.var = int_var
#        self.child = child
#        self.act = int_act
#
#    def __repr__(self):
#        return f'int<<d{self.children[0]}({self.child})'
#
#    def assign(self, var_name: str, value: int | float):
#        return IntegrationNode(self.act,
#                               self.var,
#                               self.child
#                               )


class EqNode(Node):
    def __init__(self, left_child: Node, right_child: Node):
        super().__init__('=', [left_child, right_child])

    @property
    def left_child(self):
        return self.children[0]

    @property
    def right_child(self):
        return self.children[1]

    def mirror(self):
        return EqNode(
            self.right_child,
            self.left_child
        )


class IntNode(Node):
    def __init__(self, var_child: Node, right_child: Node):
        super().__init__('intOp', [var_child, right_child])

    @property
    def var_child(self):
        return self.children[0]

    @property
    def right_child(self):
        return self.children[1]

    def __repr__(self):
        return f'to int ({self.right_child}) by ({self.var_child})'

    def assign(self, var_name: str, value: int | float):
        return IntNode(
            self.var_child,
            self.right_child.assign(var_name, value)
        )


class DiffNode(Node):
    def __init__(self, var_child: Node, right_child: Node):
        super().__init__('diffOp', [var_child, right_child])

    @property
    def var_child(self):
        return self.children[0]

    @property
    def right_child(self):
        return self.children[1]

    def __repr__(self):
        return f'to diff d({self.right_child}) by ({self.var_child})'

    def assign(self, var_name: str, value: int | float):
        return DiffNode(
            self.var_child,
            self.right_child.assign(var_name, value)
        )

    def split(self):
        return BinaryOperation('/',
                               self.right_child.diff(),
                               self.var_child.diff()
                               )


def reverse(operation:str):
    if operation == '+':
        return '-'
    if operation == '-':
        return '+'
    if operation == '*':
        return '/'
    if operation == '/':
        return '*'


def move(BO: BinaryOperation, eq: EqNode, side: str, cNo: int):
    movenode = BO.children[cNo]
    if BO.op == '+' or BO.op == '-':
        BO.children[cNo] = ValueNode(0)
    elif BO.op == '*' or BO.op == '/':
        BO.children[cNo] = ValueNode(1)
    if side == '>':
        eq = EqNode(eq.left_child,BinaryOperation(reverse(BO.op),eq.right_child,movenode))
    else:
        eq = EqNode(BinaryOperation(reverse(BO.op), eq.left_child, movenode),eq.right_child)
    return eq


def simplify(head:Node):
    for h in head.children:
        if h is BinaryOperation:
            if h.op == '*' or h.op == '/':

            if h.op == '+' or h.op == '+':

        if h.children is not None:
            for k in h.children:
                simplify(k)


# class Operation

# class NonbiOperation(Node)

# class equationNode(Node)

# def DoubleAction(left_node: Node, Right_node: Node):

# def SimplifyNode # добавить в корень Node

# def replaceNode # добавить в корень Node


diff1 = DiffNode(VariableNode('x'),VariableNode('y'))
#print(diff1)
mult1 = BinaryOperation('*',VariableNode('x'),diff1)
#print(mult1)
headeq = EqNode(mult1,VariableNode('y'))
#print(headeq)

diff1 = diff1.split()
mult1 = BinaryOperation('*',VariableNode('x'),diff1)
headeq = EqNode(mult1,VariableNode('y'))
#print(diff1)
print(headeq)

headeq = move(diff1,headeq,'>',1)
print(headeq)
headeq = move(headeq.right_child, headeq,'<',0)
print(headeq)
headeq = move(mult1, headeq, '>', 0)
print(headeq)
print(headeq.Seekdiff())

