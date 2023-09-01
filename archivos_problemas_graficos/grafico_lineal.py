#cuantas hambuguesas se come bollito en discotecas

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\burguers.csv")

sns.lineplot(x="fecha",y="burguers",data= df)

plt.plot("01-09",17,"o")

plt.show()


