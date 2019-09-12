from lesson import Lesson
from lesson_schedule import LessonSchedule

lesson1 = Lesson('Monday', 8, 0, 'Polish')
lesson2 = Lesson('Monday', 8, 50, 'English')
lesson3 = Lesson('Tuesday', 9, 45, 'Math')
lesson4 = Lesson('Monday', 8, 0, 'Polish')

lesson_schedule = LessonSchedule()
lesson_schedule.addLesson(lesson1)
lesson_schedule.addLesson(lesson2)
lesson_schedule.addLesson(lesson3)
lesson_schedule.addLesson(lesson4)

lesson_schedule.print_all()