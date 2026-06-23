import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("¡Todo cargó perfecto con Pandas versión:", pd.__version__, "!")

# Cargamos y leemos la base de datos que acabas de arrastrar:
df = pd.read_csv('btcusd_1-min_data.csv')
print(df.head())
