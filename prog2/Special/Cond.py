# Cond -- Parse tree node strategy for printing the special form cond

from Tree import BoolLit
from Tree import Nil
#from Tree import Unspecific
from Print import Printer
from Special import Special

class Cond(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printCond(t, n, p)

    def eval(self, exp, env):
        n = Special.util.length(exp)
        if n < 2:
            self._error("cond error")
            return Nil.getInstance()
        else:
            return self.__evaluate(exp.getCdr(), env)

    def __evaluate(self, exp, env):
        if exp.isNull():
            return Nil.getInstance()
        cnd = exp.getCar()
        if Special.util.length(cnd) < 1:
            self._error("first cond error")
            return Nil.getInstance()
        name = cnd.getCar()
        rest = cnd.getCdr()
        if name.isSymbol():
            if test.getName() == "else":
                if not (rest.isNull() or exp.getCdr().isNull()):
                    self._error("second cond error")
                    return Nil.getInstance()
                return Special.util.begin(rest, env)
            val = test.eval(env)
            if val != BoolLit.getInstance(False):
                if rest.isNull():
                    return val
        t = rest.getCar()
        if t.isSymbol():
            if t.getName() == "=>":
                if Special.util.length(rest) != 2:
                    self._error("third cond error")
                    return Nil.getInstance()
                func = body.getCdr().getCar().eval(env)
                return func.apply(val)
            return Special.util.begin(body, env)
        else:
            return self.__evalClauses(exp.getCdr(), env)

    def eval(self, exp, env):
        n = Special.util.length(exp)
        if n < 2:
            self._error("fourth cond error")
            return Nil.getInstance()
        else:
            return self.__evalClauses(exp.getCdr(), env)