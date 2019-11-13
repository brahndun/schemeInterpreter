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
            return Nil.getInstance()
        else:
            f = exp.getCar().eval(env)
            a = Special.util.mapeval(exp.getCdr(), env)
            return f.apply(a)

    def print(self, t, n, p):
        Printer.printRegular(t, n, p)
