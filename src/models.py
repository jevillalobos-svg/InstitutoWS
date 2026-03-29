from dataclasses import dataclass
from typing import Optional

@dataclass
class Student:
    id: int
    name: str
    email: str

@dataclass
class Course:
    id: int
    name: str
    description: str

@dataclass
class Enrollment:
    id: int
    student_id: int
    course_id: int