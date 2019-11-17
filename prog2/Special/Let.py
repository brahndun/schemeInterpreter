# Let -- Parse tree node strategy for printing the special form let

from Tree import Nil
from Tree import Environment
from Print import Printer
from Special import Special

class Let(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printLet(t, n, p)

    @staticmethod
    def __define(bind, env, eenv):
        if bind.isNull():
            return 0
        else:
            b = bind.getCar()
            if Special.util.length(b) != 2:
                return -1
            temp0 = b.getCar()
            temp1 = b.getCdr().getCar().eval(env)
            eenv.define(temp0, temp1)
            return Let.__define(bind.getCdr(), env, eenv)

    def eval(self, exp, env):
        n = Special.util.length(exp)
        if n < 3:
            self._error('expression error')
            return Nil.getInstance()
        desc = exp.getCdr().getCar()
        rest = exp.getCdr().getCdr()
        n = Special.util.length(desc)
        if n < 1:
            self._error('expression error')
            return Nil.getInstance()
        eenv = Environment(env)
        if Let.__define(desc, env, eenv) < 0:
            self._error('expression error')
            return Nil.getInstance()
        else:
            return Special.util.begin(rest, eenv)