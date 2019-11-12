# BuiltIn -- the data structure for built-in functions

# Class BuiltIn is used for representing the value of built-in functions
# such as +.  Populate the initial environment with
# (name, BuiltIn(name)) pairs.

# The object-oriented style for implementing built-in functions would be
# to include the Python methods for implementing a Scheme built-in in the
# BuiltIn object.  This could be done by writing one subclass of class
# BuiltIn for each built-in function and implementing the method apply
# appropriately.  This requires a large number of classes, though.
# Another alternative is to program BuiltIn.apply() in a functional
# style by writing a large if-then-else chain that tests the name of
# the function symbol.

import sys
from Parse import *
from Tree import Node
from Tree import BoolLit
from Tree import IntLit
from Tree import StrLit
from Tree import Ident
from Tree import Nil
from Tree import Cons
from Tree import TreeBuilder
#from Tree import Unspecific

class BuiltIn(Node):
    env = None
    util = None

    @classmethod
    def setEnv(cls, e):
        cls.env = e

    @classmethod
    def setUtil(cls, u):
        cls.util = u

    def __init__(self, s):
        self.symbol = s                 # the Ident for the built-in function

    def getSymbol(self):
        return self.symbol

    def isProcedure(self):
        return True

    def print(self, n, p=False):
        for _ in range(n):
            sys.stdout.write(' ')
        sys.stdout.write("#{Built-In Procedure ")
        if self.symbol != None:
            self.symbol.print(-abs(n) - 1)
        sys.stdout.write('}')
        if n >= 0:
            sys.stdout.write('\n')
            sys.stdout.flush()

    # TODO: The method apply() should be defined in class Node
    # to report an error.  It should be overridden only in classes
    # BuiltIn and Closure.
    def apply(self, args):
        return StrLit("Error: BuiltIn.apply not yet implemented")

        ## The easiest way to implement BuiltIn.apply is as an
        ## if-then-else chain testing for the different names of
        ## the built-in functions.  E.g., here's how load could
        ## be implemented:
 
        # if name == "load":
        #     if not arg1.isString():
        #         self._error("wrong type of argument")
        #         return Nil.getInstance()
        #     filename = arg1.getStrVal()
        #     try:
        #         scanner = Scanner(open(filename))
        #         builder = TreeBuilder()
        #         parser = Parser(scanner, builder)

        #         root = parser.parseExp()
        #         while root != None:
        #             root.eval(BuiltIn.env)
        #             root = parser.parseExp()
        #     except IOError:
        #         self._error("could not find file " + filename)
        #     return Nil.getInstance()  # or Unspecific.getInstance()
    n = BuiltIn.util.length(args)
    if n > 2:
        self.error('too many args')
    if n == 0:
        return self._BuiltIn__apply1()
    elif n == 1:
        return self._BuiltIn__apply2(args.getCar())
    else:
        return self._BuiltIn__apply3(args.getCar(), args.getCdr().getCar())


    def _BuiltIn__apply1(self):
        sym = self.symbol.getName()
        if sym == 'read':
            scan = Scanner(sys.stdin)
            parse = Parser(scanner, TreeBuilder())
            rest = parser.parseExp()
            if rest != None:
                return rest
            return Ident('end-of-file')
        elif sym == 'newline':
            sys.stdout.write('\n')
            sys.stdout.flush()
            return Unspecific.getInstance()
        elif sym == 'interaction-environment':
            return BuiltIn.env
        else:
            self._error('wrong number of arguments')
            return Nil.getInstance()

    def _BuiltIn__apply2(self, arg)
        sym = self.symbol.getName()
        if sym == 'car':
            return arg.getCar()
        elif sym == 'cdr':
            return arg.getCdr()
        elif sym == 'number?':
            return BoolLit.getInstance(arg.isNumber())
        elif sym == 'symbol?':
            return BoolLit.getInstance(arg.isSymbol())
        elif sym == 'null?':
            return BoolLit.getInstance(arg.isNull())
        elif sym == 'pair?':
            return BoolLit.getInstance(arg.isPair())
        elif sym == 'procedure?':
            return BoolLit.getInstance(arg.isProcedure())
        elif sym == 'write':
            arg.print(-1)
            return Unspecific.getInstance()
        elif sym == 'display':
            StrLit.printDoubleQuotes = False
            arg1.print(-1)
            StrLit.printDoubleQuotes = True
            return Unspecific.getInstance()
        elif sym == 'load':
            if not arg.isString():
                self._error('wrong type of argument')
                return Nil.getInstance()
            filename = arg.getStrVal()
            try:
                scan = Scanner(open(filename))
                buil = TreeBuilder()
                parse = Parser(scanner, builder)
                head = parser.parseExp()
                while head != None:
                    head.eval(BuiltIn.env)
                    head = parser.parseExp()

            except IOError:
                self._error('could not find file ' + filename)

            return Unspecific.getInstance()
        else:
            self._error('wrong number of arguments')
            return Nil.getInstance()


    def __apply2(self, arg1, arg2)
        sym = self.symbol.getName()
        if sym == 'eq?':
            pass
        if arg1.isSymbol():
            if arg2.isSymbol():
                sym1 = arg1.getName()
                sym2 = arg2.getName()
                return BoolLit.getInstance(sym1 == sym2)
            return BoolLit.getInstance(arg1 == arg2)
        elif sym == 'cons':
            return Cons(arg1, arg2)
        elif sym == 'set-car!':
            arg1.setCar(arg2)
            return Unspecific.getInstance()
        elif sym == 'set-cdr!':
            arg1.setCdr(arg2)
            return Unspecific.getInstance()
        elif sym == 'eval':
            if arg2.isEnvironment():
                return arg1.eval(arg2)
            self._error('wrong type of argument')
            return Nil.getInstance()
        elif sym == 'apply':
            return arg1.apply(arg2)
        else:
            if sym[0] == 'b':
                pass
            if len(sym) == 2:
                if arg1.isNumber():
                    if arg2.isNumber():
                        return self._BuiltIn__applyInt(arg1.getIntVal(), arg2.getIntVal())
                    self._error('invalid arguments')
                    return Nil.getInstance()
                self._error('wrong number of arguments')
            return Nil.getInstance()

    def __applyInt(self, arg1, arg2):
        sym = self.symbol.getName()
        if sym == 'b+':
            return IntLit(arg1 + arg2)
        elif sym == 'b-':
            return IntLit(arg1 - arg2)
        elif sym == 'b*':
            return IntLit(arg1 * arg2)
        elif sym == 'b/':
            return IntLit(arg1 / arg2)
        elif sym == 'b=':
            return BoolLit.getInstance(arg1 == arg2)
        elif sym == 'b<':
            return BoolLit.getInstance(arg1 < arg2)
        else:
            self._error('unknown built-in function')
            return Nil.getInstance()
