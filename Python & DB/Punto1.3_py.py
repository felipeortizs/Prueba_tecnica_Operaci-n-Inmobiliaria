import pandas as pd

# Cargar los archivos CSV
archivo_1 = pd.read_csv('./Archivo_1 1.csv', encoding='utf-8')
archivo_2 = pd.read_csv('./Archivo_2.csv', encoding='utf-8')
archivo_3 = pd.read_csv('./Archivo_3.csv', encoding='utf-8')

# Paso 1: Filtrar transacciones de dispositivos tipo POS
archivo_1_2 = archivo_1.merge(archivo_2, left_on='cod_dispositivo', right_on='codigo', how='inner')
transacciones_pos = archivo_1_2[archivo_1_2['tipo'] == 'POS']

# Paso 2: Relacionar con los barrios
transacciones_pos = transacciones_pos.merge(archivo_3, left_on='id_barrio', right_on='codigo', how='inner')

# Paso 3: Contar clientes únicos por barrio
clientes_por_barrio = transacciones_pos.groupby('nombre')['registro'].nunique().reset_index()
clientes_por_barrio.columns = ['barrio', 'clientes_unicos']

# Paso 4: Seleccionar los 5 barrios con más clientes únicos
top_5_barrios = clientes_por_barrio.sort_values(by='clientes_unicos', ascending=False).head(5)

# Exportar los resultados a un CSV
output_path = './top_5_barrios_python.csv'
top_5_barrios.to_csv(output_path, index=False, sep=';', encoding='utf-8-sig')

# Mostrar los resultados
print("Top 5 Barrios con más Clientes Únicos (Python):")
print(top_5_barrios)

print(f"\nArchivo exportado exitosamente a: {output_path}")
