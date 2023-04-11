#this is a student class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

if __name__ == '__main__':
    s1 = Student("William", 12)
