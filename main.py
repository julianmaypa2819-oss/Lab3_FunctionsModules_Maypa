# main.py
import grades
# Student Identity Configuration
LAST_NAME = "Maypa"
STUDENT_ID = "TUPM-25-0357"

SEED_DIGIT = int('TUPM-25-0357'[-1])
ID_SUM = sum(int(d) for d in 'TUPM-25-0357' if d.isdigit())
NAME_LENGTH: len('Maypa')

# Generate student-unique scores
scores = [
    7 * 10,
    22 % 100,
    5 * 7
]

average = grades.compute_average(scores)
grade = grades.assign_grade(average)
remark = grades.generate_remarks(grade)

print("=" * 40)
print(f"Student: {'Maypa'}")
print(f"Student ID: {'TUPM-25-0357'}")
print(f"Generated Scores: {scores}")
print(f"Average: {round(average,2)}")
print(f"Grade: {grade}")
print(f"Remark: {remark}")
print("=" * 40)