# Set -- Parse tree node strategy for printing the special form set!

from Tree import Nil
#from Tree import Unspecific
from Print import Printer
from Special import Special

class Set(Special):
    def __init__(self):
        pass
    
    def print(self, t, n, p):
        Printer.printSet(t, n, p)

    def eval(self, exp, env):
        #sys.stdout.write('inside set.eval')
        t = Special.util.length(exp)
        if t != 3:
            self._error("set error")
            return Nil.getInstance()
        else:
            vars = exp.getCdr().getCar()
            val = exp.getCdr().getCdr().getCar()
            env.assign(vars, val.eval(env))
            return Nil.getInstance()