import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('student_habits_performance.csv')

# Frequência de exercícios físicos
for col in ["exercise_frequency", "mental_health_rating", "diet_quality"]:
    sns.boxplot(x=col, y="exam_score", data=df)
    plt.show()