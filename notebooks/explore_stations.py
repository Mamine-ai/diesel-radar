import duckdb

duckdb.sql(""" 

      SELECT 
         name,
         brand,
         place,
         dist,
         diesel
     FROM 'data/raw/stations.json'
     WHERE diesel IS NOT NULL
     ORDER BY diesel, dist
     LIMIT 5




""").show()
