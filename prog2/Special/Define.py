# Define -- Parse tree node strategy for printing the special form define

from Tree import Ident
from Tree import Nil
from Tree import Cons
from Tree import Void
from Print import Printer
from Special import Special

class Define(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printDefine(t, n, p)

    def eval(self, exp, env):
        n = Special.util.length(exp)
        if n < 3:
            self._error('expression error')
            return Nil.getInstance()
        else:
            vb = exp.getCdr().getCar()
            if vb.isSymbol():
                if n == 3:
                    value = exp.getCdr().getCdr().getCar()
                    env.define(vb, value.eval(env))
                    return Nil.getInstance()
                if not vb.isPair():
                    self._error('expression error')
                    return Nil.getInstance()
                name = vb.getCar()
                params = vb.getCdr()
                rest = exp.getCdr().getCdr()
                if not (name.isSymbol() and self.__checker(params)):
                    self._error('definition error')
                    return Nil.getInstance()
                func = Cons(Ident('lambda'), Cons(params, rest))
                env.define(name, func.eval(env))
            return Nil.getInstance()

    def __checker(self, params):
            return params.isNull() or params.isSymbol() or params.isPair() and params.getCar().getSymbol() and self.__checker(params.getCdr())