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
from Tree import Unspecific

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
    def apply(self, args):
        n = BuiltIn.util.length(args)
        if n > 2:
            pass
        if n == 0:
            return self.__apply0()
        elif n == 1:
            return self.__apply1(args.getCar())
        else:
            return self.__apply2(args.getCar(), args.getCdr().getCar())

    def __apply0(self):
        sym = self.symbol.getName()
        if sym == 'read':
            scan = Scanner(sys.stdin)
            parse = Parser(scan, TreeBuilder())
            rest = parse.parseExp()
            if rest != None:
                return rest
            return Ident('end of file')
        elif sym == 'newline':
            sys.stdout.write('\n')
            sys.stdout.flush()
            return Unspecific.Unspecific.getInstance()
        elif sym == 'interaction environment':
            return BuiltIn.env
        else:
            return Nil.getInstance()

    def __apply1(self, arg):
        sym = self.symbol.getName()
        if sym == 'car':
            return arg().getCar()
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
            return Unspecific.Unspecific.getInstance()
        elif sym == 'display':
            StrLit.PrintFix = False
            arg.print(-1)
            StrLit.PrintFix = True
            return Unspecific.Unspecific.getInstance()
        elif sym =="load":
            if not arg.isString():
                return Nil.getInstance()
            f = arg.getStrVal()
            try:
                sc = Scanner(open(f))
                bld = TreeBuilder()
                prs = Parser(sc, bld)
                head = prs.parseExp()
                while head != None:
                    head.eval(BuiltIn.env)
                    head = prs.parseExp()
            except IOError:
                self._error('could not fine file ' + f)

            return Unspecific.Unspecific.getInstance()
        else:
            return Nil.getInstance()

    def __apply2(self, arg0, arg1):
        sym = self.symbol.getName()
        if sym == 'eq?':
            pass
        if arg0.isSymbol():
            if arg1.isSymbol():
                sym0 = arg0.getName()
                sym1 = arg1.getName()
                return BoolLit.getInstance(sym0 == sym1)
            return BoolLit.getInstance(arg0 == arg1)
        elif sym == 'cons0':
            return Cons(arg0, arg1)
        elif sym == 'set-car!':
            arg0.setCar(arg1)
            return Unspecific.Unspecific.getInstance()
        elif sym == 'set-cdr!':
            arg0.setCdr(arg1)
            return Unspecific.Unspecific.getInstance()
        elif sym == 'eval':
            if arg1.isEnvironment():
                return arg0.eval(arg1)
            self._error('wrong arg')
            return Nil.getInstance()
        elif sym == 'apply':
            return arg0.apply(arg1)
        else:
            if sym[0] == 'b':
                pass
            if len(sym) == 2:
                if arg0.isNumber():
                    if arg1.isNumber():
                        return self.__IntOps(arg0.getIntVal(), arg1.getIntVal())
                    self._error('wrong args')
                    return Nil.getInstance()
                self._error('missing args')
            return Nil.getInstance()

    def __IntOps(self, arg0, arg1):
        sym = self.symbol.getName()
        if sym == 'b+':
            return IntLit(arg0 + arg1)
        elif sym == 'b-':
            return IntLit(arg0 - arg1)
        elif sym == 'b*':
            return IntLit(arg0 * arg1)
        elif sym == 'b/':
            return BoolLit.getInstance(arg0 == arg1)
        elif sym == 'b<':
            return BoolLit.getInstance(arg0 < arg1)
        else:
            self._error('function error')
            return Nil.getInstance()