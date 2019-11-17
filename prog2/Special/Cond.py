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
            self._error('expression error')
            return Nil.getInstance()
        else:
            return Cond.__evaluate(self, exp.getCdr(), env)

    def __evaluate(self, exp, env):
        if exp.isNull():
            return Nil.getInstance()
        car = exp.getCar()
        if Special.util.length(car) < 1:
            self._error('expression error')
            return Nil.getInstance()
        caar = car.getCar()
        cadr = car.getCdr()
        if caar.isSymbol():
            if caar.getName() == 'else':
                if not (cadr.isNull() or exp.getCdr().isNull()):
                    self._error('expression error')
                    return Nil.getInstance()
                return Special.util.begin(cadr, env)
            value = caar.eval(env)
            if value != BoolLit.getInstance(False):
                if cadr.isNull():
                    return value
        cadar = cadr.getCar()
        if cadar.isSymbol():
            if cadar.getName() == '=>':
                if Special.util.length(cadr) != 2:
                    self._error('expression error')
                    return Nil.getInstance()
                func = cadr.getCdr().getCar().eval(env)
                return func.apply(value)
            return Special.util.begin(cadr, env)
        else:
            return self.__evaluate(exp.getCdr(), env)


