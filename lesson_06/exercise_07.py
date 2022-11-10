class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_info(self):
        if self.grade <= 2:
            return f"{self.name} has failed."
        else:
            return f"{self.name} has graduated."


s1 = Student("Victor", 2)
s2 = Student("John", 1)
s3 = Student("Bob", 3)

print(s1.get_info())
print(s2.get_info())
print(s3.get_info())

