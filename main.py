import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset (replace 'your_dataset.csv' with the actual filename)
df = pd.read_csv("synthetic_population.csv")

# Assuming 'gender' is the column representing genders
gender_counts = df['gender'].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(gender_counts.index, gender_counts.values, color='teal')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender in the Population')
plt.xticks(rotation=0)
plt.show()
