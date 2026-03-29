from .models import Student, Course, Enrollment

# In-memory storage
students = {}
courses = {}
enrollments = {}
next_student_id = 1
next_course_id = 1
next_enrollment_id = 1

# Student CRUD
def create_student(name: str, email: str) -> Student:
    global next_student_id
    student = Student(id=next_student_id, name=name, email=email)
    students[student.id] = student
    next_student_id += 1
    return student

def get_student(student_id: int) -> Student:
    return students.get(student_id)

def get_all_students() -> list[Student]:
    return list(students.values())

def update_student(student_id: int, name: str = None, email: str = None) -> bool:
    student = students.get(student_id)
    if student:
        if name:
            student.name = name
        if email:
            student.email = email
        return True
    return False

def delete_student(student_id: int) -> bool:
    if student_id in students:
        del students[student_id]
        # Also delete enrollments
        to_delete = [eid for eid, e in enrollments.items() if e.student_id == student_id]
        for eid in to_delete:
            del enrollments[eid]
        return True
    return False

# Course CRUD
def create_course(name: str, description: str) -> Course:
    global next_course_id
    course = Course(id=next_course_id, name=name, description=description)
    courses[course.id] = course
    next_course_id += 1
    return course

def get_course(course_id: int) -> Course:
    return courses.get(course_id)

def get_all_courses() -> list[Course]:
    return list(courses.values())

def update_course(course_id: int, name: str = None, description: str = None) -> bool:
    course = courses.get(course_id)
    if course:
        if name:
            course.name = name
        if description:
            course.description = description
        return True
    return False

def delete_course(course_id: int) -> bool:
    if course_id in courses:
        del courses[course_id]
        # Delete enrollments
        to_delete = [eid for eid, e in enrollments.items() if e.course_id == course_id]
        for eid in to_delete:
            del enrollments[eid]
        return True
    return False

# Enrollment CRUD
def create_enrollment(student_id: int, course_id: int) -> Enrollment:
    if student_id not in students or course_id not in courses:
        return None
    global next_enrollment_id
    enrollment = Enrollment(id=next_enrollment_id, student_id=student_id, course_id=course_id)
    enrollments[enrollment.id] = enrollment
    next_enrollment_id += 1
    return enrollment

def get_enrollment(enrollment_id: int) -> Enrollment:
    return enrollments.get(enrollment_id)

def get_all_enrollments() -> list[Enrollment]:
    return list(enrollments.values())

def update_enrollment(enrollment_id: int, student_id: int = None, course_id: int = None) -> bool:
    enrollment = enrollments.get(enrollment_id)
    if enrollment:
        if student_id and student_id in students:
            enrollment.student_id = student_id
        if course_id and course_id in courses:
            enrollment.course_id = course_id
        return True
    return False

def delete_enrollment(enrollment_id: int) -> bool:
    if enrollment_id in enrollments:
        del enrollments[enrollment_id]
        return True
    return False