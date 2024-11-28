-- Paso 1: Filtrar transacciones en dispositivos tipo POS y relacionar con barrios
WITH TransaccionesPOS AS (
    SELECT 
        a1.registro AS cliente_id,
        a3.nombre AS barrio
    FROM Archivo_1 a1
    JOIN Archivo_2 a2 ON a1.cod_dispositivo = a2.codigo
    JOIN Archivo_3 a3 ON a2.id_barrio = a3.codigo
    WHERE a2.tipo = 'POS'
),
-- Paso 2: Contar clientes únicos por barrio
ClientesPorBarrio AS (
    SELECT 
        barrio,
        COUNT(DISTINCT cliente_id) AS clientes_unicos
    FROM TransaccionesPOS
    GROUP BY barrio
),
-- Paso 3: Seleccionar los 5 barrios con más clientes únicos
Top5Barrios AS (
    SELECT 
        barrio,
        clientes_unicos
    FROM ClientesPorBarrio
    ORDER BY clientes_unicos DESC
    LIMIT 5
)
-- Resultado final
SELECT * 
FROM Top5Barrios;