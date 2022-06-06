def add_numbers(x,y):
    result = x + y
    return result
print()

def mult_numbers(x,y):
    result = x * y
    return result
print()

def div_numbers(x,y):
    result = x/y
    return result
print()

def sub_numbers(x,y):
    result = x-y
    return result
    

class student:
    def _init_(self,name,hobby,year_of_birth):
        self.name = name
        self.hobby = hobby
        self.year_of_birth = year_of_birth

    def greet_student(name):
        print("Hello from" +name.title())

