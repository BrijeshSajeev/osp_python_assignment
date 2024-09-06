# Create a dictionary with name as key and marks of 3 subjects as values for 5 students. Print the name and average of marks as a dictionary.

def student_averages(students):
    return {name: sum(marks) / len(marks) for name, marks in students.items()}

# Sample input
students = {
    'John': [80, 90, 85],
    'Jane': [78, 90, 95],
    'Alice': [65, 75, 100],
    'Bob': [85, 87, 89],
    'Charlie': [90, 92, 85]
}

# Sample output
print(student_averages(students))

