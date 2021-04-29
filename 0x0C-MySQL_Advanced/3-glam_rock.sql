-- Data Base metal_bands
-- select columns name and lifespan

SELECT band_name,
ifnull(split, YEAR(CURDATE())) - formed AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC
