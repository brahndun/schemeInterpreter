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
            return self.__evaluate(exp.getCdr(), env)

    def __evaluate(self, exp, env):
        if exp.isNull():
            return Nil.getInstance()
        car = exp.getCar()
        if Special.util.length(car) < 1:
            self._error('expression error')
            return Nil.getInstance()
        head = car.getCar()
        rest = car.getCdr()
        if head.isSymbol():
            if head.getName() == 'else':
                if not (rest.isNull() or exp.getCdr().isNull()):
                    self._error('expression error')
                    return Nil.getInstance()
                return Special.util.begin(rest, env)
            value = head.eval(env)
            if value != BoolLit.getInstance(False):
                if rest.isNull():
                    return value
        other = rest.getCar()
        if other.isSymbol():
            if other.getName() == '=>':
                if Special.util.length(rest) != 2:
                    self._error('expression error')
                    return Nil.getInstance()
                func = rest.getCdr().getCar().eval(env)
                return func.apply(value)
            return Special.util.begin(rest, env)
        else:
            return self.__evaluate(exp.getCdr(), env)


