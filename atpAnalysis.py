import pandas as pd
 

df0 = pd.read_csv('calendario_atp_2026.csv', sep=";", header=1)


# Análisis rápido por categoría
conteo_categorias = df0['Nivel'].value_counts()


# 3. Ahora separamos Ciudad de País (usualmente separados por coma)
df0[['ciudad', 'pais']] = df0['Nombre de torneo y ciudad'].str.split(', ', expand=True)

# 1. Supongamos que tenemos: "Rolex Monte-Carlo Masters (Monte Carlo, Monaco)"
# Primero separamos el nombre del torneo de la ubicación
df0[['torneo', 'ubicacion_sucia']] = df0['Nombre de torneo y ciudad'].str.split(' \(', expand=True)

# 2. Limpiamos el paréntesis de cierre en la ubicación
df0['ubicacion_sucia'] = df0['ubicacion_sucia'].str.replace('\)', '', regex=True)


df0['pais_final'] = df0['pais'].combine_first(df0['ubicacion_sucia'])

#Eliminar columnas
df = df0.drop(['Nombre de torneo y ciudad','pais','ciudad', 'ubicacion_sucia'],axis=1) 


df['pais_final'] = df['pais_final'].replace('Spain','España')
# Rellena cualquier valor nulo con el nuevo texto
df['pais_final'] = df['pais_final'].fillna('Sedes múltiples')
