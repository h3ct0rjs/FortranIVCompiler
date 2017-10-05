# coding: utf-8
'''
'''

import pydotplus as pgv
import astfortran as ast


class DotCode(ast.NodeVisitor):
    '''
    Clase Node visitor que crea secuencia de instrucciones Dot
    '''

    def __init__(self):
        super(DotCode, self).__init__()

        # Secuencia para nombres de nodos
        self.id = 0

        # Stack para retornar nodos procesados
        self.stack = []

        # Inicializacion del grafo para Dot
        self.dot = pgv.Dot('AST', graph_type='digraph')
        self.dot.set_node_defaults(
            shape='box', color='lightgray', style='filled')
        self.dot.set_edge_defaults(arrowhead='none')

    def __repr__(self):
        return self.dot.to_string()

    def new_node(self, node=None, label=None, shape="box"):
        '''
        Crea una variable temporal como nombre del nodo
        '''
        if label is None:
            label = node.__class__.__name__
        self.id += 1
        return pgv.Node('n{}'.format(self.id), label=label, shape=shape)

    def generic_visit(self, node):
        target=self.new_node(node)
        self.dot.add_node(target)
        for field in getattr(node, "_fields"):
            value = getattr(node, field, None)
            if isinstance(value, list):
                for i in value:
                    if isinstance(i, ast.AST):
                        self.visit(i)
                        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
                    elif(i is not None):
                        targetHijo=self.new_node(label=i, shape="circle")
                        self.dot.add_node(targetHijo)
                        self.dot.add_edge(pgv.Edge(target, targetHijo))
            elif isinstance(value, ast.AST):
                self.visit(value)
                self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
            elif(value is not None):
                targetHijo=self.new_node(label=value, shape="circle")
                self.dot.add_node(targetHijo)
                self.dot.add_edge(pgv.Edge(target, targetHijo))
        self.stack.append(target)
"""
    def visit_Program(self, node):
        target = self.new_node(node)
        self.dot.add_node(target)
        self.visit(node.statements)
        self.generic_visit(node)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))

    def visit_Extern(self, node):
        target = self.new_node(node)
        self.dot.add_node(target)
        self.visit(node.func_prototype)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
        self.stack.append(target)

    def visit_FuncDeclaration(self, node):
        target = self.new_node(node)
        self.dot.add_node(target)

        self.visit(node.func_prototype)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))

        self.visit(node.body)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
        self.stack.append(target)

    def visit_FuncPrototype(self, node):
        label = node.__class__.__name__ + \
            '\n(id={}, typename={})'.format(node.id, node.typename)
        target = self.new_node(node, label)
        self.dot.add_node(target)

        self.visit(node.params)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
        self.stack.append(target)

    def visit_Statements(self, node):
        target = self.new_node(node)
        self.dot.add_node(target)
        for stmt in node.statements:
            self.visit(stmt)
            self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
        self.stack.append(target)

    def visit_Statement(self, node):
        target = self.new_node(node)
        self.dot.add_node(target)
        self.visit(node.statement)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
        self.stack.append(target)

    def visit_PrintStatement(self, node):
        target = self.new_node(node)
        self.dot.add_node(target)
        self.visit(node.expr)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
        self.stack.append(target)

    def visit_ReturnStatement(self, node):
        target = self.new_node(node)
        self.dot.add_node(target)
        self.visit(node.expression)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
        self.stack.append(target)

    def visit_AssignmentStatement(self, node):
        label = node.__class__.__name__ + \
            '\n(location={})'.format(node.location)
        target = self.new_node(node, label)
        self.dot.add_node(target)
        self.visit(node.value)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
        self.stack.append(target)

    def visit_RelationalOp(self, node):
        target = self.new_node(node, node.op)
        target.set('shape', 'diamond')
        self.dot.add_node(target)

        self.visit(node.left)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop(), label='left'))

        self.visit(node.right)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop(), label='right'))
        self.stack.append(target)

    def visit_BinaryOp(self, node):
        target = self.new_node(node, node.op)
        target.set('shape', 'circle')
        self.dot.add_node(target)

        self.visit(node.left)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop(), label='left'))

        self.visit(node.right)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop(), label='right'))
        self.stack.append(target)

    def visit_UnaryOp(self, node):
        target = self.new_node(node, node.op)
        target.set('shape', 'circle')
        self.dot.add_node(target)

        self.visit(node.left)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop(), label='left'))

    def visit_FuncCall(self, node):
        label = node.__class__.__name__ + '\n(id={})'.format(node.id)
        target = self.new_node(node, label)
        self.dot.add_node(target)

        self.visit(node.params)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))

    def visit_Group(self, node):
        target = self.new_node(node)
        self.dot.add_node(target)

        self.visit(node.expression)
        self.dot.add_edge(pgv.Edge(target, self.stack.pop()))
"""
1