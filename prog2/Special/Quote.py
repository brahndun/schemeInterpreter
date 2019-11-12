# Quote -- Parse tree node strategy for printing the special form quote

from Tree import Nil
from Print import Printer
from Special import Special

class Quote(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printQuote(t, n, p)

    def eval(self, exp, env):
        n = Special.util.length(exp)
        if n != 2:
            self._error('expression error')
            return Nil.getInstance()
        else:
            return exp.getCdr().getCar()