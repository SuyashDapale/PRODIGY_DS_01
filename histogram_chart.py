import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset (replace 'your_dataset.csv' with the actual filename)
df = pd.read_csv('synthetic_population.csv')

# Assuming 'age' is the column representing ages
plt.figure(figsize=(8, 5))
plt.hist(df['age'].dropna(), bins=10, color='lightblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Ages in the Population')
plt.show()
