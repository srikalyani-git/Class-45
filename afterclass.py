class expression:
    def __init__(self,num1,num2,num3):
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.num3 = int(num3)
    
    def add(self):
        print(self.num1 + self.num2 + self.num3, "Is the sum")

one = expression("5",7,9)
one.add()