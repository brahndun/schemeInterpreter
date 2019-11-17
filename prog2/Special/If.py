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
        n = Special.util.length(exp)
        if n < 3 or n > 4:
            self._error('expression error')
            return Nil.getInstance()
        temp0 = exp.getCdr().getCar()
        temp1 = exp.getCdr().getCdr().getCar()
        if n == 3:
            envexp = Nil.getInstance()
        else:
            envexp = exp.getCdr().getCdr().getCdr().getCar()
        if temp0.eval(env) != BoolLit.getInstance(False):
            return temp1.eval(env)
        else:
            return envexp.eval(env)