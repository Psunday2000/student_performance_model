import pandas as pd
import matplotlib.pyplot as plt

# Load the generated student data
student_data = pd.read_csv('student_data_train.csv')

# Plot the relationship between grades and selected categorical features
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
pd.crosstab(student_data['Total Grade'], student_data['Extracurricular Activities']).plot(kind='bar', stacked=True, ax=plt.gca())
plt.title('Grade vs Extracurricular Activities')
plt.xlabel('Total Grade')
plt.ylabel('Count')
plt.legend(title='Extracurricular Activities', loc='upper right')

plt.subplot(2, 2, 2)
pd.crosstab(student_data['Total Grade'], student_data['Online Time (Daily)']).plot(kind='bar', stacked=True, ax=plt.gca())
plt.title('Grade vs Online Time (Daily)')
plt.xlabel('Total Grade')
plt.ylabel('Count')
plt.legend(title='Online Time (Daily)', loc='upper right')

plt.subplot(2, 2, 3)
pd.crosstab(student_data['Total Grade'], student_data['Free Time Activities']).plot(kind='bar', stacked=True, ax=plt.gca())
plt.title('Grade vs Free Time Activities')
plt.xlabel('Total Grade')
plt.ylabel('Count')
plt.legend(title='Free Time Activities', loc='upper right')

plt.subplot(2, 2, 4)
pd.crosstab(student_data['Total Grade'], student_data['Alcoholic Consumption']).plot(kind='bar', stacked=True, ax=plt.gca())
plt.title('Grade vs Alcoholic Consumption')
plt.xlabel('Total Grade')
plt.ylabel('Count')
plt.legend(title='Alcoholic Consumption', loc='upper right')

plt.tight_layout()
plt.show()
