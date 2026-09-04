import numpy as np
import pandas as pd
import sqlite3

df_raw = pd.read_csv('gaiaDR3.csv')
print(df_raw.head())

df_clean = df_raw[["BP-RP","Gmag","Plx"]]
df_clean = df_clean.dropna()
print(df_clean.head())


conexion = sqlite3.connect("datos_mision.db")

df_clean.to_sql("datos", conexion, if_exists="replace",index=False )

conexion.close()
