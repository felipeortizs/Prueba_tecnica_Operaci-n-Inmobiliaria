import pandas as pd

# Cargar los archivos CSV con la codificación adecuada (prueba con 'utf-8' o 'ISO-8859-1')
archivo_1 = pd.read_csv('./Archivo_1 1.csv', encoding='utf-8')
archivo_2 = pd.read_csv('./Archivo_2.csv', encoding='utf-8')
archivo_3 = pd.read_csv('./Archivo_3.csv', encoding='utf-8')

# Paso 1: Calcular el total transaccionado por cliente
total_por_cliente = archivo_1.groupby('registro')['mnt_total_trx'].sum().reset_index()
total_por_cliente.columns = ['cliente_id', 'total_cliente']

# Paso 2: Unir tablas y calcular porcentaje de dinero por barrio
archivo_1_2 = archivo_1.merge(archivo_2, left_on='cod_dispositivo', right_on='codigo', how='inner')
archivo_1_2_3 = archivo_1_2.merge(archivo_3, left_on='id_barrio', right_on='codigo', how='inner')

# Agrupar por cliente y barrio
porcentaje_por_barrio = archivo_1_2_3.groupby(['registro', 'nombre'])['mnt_total_trx'].sum().reset_index()
porcentaje_por_barrio = porcentaje_por_barrio.merge(total_por_cliente, left_on='registro', right_on='cliente_id', how='inner')
porcentaje_por_barrio['porcentaje'] = (porcentaje_por_barrio['mnt_total_trx'] / porcentaje_por_barrio['total_cliente']) * 100

# Paso 3: Filtrar barrios que cumplen con ≥ 51%
barrios_transaccionales = porcentaje_por_barrio[porcentaje_por_barrio['porcentaje'] >= 51][['cliente_id', 'nombre', 'porcentaje']]

# Ajustar el formato del porcentaje a 2 decimales
barrios_transaccionales['porcentaje'] = barrios_transaccionales['porcentaje'].round(2)

# Exportar el resultado a CSV
output_path = './punto1_py.csv'
barrios_transaccionales.to_csv(output_path, index=False, encoding='utf-8-sig')

# Mostrar el dataframe resultante
print("Resultados del Punto 1 - Barrios Más Transaccionales por Cliente:")
print(barrios_transaccionales.head())

print(f"\nArchivo exportado exitosamente a: {output_path}")


