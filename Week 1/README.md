Q1) --rm

Q2) 0.42.0

Q3) 15612
SELECT COUNT(*)
FROM public.green_taxi_trips
WHERE DATE(lpep_pickup_datetime) = '2019-09-18' AND DATE(lpep_dropoff_datetime) = '2019-09-18'

Q4) 2019-09-26
SELECT DATE(lpep_pickup_datetime)
FROM public.green_taxi_trips
ORDER BY trip_distance DESC
LIMIT 1

Q5) "Brooklyn" "Manhattan" "Queens"
SELECT "Borough"
FROM public.green_taxi_trips g
JOIN public.zones z
ON g."PULocationID" = z."LocationID"
WHERE DATE(lpep_pickup_datetime) = '2019-09-18'
GROUP BY "Borough"
HAVING SUM(total_amount) > 50000

Q6)JFK Airport
SELECT z2."Zone"
FROM public.green_taxi_trips g
JOIN public.zones z
ON g."PULocationID" = z."LocationID"
JOIN public.zones z2
ON g."DOLocationID" = z2."LocationID"
WHERE EXTRACT(MONTH FROM lpep_pickup_datetime) = '9' 
	AND EXTRACT(YEAR FROM lpep_pickup_datetime) ='2019' 
	AND z."Zone" = 'Astoria'
ORDER BY tip_amount DESC
LIMIT 1

Q7)
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

   local_file.example will be created
  + resource "local_file" "example" {
      + content              = "Hello, GitHub Codespaces!"
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "output.txt"
      + id                   = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes


