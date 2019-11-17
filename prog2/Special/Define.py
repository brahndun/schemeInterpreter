# Define -- Parse tree node strategy for printing the special form define

from Tree import Ident
from Tree import Nil
from Tree import Cons
#from Tree import Void
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
            var = exp.getCdr().getCar()
            if var.isSymbol():
                if n == 3:
                    val = exp.getCdr().getCdr().getCar()
                    env.define(var, val.eval(env))
                    return Nil.getInstance()
                if not var.isPair():
                    self._error('expression error')
                    return Nil.getInstance()
                name = var.getCar()
                params = var.getCdr()
                rest = exp.getCdr().getCdr()
                if not (name.isSymbol() and __checker(params)):
                    self._error('definition error')
                    return Nil.getInstance()
                func = Cons(Ident('lambda'), Cons(params, rest))
                env.define(name, func.eval(env))
            return Nil.getInstance()

        def __checker(self, parms):
            return parms.isNull() or parms.isSymbol() or parms.isPair() and parms.getCar().isSymbol() and self._Define__checkSymbols(parms.getCdr())