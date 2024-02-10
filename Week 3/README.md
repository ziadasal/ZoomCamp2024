Create an external table using the Green Taxi Trip Records Data for 2022. </br>
Create a table in BQ using the Green Taxi Trip Records for 2022 (do not partition or cluster this table). </br>
</p>

``` SQL
CREATE EXTERNAL TABLE IF NOT EXISTS week3_zoomcamp.external_green

OPTIONS(
format = 'PARQUET',
uris = ['gs://week3-bucketerino-parquet/green/*.parquet']
);

CREATE TABLE IF NOT EXISTS week3_zoomcamp.native_green AS
SELECT * FROM week3_zoomcamp.external_green;
```

## Question 1:

```SQL
SELECT COUNT(1) FROM `stoked-champion-410819.week3_zoomcamp.native_green`
```

## Question 2:
```SQL
-- native:
SELECT COUNT(DISTINCT(PULocationID)) FROM `stoked-champion-410819.week3_zoomcamp.native_green`

-- external:
SELECT COUNT(DISTINCT(PULocationID)) FROM `stoked-champion-410819.week3_zoomcamp.external_green`
```

## Question 3:
```SQL
SELECT COUNT(1) FROM `stoked-champion-410819.week3_zoomcamp.native_green` WHERE fare_amount = 0.0
-- 1,622
```

## Question 4:
```SQL
CREATE TABLE week3_zoomcamp.green_partitioned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT * FROM week3_zoomcamp.native_green;
```

## Question 5:

```SQL
SELECT DISTINCT(PULocationID) FROM `stoked-champion-410819.week3_zoomcamp.native_green`
WHERE DATE(lpep_pickup_datetime)
        BETWEEN
          DATE("2022-06-01") AND DATE("2022-06-30")
SELECT DISTINCT(PULocationID) FROM `stoked-champion-410819.week3_zoomcamp.green_partitioned_clustered`
WHERE DATE(lpep_pickup_datetime)
        BETWEEN
          DATE("2022-06-01") AND DATE("2022-06-30")
```


## (Bonus: Not worth points) Question 8:
```SQL
SELECT COUNT(1) FROM `stoked-champion-410819.week3_zoomcamp.native_green`
--0B
```
 