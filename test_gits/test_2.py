
class Pile:
    data = list()
    
    def __init__(self) -> None:
        pass
    def push(self, x):
        self.data.append(x)
    def pop(self):
        self.data.pop()
    def top(self,x):
        self.data.insert(0,x)
    