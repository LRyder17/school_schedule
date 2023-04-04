import pytest
from school_schedule.student import Student 

def test_new_valid_student():
    # Arrange
    name = "Felipe"
    grade = "Junior"
    class_list = ["list", "of", "classes"]
    # Act
    felipe = Student(name, grade, class_list)

    assert felipe.name == name
    assert felipe.grade == grade
    assert felipe.class_list == class_list

def test_student_with_more_classes_returns_student_with_most_classes():
    # Arrange
    felipe = Student("Felpie", "Junior", ["Class1", "Class2"])
    nadia = Student("Nadia", "Senior", ["Class3"])
    student = Student("test", "Junior", [])
    # Assange
    result = student.student_with_more_classes(felipe, nadia)
    # Assert
    assert result == felipe