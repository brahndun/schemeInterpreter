# Regular -- Parse tree node strategy for printing regular lists

from Tree import Nil
from Print import Printer
from Special import Special

class Regular(Special):
    def __init__(self):
        pass

    def eval(self, exp, env):
        n = Special.util.length(exp)
        if n < 1:
            self._error('expression error')
            return Nil.getInstance()
        else:
            func = exp.getCar().eval(env)
            args = Special.util.mapeval(exp.getCdr(), env)
            return func.apply(args)

    def print(self, t, n, p):
        Printer.printRegular(t, n, p)
