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


#class IntegrationNode(Node):
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

class IntegrationNode(Node):
    def __init__(self, op: ..., var_child: Node, right_child: Node):
        super().__init__(op, [var_child, right_child])

    @property
    def var_child(self):
        return self.children[0]

    @property
    def right_child(self):
        return self.children[1]

    def __repr__(self):
        return f'int<<d({self.children[0]})({self.children[1]})'

    def assign(self, var_name: str, value: int | float):
        return IntegrationNode(
            self.op,
            self.var_child,
            self.right_child.assign(var_name, value)
        )

class DiffNode(Node):
    def __init__(self, op: ..., var_child: Node, right_child: Node):
        super().__init__(op, [var_child, right_child])

    @property
    def var_child(self):
        return self.children[0]

    @property
    def right_child(self):
        return self.children[1]

    def __repr__(self):
        return f'diff<<d({self.children[0]})({self.children[1]})'

    def assign(self, var_name: str, value: int | float):
        return IntegrationNode(
            self.op,
            self.var_child,
            self.right_child.assign(var_name, value)
        )

class NonbiOperation(Node)
    ...
class equationNode(Node)
    ...
     def DoubleAction(left_node: Node, Right_node: Node):
        ...
def SimplifyNode # добавить в корень Node
    ...
def replaceNode # добавить в корень Node
    ...

node = Node('max', [ValueNode(1), VariableNode('x'), VariableNode('y')])
inode = IntegrationNode('intr1',VariableNode('x'),node)
binop_node = BinaryOperation('+', inode, ValueNode(2))
print(binop_node)
print(binop_node.assign('y', 100))