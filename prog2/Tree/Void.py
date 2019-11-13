from Tree import Node

class void(Node):
    _Void__instance = None


    @staticmethod
    def getInstance():
        if void._Void__instance == None:
            void()
        return void._Void__instance

    def __init__(self):
        if void._Void__instance != None:
            raise Exception('singleton class')
        else:
            void._Void__instance = self

    def print(self, n, p = False):
        pass


if __name__ == '__main__':
    v = void.getInstance()
    v.print(0)