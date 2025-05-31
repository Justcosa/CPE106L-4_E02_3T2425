import random

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"Student Name: {self.name}, GPA: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

def project2():
    students = [
        Student("Evan", 3.0),
        Student("Diana", 3.6),
        Student("Charlie", 3.2),
        Student("Alice", 3.9),
        Student("Bob", 3.5)
    ]

    print("\nOriginal List:")
    for student in students:
        print(student)

    random.shuffle(students)
    print("\nShuffled List:")
    for student in students:
        print(student)

    students.sort()
    print("\nSorted List (by name):")
    for student in students:
        print(student)

if __name__ == "__main__":
    project2()
