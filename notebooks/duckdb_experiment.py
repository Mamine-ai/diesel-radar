import duckdb

con = duckdb.connect()

con.sql("""

CREATE TABLE IF NOT EXISTS raw_prices(

     station_id VARCHAR NOT NULL,
     fetched_at TIMESTAMP NOT NULL,
     status VARCHAR,
     e5 DECIMAL(5,3),
     e10 DECIMAL(5,3),
     diesel DECIMAL(5,3),

     PRIMARY KEY (station_id, fetched_at))
""")


con.sql("""
insert into raw_prices VALUES('stationb', '2026-11-21 19:30:50', 'open' , 1.25, 2.52, 1.65) """)


con.sql("""        SELECT * FROM raw_prices""").show()


con.sql("""
insert into raw_prices VALUES('stationb', '2026-11-21 20:20:25' , 'closed' , NULL, NULL, NULL)

""").show()

con.sql("""  SELECT * FROM raw_prices
""").show()


con.sql("""
 insert into raw_prices VALUES('station12', '2026-11-21 19:30:50', 'open' , 1.25, 2.52, 1.65)

""")
