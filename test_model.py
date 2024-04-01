import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import random

# Load the model
model = joblib.load('student_performance_predictor.joblib')

# Load the label encoders
label_encoders = joblib.load('label_encoders.joblib')


# Function to preprocess user input
def preprocess_input(user_input):
    input_data = user_input.copy()
    for column in input_data.keys():
        if column in label_encoders.keys():
            input_data[column] = label_encoders[column].transform([input_data[column]])[0]
    return [list(input_data.values())]

# Generate random values for all inputs
user_input = {}
user_input['Age'] = random.randint(18, 25)
user_input['Gender'] = random.choice(['Male', 'Female'])
user_input['Marital Status'] = random.choice(['Single', 'Married', 'Engaged'])
user_input['Children (if Married)'] = random.randint(0, 5) if user_input['Marital Status'] == 'Married' else 0
user_input['Mother Education'] = random.choice(['High School', 'College', "Bachelor's Degree", "Master's Degree", 'Doctorate'])
user_input['Father Education'] = random.choice(['High School', 'College', "Bachelor's Degree", "Master's Degree", 'Doctorate'])
user_input['Guardian (Sponsor)'] = random.choice(['Father', 'Mother', 'Brother', 'Sister', 'Uncle', 'Aunty'])
user_input['Extracurricular Activities'] = random.choice(['Yes', 'No'])
user_input['Online Time (Daily)'] = random.randint(0, 24)
user_input['Family Relationship'] = random.choice(['Good', 'Average', 'Poor'])
user_input['Free Time Activities'] = random.choice(['Sports', 'Reading', 'Watching TV', 'Socializing'])
user_input['Alcoholic Consumption'] = random.choice(['Low', 'Moderate', 'High'])
user_input['Religious Programs (Weekly)'] = random.randint(0, 7)
user_input['Computer/Laptop Access (for Practicals)'] = random.choice(['Yes', 'No'])
user_input['Attendance (%)'] = random.randint(0, 100)
user_input['Assignment Completion (%)'] = random.randint(0, 100)
user_input['Test Score (25%)'] = random.randint(0, 25)
user_input['Practical Score (25%)'] = random.randint(0, 25)
user_input['Exam Score (50%)'] = random.randint(0, 50)

# Preprocess the input
user_input_preprocessed = preprocess_input(user_input)

# Make prediction
prediction = model.predict(user_input_preprocessed)

# Display the generated values and predicted performance
print("Generated Input Values:")
for key, value in user_input.items():
    print(f"{key}: {value}")
print("\nPredicted Performance:", prediction[0])
