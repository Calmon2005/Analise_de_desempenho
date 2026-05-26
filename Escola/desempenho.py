import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv(r'Escola\\student_habits_performance.csv')

# Gráfico de dispersao com linha de regressao
# x="study_hours_per_day" / y="exam_score"
sns.lmplot(data=df, x="study_hours_per_day", y="exam_score")
plt.title("Mais estudo -> maior a nota")
plt.show()

#Comparando meédias: quem, estuda >5h x <2h
filtro_estudo_alto = df ["study_hours_per_day"] > 5
filtro_estudo_baixo = df ["study_hours_per_day"] <2

grupo_de_estudo_alto = df [filtro_estudo_alto]["exam_score"]
grupo_de_estudo_baixo = df [filtro_estudo_baixo]["esxam_score"]

print("Media notas (estuda >5:", grupo_de_estudo_alto.mean())
print("Media notas (estuda <2:", grupo_de_estudo_baixo.mean())