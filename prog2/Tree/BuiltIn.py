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

        t = BuiltIn.util.length(args)
        #sys.stdout.write('apply called')
        if t > 2:
            self._error("Too many arguments1")
        if t == 0:
            #sys.stdout.write('apply0 called')
            return self.__apply0()
        elif t == 1:
            #sys.stdout.write('apply1 called')
            return self.__apply1(args.getCar())
        else:
            #sys.stdout.write('apply2 called')
            return self.__apply2(args.getCar(), args.getCdr().getCar())

    def __apply0(self):
        #sys.stdout.write('inside apply0')
        sym = self.symbol.getName()
        if sym == "read":
            scan = Scanner(sys.stdin)
            parse = Parser(scan, TreeBuilder())
            rest = parse.parseExp()
            if rest != None:
                return rest
            return Ident("end-of-file")
        elif sym == "newline":
            sys.stdout.write('\n')
            sys.stdout.flush()
            return Nil.getInstance()
        elif sym == "interaction-environment":
            return BuiltIn.env
        else:
            self._error("argument error 0")
            return Nil.getInstance()

    def __apply1(self, arg):
        #sys.stdin.write('inside apply1')
        sym = self.symbol.getName()
        if sym == "car":
            return arg.getCar()
        elif sym == "cdr":
            return arg.getCdr()
        elif sym == "number?":
            return BoolLit.getInstance(arg.isNumber())
        elif sym == "symbol?":
            return BoolLit.getInstance(arg.isSymbol())
        elif sym == "null?":
            return BoolLit.getInstance(arg.isNull())
        elif sym == "pair?":
            return BoolLit.getInstance(arg.isPair())
        elif sym == "procedure?":
            return BoolLit.getInstance(arg.isProcedure())
        elif sym == "write":
            arg.print(-1)
            return Nil.getInstance()
        elif sym == "display":
            StrLit.DoubleQuotes = False
            arg.print(-1)
            StrLit.DoubleQuotes = True
            return Nil.getInstance()
        elif sym == "load":
            #sys.stdout.write('load successful')
            if not arg.isString():
                self._error("first argument error")
                return Nil.getInstance()
            f = arg.getStrVal()
            #sys.stdout.write('before try')
            try:
                scan = Scanner(open(f))
                #sys.stdout.write('1')
                build = TreeBuilder()
                #sys.stdout.write('2')
                parse = Parser(scan, build)
                #sys.stdout.write('3')
                head = parse.parseExp()
                #sys.stdout.write('4')
                while head != None:
                    head.eval(BuiltIn.env)
                    #sys.stdout.write('loop1')
                    head = parse.parseExp()
                    #sys.stdout.write('loop2')

            except IOError:
                self._error("file not found " + f )

            return Nil.getInstance()
        else:
            self._error("first argument error")
            return Nil.getInstance()

    def __apply2(self, arg1, arg2):
        #sys.stdout.write('inside apply2')
        sym = self.symbol.getName()
        if sym == "eq?":
            return BoolLit.getInstance(arg1 is arg2)
        elif sym == "cons":
            return Cons(arg1, arg2)
        elif sym == "set-car!":
            arg1.setCar(arg2)
            return Nil.getInstance()
        elif sym == "set-cdr!":
            arg1.setCdr(arg2)
            return Nil.getInstance()
        elif sym == "eval":
            if arg2.isEnvironment():
                return arg1.eval(arg2)
            self._error("second argument error")
            return Nil.getInstance()
        elif sym == "apply":
            return arg1.apply(arg2)
        else:
            if sym[0] == "b":
                pass
            if len(sym) == 2:
                if arg1.isNumber():
                    if arg2.isNumber():
                        return self.__IntOps(arg1.getIntVal(), arg2.getIntVal())
                    self._error("argument error")
                    return Nil.getInstance()
                self._error("argument error")
            return Nil.getInstance()

    def __IntOps(self, arg1, arg2):
        sym = self.symbol.getName()
        if sym == "b+":
            return IntLit(arg1 + arg2)
        elif sym == "b-":
            return IntLit(arg1 - arg2)
        elif sym == "b*":
            return IntLit(arg1 * arg2)
        elif sym == "b/":
            return IntLit(arg1 / arg2)
        elif sym == "b=":
            return BoolLit.getInstance(arg1 == arg2)
        elif sym == "b<":
            return BoolLit.getInstance(arg1 < arg2)
        else:
            self._error("Unknown BuiltIn function")
            return Nil.getInstance()