#ingreso anual que puede incluso ser mensual 

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\victor_income.csv")

#creando el grafico
sns.barplot(x="fuente",y="income",data= df)

#obteniendo el total de ingresos
total_income= df["income"].sum()

#mostrando el total
print(f"El total de ingresos es de:\n{total_income}$")

#mostrando el grafico
plt.show()


