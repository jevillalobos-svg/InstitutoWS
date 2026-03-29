import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from crud import (
    create_student, get_student, get_all_students, update_student, delete_student,
    create_course, get_course, get_all_courses, update_course, delete_course,
    create_enrollment, get_enrollment, get_all_enrollments, update_enrollment, delete_enrollment
)

def test_students():
    # Create
    s = create_student("Test Student", "test@example.com")
    assert s.id == 1
    assert s.name == "Test Student"

    # Get
    s2 = get_student(1)
    assert s2 == s

    # Update
    update_student(1, name="Updated Name")
    assert get_student(1).name == "Updated Name"

    # Delete
    delete_student(1)
    assert get_student(1) is None

def test_courses():
    c = create_course("Test Course", "Description")
    assert c.id == 1
    assert c.name == "Test Course"

    update_course(1, description="Updated Desc")
    assert get_course(1).description == "Updated Desc"

    delete_course(1)
    assert get_course(1) is None

def test_enrollments():
    s = create_student("Student", "email")
    c = create_course("Course", "Desc")
    e = create_enrollment(s.id, c.id)
    assert e.id == 1
    assert e.student_id == s.id

    delete_enrollment(1)
    assert get_enrollment(1) is None

if __name__ == "__main__":
    test_students()
    test_courses()
    test_enrollments()
    print("All tests passed!")