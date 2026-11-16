class Student:
    def __init__(self, student_id: int, name: str):
        self._student_id = student_id
        self._name = name


    def student_id(self) -> int:
        return self._student_id


    def name(self) -> str:
        return self._name



class Club:
    def __init__(self):
        self._students = {}


    def number_of_students(self) -> int:
        return len(self._students)


    def add_student(self, student_to_add: Student) -> None:
        if student_to_add.student_id() in self._students:
            raise ValueError(f'student {student_to_add.student_id()} already in club')

        self._students[student_to_add.student_id()] = student_to_add


    def student_with_id(self, student_id: int) -> Student | None:
        return self._students.get(student_id)
