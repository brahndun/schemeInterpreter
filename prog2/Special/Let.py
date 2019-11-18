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
    #sys.stdout.write('inside static define')
    def __define(bind, env, lenv):
        if bind.isNull():
            return 0
        else:
            b = bind.getCar()
            if Special.util.length(b) != 2:
                return -1
            vars = b.getCar()
            val = b.getCdr().getCar().eval(env)
            lenv.define(vars, val)
            return Let.__define(bind.getCdr(), env, lenv)

    def eval(self, exp, env):
        #sys.stdout.write('inside let.eval')
        t = Special.util.length(exp)
        if t < 3:
            self._error("first let error")
            return Nil.getInstance()
        name = exp.getCdr().getCar()
        rest = exp.getCdr().getCdr()
        t = Special.util.length(bind)
        if t < 1:
            self._error("second let error")
            return Nil.getInstance()
        lenv = Environment(env)
        if Let.__define(name, env, lenv) < 0:
            self._error("third let error")
            return Nil.getInstance()
        else:
            return Special.util.begin(rest, lenv)