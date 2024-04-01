import csv
from faker import Faker
import random

fake = Faker()

def generate_student_data_balanced(num_students):
    student_data = []
    grade_counts = {
        'A': int(num_students * 0.3),
        'B': int(num_students * 0.2),
        'C': int(num_students * 0.15),
        'D': int(num_students * 0.15),
        'E': int(num_students * 0.1),
        'F': int(num_students * 0.1)
    }

    for grade, count in grade_counts.items():
        for _ in range(count):
            # Generate random values for all factors
            age = random.randint(18, 25)
            gender = random.choice(['Male', 'Female'])
            marital_status = random.choice(['Single', 'Married', 'Engaged'])
            children = random.randint(0, 5) if marital_status == 'Married' else 0
            mother_education = random.choice(['High School', 'College', "Bachelor's Degree", "Master's Degree", 'Doctorate'])
            father_education = random.choice(['High School', 'College', "Bachelor's Degree", "Master's Degree", 'Doctorate'])
            relationship_with_student = random.choice(['Father', 'Mother', 'Brother', 'Sister', 'Uncle', 'Aunty'])
            extracurricular_activities = random.choice(['Yes', 'No'])
            online_time = random.randint(0, 24)
            family_relationship = random.choice(['Good', 'Average', 'Poor'])
            free_time_activities = random.choice(['Sports', 'Reading', 'Watching TV', 'Socializing'])
            alcoholic_consumption = random.choice(['Low', 'Moderate', 'High'])
            religious_programs = random.randint(0, 7)
            computer_access = random.choice(['Yes', 'No'])

            # Generate scores for test, practical, and exam
            test_score = random.randint(0, 10)
            practical_score = random.randint(0, 30)
            exam_score = random.randint(0, 60)

            # Calculate total score
            total_score = test_score + practical_score + exam_score

            # Determine performance based on total score
            if total_score >= 70:
                performance = 'A'
            elif total_score >= 60:
                performance = 'B'
            elif total_score >= 50:
                performance = 'C'
            elif total_score >= 40:
                performance = 'D'
            elif total_score >= 30:
                performance = 'E'
            else:
                performance = 'F'

             # Generate random percentage scores for attendance and assignment completion
            # attendance = random.randint(0, 100)
            # assignment_completion = random.randint(0, 100)

            # Adjust attendance and assignment completion based on grade
            if performance in ['A', 'B', 'C']:
                attendance = random.randint(75, 99)
                assignment_completion = random.randint(75, 99)
            elif performance in ['D', 'E']:
                attendance = random.randint(60, 75)
                assignment_completion = random.randint(60, 75)
            else:
                attendance = random.randint(0, 40)
                assignment_completion = random.randint(0, 40)

            student_data.append({
                'Attendance (%)': attendance,
                'Assignment Completion (%)': assignment_completion,
                'Test Score (10%)': test_score,
                'Practical Score (30%)': practical_score,
                'Exam Score (60%)': exam_score,
                'Total Score': total_score,
                'Performance': performance,
                'Age': age,
                'Gender': gender,
                'Marital Status': marital_status,
                'Children (if Married)': children,
                'Mother Education': mother_education,
                'Father Education': father_education,
                'Relationship with Student': relationship_with_student,
                'Extracurricular Activities': extracurricular_activities,
                'Online Time (Daily)': online_time,
                'Family Relationship': family_relationship,
                'Free Time Activities': free_time_activities,
                'Alcoholic Consumption': alcoholic_consumption,
                'Religious Programs (Weekly)': religious_programs,
                'Computer/Laptop Access (for Practicals)': computer_access
            })

    return student_data

# Generate 5000 student records for training with balanced grades
num_students_train = 5000
student_data_test_balanced = generate_student_data_balanced(num_students_train)

# Save the balanced training data to a CSV file
with open('student_data_test_balanced.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=student_data_test_balanced[0].keys())
    writer.writeheader()
    for student in student_data_test_balanced:
        writer.writerow(student)

print("Generated balanced student data for training saved to student_data_test_balanced.csv")
