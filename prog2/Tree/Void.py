from Tree import Node

class void(node):
    _Void__instance = None


    @staticmethod
    def getInstance():
        if Void._Void__instance == None:
            Void()
        return Void._Void__instance

    def __init__(self):
        if Void._Void__instance != None:
            raise Exception('singleton class')
        else:
        Void._Void__instance = self

    def print(self, n, p = false):
        pass


if __name__ == '__main__':
    v = Void.getInstance()
    v.print(0)