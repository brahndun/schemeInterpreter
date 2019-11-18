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
        #sys.stdout.write('inside define.eval')
        t = Special.util.length(exp)
        if t < 3:
            self._error("define error")
            return Nil.getInstance()
        elif exp.getCdr().getCar().isPair():
            vars = exp.getCdr().getCar()
            parms = vars.getCdr()
            sym = vars.getCar()

            rest = exp.getCdr().getCdr()
            func = Cons(Ident("lambda"), Cons(parms, rest))
            env.define(sym, func.eval(env))
            return Nil.getInstance()
        else:
            vars = exp.getCdr().getCar()
            val = exp.getCdr().getCdr().getCar()
            if vars.isSymbol():
                if t == 3:
                    env.define(vars, val.eval(env))
            return Nil.getInstance()