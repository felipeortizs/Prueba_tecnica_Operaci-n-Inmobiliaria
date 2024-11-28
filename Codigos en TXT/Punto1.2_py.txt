import pandas as pd

# Cargar el archivo de transacciones
archivo_1 = pd.read_csv('./Archivo_1 1.csv', encoding='utf-8')

# Paso 1: Contar clientes únicos por dispositivo
clientes_por_dispositivo = archivo_1.groupby('cod_dispositivo')['registro'].nunique().reset_index()
clientes_por_dispositivo.columns = ['cod_dispositivo', 'clientes_unicos']

# Paso 2: Filtrar dispositivos con al menos 100 clientes únicos
dispositivos_filtrados = clientes_por_dispositivo[clientes_por_dispositivo['clientes_unicos'] >= 100]

# Ordenar los dispositivos por la cantidad de clientes únicos en orden descendente
dispositivos_filtrados = dispositivos_filtrados.sort_values(by='clientes_unicos', ascending=False)

# Exportar el resultado a un archivo CSV
output_path = './solucion_ej_2.csv'
dispositivos_filtrados.to_csv(output_path, index=False, sep=';', encoding='utf-8-sig')

# Mostrar los primeros resultados
print("Dispositivos con al menos 100 clientes únicos:")
print(dispositivos_filtrados.head())

print(f"\nArchivo exportado exitosamente a: {output_path}")
