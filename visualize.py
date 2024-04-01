import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the generated student data
student_data = pd.read_csv('student_data_train.csv')

# Define a custom color palette
colors = sns.color_palette("Set1")

# Plot the relationship between Performances and selected categorical features
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
pd.crosstab(student_data['Performance'], student_data['Extracurricular Activities']).plot(kind='bar', stacked=True, ax=plt.gca(), color=colors)
plt.title('Performance vs Extracurricular Activities')
plt.xlabel('Performance')
plt.ylabel('Count')
plt.legend(title='Extracurricular Activities', loc='upper right')

plt.subplot(2, 2, 2)
pd.crosstab(student_data['Performance'], student_data['Online Time (Daily)']).plot(kind='bar', stacked=True, ax=plt.gca(), color=colors)
plt.title('Performance vs Online Time (Daily)')
plt.xlabel('Performance')
plt.ylabel('Count')
plt.legend(title='Online Time (Daily)', loc='upper right')

plt.subplot(2, 2, 3)
pd.crosstab(student_data['Performance'], student_data['Free Time Activities']).plot(kind='bar', stacked=True, ax=plt.gca(), color=colors)
plt.title('Performance vs Free Time Activities')
plt.xlabel('Performance')
plt.ylabel('Count')
plt.legend(title='Free Time Activities', loc='upper right')

plt.subplot(2, 2, 4)
pd.crosstab(student_data['Performance'], student_data['Alcoholic Consumption']).plot(kind='bar', stacked=True, ax=plt.gca(), color=colors)
plt.title('Performance vs Alcoholic Consumption')
plt.xlabel('Performance')
plt.ylabel('Count')
plt.legend(title='Alcoholic Consumption', loc='upper right')

plt.tight_layout()
plt.savefig('relationship_plot.jpg', dpi=900)
plt.show()
