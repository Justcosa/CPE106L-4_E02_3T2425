import random

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"Student Name: {self.name}, GPA: {self.gpa}"

    # Equality based on name
    def __eq__(self, other):
        return self.name == other.name

    # Less than based on name
    def __lt__(self, other):
        return self.name < other.name

    # Greater than or equal based on name
    def __ge__(self, other):
        return self.name >= other.name


def project2():
    # Step 1: Create list of students
    students = [
        Student("Evan", 3.0),
        Student("Diana", 3.6),
        Student("Charlie", 3.2),
        Student("Alice", 3.9),
        Student("Bob", 3.5)
    ]

    print("Original List:")
    for student in students:
        print(student)

    # Step 2: Shuffle the list
    random.shuffle(students)
    print("\nShuffled List:")
    for student in students:
        print(student)

    # Step 3: Sort the list by name
    students.sort()
    print("\nSorted List (by name):")
    for student in students:
        print(student)


if __name__ == "__main__":
    project2()
