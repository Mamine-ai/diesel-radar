import duckdb

duckdb.sql("""

     SELECT * 
     FROM 'data/raw/stations.json'
     ORDER BY diesel
     LIMIT 5
     
     """).show()
