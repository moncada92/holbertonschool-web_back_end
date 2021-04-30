-- Old school band
-- lifespan by band and style
SELECT band_name,
IFNULL(split, 2020) - formed as lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;