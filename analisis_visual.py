import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conexion = sqlite3.connect("datos_mision.db")
consulta = "SELECT * FROM datos;"

df = pd.read_sql_query(consulta, conexion)
conexion.close()

df["Magnitude"] = df["Gmag"]- 5 * (np.log10(1000/df["Plx"])) + 5
print(df)

plt.figure()
plt.scatter(df["BP-RP"], df["Magnitude"], marker="*",color = "red")
plt.gca().invert_yaxis()
plt.title('Diagrama de Hertzsprung-Russell')
plt.savefig('resultado.png')
