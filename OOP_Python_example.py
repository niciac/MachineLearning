# from Partick Loeber tutorial on youtube @ python engineer

# position, name, age, position, salary
se1 = ["Software Engineer", "Max", 20, "Junion", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]
d1 = ["Designer", "Philipp"]

# # any person can work in function code
# def code(se):
#     print(f"{se[1]} is writing code")

# code(se1)
# code(se2)
# code(d1)


# this is a class
class SoftwareEngineer:
    
    # class attributes
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    # instance method
    def code(self):
        print(f"{self.name} is writing code")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")
    
    def information(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information


#instance of the class
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
# print(se1.name, se1.age)

# print(SoftwareEngineer.alias)

se2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
# print(se2.alias)

# recap
# create a class (blueprint)
#  create a instance (object)
# class vs instance
# instance attributes: defined in __init__(self)
# class attribute

# se1.code()
# se2.code()
se1.code_in_language("Python")
se2.code_in_language("C++")

print(se1.information())

