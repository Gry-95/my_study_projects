from django.test import TestCase
from django.urls import reverse
from .models import Student


class StudentModelTestCase(TestCase):

    @staticmethod
    def print_info(message):
        count = Student.objects.count()
        print(f"{message}: #all_students={count}")

    def setUp(self):
        print('-' * 20)
        self.print_info('Start setUp')
        self.student = Student.objects.create(first_name='Test name', last_name='Test lastname', age=19, email="qwe@ro.ru")
        Student.objects.create(first_name='Test name2', last_name='Test lastname2', age=29, email="qweqwase@ro.ru")
        Student.objects.create(first_name='Test name3', last_name='Test lastname3', age=39, email="qweqwe@ro.ru")
        self.print_info('Finish setUp')

    def test_student_creation(self):
        # Проверка создания объекта Student
        self.print_info('Start test_student_creation')
        self.assertEqual(self.student.first_name, 'Test name')
        self.assertEqual(self.student.last_name, 'Test lastname')
        self.assertEqual(self.student.age, 19)
        self.assertEqual(self.student.email, 'qwe@ro.ru')
        self.print_info('Finish test_movie_creation')

    def test_student_get_all(self):
        # Проверка получения всех записей из бд
        self.print_info('Start test_student_get_all')
        students = Student.objects.all()
        self.assertEqual(len(students), 3)
        self.print_info('Finish test_student_get_all')