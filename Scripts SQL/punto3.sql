WITH Dispensadores AS (
    SELECT
        a1.cod_dispositivo,
        a2.id_barrio
    FROM
        Archivo_1 a1
    INNER JOIN
        Archivo_2 a2
    ON
        a1.cod_dispositivo = a2.codigo
    WHERE
        a1.canal = 'DISPENSADOR'
),
BarrioFrecuencia AS (
    SELECT
        d.id_barrio,
        COUNT(d.cod_dispositivo) AS total_disp
    FROM
        Dispensadores d
    GROUP BY
        d.id_barrio
),
BarrioAcumulado AS (
    SELECT
        bf.id_barrio,
        bf.total_disp,
        SUM(bf.total_disp) OVER (ORDER BY bf.total_disp DESC) AS acum_disp,
        SUM(bf.total_disp) OVER () AS total_general,
        SUM(bf.total_disp) OVER (ORDER BY bf.total_disp DESC) * 1.0 /
        SUM(bf.total_disp) OVER () AS porcentaje_acum
    FROM
        BarrioFrecuencia bf
),
BarriosSeleccionados AS (
    SELECT
        ba.id_barrio,
        ba.total_disp,
--        ba.acum_disp,
        ba.total_general,
        ba.porcentaje_acum * 100 porcentaje_acum
    FROM
        BarrioAcumulado ba
    WHERE
        ba.porcentaje_acum <= 0.60
)
SELECT
	a.nombre
	, bs.*
FROM BarriosSeleccionados BS
left join Archivo_3 a ON BS.id_barrio = a.codigo
ORDER BY porcentaje_acum ASC