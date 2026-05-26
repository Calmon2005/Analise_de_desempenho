import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv(r'Escola\\student_habits_performance.csv')

# Redes sociais: distribuicao geral (Hostograma)
# x= "social_emdia_hours"

'''sns.histplot(data=df, x="social_media_hours")
plt.title("Distruicao de tempo em redes sociais")
plt.show()'''

# Avaliando notas médias
# por diferentes intervalos (bins) de períodos gastos em redes sociais
# ["0-2", "2-4", "4-6", "6+"]
df["social_media_bin"] = pd.cut(
    df["social_media_hours"],
    bins= [0, 2, 4, 6],
    labels=["0-2h", "2h-4h", "4h-6h"]
    )



# Plotar gráfico de caixa (boxplot)
sns.boxplot(x="social_media_bin", y="exam_score", data=df)
plt.title("Notas por tempo em redes sociais")
plt.show()
