# Regular -- Parse tree node strategy for printing regular lists

from Tree import Nil
from Print import Printer
from Special import Special

class Regular(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printRegular(t, n, p)

    def eval(self, exp, env):
        #sys.stdout.write('inside regular.eval')
        t = Special.util.length(exp)
        if t < 1:
            self._error("regular error")
            return Nil.getInstance()
        else:
            func = exp.getCar().eval(env)
            args = Special.util.mapeval(exp.getCdr(), env)
            return func.apply(args)