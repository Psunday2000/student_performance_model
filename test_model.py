import pandas as pd
import joblib
import random

# Load the trained decision tree classifier model
model = joblib.load('decision_tree_classifier_model.joblib')

# Define a function to predict a student's grade
def predict_grade_from_csv(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Select a random row from the DataFrame
    random_index = random.randint(0, len(df) - 1)
    random_row = df.iloc[random_index]

    # Print the selected random row
    print("Selected random row:")
    print(random_row)

    # Prepare the features for prediction
    columns_in_order = ['Attendance (%)', 'Assignment Completion (%)', 'Test Score (25%)', 'Practical Score (25%)', 'Exam Score (50%)', 'Age', 'Gender', 'Marital Status', 'Children (if Married)', 'Mother Education', 'Father Education', 'Guardian (Sponsor)', 'Extracurricular Activities', 'Online Time (Daily)', 'Family Relationship', 'Free Time Activities', 'Alcoholic Consumption', 'Religious Programs (Weekly)', 'Computer/Laptop Access (for Practicals)']
    X = pd.DataFrame([random_row], columns=columns_in_order)

    # Encode categorical variables
    categorical_columns = ['Gender', 'Marital Status', 'Mother Education', 'Father Education', 'Guardian (Sponsor)', 'Extracurricular Activities', 'Family Relationship', 'Free Time Activities', 'Alcoholic Consumption', 'Computer/Laptop Access (for Practicals)']
    X_encoded = pd.get_dummies(X, columns=categorical_columns)

    # Ensure the columns in X_encoded match the columns used during training
    missing_columns = set(model.feature_names_in_) - set(X_encoded.columns)
    extra_columns = set(X_encoded.columns) - set(model.feature_names_in_)
    X_encoded = X_encoded.reindex(columns=model.feature_names_in_, fill_value=0)

    # Predict the grade
    prediction = model.predict(X_encoded)[0]
    print(f"\nThe predicted grade is: {prediction}")

# Path to the CSV file
file_path = 'student_data_test.csv'

# Run the prediction function with random input from the CSV file
predict_grade_from_csv(file_path)
