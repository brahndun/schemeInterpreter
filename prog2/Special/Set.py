# Set -- Parse tree node strategy for printing the special form set!

from Tree import Nil
from Tree import Unspecific
from Print import Printer
from Special import Special

class Set(Special):
    def __init__(self):
        pass
    def print(self, t, n, p):
        Printer.printSet(t, n, p)

    def eval(self, exp, env):
        n = Special.util.length(exp)
        if n != 3:
            self._error('expression error')
            return Nil.getInstance()
        else:
            vb = exp.getCdr().getCar()
            vl = exp.getCdr().getCdr().getCar()
            env.assign(vb, vl.eval(env))
            return Unspecific.Unspecific.getInstance()