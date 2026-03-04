class employee:
    def __init__(self,name):
        self.name = name
        print("My name is",name)
    def __del__(self):
        print("destructor called, employee deleted")

em1 = employee("joe")
del em1
print(em1.name)