class C1:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def display(self):
        print("a = ",self.a)
        print("b = ",self.b)


class C2(C1):               #C1 is base class and C2 is derived class
    def __init__(self,a,b,c,d):
        super(C2,self).__init__(a,b)
        self.c = c
        self.d = d
    def display(self):
        super(C2,self).display()
        print("c = ",self.c)
        print("d = ",self.d)


obj1 = C1(1,2)
obj1.display()
obj2 = C2(10,20,30,40)
obj2.display()