# If -- Parse tree node strategy for printing the special form if

from Tree import BoolLit
from Tree import Nil
#from Tree import Unspecific
from Print import Printer
from Special import Special

class If(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printIf(t, n, p)

    def eval(self, exp, env):
        n = Special.until.length(exp)
        if n < 3 or n > 4:
            self._error('expression error')
            return Nil.getInstance()
        temp0 = exp.getCdr().getCar()
        temp1 = exp.getCdr().getCdr().getCar()
        if n == 3:
            exp0 = Nil.getInstance()
        else:
            exp0 = exp.getCdr().getCdr().getCdr().getCar()
        if test.eval(env) != BoolLit.getInstance(False):
            return temp1.eval(env)
        else:
            return exp0.eval(env)