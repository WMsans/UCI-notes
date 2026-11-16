from problem3 import Student, Club
import random
import unittest


class StudentTest(unittest.TestCase):
    def test_has_id_given_when_created(self):
        student1 = Student(12345, 'Ada Lovelace')
        student2 = Student(34567, 'Grace Hopper')

        self.assertEqual(student1.student_id(), 12345)
        self.assertEqual(student2.student_id(), 34567)


    def test_has_name_given_when_created(self):
        student = Student(12345, 'Ada Lovelace')

        self.assertEqual(student.name(), 'Ada Lovelace')



class ClubTest(unittest.TestCase):
    def setUp(self):
        self._club = Club()
        self._student_ids = list(range(1000, 9999))
        random.shuffle(self._student_ids)

        
    def test_new_clubs_have_no_students(self):
        self.assertEqual(self._club.number_of_students(), 0)


    def test_after_adding_student__has_1_student(self):
        self._club.add_student(self._create_test_student())
        self.assertEqual(self._club.number_of_students(), 1)


    def test_continuing_to_add_students_means_more_students(self):
        for student_count in range(1, 101):
            self._club.add_student(self._create_test_student())
            self.assertEqual(self._club.number_of_students(), student_count)


    def test_adding_student_with_id_already_in_club_is_an_error(self):
        existing = self._create_test_student()
        duplicate = Student(existing.student_id(), 'Somebody Else')
        self._club.add_student(existing)

        with self.assertRaises(ValueError):
            self._club.add_student(duplicate)


    def test_failed_addition_keeps_the_original_student(self):
        existing = self._create_test_student()
        self._club.add_student(existing)

        with self.assertRaises(ValueError):
            self._club.add_student(Student(existing.student_id(), 'Somebody Else'))

        self.assertIs(self._club.student_with_id(existing.student_id()), existing)
        self.assertEqual(self._club.number_of_students(), 1)


    def test_student_in_club_is_found_by_id(self):
        student = self._create_test_student()
        self._club.add_student(student)

        self.assertIs(self._club.student_with_id(student.student_id()), student)


    def test_student_not_in_club_gives_none(self):
        self.assertIsNone(self._club.student_with_id(12345))


    def test_only_the_requested_student_is_found(self):
        students = [self._create_test_student() for _ in range(5)]

        for student in students:
            self._club.add_student(student)

        self.assertIs(self._club.student_with_id(students[3].student_id()),
                      students[3])


    def test_found_student_keeps_its_name(self):
        student = Student(self._student_ids.pop(), 'Ada Lovelace')
        self._club.add_student(student)

        self.assertEqual(self._club.student_with_id(student.student_id()).name(),
                         'Ada Lovelace')


    def _create_test_student(self):
        return Student(self._student_ids.pop(), 'Test Student')



if __name__ == '__main__':
    unittest.main()
