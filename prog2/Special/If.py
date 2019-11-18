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
        #sys.stdout.write('inside apply.eval')
        t = Special.util.length(exp)
        if t < 3 or t > 4:
            self._error("special if error")
            return Nil.getInstance()
        temp = exp.getCdr().getCar()
        temp1 = exp.getCdr().getCdr().getCar()
        if t == 3:
            eexp = Nil.getInstance()
        else:
            eexp = exp.getCdr().getCdr().getCdr().getCar()
        if temp.eval(env) != BoolLit.getInstance(False):
            return temp1.eval(env)
        else:
            return eexp.eval(env)