-- Paso 1: Contar clientes únicos por dispositivo
WITH ClientesPorDispositivo AS (
    SELECT 
        a1.cod_dispositivo,
        COUNT(DISTINCT a1.registro) AS clientes_unicos
    FROM Archivo_1 a1
    GROUP BY a1.cod_dispositivo
)
-- Paso 2: Filtrar dispositivos con al menos 100 clientes únicos
SELECT 
    cpd.cod_dispositivo,
    cpd.clientes_unicos
FROM ClientesPorDispositivo cpd
WHERE cpd.clientes_unicos >= 100
ORDER BY cpd.clientes_unicos DESC;