from util.util import *
'''
Objetos Arbol de Sintaxis Abstracto (AST - Abstract Syntax Tree).

Este archivo define las clases para los diferentes tipos de nodos del
árbol de sintaxis abstracto.  Durante el análisis sintático, se debe
crear estos nodos y conectarlos.  En general, usted tendrá diferentes
nodos AST para cada tipo de regla gramatical.  Algunos ejemplos de
nodos AST pueden ser encontrados al comienzo del archivo.  Usted deberá
añadir más.
'''

# NO MODIFICAR


class AST(object):
    '''
    Clase base para todos los nodos del AST.  Cada nodo se espera
    definir el atributo _fields el cual enumera los nombres de los
    atributos almacenados.  El método a continuación __init__() toma
    argumentos posicionales y los asigna a los campos apropiados.
    Cualquier argumento adicional especificado como keywords son
    también asignados.
    '''
    _fields = []

    def __init__(self, *args, **kwargs):
        assert len(args) == len(self._fields)
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        # Asigna argumentos adicionales (keywords) si se suministran
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        return self.__class__.__name__

    def pprint(self):
        for depth, node in flatten(self):
            print("%s%s|%s" % (tree, "-" * (4 * depth), node))

        print('{}'.format(reset))


def validate_fields(**fields):
    def validator(cls):
        old_init = cls.__init__

        def __init__(self, *args, **kwargs):
            old_init(self, *args, **kwargs)
            for field, expected_type in fields.items():
                assert isinstance(getattr(self, field), expected_type)
        cls.__init__ = __init__
        return cls
    return validator

# ----------------------------------------------------------------------
# Nodos AST especificos
#
# Para cada nodo es necesario definir una clase y añadir la
# especificación del apropiado _fields = [] que indique que campos
# deben ser almacenados.
# A modo de ejemplo, para un operador binario es posible almacenar el
# operador, la expresión izquierda y derecha, como esto:
#
#    class Binop(AST):
#        _fields = ['op','left','right']
# ----------------------------------------------------------------------


@validate_fields(statements=list)
class Program(AST):
    _fields = ['statements']

    def append(self, statement):
        self.statements.append(statement)


class Statement(AST):
    _fields = ['INT', 'command']


class Assign(AST):
    _fields = ['variable', 'expr']

''' command Section '''


class CommandCall(AST):
    _fields = ['callOpt']


class CommandData(AST):
    _fields = ['datOpt']


class CommandDimmension(AST):
    _fields = ['dimmenOpt']


class CommandDo(AST):
    _fields = ['doOpt']

'''
class CommandFormat(AST):
    _fields = ['formatOption']
'''

@validate_fields(convers=list, strlist=list, hstrlist=list, ints=list, times=list)
class CommandFormat(AST):
    _fields = ['convers', 'strlist', 'hstrlist', 'ints', 'times']

    def append(self, conver, string, hString, int, time):
        self.convers.append(conver)
        self.strlist.append(string)
        self.hstrlist.append(hString)
        self.ints.append(int)
        self.times.append(time)

class CommandFunction(AST):
    _fields = ['ID', 'varlist']


class CommandGoTo(AST):
    _fields = ['gotoOpt']


class CommandIf(AST):
    _fields = ['relexpr', 'ifOption']


class CommandInteger(AST):
    _fields = ['exprlist']


class CommandPause(AST):
    _fields = ['pauseOpt']


class CommandReal(AST):
    _fields = ['exprlist']


class CommandRead(AST):
    _fields = ['optionsIO', 'idList']


class CommandStop(AST):
    _fields = ['stopOpt']


class CommandSubroutine(AST):
    _fields = ['ID', 'varlist']


class CommandWrite(AST):
    _fields = ['optionsIO', 'idList']

'''variable Section'''


class Variable(AST):
    _fields = ['ID', 'expr', 'expr']

'''varlist Section'''


@validate_fields(varlist=list)
class Varlist(AST):
    _fields = ['varlist']

    def append(self, variable):
        self.varlist.append(variable)

''' number Section '''


class Number(AST):
    _fields = ['MINUS', 'INT', 'RREAL']

'''expr Section'''


class Expr(AST):
    _fields = ['expr0', 'operator', 'expr1']


class ExprMinus(AST):
    _fields = ['MINUS', 'expr']


class ExprParen(AST):
    _fields = ['expr']


class ExprSingle(AST):
    _fields = ['INT', 'REAL', 'variable']


@validate_fields(exprList=list)
class ExprList(AST):
    _fields = ['exprList']

    def append(self, expr):
        self.exprList.append(expr)


class Relexpr(AST):
    _fields = ['expr0', 'relationOp', 'expr1']


class LogicalRelexpr(AST):
    _fields = ['relexpr0', 'logicalOp', 'relexpr1']


class NotRelexpr(AST):
    _fields = ['NOT', 'relexpr']


class RelexprSingle(AST):
    _fields = ['expr']

''' callOption Section  '''


class CallOption(AST):
    _fields = ['ID', 'idList']


class CallOptionExit(AST):
    _fields = ['callExit']


class CallExit(AST):
    _fields = ['INT']

'''  idList Section  '''


@validate_fields(idList=list)
class IdList(AST):
    _fields = ['idList']

    def append(self, id):
        self.idList.append(id)

''' dataOptions Section  '''


@validate_fields(datalists=list, varlists=list)
class DataOption(AST):
    _fields = ['varlists', 'datalists']

    def append(self, varlist, datalist):
        self.datalists.append(datalist)
        self.varlists.append(varlist)


@validate_fields(dataPars=list, dataSingles=list)
class DataList(AST):
    _fields = ['INT', 'number']

    def append(self, datasingle, datapar):
        self.dataPars.append(datapar)
        self.dataSingles.append(datasingle)


@validate_fields(ids=list, intlists=list)
class DimmensionOption(AST):
    _fields = ['ID', 'intlists']

    def append(self,id, intlist):
        self.ids.append(id)
        self.intlists.append(intlist)


@validate_fields(intlist=list)
class Intlist(AST):
    _fields = ['INT']

    def append(self, int):
        self.intlist.append(int)


class DoOption(AST):
    _fields = ['INT0', 'variable', 'INT1', 'INT2', 'INT3']

'''
@validate_fields(convers=list, strlist=list, hstrlist=list, ints=list, times=list)
class FormatOptList(AST):
    _fields = ['convers', 'strlist', 'hstrlist', 'ints', 'times']

    def append(self, conver, string, hString, int, time):
        self.convers.append(conver)
        self.strlist.append(string)
        self.hstrlist.append(hString)
        self.ints.append(int)
        self.times.append(time)
'''

class GotoOptionInt(AST):
    _fields = ['INT']


class GotoOptionIntlist(AST):
    _fields = ['intlist', 'variable']


class IfOption(AST):
    _fields = ['INT0', 'INT1', 'INT2']


class PauseOption(AST):
    _fields = ['INT']


class StopOption(AST):
    _fields = ['INT']


class WriteRead(AST):
    _fields = ['optionsIO', 'idList']


class OptionsIOInt(AST):
    _fields = ['INT0', 'INT1']


class OptionsIOID(AST):
    _fields = ['ID', 'INT']


# Usted deberá añadir mas nodos aquí.  Algunos nodos sugeridos son
# BinaryOperator, UnaryOperator, ConstDeclaration, VarDeclaration,
# AssignmentStatement, etc...

# ----------------------------------------------------------------------
#                  NO MODIFIQUE NADA AQUI ABAJO
# ----------------------------------------------------------------------

# Las clase siguientes para visitar y reescribir el AST son tomadas
# desde el módulo ast de python .

# NO MODIFIQUE
class NodeVisitor(object):
    '''
    Clase para visitar nodos del árbol de sintaxis.  Se modeló a partir
    de una clase similar en la librería estándar ast.NodeVisitor.  Para
    cada nodo, el método visit(node) llama un método visit_NodeName(node)
    el cual debe ser implementado en la subclase.  El método genérico
    generic_visit() es llamado para todos los nodos donde no hay
    coincidencia con el método visit_NodeName().

    Es es un ejemplo de un visitante que examina operadores binarios:

    class VisitOps(NodeVisitor):
            visit_Binop(self,node):
                    print("Operador binario", node.op)
                    self.visit(node.left)
                    self.visit(node.right)
            visit_Unaryop(self,node):
                    print("Operador unario", node.op)
                    self.visit(node.expr)

    tree = parse(txt)
    VisitOps().visit(tree)
    '''

    def visit(self, node):
        '''
        Ejecuta un método de la forma visit_NodeName(node) donde
        NodeName es el nombre de la clase de un nodo particular.
        '''
        if node:
            method = 'visit_' + node.__class__.__name__
            visitor = getattr(self, method, self.generic_visit)
            return visitor(node)
        else:
            return None

    def generic_visit(self, node):
        '''
        Método ejecutado si no se encuentra médodo aplicable visit_.
        Este examina el nodo para ver si tiene _fields, es una lista,
        o puede ser recorrido completamente.
        '''
        for field in getattr(node, "_fields"):
            value = getattr(node, field, None)
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, AST):
                        self.visit(item)
            elif isinstance(value, AST):
                self.visit(value)

# NO MODIFICAR


class NodeTransformer(NodeVisitor):
    '''
    Clase que permite que los nodos del arbol de sintaxis sean
    reemplazados/reescritos.  Esto es determinado por el valor retornado
    de varias funciones visit_().  Si el valor retornado es None, un
    nodo es borrado. Si se retorna otro valor, reemplaza el nodo
    original.

    El uso principal de esta clase es en el código que deseamos aplicar
    transformaciones al arbol de sintaxis.  Por ejemplo, ciertas
    optimizaciones del compilador o ciertas reescrituras de pasos
    anteriores a la generación de código.
    '''

    def generic_visit(self, node):
        for field in getattr(node, "_fields"):
            value = getattr(node, field, None)
            if isinstance(value, list):
                newvalues = []
                for item in value:
                    if isinstance(item, AST):
                        newnode = self.visit(item)
                        if newnode is not None:
                            newvalues.append(newnode)
                    else:
                        newvalues.append(n)
                value[:] = newvalues
            elif isinstance(value, AST):
                newnode = self.visit(value)
                if newnode is None:
                    delattr(node, field)
                else:
                    setattr(node, field, newnode)
        return node

# NO MODIFICAR


def flatten(top):
    '''
    Aplana el arbol de sintaxis dentro de una lista para efectos
    de depuración y pruebas.  Este retorna una lista de tuplas de
    la forma (depth, node) donde depth es un entero representando
    la profundidad del arból de sintaxis y node es un node AST
    asociado.
    '''
    class Flattener(NodeVisitor):

        def __init__(self):
            self.depth = 0
            self.nodes = []

        def generic_visit(self, node):
            self.nodes.append((self.depth, node))
            self.depth += 1
            NodeVisitor.generic_visit(self, node)
            self.depth -= 1

    d = Flattener()
    d.visit(top)
    return d.nodes
