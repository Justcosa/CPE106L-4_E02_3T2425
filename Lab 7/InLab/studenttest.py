# filepath: student-score-analyzer/student-score-analyzer/src/studenttest.py
"""
File: studenttest.py
Tester program for the Student class.
"""

from student import Student

def main():
    """Test the Student class."""
    # Create a Student instance
    student = Student("Alice", 5)
    
    # Randomize scores
    student.randomizeScores(5, 70, 100)
    
    # Display student information
    print(student)
    
    # Set specific scores
    student.setScore(1, 85)
    student.setScore(2, 90)
    
    # Retrieve and print specific scores
    print("Score 1:", student.getScore(1))
    print("Score 2:", student.getScore(2))
    
    # Calculate and print average score
    print("Average Score:", student.getAverageScore())
    
    # Calculate and print statistics
    print("Mean:", student.getMean())
    print("Median:", student.getMedian())
    print("Mode:", student.getMode())
    print("Standard Deviation:", student.getStd())
    
    # Print high score
    print("High Score:", student.getHighScore())

if __name__ == "__main__":
    main()
