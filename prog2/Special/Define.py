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
        elif exp.getCdr().getCar().isPair():
            vari = exp.getCdr().getCar()
            params = vari.getCdr()
            name = vari.getCar()
            rest = exp.getCdr().getCdr()
            func = Cons(Ident('lambda'), Cons (params, rest))
            env.define(name, func.eval(env))
            return Nil.getInstance()
        else:
            vari = exp.getCdr().getCar()
            value = exp.getCdr().getCdr().getCar()
            if vari.isSymbol():
                if n == 3:
                    env.define(vari, value.eval(env))
            return Nil.getInstance()