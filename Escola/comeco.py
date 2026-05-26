import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv(r'completo\\student_habits_performance.csv')
cols = [
    "study_hours_per_day",
    "social_media_hours",
    "netflix_hours",
    "sleep_hours",
    "attendance_percentage",
    "exercise_frequency",
    "mental_health_rating",
    "exam_score",
]

# Plotar mapa de calor (heatmap)
sns.heatmap(df[cols].corr(), annot=True)
plt.title("Correlação entre hábitos e nota final")
plt.show()