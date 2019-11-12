# Begin -- Parse tree node strategy for printing the special form begin

from Tree import Nil
from Print import Printer
from Special import Special
import Util

class Begin(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printBegin(t, n, p)

    def eval(self, t, n, p):
        n = Special.util.length(exp)
        if n < 2:
            return Nil.getInstance()
        else:
            return Special.util.begin(exp.getCdr(), env)
