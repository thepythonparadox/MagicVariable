class Employee:
    def method1(self):
        print("this is method 1")

    def __str__(self):
        return("This is from Employee class")

    def __repr__(self):
        return "This is repr method from Employee class"

e = Employee()
print(e)