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
            marital_status = random.choice(['Single', 'Married', 'Divorced', 'Widowed'])
            children = random.randint(0, 5) if marital_status == 'Married' else 0
            mother_education = random.choice(['High School', 'College', "Bachelor's Degree", "Master's Degree", 'Doctorate'])
            father_education = random.choice(['High School', 'College', "Bachelor's Degree", "Master's Degree", 'Doctorate'])
            guardian = fake.name()
            extracurricular_activities = random.choice(['Yes', 'No'])
            online_time = random.randint(0, 24)
            family_relationship = random.choice(['Good', 'Average', 'Poor'])
            free_time_activities = random.choice(['Sports', 'Reading', 'Watching TV', 'Socializing'])
            alcoholic_consumption = random.choice(['Low', 'Moderate', 'High'])
            religious_programs = random.randint(0, 7)
            computer_access = random.choice(['Yes', 'No'])
            
            # Match factors with grades
            if grade in ['A', 'B']:
                extracurricular_activities = 'Yes'
                online_time = random.randint(2, 8)
                free_time_activities = random.choice(['Sports', 'Reading'])
                alcoholic_consumption = random.choice(['Low', 'Moderate'])
                computer_access = 'Yes'
            elif grade in ['C', 'D']:
                extracurricular_activities = 'No'
                online_time = random.randint(0, 3)
                free_time_activities = random.choice(['Reading', 'Watching TV', 'Sports'])
                alcoholic_consumption = random.choice(['Low', 'Moderate'])
                computer_access = random.choice(['Yes', 'No'])
            else:
                extracurricular_activities = 'No'
                online_time = 0
                free_time_activities = 'Watching TV'
                alcoholic_consumption = 'High'
                computer_access = 'No'
                
            # Assign weights based on grade
            total_score = random.uniform(0, 100)
            total_weight = [0.1, 0.2, 0.3, 0.2, 0.2]  # Initial weight for each parameter
            if grade == 'A':
                total_weight = [0.15, 0.25, 0.35, 0.15, 0.1]
            elif grade == 'B':
                total_weight = [0.1, 0.2, 0.3, 0.2, 0.2]
            elif grade == 'C':
                total_weight = [0.05, 0.15, 0.25, 0.25, 0.3]
            elif grade == 'D':
                total_weight = [0.05, 0.1, 0.2, 0.3, 0.35]
            elif grade == 'E':
                total_weight = [0.05, 0.05, 0.1, 0.3, 0.5]
            elif grade == 'F':
                total_weight = [0.05, 0.05, 0.05, 0.2, 0.65]

            # Calculate scores based on weights
            attendance = round(total_score * total_weight[0], 1)
            assignment_completion = round(total_score * total_weight[1], 1)
            test_score = round(total_score * total_weight[2], 1)
            practical_score = round(total_score * total_weight[3], 1)
            exam_score = round(total_score * total_weight[4], 1)

            student_data.append({
                'Attendance (%)': attendance,
                'Assignment Completion (%)': assignment_completion,
                'Test Score (25%)': test_score,
                'Practical Score (25%)': practical_score,
                'Exam Score (50%)': exam_score,
                'Total Grade': grade,
                'Age': age,
                'Gender': gender,
                'Marital Status': marital_status,
                'Children (if Married)': children,
                'Mother Education': mother_education,
                'Father Education': father_education,
                'Guardian (Sponsor)': guardian,
                'Extracurricular Activities': extracurricular_activities,
                'Online Time (Daily)': online_time,
                'Family Relationship': family_relationship,
                'Free Time Activities': free_time_activities,
                'Alcoholic Consumption': alcoholic_consumption,
                'Religious Programs (Weekly)': religious_programs,
                'Computer/Laptop Access (for Practicals)': computer_access
            })

    return student_data

# Generate 100,000 student records for training with balanced grades
num_students_train = 5000
student_data_test_balanced = generate_student_data_balanced(num_students_train)

# Save the balanced training data to a CSV file
with open('student_data_test_balanced.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=student_data_test_balanced[0].keys())
    writer.writeheader()
    for student in student_data_test_balanced:
        writer.writerow(student)

print("Generated balanced student data for training saved to student_data_test_balanced.csv")
