import sys
from Tree import Node

class Unspecific(Node):
    _Unspecific__instance = None

    @staticmethod
    def getInstance():
        if Unspecific._Unspecific__instance == None:
            Unspecific()
        return Unspecific._Unspecific__instance

    def __init__(self):
        if Unspecific._Unspecific__instance != None:
            raise Exception('Singleton instance')
        else:
            Unspecific._Unspecific__instance = self

    def print(self, n, p=False):
        for _ in range(n):
            sys.stdout.write(' ')

        sys.stdout.write('#{Unspecific}')
        if n >= 0:
            sys.stdout.write('\n')
            sys.stdout.flush()


if __name__ == '__main__':
    n = Unspecific.getInstance()
    n.print(0)