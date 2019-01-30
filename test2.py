class FibO:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def fiboSum(self, obj):
        self.x += obj.x
        self.y += obj.y
        self.z += obj.z

    def getCoord(self):
        print(self.x, self.y, self.z)

    def deepCopy(self, obj):
        self.x, self.y, self.z = obj.x, obj.y, obj.z

obj1 = FibO(1,2,3)
obj2 = FibO(4,5,6)
obj3 = FibO(obj1.x, obj1.y, obj1.z)
obj3.fiboSum(obj2)
obj1.getCoord()
obj2.getCoord()
obj3.getCoord()
