import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('Escola\\student_habits_performance.csv')

# Comparando médias: quem estuda >5h x <2h
filtro_estudo_alto = df["study_hours_per_day"] > 5
filtro_estudo_baixo = df["study_hours_per_day"] < 2

grupo_estudo_alto = df[filtro_estudo_alto]["exam_score"]
grupo_estudo_baixo = df[filtro_estudo_baixo]["exam_score"]

print("Média notas (estuda >5h):", grupo_estudo_alto.mean())
print("Média notas (estuda <2h):", grupo_estudo_baixo.mean())