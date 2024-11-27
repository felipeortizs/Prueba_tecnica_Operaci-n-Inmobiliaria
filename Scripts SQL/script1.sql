-- Paso 1: Calcular el total de dinero transaccionado por cliente
WITH TotalPorCliente AS (
    SELECT 
        registro AS cliente_id,
        SUM(mnt_total_trx) AS total_cliente
    FROM Archivo_1
    GROUP BY registro
),
-- Paso 2: Calcular el porcentaje de dinero por barrio para cada cliente
PorcentajePorBarrio AS (
    SELECT 
        a1.registro AS cliente_id,
        a3.nombre AS barrio,
        SUM(a1.mnt_total_trx) AS total_barrio,
        (SUM(a1.mnt_total_trx) * 100.0 / tc.total_cliente) AS porcentaje
    FROM Archivo_1 a1
    JOIN Archivo_2 a2 ON a1.cod_dispositivo = a2.codigo
    JOIN Archivo_3 a3 ON a2.id_barrio = a3.codigo
    JOIN TotalPorCliente tc ON a1.registro = tc.cliente_id
    GROUP BY a1.registro, a3.nombre, tc.total_cliente
),
-- Paso 3: Filtrar los barrios que cumplen con el criterio del 51%
BarriosTransaccionales AS (
    SELECT 
        cliente_id,
        barrio,
        porcentaje
    FROM PorcentajePorBarrio
    WHERE porcentaje >= 51
)
-- Paso 4: Resultado final
SELECT cliente_id,
        barrio,
        ROUND(porcentaje, 2)
FROM BarriosTransaccionales
ORDER BY cliente_id, porcentaje DESC;