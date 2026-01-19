class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"{self.name} has been created")
    def __del__(self):
        print(f"{self.name} has been destroyed")

p1=person("nikhil",22)
del p1            
    