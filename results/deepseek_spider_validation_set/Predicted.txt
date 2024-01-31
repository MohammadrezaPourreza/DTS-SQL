SELECT COUNT(*) FROM singer
SELECT COUNT(*) FROM singer
SELECT name , country , age FROM singer ORDER BY age DESC
SELECT name , country , age FROM singer ORDER BY age DESC
SELECT AVG(age) , MIN(age) , MAX(age) FROM singer WHERE country = 'France'
SELECT AVG(age) , MIN(age) , MAX(age) FROM singer WHERE country = 'France'
SELECT name , song_release_year FROM singer ORDER BY age LIMIT 1
SELECT song_name , song_release_year FROM singer ORDER BY age LIMIT 1
SELECT DISTINCT country FROM singer WHERE age > 20
SELECT DISTINCT country FROM singer WHERE age > 20
SELECT country , COUNT(*) FROM singer GROUP BY country
SELECT country , COUNT(*) FROM singer GROUP BY country
SELECT song_name FROM singer WHERE age > (SELECT AVG(age) FROM singer)
SELECT song_name FROM singer WHERE age > (SELECT AVG(age) FROM singer)
SELECT location , name FROM stadium WHERE capacity BETWEEN 5000 AND 10000
SELECT location , name FROM stadium WHERE capacity BETWEEN 5000 AND 10000
SELECT MAX(capacity) , AVG(capacity) FROM stadium
SELECT AVG(capacity) , MAX(capacity) FROM stadium
SELECT name , capacity FROM stadium ORDER BY average DESC LIMIT 1
SELECT name , capacity FROM stadium ORDER BY average DESC LIMIT 1
SELECT COUNT(*) FROM concert WHERE year = 2014 OR year = 2015
SELECT COUNT(*) FROM concert WHERE year = 2014 OR year = 2015
SELECT t1.name , COUNT(*) FROM stadium as t1 JOIN concert as t2 ON t1.stadium_id = t2.stadium_id GROUP BY t1.stadium_id
SELECT t1.name , COUNT(*) FROM stadium as t1 JOIN concert as t2 ON t1.stadium_id = t2.stadium_id GROUP BY t1.stadium_id
SELECT t1.name , t1.capacity FROM stadium as t1 JOIN concert as t2 ON t1.stadium_id = t2.stadium_id WHERE t2.year >= 2014 GROUP BY t1.stadium_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.name , t1.capacity FROM stadium as t1 JOIN concert as t2 ON t1.stadium_id = t2.stadium_id WHERE t2.year > 2013 GROUP BY t1.stadium_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT year FROM concert GROUP BY year ORDER BY COUNT(*) DESC LIMIT 1
SELECT year FROM concert GROUP BY year ORDER BY COUNT(*) DESC LIMIT 1
SELECT name FROM stadium WHERE stadium_id NOT IN (SELECT stadium_id FROM concert)
SELECT name FROM stadium WHERE stadium_id NOT IN (SELECT stadium_id FROM concert)
SELECT country FROM singer WHERE age < 30 INTERSECT SELECT country FROM singer WHERE age > 40
SELECT name FROM stadium EXCEPT SELECT t2.name FROM concert as t1 JOIN stadium as t2 ON t1.stadium_id = t2.stadium_id WHERE t1.year = 2014
SELECT name FROM stadium WHERE stadium_id NOT IN (SELECT stadium_id FROM concert WHERE year = 2014)
SELECT t1.concert_name , t1.theme , COUNT(*) FROM concert as t1 JOIN singer_in_concert as t2 ON t1.concert_id = t2.concert_id GROUP BY t1.concert_id
SELECT t1.concert_name , t1.theme , COUNT(*) FROM concert as t1 JOIN singer_in_concert as t2 ON t1.concert_id = t2.concert_id GROUP BY t1.concert_id
SELECT t1.name , COUNT(*) FROM singer as t1 JOIN singer_in_concert as t2 ON t1.singer_id = t2.singer_id GROUP BY t1.singer_id
SELECT t1.name , COUNT(*) FROM singer as t1 JOIN singer_in_concert as t2 ON t1.singer_id = t2.singer_id GROUP BY t1.singer_id
SELECT t1.name FROM singer as t1 JOIN concert as t2 ON t1.singer_id = t3.singer_id WHERE t2.year = 2014
SELECT t1.name FROM singer as t1 JOIN concert as t2 ON t1.singer_id = t3.singer_id JOIN singer_in_concert as t3 ON t2.concert_id = t3.concert_id WHERE t2.year = 2014
SELECT name , country FROM singer WHERE song_name LIKE '%Hey%'
SELECT name , country FROM singer WHERE song_name LIKE '%Hey%'
SELECT t1.name , t1.location FROM stadium as t1 JOIN concert as t2 ON t1.stadium_id = t2.stadium_id WHERE t2.year = 2014 INTERSECT SELECT t1.name , t1.location FROM stadium as t1 JOIN concert as t2 ON t1.stadium_id = t2.stadium_id WHERE t2.year = 2015
SELECT t1.name , t1.location FROM stadium as t1 JOIN concert as t2 ON t1.stadium_id = t2.stadium_id WHERE t2.year = 2014 INTERSECT SELECT t1.name , t1.location FROM stadium as t1 JOIN concert as t2 ON t1.stadium_id = t2.stadium_id WHERE t2.year = 2015
SELECT COUNT(*) FROM stadium as t1 JOIN concert as t2 ON t1.stadium_id = t2.stadium_id WHERE t1.capacity = (SELECT MAX(capacity) FROM stadium)
SELECT COUNT(*) FROM stadium as t1 JOIN concert as t2 ON t1.stadium_id = t2.stadium_id WHERE t1.capacity = (SELECT MAX(capacity) FROM stadium)
SELECT COUNT(*) FROM pets WHERE weight > 10
SELECT COUNT(*) FROM pets WHERE weight > 10
SELECT weight FROM pets WHERE pet_age = ( SELECT MIN(pet_age) FROM pets WHERE pettype = "dog" ) AND pettype = "dog"
SELECT weight FROM pets WHERE pet_age = ( SELECT MIN(pet_age) FROM pets WHERE pettype = "dog" ) AND pettype = "dog"
SELECT MAX(weight) , pettype FROM pets GROUP BY pettype
SELECT MAX(weight) , pettype FROM pets GROUP BY pettype
SELECT COUNT(*) FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t3.stuid = t1.stuid WHERE t3.age > 20
SELECT COUNT(*) FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t3.stuid = t1.stuid WHERE t3.age > 20
SELECT COUNT(*) fROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t3.stuid = t1.stuid WHERE t2.pettype = "dog" AND t3.sex = "f"
SELECT COUNT(*) fROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t3.stuid = t1.stuid WHERE t2.pettype = "dog" AND t3.sex = "f"
SELECT COUNT(DISTINCT pettype) FROM pets
SELECT COUNT(DISTINCT pettype) FROM pets
SELECT t3.fname FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t1.stuid = t3.stuid WHERE t2.pettype = "cat" OR t2.pettype = "dog"
SELECT t3.fname FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t1.stuid = t3.stuid WHERE t2.pettype = "cat" OR t2.pettype = "dog"
SELECT t3.fname FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t1.stuid = t3.stuid WHERE t2.pettype = "cat" INTERSECT SELECT t3.fname FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t1.stuid = t3.stuid WHERE t2.pettype = "dog"
SELECT t3.fname FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t1.stuid = t3.stuid WHERE t2.pettype = 'cat' INTERSECT SELECT t3.fname FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t1.stuid = t3.stuid WHERE t2.pettype = 'dog'
SELECT major , age FROM student WHERE stuid NOT IN (SELECT stuid FROM has_pet WHERE petid IN (SELECT petid FROM pets WHERE pettype = "Cat"))
SELECT t2.major , t2.age FROM has_pet as t1 JOIN student as t2 ON t1.stuid = t2.stuid WHERE t1.petid != 2001
SELECT stuid FROM has_pet EXCEPT SELECT t1.stuid FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid WHERE t2.pettype = 'cat'
SELECT stuid FROM has_pet EXCEPT SELECT t1.stuid FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid WHERE t2.pettype = 'cat'
SELECT t3.fname , t3.age FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t1.stuid = t3.stuid WHERE t2.pettype = "dog" EXCEPT SELECT t3.fname , t3.age FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t1.stuid = t3.stuid WHERE t2.pettype = "cat"
SELECT t3.fname FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t3.stuid = t1.stuid WHERE t2.pettype = "dog" EXCEPT SELECT t3.fname FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t3.stuid = t1.stuid WHERE t2.pettype = "cat"
SELECT pettype , weight FROM pets ORDER BY pet_age LIMIT 1
SELECT pettype , weight FROM pets ORDER BY pet_age LIMIT 1
SELECT petid , weight FROM pets WHERE pet_age > 1
SELECT petid , weight FROM pets WHERE pet_age > 1
SELECT pettype , AVG(pet_age) , MAX(pet_age) FROM pets GROUP BY pettype
SELECT pettype , AVG(pet_age) , MAX(pet_age) FROM pets GROUP BY pettype
SELECT pettype , AVG(weight) FROM pets GROUP BY pettype
SELECT pettype , AVG(weight) FROM pets GROUP BY pettype
SELECT t2.fname , t2.age FROM has_pet as t1 JOIN student as t2 ON t1.stuid = t2.stuid
SELECT DISTINCT t2.fname , t2.age FROM has_pet as t1 JOIN student as t2 ON t1.stuid = t2.stuid
SELECT t1.petid FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t3.stuid = t1.stuid WHERE t3.lname = 'Smith'
SELECT t1.petid FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t3.stuid = t1.stuid WHERE t3.lname = 'Smith'
SELECT stuid , COUNT(*) FROM has_pet GROUP BY stuid
SELECT t1.stuid , COUNT(*) FROM has_pet as t1 JOIN student as t2 ON t1.stuid = t2.stuid GROUP BY t1.stuid
SELECT t2.fname , t2.sex FROM has_pet as t1 JOIN student as t2 ON t1.stuid = t2.stuid GROUP BY t1.stuid HAVING COUNT(*) > 1
SELECT t2.fname , t2.sex FROM has_pet as t1 JOIN student as t2 ON t1.stuid = t2.stuid GROUP BY t1.stuid HAVING COUNT(*) > 1
SELECT t3.lname FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t3.stuid = t1.stuid WHERE t2.pettype = "cat" AND t2.pet_age = 3
SELECT t3.lname FROM has_pet as t1 JOIN pets as t2 ON t1.petid = t2.petid JOIN student as t3 ON t3.stuid = t1.stuid WHERE t2.pettype = "cat" AND t2.pet_age = 3
SELECT AVG(age) FROM student WHERE stuid NOT IN (SELECT stuid FROM has_pet)
SELECT AVG(age) FROM student WHERE stuid NOT IN (SELECT stuid FROM has_pet)
SELECT COUNT(*) FROM continents
SELECT COUNT(*) FROM continents
SELECT t1.contid , t1.continent , COUNT(*) FROM continents as t1 JOIN countries as t2 ON t1.contid = t2.continent GROUP BY t1.contid
SELECT t1.contid , t1.continent , COUNT(*) FROM continents as t1 JOIN countries as t2 ON t1.contid = t2.continent GROUP BY t1.contid
SELECT COUNT(*) FROM countries
SELECT COUNT(*) FROM countries
SELECT t2.fullname , t1.maker , COUNT(*) FROM model_list as t1 JOIN car_makers as t2 ON t1.maker = t2.id GROUP BY t1.maker
SELECT t1.fullname , t1.id , COUNT(*) FROM car_makers as t1 JOIN model_list as t2 ON t1.id = t2.maker GROUP BY t1.id
SELECT id FROM cars_data ORDER BY horsepower LIMIT 1
SELECT id FROM cars_data ORDER BY horsepower ASC LIMIT 1
SELECT id FROM cars_data WHERE weight < (SELECT AVG(weight) FROM cars_data)
SELECT t1.model FROM car_names as t1 JOIN cars_data as t2 ON t1.makeid = t2.id WHERE t2.weight < (SELECT AVG(weight) FROM cars_data)
SELECT DISTINCT t1.make FROM car_names as t1 JOIN cars_data as t2 ON t1.makeid = t2.id WHERE t2.year = 1970
SELECT DISTINCT t1.maker FROM car_makers as t1 JOIN car_names as t2 ON t1.id = t2.makeid JOIN cars_data as t3 ON t2.makeid = t3.id WHERE t3.year = 1970
SELECT t1.make , t2.year FROM car_names as t1 JOIN cars_data as t2 ON t1.makeid = t2.id ORDER BY t2.year asC LIMIT 1
SELECT t1.make , t2.year FROM car_names as t1 JOIN cars_data as t2 ON t1.makeid = t2.id ORDER BY t2.year LIMIT 1
SELECT DISTINCT id FROM cars_data WHERE year > 1980
SELECT DISTINCT id FROM cars_data WHERE year > 1980
SELECT t2.continent , COUNT(*) FROM car_makers as t1 JOIN continents as t2 ON t1.country = t3.countryid GROUP BY t2.contid
SELECT t2.continent , COUNT(*) FROM car_makers as t1 JOIN continents as t2 ON t1.country = t2.contid GROUP BY t2.contid
SELECT t2.countryname FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid GROUP BY t1.country ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.countryname FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid GROUP BY t1.country ORDER BY COUNT(*) DESC LIMIT 1
SELECT COUNT(*) , t1.fullname FROM car_makers as t1 JOIN model_list as t2 ON t1.id = t2.maker GROUP BY t1.id
SELECT COUNT(*) , t1.maker , t2.id , t2.fullname FROM model_list as t1 JOIN car_makers as t2 ON t1.maker = t2.id GROUP BY t1.maker
SELECT t2.accelerate FROM car_names as t1 JOIN cars_data as t2 ON t1.makeid = t2.id WHERE t1.make = "amc" AND t1.model = "hornet sportabout (sw)"
SELECT t1.acceleration FROM model_list as t1 JOIN car_names as t2 ON t1.model = t2.model WHERE t1.model = "amc" AND t2.make = "hornet sportabout"
SELECT COUNT(*) FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid WHERE t2.countryname = "france"
SELECT COUNT(*) FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid WHERE t2.countryname = "france"
SELECT COUNT(*) FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid WHERE t2.countryname = "usa"
SELECT COUNT(*) FROM car_makers as t1 JOIN model_list as t2 ON t1.id = t2.maker JOIN countries as t3 ON t1.country = t3.countryid WHERE t3.countryname = "usa"
SELECT AVG(mpg) FROM cars_data WHERE cylinders = 4
SELECT AVG(mpg) FROM cars_data WHERE cylinders = 4
SELECT MIN(weight) FROM cars_data WHERE cylinders = 8 AND year = 1974
SELECT MIN(weight) FROM cars_data WHERE cylinders = 8 AND year = 1974
SELECT maker , model FROM model_list
SELECT maker , model FROM model_list
SELECT t2.countryname , t2.countryid FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid GROUP BY t2.countryid HAVING COUNT(*) >= 1
SELECT t2.countryname , t1.country FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid GROUP BY t1.country HAVING COUNT(*) >= 1
SELECT COUNT(*) FROM cars_data WHERE horsepower > 150
SELECT COUNT(*) FROM cars_data WHERE horsepower > 150
SELECT AVG(weight) , year FROM cars_data GROUP BY year
SELECT AVG(weight) , year FROM cars_data GROUP BY year
SELECT t3.countryname FROM car_makers as t1 JOIN continents as t2 ON t1.country = t2.contid JOIN countries as t3 ON t1.country = t3.countryid WHERE t2.continent = "europe" GROUP BY t3.countryname HAVING COUNT(*) >= 3
SELECT t3.countryname FROM car_makers as t1 JOIN continents as t2 ON t1.country = t2.contid JOIN countries as t3 ON t1.country = t3.countryid WHERE t2.continent = "europe" GROUP BY t3.countryname HAVING COUNT(*) >= 3
SELECT MAX(t2.horsepower) , t1.make FROM car_names as t1 JOIN cars_data as t2 ON t1.makeid = t2.id WHERE t2.cylinders = 3
SELECT t1.make , t1.model FROM car_names as t1 JOIN cars_data as t2 ON t1.makeid = t2.id WHERE t2.cylinders = 3 ORDER BY t2.horsepower DESC LIMIT 1
SELECT t1.model FROM model_list as t1 JOIN cars_data as t2 ON t1.modelid = t2.id ORDER BY t2.mpg DESC LIMIT 1
SELECT id FROM cars_data ORDER BY mpg DESC LIMIT 1
SELECT AVG(horsepower) FROM cars_data WHERE year < 1980
SELECT AVG(horsepower) FROM cars_data WHERE year < 1980
SELECT AVG(t2.edispl) FROM model_list as t1 JOIN cars_data as t2 ON t1.modelid = t2.id WHERE t1.model = "volvo"
SELECT AVG(t3.edispl) FROM model_list as t1 JOIN car_names as t2 ON t1.modelid = t2.makeid JOIN cars_data as t3 ON t2.makeid = t3.id WHERE t1.model = "volvo"
SELECT MAX(accelerate) , cylinders FROM cars_data GROUP BY cylinders
SELECT MAX(accelerate) , cylinders FROM cars_data GROUP BY cylinders
SELECT model FROM car_names GROUP BY model ORDER BY COUNT(*) DESC LIMIT 1
SELECT model FROM model_list GROUP BY model ORDER BY COUNT(*) DESC LIMIT 1
SELECT COUNT(*) FROM cars_data WHERE cylinders > 4
SELECT COUNT(*) FROM cars_data WHERE cylinders > 4
SELECT COUNT(*) FROM cars_data WHERE year = "1980"
SELECT COUNT(*) FROM cars_data WHERE year = 1980
SELECT COUNT(*) FROM car_makers as t1 JOIN model_list as t2 ON t1.id = t2.maker WHERE t1.fullname = "American Motor Company"
SELECT COUNT(*) FROM car_makers as t1 JOIN model_list as t2 ON t1.id = t2.maker WHERE t1.maker = "american motor company"
SELECT t1.fullname , t1.id FROM car_makers as t1 JOIN model_list as t2 ON t1.id = t2.maker GROUP BY t1.id HAVING COUNT(*) > 3
SELECT t2.maker , t1.maker FROM model_list as t1 JOIN car_makers as t2 ON t1.maker = t2.id GROUP BY t1.maker HAVING COUNT(*) > 3
SELECT DISTINCT t1.model FROM model_list as t1 JOIN car_makers as t2 ON t1.maker = t2.id JOIN cars_data as t3 ON t1.modelid = t3.id WHERE t2.fullname = "General Motors" OR t3.weight > 3500
SELECT DISTINCT t1.model FROM model_list as t1 JOIN car_makers as t2 ON t1.maker = t2.id JOIN cars_data as t3 ON t1.modelid = t3.id WHERE t2.maker = "General Motors" OR t3.weight > 3500
SELECT year FROM cars_data WHERE weight BETWEEN 3000 AND 4000
SELECT DISTINCT year FROM cars_data WHERE weight < 4000 INTERSECT SELECT DISTINCT year FROM cars_data WHERE weight > 3000
SELECT horsepower FROM cars_data ORDER BY accelerate DESC LIMIT 1
SELECT horsepower FROM cars_data ORDER BY accelerate DESC LIMIT 1
SELECT cylinders FROM model_list as t1 JOIN cars_data as t2 ON t1.modelid = t2.id WHERE t1.model = "volvo" ORDER BY accelerate LIMIT 1
SELECT COUNT(*) FROM model_list as t1 JOIN car_names as t2 ON t1.model = t2.model WHERE t2.make = "volvo" ORDER BY t1.accelerate LIMIT 1
SELECT COUNT(*) FROM cars_data WHERE accelerate > (SELECT MAX(horsepower) FROM cars_data)
SELECT COUNT(*) FROM cars_data WHERE accelerate > (SELECT MAX(horsepower) FROM cars_data)
SELECT COUNT(DISTINCT country) FROM car_makers GROUP BY country HAVING COUNT(*) > 2
SELECT COUNT(DISTINCT country) FROM car_makers GROUP BY country HAVING COUNT(*) > 2
SELECT COUNT(*) FROM cars_data WHERE cylinders > 6
SELECT COUNT(*) FROM cars_data WHERE cylinders > 6
SELECT id FROM cars_data WHERE cylinders = 4 ORDER BY horsepower DESC LIMIT 1
SELECT id FROM cars_data WHERE cylinders = 4 ORDER BY horsepower DESC LIMIT 1
SELECT t1.makeid , t1.make FROM car_names as t1 JOIN cars_data as t2 ON t1.makeid = t2.id WHERE t2.horsepower > (SELECT MIN(horsepower) FROM cars_data) AND t2.cylinders <= 3
SELECT t1.makeid , t1.make FROM car_names as t1 JOIN cars_data as t2 ON t1.makeid = t2.id WHERE t2.cylinders < 4 EXCEPT SELECT t1.makeid , t1.make FROM car_names as t1 JOIN cars_data as t2 ON t1.makeid = t2.id WHERE t2.horsepower = (SELECT MIN(horsepower) FROM cars_data)
SELECT MAX(mpg) FROM cars_data WHERE cylinders = 8 OR year < 1980
SELECT MAX(mpg) FROM cars_data WHERE cylinders = 8 OR year < 1980
SELECT t2.model FROM car_makers as t1 JOIN model_list as t2 ON t1.id = t2.maker JOIN cars_data as t3 ON t2.modelid = t3.id WHERE t3.weight < 3500 AND t1.fullname != 'Ford Motor Company'
SELECT DISTINCT t2.model FROM car_makers as t1 JOIN car_names as t2 ON t1.id = t3.id JOIN cars_data as t3 ON t2.makeid = t3.id WHERE t3.weight < 3500 AND t1.maker != "ford"
SELECT countryname FROM countries EXCEPT SELECT t2.countryname FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid
SELECT countryname FROM countries EXCEPT SELECT t2.countryname FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid
SELECT t1.maker , t2.id FROM model_list as t1 JOIN car_makers as t2 ON t1.maker = t2.id GROUP BY t2.id HAVING COUNT(*) >= 2 INTERSECT SELECT t1.maker , t2.id FROM model_list as t1 JOIN car_makers as t2 ON t1.maker = t2.id GROUP BY t2.id HAVING COUNT(*) > 3
SELECT t1.makerid , t2.maker FROM model_list as t1 JOIN car_makers as t2 ON t1.maker = t2.maker GROUP BY t1.maker HAVING COUNT(*) >= 2 INTERSECT SELECT t1.makerid , t2.maker FROM model_list as t1 JOIN car_makers as t2 ON t1.maker = t2.maker GROUP BY t1.maker HAVING COUNT(*) > 3
SELECT t1.id , t3.countryname FROM car_makers as t1 JOIN model_list as t2 ON t1.id = t2.maker JOIN countries as t3 ON t1.country = t3.countryid GROUP BY t1.country HAVING COUNT(*) > 3 UNION SELECT t1.id , t3.countryname FROM car_makers as t1 JOIN model_list as t2 ON t1.id = t2.maker JOIN countries as t3 ON t1.country = t3.countryid WHERE t2.model = 'fiat'
SELECT t1.id , t1.country FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid GROUP BY t1.country HAVING COUNT(*) > 3 UNION SELECT t1.id , t1.country FROM car_makers as t1 JOIN countries as t2 ON t1.country = t2.countryid WHERE t2.countryname = "fiat"
SELECT country FROM airlines WHERE airline = "JetBlue Airways"
SELECT country FROM airlines WHERE airline = 'Jetblue Airways'
SELECT abbreviation FROM airlines WHERE airline = "JetBlue Airways"
SELECT abbreviation FROM airlines WHERE airline = 'Jetblue Airways'
SELECT airline , abbreviation FROM airlines WHERE country = 'USA'
SELECT airline , abbreviation FROM airlines WHERE country = 'USA'
SELECT airportcode , airportname FROM airports WHERE city = "Anthony"
SELECT airportcode , airportname FROM airports WHERE city = "Anthony"
SELECT COUNT(*) FROM airlines
SELECT COUNT(*) FROM airlines
SELECT COUNT(*) FROM airports
SELECT COUNT(*) FROM airports
SELECT COUNT(*) FROM flights
SELECT COUNT(*) FROM flights
SELECT airline FROM airlines WHERE abbreviation = 'UAL'
SELECT airline FROM airlines WHERE abbreviation = 'UAL'
SELECT COUNT(*) FROM airlines WHERE country = 'USA'
SELECT COUNT(*) FROM airlines WHERE country = 'USA'
SELECT city , country FROM airports WHERE airportname = "Alton"
SELECT city , country FROM airports WHERE airportname = "Alton"
SELECT airportname FROM airports WHERE airportcode = 'AKO'
SELECT airportname FROM airports WHERE airportcode = 'AKO'
SELECT airportname FROM airports WHERE city = 'Aberdeen'
SELECT airportname FROM airports WHERE city = "Aberdeen"
SELECT COUNT(*) FROM flights WHERE sourceairport = 'APG'
SELECT COUNT(*) FROM flights WHERE sourceairport = 'APG'
SELECT COUNT(*) FROM flights WHERE destairport = 'ATO'
SELECT COUNT(*) FROM flights WHERE destairport = 'ATO'
SELECT COUNT(*) FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.sourceairport WHERE t1.city = "Aberdeen"
SELECT COUNT(*) FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.sourceairport WHERE t1.city = "Aberdeen"
SELECT COUNT(*) FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.destairport WHERE t1.city = "Aberdeen"
SELECT COUNT(*) FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.destairport WHERE t1.city = "Aberdeen"
SELECT COUNT(*) FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.sourceairport WHERE t1.city = 'Aberdeen' INTERSECT SELECT COUNT(*) FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.destairport WHERE t1.city = 'Ashley'
SELECT COUNT(*) FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.sourceairport WHERE t1.city = "Aberdeen" INTERSECT SELECT COUNT(*) FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.destairport WHERE t1.city = "Ashley"
SELECT COUNT(*) FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t1.airline = 'JetBlue Airways'
SELECT COUNT(*) FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t1.airline = 'Jetblue Airways'
SELECT COUNT(*) FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t1.airline = 'United Airlines' AND t2.destairport = 'ASY'
SELECT COUNT(*) FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t1.airline = 'United Airlines' AND t2.destairport = 'ASY'
SELECT COUNT(*) FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t1.airline = 'United Airlines' AND t2.sourceairport = 'AHD'
SELECT COUNT(*) FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t1.airline = 'United Airlines' AND t2.sourceairport = 'AHD'
SELECT COUNT(*) FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline JOIN airports as t3 ON t2.destairport = t3.airportcode WHERE t1.airline = 'United Airlines' AND t3.city = 'Aberdeen'
SELECT COUNT(*) FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline JOIN airports as t3 ON t2.destairport = t3.airportcode WHERE t1.airline = 'United Airlines' AND t3.city = 'Aberdeen'
SELECT t1.city FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.destairport GROUP BY t1.city ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.city FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.destairport GROUP BY t1.city ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.city FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.sourceairport GROUP BY t1.city ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.city FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.sourceairport GROUP BY t2.sourceairport ORDER BY COUNT(*) DESC LIMIT 1
SELECT destairport FROM flights GROUP BY destairport ORDER BY COUNT(*) DESC LIMIT 1
SELECT sourceairport FROM flights GROUP BY sourceairport ORDER BY COUNT(*) DESC LIMIT 1
SELECT sourceairport FROM flights GROUP BY sourceairport ORDER BY COUNT(*) LIMIT 1
SELECT sourceairport FROM flights GROUP BY sourceairport ORDER BY COUNT(*) LIMIT 1
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline GROUP BY t1.uid ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline GROUP BY t2.airline ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.abbreviation , t1.country FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline GROUP BY t2.airline ORDER BY COUNT(*) LIMIT 1
SELECT t1.abbreviation , t1.country FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline GROUP BY t2.airline ORDER BY COUNT(*) LIMIT 1
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.sourceairport = 'AHD'
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.sourceairport = 'AHD'
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.destairport = 'AHD'
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.destairport = 'AHD'
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.sourceairport = 'APG' INTERSECT SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.sourceairport = 'CVO'
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.sourceairport = 'APG' INTERSECT SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.sourceairport = 'CVO'
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.sourceairport = 'CVO' EXCEPT SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.sourceairport = 'APG'
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.sourceairport = 'CVO' EXCEPT SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t2.sourceairport = 'APG'
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline GROUP BY t1.uid HAVING COUNT(*) >= 10
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline GROUP BY t1.uid HAVING COUNT(*) >= 10
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline GROUP BY t2.airline HAVING COUNT(*) < 200
SELECT t1.airline FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline GROUP BY t1.uid HAVING COUNT(*) < 200
SELECT t2.flightno FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t1.airline = "United Airlines"
SELECT t2.flightno FROM airlines as t1 JOIN flights as t2 ON t1.uid = t2.airline WHERE t1.airline = 'United Airlines'
SELECT flightno FROM flights WHERE sourceairport = "APG"
SELECT flightno FROM flights WHERE sourceairport = 'APG'
SELECT flightno FROM flights WHERE destairport = "APG"
SELECT flightno FROM flights WHERE destairport = 'APG'
SELECT t2.flightno FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.sourceairport WHERE t1.city = "Aberdeen"
SELECT t2.flightno FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.sourceairport WHERE t1.city = "Aberdeen"
SELECT t2.flightno FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.destairport WHERE t1.city = "Aberdeen"
SELECT t2.flightno FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.destairport WHERE t1.city = "Aberdeen"
SELECT COUNT(*) FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.destairport WHERE t1.city = "Aberdeen" OR t1.city = "Abilene"
SELECT COUNT(*) FROM airports as t1 JOIN flights as t2 ON t1.airportcode = t2.destairport WHERE t1.city = "Aberdeen" OR t1.city = "Abilene"
SELECT airportname FROM airports WHERE airportcode NOT IN (SELECT sourceairport FROM flights) AND airportcode NOT IN (SELECT destairport FROM flights)
SELECT airportname FROM airports WHERE airportcode NOT IN (SELECT sourceairport FROM flights) AND airportcode NOT IN (SELECT destairport FROM flights)
SELECT COUNT(*) FROM employee
SELECT COUNT(*) FROM employee
SELECT name FROM employee ORDER BY age ASC
SELECT name FROM employee ORDER BY age ASC
SELECT COUNT(*) , city FROM employee GROUP BY city
SELECT COUNT(*) , city FROM employee GROUP BY city
SELECT city FROM employee WHERE age < 30 GROUP BY city HAVING COUNT(*) > 1
SELECT city FROM employee WHERE age < 30 GROUP BY city HAVING COUNT(*) > 1
SELECT location , COUNT(*) FROM shop GROUP BY location
SELECT location , COUNT(*) FROM shop GROUP BY location
SELECT manager_name , district FROM shop ORDER BY number_products DESC LIMIT 1
SELECT manager_name , district FROM shop ORDER BY number_products DESC LIMIT 1
SELECT MIN(number_products) , MAX(number_products) FROM shop
SELECT MIN(number_products) , MAX(number_products) FROM shop
SELECT name , location , district FROM shop ORDER BY number_products DESC
SELECT name , location , district FROM shop ORDER BY number_products DESC
SELECT name FROM shop WHERE number_products > (SELECT AVG(number_products) FROM shop)
SELECT name FROM shop WHERE number_products > (SELECT AVG(number_products) FROM shop)
SELECT t2.name FROM evaluation as t1 JOIN employee as t2 ON t1.employee_id = t2.employee_id GROUP BY t1.employee_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.name FROM evaluation as t1 JOIN employee as t2 ON t1.employee_id = t2.employee_id GROUP BY t1.employee_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.name FROM evaluation as t1 JOIN employee as t2 ON t1.employee_id = t2.employee_id ORDER BY t1.bonus DESC LIMIT 1
SELECT t2.name FROM evaluation as t1 JOIN employee as t2 ON t1.employee_id = t2.employee_id ORDER BY t1.bonus DESC LIMIT 1
SELECT name FROM employee WHERE employee_id NOT IN (SELECT employee_id FROM evaluation)
SELECT name FROM employee WHERE employee_id NOT IN (SELECT employee_id FROM evaluation)
SELECT t1.name FROM shop as t1 JOIN hiring as t2 ON t1.shop_id = t2.shop_id GROUP BY t2.shop_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.name FROM hiring as t1 JOIN shop as t2 ON t1.shop_id = t2.shop_id GROUP BY t1.shop_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT name FROM hiring as t1 JOIN shop as t2 ON t1.shop_id = t2.shop_id WHERE t1.employee_id IS NULL
SELECT name FROM hiring as t1 JOIN shop as t2 ON t1.shop_id = t2.shop_id GROUP BY t1.shop_id HAVING COUNT(*) = 0
SELECT COUNT(*) , t1.name FROM shop as t1 JOIN hiring as t2 ON t1.shop_id = t2.shop_id GROUP BY t1.shop_id
SELECT COUNT(*) , t1.name FROM shop as t1 JOIN hiring as t2 ON t1.shop_id = t2.shop_id GROUP BY t1.shop_id
SELECT SUM(bonus) FROM evaluation
SELECT SUM(bonus) FROM evaluation
SELECT * FROM hiring
SELECT * FROM hiring
SELECT district FROM shop WHERE number_products < 3000 INTERSECT SELECT district FROM shop WHERE number_products > 10000
SELECT district FROM shop WHERE number_products < 3000 INTERSECT SELECT district FROM shop WHERE number_products > 10000
SELECT COUNT(DISTINCT location) FROM shop
SELECT COUNT(DISTINCT location) FROM shop
SELECT COUNT(*) FROM documents
SELECT COUNT(*) FROM documents
SELECT document_id , document_name , document_description FROM documents
SELECT document_id , document_name , document_description FROM documents
SELECT document_name , template_id FROM documents WHERE document_description LIKE '%w%'
SELECT document_name , template_id FROM documents WHERE document_description LIKE '%w%'
SELECT document_id , template_id , document_description FROM documents WHERE document_name = "Robbin CV"
SELECT document_id , template_id , document_description FROM documents WHERE document_name = "Robbin CV"
SELECT COUNT(DISTINCT template_id) FROM documents
SELECT COUNT(DISTINCT template_id) FROM documents
SELECT COUNT(*) FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id WHERE t2.template_type_code = 'PPT'
SELECT COUNT(*) FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id WHERE t2.template_type_code = "PPT"
SELECT template_id , COUNT(*) FROM documents GROUP BY template_id
SELECT template_id , COUNT(*) FROM documents GROUP BY template_id
SELECT t1.template_id , t2.template_type_code FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id GROUP BY t1.template_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.template_id , t2.template_type_code FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id GROUP BY t1.template_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT template_id FROM documents GROUP BY template_id HAVING COUNT(*) > 1
SELECT template_id FROM documents GROUP BY template_id HAVING COUNT(*) > 1
SELECT template_id FROM templates EXCEPT SELECT template_id FROM documents
SELECT template_id FROM templates EXCEPT SELECT template_id FROM documents
SELECT COUNT(*) FROM templates
SELECT COUNT(*) FROM templates
SELECT template_id , version_number , template_type_code FROM templates
SELECT template_id , version_number , template_type_code FROM templates
SELECT DISTINCT template_type_code FROM templates
SELECT DISTINCT template_type_code FROM ref_template_types
SELECT template_id FROM templates WHERE template_type_code = "PP" OR template_type_code = "PPT"
SELECT template_id FROM templates WHERE template_type_code = "PP" OR template_type_code = "PPT"
SELECT COUNT(*) FROM templates WHERE template_type_code = "CV"
SELECT COUNT(*) FROM templates WHERE template_type_code = "CV"
SELECT version_number , template_type_code FROM templates WHERE version_number > 5
SELECT version_number , template_type_code FROM templates WHERE version_number > 5
SELECT template_type_code , COUNT(*) FROM templates GROUP BY template_type_code
SELECT template_type_code , COUNT(*) FROM templates GROUP BY template_type_code
SELECT template_type_code FROM templates GROUP BY template_type_code ORDER BY COUNT(*) DESC LIMIT 1
SELECT template_type_code FROM templates GROUP BY template_type_code ORDER BY COUNT(*) DESC LIMIT 1
SELECT template_type_code FROM templates GROUP BY template_type_code HAVING COUNT(*) < 3
SELECT template_type_code FROM templates GROUP BY template_type_code HAVING COUNT(*) < 3
SELECT version_number , template_type_code FROM templates ORDER BY version_number ASC LIMIT 1
SELECT version_number , template_type_code FROM templates ORDER BY version_number ASC LIMIT 1
SELECT t2.template_type_code FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id WHERE t1.document_name = "Data base"
SELECT t2.template_type_code FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id WHERE t1.document_name = "Data base"
SELECT t1.document_name FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id WHERE t2.template_type_code = "BK"
SELECT t1.document_name FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id WHERE t2.template_type_code = "BK"
SELECT t2.template_type_code , COUNT(*) FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id GROUP BY t2.template_type_code
SELECT t2.template_type_code , COUNT(*) FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id GROUP BY t2.template_type_code
SELECT t2.template_type_code FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id GROUP BY t2.template_type_code ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.template_type_code FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id GROUP BY t2.template_type_code ORDER BY COUNT(*) DESC LIMIT 1
SELECT template_type_code FROM templates EXCEPT SELECT t2.template_type_code FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id
SELECT template_type_code FROM templates EXCEPT SELECT t2.template_type_code FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id
SELECT template_type_code , template_type_description FROM ref_template_types
SELECT template_type_code , template_type_description FROM ref_template_types
SELECT template_type_description FROM ref_template_types WHERE template_type_code = "AD"
SELECT template_type_description FROM ref_template_types WHERE template_type_code = "AD"
SELECT template_type_code FROM ref_template_types WHERE template_type_description = "Book"
SELECT template_type_code FROM ref_template_types WHERE template_type_description = "Book"
SELECT DISTINCT t1.template_type_description FROM ref_template_types as t1 JOIN templates as t2 ON t1.template_type_code = t2.template_type_code
SELECT DISTINCT t2.template_details FROM documents as t1 JOIN templates as t2 ON t1.template_id = t2.template_id
SELECT t2.template_id FROM ref_template_types as t1 JOIN templates as t2 ON t1.template_type_code = t2.template_type_code WHERE t1.template_type_description = "Presentation"
SELECT t2.template_id FROM ref_template_types as t1 JOIN templates as t2 ON t1.template_type_code = t2.template_type_code WHERE t1.template_type_description = 'Presentation'
SELECT COUNT(*) FROM paragraphs
SELECT COUNT(*) FROM paragraphs
SELECT COUNT(*) FROM documents as t1 JOIN paragraphs as t2 ON t1.document_id = t2.document_id WHERE t1.document_name = 'Summer Show'
SELECT COUNT(*) FROM documents as t1 JOIN paragraphs as t2 ON t1.document_id = t2.document_id WHERE t1.document_name = 'Summer Show'
SELECT other_details FROM paragraphs WHERE paragraph_text = 'Korea'
SELECT other_details FROM paragraphs WHERE paragraph_text LIKE '%Korea%'
SELECT t2.paragraph_id , t2.paragraph_text FROM documents as t1 JOIN paragraphs as t2 ON t1.document_id = t2.document_id WHERE t1.document_name = 'Welcome to NY'
SELECT t2.paragraph_id , t2.paragraph_text FROM documents as t1 JOIN paragraphs as t2 ON t1.document_id = t2.document_id WHERE t1.document_name = 'Welcome to NY'
SELECT t2.paragraph_text FROM documents as t1 JOIN paragraphs as t2 ON t1.document_id = t2.document_id WHERE t1.document_name = "Customer reviews"
SELECT t2.paragraph_text FROM documents as t1 JOIN paragraphs as t2 ON t1.document_id = t2.document_id WHERE t1.document_name = 'Customer reviews'
SELECT document_id , COUNT(*) FROM paragraphs GROUP BY document_id ORDER BY document_id
SELECT document_id , COUNT(*) FROM paragraphs GROUP BY document_id ORDER BY document_id
SELECT t1.document_id , t1.document_name , COUNT(*) FROM documents as t1 JOIN paragraphs as t2 ON t1.document_id = t2.document_id GROUP BY t1.document_id
SELECT t1.document_id , t1.document_name , COUNT(*) FROM documents as t1 JOIN paragraphs as t2 ON t1.document_id = t2.document_id GROUP BY t1.document_id
SELECT document_id FROM paragraphs GROUP BY document_id HAVING COUNT(*) >= 2
SELECT document_id FROM paragraphs GROUP BY document_id HAVING COUNT(*) >= 2
SELECT t1.document_id , t1.document_name FROM documents as t1 JOIN paragraphs as t2 ON t1.document_id = t2.document_id GROUP BY t1.document_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.document_id , t1.document_name FROM documents as t1 JOIN paragraphs as t2 ON t1.document_id = t2.document_id GROUP BY t1.document_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT document_id FROM paragraphs GROUP BY document_id ORDER BY COUNT(*) LIMIT 1
SELECT document_id FROM paragraphs GROUP BY document_id ORDER BY COUNT(*) LIMIT 1
SELECT document_id FROM paragraphs GROUP BY document_id HAVING COUNT(*) BETWEEN 1 AND 2
SELECT document_id FROM paragraphs GROUP BY document_id HAVING COUNT(*) BETWEEN 1 AND 2
SELECT document_id FROM paragraphs WHERE paragraph_text = 'Brazil' INTERSECT SELECT document_id FROM paragraphs WHERE paragraph_text = 'Ireland'
SELECT document_id FROM paragraphs WHERE paragraph_text = 'Brazil' INTERSECT SELECT document_id FROM paragraphs WHERE paragraph_text = 'Ireland'
SELECT COUNT(*) FROM teacher
SELECT COUNT(*) FROM teacher
SELECT name FROM teacher ORDER BY age ASC
SELECT name FROM teacher ORDER BY age ASC
SELECT age , hometown FROM teacher
SELECT age , hometown FROM teacher
SELECT name FROM teacher WHERE hometown != 'Little Lever Urban District'
SELECT name FROM teacher WHERE hometown != 'Little Lever Urban District'
SELECT name FROM teacher WHERE age = 32 OR age = 33
SELECT name FROM teacher WHERE age = 32 OR age = 33
SELECT hometown FROM teacher ORDER BY age LIMIT 1
SELECT hometown FROM teacher ORDER BY age LIMIT 1
SELECT hometown , COUNT(*) FROM teacher GROUP BY hometown
SELECT COUNT(*) , hometown FROM teacher GROUP BY hometown
SELECT hometown FROM teacher GROUP BY hometown ORDER BY COUNT(*) DESC LIMIT 1
SELECT hometown FROM teacher GROUP BY hometown ORDER BY COUNT(*) DESC LIMIT 1
SELECT hometown FROM teacher GROUP BY hometown HAVING COUNT(*) >= 2
SELECT hometown FROM teacher GROUP BY hometown HAVING COUNT(*) >= 2
SELECT t2.name , t1.course FROM course as t1 JOIN teacher as t2 ON t1.course_id = t3.course_id JOIN course_arrange as t3 ON t2.teacher_id = t3.teacher_id
SELECT t2.name , t1.course FROM course as t1 JOIN teacher as t2 ON t1.course_id = t3.course_id JOIN course_arrange as t3 ON t2.teacher_id = t3.teacher_id
SELECT t2.name , t1.course FROM course as t1 JOIN teacher as t2 ON t1.course_id = t3.course_id JOIN course_arrange as t3 ON t2.teacher_id = t3.teacher_id ORDER BY t2.name asC
SELECT t2.name , t1.course FROM course as t1 JOIN teacher as t2 ON t1.course_id = t3.course_id JOIN course_arrange as t3 ON t2.teacher_id = t3.teacher_id ORDER BY t2.name asC
SELECT t2.name FROM course as t1 JOIN teacher as t2 ON t1.course_id = t3.course_id JOIN course_arrange as t3 ON t2.teacher_id = t3.teacher_id WHERE t1.course = "Math"
SELECT t2.name FROM course as t1 JOIN teacher as t2 ON t1.course_id = t3.course_id JOIN course_arrange as t3 ON t2.teacher_id = t3.teacher_id WHERE t1.course = "Math"
SELECT t1.name , COUNT(*) FROM teacher as t1 JOIN course_arrange as t2 ON t1.teacher_id = t2.teacher_id GROUP BY t1.teacher_id
SELECT t1.name , COUNT(*) FROM teacher as t1 JOIN course_arrange as t2 ON t1.teacher_id = t2.teacher_id GROUP BY t1.teacher_id
SELECT t1.name FROM teacher as t1 JOIN course_arrange as t2 ON t1.teacher_id = t2.teacher_id GROUP BY t1.teacher_id HAVING COUNT(*) >= 2
SELECT t1.name FROM teacher as t1 JOIN course_arrange as t2 ON t1.teacher_id = t2.teacher_id GROUP BY t1.teacher_id HAVING COUNT(*) >= 2
SELECT name FROM teacher WHERE teacher_id NOT IN (SELECT teacher_id FROM course_arrange)
SELECT name FROM teacher WHERE teacher_id NOT IN (SELECT teacher_id FROM course_arrange)
SELECT COUNT(*) FROM visitor WHERE age < 30
SELECT name FROM visitor WHERE level_of_membership > 4 ORDER BY level_of_membership DESC
SELECT AVG(age) FROM visitor WHERE level_of_membership <= 4
SELECT name , level_of_membership FROM visitor WHERE level_of_membership > 4 ORDER BY age DESC
SELECT museum_id , name FROM museum ORDER BY num_of_staff DESC LIMIT 1
SELECT AVG(num_of_staff) FROM museum WHERE open_year < 2009
SELECT open_year , num_of_staff FROM museum WHERE name = 'Plaza Museum'
SELECT name FROM museum WHERE num_of_staff > (SELECT MIN(num_of_staff) FROM museum WHERE open_year > 2010)
SELECT t1.id , t1.name , t1.age FROM visitor as t1 JOIN visit as t2 ON t1.id = t2.visitor_id GROUP BY t2.visitor_id HAVING COUNT(*) > 1
SELECT t1.id , t1.name , t1.level_of_membership FROM visitor as t1 JOIN visit as t2 ON t1.id = t2.visitor_id GROUP BY t2.visitor_id ORDER BY SUM(t2.total_spent) DESC LIMIT 1
SELECT t1.museum_id , t1.name FROM museum as t1 JOIN visit as t2 ON t1.museum_id = t2.museum_id GROUP BY t1.museum_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT name FROM visit as t1 JOIN museum as t2 ON t1.museum_id = t2.museum_id WHERE visitor_id IS NULL
SELECT t1.name , t1.age FROM visitor as t1 JOIN visit as t2 ON t1.id = t2.visitor_id GROUP BY t2.visitor_id ORDER BY SUM(t2.num_of_ticket) DESC LIMIT 1
SELECT AVG(num_of_ticket) , MAX(num_of_ticket) FROM visit
SELECT SUM(t2.total_spent) FROM visitor as t1 JOIN visit as t2 ON t1.id = t2.visitor_id WHERE t1.level_of_membership = 1
SELECT t2.name FROM museum as t1 JOIN visitor as t2 ON t1.museum_id = t3.museum_id JOIN visit as t3 ON t2.id = t3.visitor_id WHERE t1.open_year < 2009 INTERSECT SELECT t2.name FROM museum as t1 JOIN visitor as t2 ON t1.museum_id = t3.museum_id JOIN visit as t3 ON t2.id = t3.visitor_id WHERE t1.open_year > 2011
SELECT COUNT(*) FROM visit WHERE museum_id NOT IN (SELECT museum_id FROM museum WHERE open_year > 2010)
SELECT COUNT(*) FROM museum WHERE open_year > 2013 OR open_year < 2008
SELECT COUNT(*) FROM players
SELECT COUNT(*) FROM players
SELECT COUNT(*) FROM matches
SELECT COUNT(*) FROM matches
SELECT first_name , birth_date FROM players WHERE country_code = 'USA'
SELECT first_name , birth_date FROM players WHERE country_code = 'USA'
SELECT AVG(loser_age) , AVG(winner_age) FROM matches
SELECT AVG(loser_age) , AVG(winner_age) FROM matches
SELECT AVG(winner_rank) FROM matches
SELECT AVG(winner_rank) FROM matches
SELECT MAX(loser_rank) FROM matches
SELECT MIN(loser_rank) FROM matches
SELECT COUNT(DISTINCT country_code) FROM players
SELECT COUNT(DISTINCT country_code) FROM players
SELECT COUNT(DISTINCT loser_name) FROM matches
SELECT COUNT(DISTINCT loser_name) FROM matches
SELECT tourney_name FROM matches GROUP BY tourney_name HAVING COUNT(*) > 10
SELECT tourney_name FROM matches GROUP BY tourney_name HAVING COUNT(*) > 10
SELECT winner_name FROM matches WHERE year = 2013 INTERSECT SELECT winner_name FROM matches WHERE year = 2016
SELECT winner_name FROM matches WHERE year = 2013 INTERSECT SELECT winner_name FROM matches WHERE year = 2016
SELECT match_num FROM matches WHERE year = 2013 OR year = 2016
SELECT COUNT(*) FROM matches WHERE year = 2013 OR year = 2016
SELECT t1.country_code , t1.first_name FROM players as t1 JOIN matches as t2 ON t1.player_id = t2.winner_id WHERE t2.tourney_name = "WTA Championships" INTERSECT SELECT t1.country_code , t1.first_name FROM players as t1 JOIN matches as t2 ON t1.player_id = t2.winner_id WHERE t2.tourney_name = "Australian Open"
SELECT t1.first_name , t1.country_code FROM players as t1 JOIN matches as t2 ON t1.player_id = t2.winner_id WHERE t2.tourney_name = "WTA Championships" INTERSECT SELECT t1.first_name , t1.country_code FROM players as t1 JOIN matches as t2 ON t1.player_id = t2.winner_id WHERE t2.tourney_name = "Australian Open"
SELECT first_name , country_code FROM players ORDER BY birth_date LIMIT 1
SELECT first_name , country_code FROM players ORDER BY birth_date LIMIT 1
SELECT first_name , last_name FROM players ORDER BY birth_date
SELECT first_name , last_name FROM players ORDER BY birth_date
SELECT first_name , last_name FROM players WHERE hand = 'L' ORDER BY birth_date
SELECT first_name , last_name FROM players WHERE hand = 'L' ORDER BY birth_date
SELECT t2.first_name , t2.country_code FROM rankings as t1 JOIN players as t2 ON t1.player_id = t2.player_id GROUP BY t1.player_id ORDER BY SUM(t1.tours) DESC LIMIT 1
SELECT t2.first_name , t2.country_code FROM rankings as t1 JOIN players as t2 ON t1.player_id = t2.player_id GROUP BY t1.player_id ORDER BY SUM(t1.tours) DESC LIMIT 1
SELECT year FROM matches GROUP BY year ORDER BY COUNT(*) DESC LIMIT 1
SELECT year FROM matches GROUP BY year ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.first_name , t2.last_name , t1.ranking_points FROM rankings as t1 JOIN players as t2 ON t1.player_id = t2.player_id GROUP BY t1.player_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.first_name , t2.last_name , t1.ranking_points FROM rankings as t1 JOIN players as t2 ON t1.player_id = t2.player_id JOIN matches as t3 ON t2.player_id = t3.winner_id GROUP BY t3.winner_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT winner_name FROM matches WHERE tourney_name = "Australian Open" ORDER BY winner_rank_points DESC LIMIT 1
SELECT t2.first_name , t2.last_name FROM rankings as t1 JOIN players as t2 ON t1.player_id = t2.player_id JOIN matches as t3 ON t2.player_id = t3.winner_id WHERE t3.tourney_name = "Australian Open" ORDER BY t1.ranking_points DESC LIMIT 1
SELECT loser_name , winner_name FROM matches ORDER BY minutes DESC LIMIT 1
SELECT winner_name , loser_name FROM matches ORDER BY minutes DESC LIMIT 1
SELECT AVG(ranking) , t2.first_name FROM rankings as t1 JOIN players as t2 ON t1.player_id = t2.player_id GROUP BY t2.first_name
SELECT t2.first_name , AVG(t1.ranking) FROM rankings as t1 JOIN players as t2 ON t1.player_id = t2.player_id GROUP BY t2.first_name
SELECT SUM(t1.ranking_points) , t2.first_name FROM rankings as t1 JOIN players as t2 ON t1.player_id = t2.player_id GROUP BY t2.first_name
SELECT t2.first_name , SUM(t1.ranking_points) FROM rankings as t1 JOIN players as t2 ON t1.player_id = t2.player_id GROUP BY t2.first_name
SELECT country_code , COUNT(*) FROM players GROUP BY country_code
SELECT country_code , COUNT(*) FROM players GROUP BY country_code
SELECT country_code FROM players GROUP BY country_code ORDER BY COUNT(*) DESC LIMIT 1
SELECT country_code FROM players GROUP BY country_code ORDER BY COUNT(*) DESC LIMIT 1
SELECT country_code FROM players GROUP BY country_code HAVING COUNT(*) > 50
SELECT country_code FROM players GROUP BY country_code HAVING COUNT(*) > 50
SELECT ranking_date , SUM(tours) FROM rankings GROUP BY ranking_date
SELECT ranking_date , SUM(tours) FROM rankings GROUP BY ranking_date
SELECT COUNT(*) , year FROM matches GROUP BY year
SELECT COUNT(*) , year FROM matches GROUP BY year
SELECT winner_name , winner_rank FROM matches ORDER BY winner_age LIMIT 3
SELECT winner_name , winner_rank FROM matches ORDER BY winner_age LIMIT 3
SELECT COUNT(DISTINCT winner_name) FROM matches WHERE tourney_name = "WTA Championships" AND winner_hand = "L"
SELECT COUNT(*) FROM matches WHERE winner_hand = "L" AND tourney_name = "WTA Championships"
SELECT t1.first_name , t1.country_code , t1.birth_date FROM players as t1 JOIN rankings as t2 ON t1.player_id = t2.player_id ORDER BY t2.ranking_points DESC LIMIT 1
SELECT t1.first_name , t1.country_code , t1.birth_date FROM players as t1 JOIN matches as t2 ON t1.player_id = t2.winner_id GROUP BY t1.player_id ORDER BY SUM(t2.winner_rank_points) DESC LIMIT 1
SELECT hand , COUNT(*) FROM players GROUP BY hand
SELECT hand , COUNT(*) FROM players GROUP BY hand
SELECT COUNT(*) FROM ship WHERE disposition_of_ship = 'Captured'
SELECT name , tonnage FROM ship ORDER BY name DESC
SELECT name , date , result FROM battle
SELECT MAX(killed) , MIN(killed) FROM death
SELECT AVG(injured) FROM death
SELECT t1.note , t1.killed , t1.injured FROM death as t1 JOIN ship as t2 ON t1.caused_by_ship_id = t2.id WHERE t2.tonnage = 't'
SELECT name , result FROM battle WHERE bulgarian_commander != 'Boril'
SELECT DISTINCT t2.id , t2.name FROM ship as t1 JOIN battle as t2 ON t1.lost_in_battle = t2.id WHERE t1.ship_type = 'Brig'
SELECT t1.id , t3.name FROM death as t1 JOIN ship as t2 ON t1.caused_by_ship_id = t2.id JOIN battle as t3 ON t2.lost_in_battle = t3.id GROUP BY t1.id HAVING SUM(t1.killed) > 10
SELECT t1.caused_by_ship_id , t2.name FROM death as t1 JOIN ship as t2 ON t1.caused_by_ship_id = t2.id GROUP BY t1.caused_by_ship_id ORDER BY SUM(t1.injured) DESC LIMIT 1
SELECT DISTINCT name FROM battle WHERE bulgarian_commander = 'Kaloyan' AND latin_commander = 'Baldwin I'
SELECT COUNT(DISTINCT result) FROM battle
SELECT COUNT(*) FROM battle WHERE id NOT IN (SELECT lost_in_battle FROM ship WHERE tonnage = '225')
SELECT t1.name , t1.date FROM battle as t1 JOIN ship as t2 ON t1.id = t2.lost_in_battle WHERE t2.name = 'Lettice' INTERSECT SELECT t1.name , t1.date FROM battle as t1 JOIN ship as t2 ON t1.id = t2.lost_in_battle WHERE t2.name = 'HMS Atalanta'
SELECT name , result , bulgarian_commander FROM battle WHERE id NOT IN (SELECT lost_in_battle FROM ship WHERE location = 'English Channel')
SELECT note FROM death WHERE note LIKE '%East%'
SELECT line_1 , line_2 FROM addresses
SELECT line_1 , line_2 FROM addresses
SELECT COUNT(*) FROM courses
SELECT COUNT(*) FROM courses
SELECT course_description FROM courses WHERE course_name = "math"
SELECT course_description FROM courses WHERE course_name = "math"
SELECT zip_postcode FROM addresses WHERE city = "Port Chelsea"
SELECT zip_postcode FROM addresses WHERE city = "Port Chelsea"
SELECT t1.department_name , t1.department_id FROM departments as t1 JOIN degree_programs as t2 ON t1.department_id = t2.department_id GROUP BY t1.department_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.department_name , t1.department_id FROM departments as t1 JOIN degree_programs as t2 ON t1.department_id = t2.department_id GROUP BY t1.department_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT COUNT(DISTINCT department_id) FROM degree_programs
SELECT COUNT(DISTINCT department_id) FROM degree_programs
SELECT COUNT(DISTINCT degree_summary_name) FROM degree_programs
SELECT COUNT(DISTINCT degree_summary_name) FROM degree_programs
SELECT COUNT(*) FROM degree_programs as t1 JOIN departments as t2 ON t1.department_id = t2.department_id WHERE t2.department_name = "engineering"
SELECT COUNT(*) FROM degree_programs as t1 JOIN departments as t2 ON t1.department_id = t2.department_id WHERE t2.department_name = "engineering"
SELECT section_name , section_description FROM sections
SELECT section_name , section_description FROM sections
SELECT t2.course_name , t1.course_id FROM sections as t1 JOIN courses as t2 ON t1.course_id = t2.course_id GROUP BY t1.course_id HAVING COUNT(*) <= 2
SELECT t2.course_name , t1.course_id FROM sections as t1 JOIN courses as t2 ON t1.course_id = t2.course_id GROUP BY t1.course_id HAVING COUNT(*) < 2
SELECT section_name FROM sections ORDER BY section_name DESC
SELECT section_name FROM sections ORDER BY section_name DESC
SELECT t1.semester_name , t1.semester_id FROM semesters as t1 JOIN student_enrolment as t2 ON t1.semester_id = t2.semester_id GROUP BY t1.semester_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.semester_name , t1.semester_id FROM semesters as t1 JOIN student_enrolment as t2 ON t1.semester_id = t2.semester_id GROUP BY t1.semester_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT department_description FROM departments WHERE department_name LIKE '%computer%'
SELECT department_description FROM departments WHERE department_name LIKE '%computer%'
SELECT t1.first_name , t1.middle_name , t1.last_name , t1.student_id FROM students as t1 JOIN student_enrolment as t2 ON t1.student_id = t2.student_id GROUP BY t1.student_id HAVING COUNT(*) = 2
SELECT t1.first_name , t1.middle_name , t1.last_name , t1.student_id FROM students as t1 JOIN student_enrolment as t2 ON t1.student_id = t2.student_id GROUP BY t1.student_id HAVING COUNT(*) = 2
SELECT t2.first_name , t2.middle_name , t2.last_name FROM degree_programs as t1 JOIN students as t2 ON t1.degree_program_id = t3.degree_program_id WHERE t1.degree_summary_name = "Bachelor"
SELECT t2.first_name , t2.middle_name , t2.last_name FROM degree_programs as t1 JOIN students as t2 ON t1.degree_program_id = t3.degree_program_id WHERE t1.degree_summary_name = "Bachelors"
SELECT t1.degree_summary_name FROM degree_programs as t1 JOIN student_enrolment as t2 ON t1.degree_program_id = t2.degree_program_id GROUP BY t1.degree_program_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.degree_summary_name FROM degree_programs as t1 JOIN student_enrolment as t2 ON t1.degree_program_id = t2.degree_program_id GROUP BY t1.degree_program_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.degree_program_id , t1.degree_summary_name FROM degree_programs as t1 JOIN student_enrolment as t2 ON t1.degree_program_id = t2.degree_program_id GROUP BY t1.degree_program_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.degree_program_id , t1.degree_summary_name FROM degree_programs as t1 JOIN student_enrolment as t2 ON t1.degree_program_id = t2.degree_program_id GROUP BY t1.degree_program_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.student_id , t1.first_name , t1.middle_name , t1.last_name , COUNT(*) , t1.student_id FROM students as t1 JOIN student_enrolment as t2 ON t1.student_id = t2.student_id GROUP BY t1.student_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.first_name , t1.middle_name , t1.last_name , t1.student_id , COUNT(*) FROM students as t1 JOIN student_enrolment as t2 ON t1.student_id = t2.student_id GROUP BY t1.student_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT semester_name FROM semesters WHERE semester_id NOT IN (SELECT semester_id FROM student_enrolment)
SELECT semester_name FROM semesters WHERE semester_id NOT IN (SELECT semester_id FROM student_enrolment)
SELECT DISTINCT t1.course_name FROM courses as t1 JOIN student_enrolment_courses as t2 ON t1.course_id = t2.course_id
SELECT t1.course_name FROM courses as t1 JOIN student_enrolment_courses as t2 ON t1.course_id = t2.course_id GROUP BY t1.course_name
SELECT t1.course_name FROM courses as t1 JOIN student_enrolment_courses as t2 ON t1.course_id = t2.course_id GROUP BY t1.course_name ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.course_name FROM courses as t1 JOIN student_enrolment_courses as t2 ON t1.course_id = t2.course_id GROUP BY t1.course_name ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.last_name FROM addresses as t1 JOIN students as t2 ON t1.address_id = t2.current_address_id WHERE t1.state_province_county = "North Carolina" EXCEPT SELECT t3.last_name FROM addresses as t1 JOIN students as t3 ON t1.address_id = t3.current_address_id JOIN student_enrolment as t4 ON t3.student_id = t4.student_id
SELECT t2.last_name FROM addresses as t1 JOIN students as t2 ON t1.address_id = t2.current_address_id WHERE t1.state_province_county = "North Carolina" EXCEPT SELECT t3.last_name FROM addresses as t1 JOIN students as t3 ON t1.address_id = t3.current_address_id JOIN student_enrolment as t4 ON t3.student_id = t4.student_id
SELECT t1.transcript_date , t1.transcript_id FROM transcripts as t1 JOIN transcript_contents as t2 ON t1.transcript_id = t2.transcript_id GROUP BY t1.transcript_id HAVING COUNT(*) >= 2
SELECT t1.transcript_date , t1.transcript_id FROM transcripts as t1 JOIN transcript_contents as t2 ON t1.transcript_id = t2.transcript_id GROUP BY t1.transcript_id HAVING COUNT(*) >= 2
SELECT cell_mobile_number FROM students WHERE first_name = "Timmothy" AND last_name = "Ward"
SELECT cell_mobile_number FROM students WHERE first_name = "Timmothy" AND last_name = "Ward"
SELECT first_name , middle_name , last_name FROM students ORDER BY date_first_registered LIMIT 1
SELECT first_name , middle_name , last_name FROM students ORDER BY date_first_registered LIMIT 1
SELECT first_name , middle_name , last_name FROM students ORDER BY date_left LIMIT 1
SELECT first_name , middle_name , last_name FROM students ORDER BY date_left LIMIT 1
SELECT first_name FROM students WHERE current_address_id != permanent_address_id
SELECT first_name FROM students WHERE current_address_id != permanent_address_id
SELECT t1.address_id , t1.line_1 , t1.line_2 , t1.line_3 , t1.city , t1.zip_postcode , t1.state_province_county , t1.country FROM addresses as t1 JOIN students as t2 ON t1.address_id = t2.current_address_id GROUP BY t1.address_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.address_id , t1.line_1 , t1.line_2 FROM addresses as t1 JOIN students as t2 ON t1.address_id = t2.current_address_id GROUP BY t1.address_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT AVG(transcript_date) FROM transcripts
SELECT AVG(transcript_date) FROM transcripts
SELECT transcript_date , other_details FROM transcripts ORDER BY transcript_date ASC LIMIT 1
SELECT transcript_date , other_details FROM transcripts ORDER BY transcript_date ASC LIMIT 1
SELECT COUNT(*) FROM transcripts
SELECT COUNT(*) FROM transcripts
SELECT transcript_date FROM transcripts ORDER BY transcript_date DESC LIMIT 1
SELECT transcript_date FROM transcripts ORDER BY transcript_date DESC LIMIT 1
SELECT student_course_id , COUNT(*) FROM transcript_contents GROUP BY student_course_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT COUNT(*) , t2.course_id FROM transcript_contents as t1 JOIN student_enrolment_courses as t2 ON t1.student_course_id = t2.student_course_id GROUP BY t2.course_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT transcript_date , transcript_id FROM transcripts GROUP BY transcript_date ORDER BY COUNT(*) LIMIT 1
SELECT t2.transcript_date , t1.transcript_id FROM transcript_contents as t1 JOIN transcripts as t2 ON t1.transcript_id = t2.transcript_id GROUP BY t1.transcript_id ORDER BY COUNT(*) asC LIMIT 1
SELECT t2.semester_name FROM degree_programs as t1 JOIN semesters as t2 ON t1.degree_program_id = t3.degree_program_id WHERE t1.degree_summary_name = "Master" INTERSECT SELECT t2.semester_name FROM degree_programs as t1 JOIN semesters as t2 ON t1.degree_program_id = t3.degree_program_id WHERE t1.degree_summary_name = "Bachelor"
SELECT t2.semester_id FROM degree_programs as t1 JOIN semesters as t2 ON t1.degree_program_id = t3.degree_program_id WHERE t1.degree_summary_name = "Master" INTERSECT SELECT t2.semester_id FROM degree_programs as t1 JOIN semesters as t2 ON t1.degree_program_id = t3.degree_program_id WHERE t1.degree_summary_name = "Bachelor"
SELECT COUNT(DISTINCT current_address_id) FROM students
SELECT DISTINCT t1.line_1 FROM addresses as t1 JOIN students as t2 ON t1.address_id = t2.current_address_id
SELECT * FROM students ORDER BY first_name DESC
SELECT other_student_details FROM students ORDER BY last_name DESC
SELECT section_description FROM sections WHERE section_name = "h"
SELECT section_description FROM sections WHERE section_name = "h"
SELECT t2.first_name FROM addresses as t1 JOIN students as t2 ON t1.address_id = t2.permanent_address_id WHERE t1.country = "Haiti" UNION SELECT t2.first_name FROM students as t2 WHERE t2.cell_mobile_number = "09700166582"
SELECT t2.first_name FROM addresses as t1 JOIN students as t2 ON t1.address_id = t2.permanent_address_id WHERE t1.country = "Haiti" UNION SELECT t2.first_name FROM students as t2 WHERE t2.cell_mobile_number = "09700166582"
SELECT title FROM cartoon ORDER BY title
SELECT title FROM cartoon ORDER BY title
SELECT title FROM cartoon WHERE directed_by = "Ben Jones"
SELECT title FROM cartoon WHERE directed_by = "Ben Jones"
SELECT COUNT(*) FROM cartoon WHERE written_by = "Joseph Kuhr"
SELECT COUNT(*) FROM cartoon WHERE written_by = "Joseph Kuhr"
SELECT title , directed_by FROM cartoon ORDER BY original_air_date
SELECT title , directed_by FROM cartoon ORDER BY original_air_date
SELECT title FROM cartoon WHERE directed_by = "Ben Jones" OR directed_by = "Brandon Vietti"
SELECT title FROM cartoon WHERE directed_by = "Ben Jones" OR directed_by = "Brandon Vietti"
SELECT country , COUNT(*) FROM tv_channel GROUP BY country ORDER BY COUNT(*) DESC LIMIT 1
SELECT country , COUNT(*) FROM tv_channel GROUP BY country ORDER BY COUNT(*) DESC LIMIT 1
SELECT COUNT(DISTINCT series_name) , COUNT(DISTINCT content) FROM tv_channel
SELECT COUNT(DISTINCT series_name) , COUNT(DISTINCT content) FROM tv_channel
SELECT content FROM tv_channel WHERE series_name = "Sky Radio"
SELECT content FROM tv_channel WHERE series_name = "Sky Radio"
SELECT package_option FROM tv_channel WHERE series_name = "Sky Radio"
SELECT package_option FROM tv_channel WHERE series_name = "Sky Radio"
SELECT COUNT(*) FROM tv_channel WHERE language = "English"
SELECT COUNT(*) FROM tv_channel WHERE language = 'english'
SELECT language , COUNT(*) FROM tv_channel GROUP BY language ORDER BY COUNT(*) ASC LIMIT 1
SELECT language , COUNT(*) FROM tv_channel GROUP BY language ORDER BY COUNT(*) ASC LIMIT 1
SELECT language , COUNT(*) FROM tv_channel GROUP BY language
SELECT language , COUNT(*) FROM tv_channel GROUP BY language
SELECT t2.series_name FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t1.title = "The Rise of the Blue Beetle!"
SELECT t2.series_name FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t1.title = "The Rise of the Blue Beetle!"
SELECT t1.title FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t2.series_name = "Sky Radio"
SELECT t1.title FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t2.series_name = "Sky Radio"
SELECT episode FROM tv_series ORDER BY rating
SELECT episode FROM tv_series ORDER BY rating
SELECT episode , rating FROM tv_series ORDER BY rating DESC LIMIT 3
SELECT episode , rating FROM tv_series ORDER BY rating DESC LIMIT 3
SELECT MIN(share) , MAX(share) FROM tv_series
SELECT MAX(share) , MIN(share) FROM tv_series
SELECT air_date FROM tv_series WHERE episode = "A Love of a Lifetime"
SELECT air_date FROM tv_series WHERE episode = "A Love of a Lifetime"
SELECT weekly_rank FROM tv_series WHERE episode = "A Love of a Lifetime"
SELECT weekly_rank FROM tv_series WHERE episode = "A Love of a Lifetime"
SELECT t1.series_name FROM tv_channel as t1 JOIN tv_series as t2 ON t1.id = t2.channel WHERE t2.episode = "A Love of a Lifetime"
SELECT t1.series_name FROM tv_channel as t1 JOIN tv_series as t2 ON t1.id = t2.channel WHERE t2.episode = "A Love of a Lifetime"
SELECT t2.episode FROM tv_channel as t1 JOIN tv_series as t2 ON t1.id = t2.channel WHERE t1.series_name = "Sky Radio"
SELECT t1.episode FROM tv_series as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t2.series_name = "Sky Radio"
SELECT directed_by , COUNT(*) FROM cartoon GROUP BY directed_by
SELECT directed_by , COUNT(*) FROM cartoon GROUP BY directed_by
SELECT production_code , channel FROM cartoon ORDER BY original_air_date DESC LIMIT 1
SELECT production_code , channel FROM cartoon ORDER BY original_air_date DESC LIMIT 1
SELECT package_option , series_name FROM tv_channel WHERE hight_definition_tv = 'yes'
SELECT package_option , series_name FROM tv_channel WHERE hight_definition_tv = 'yes'
SELECT t2.country FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t1.written_by = "Todd Casey"
SELECT t2.country FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t1.written_by = "Todd Casey"
SELECT country FROM tv_channel EXCEPT SELECT t2.country FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t1.written_by = "Todd Casey"
SELECT country FROM tv_channel EXCEPT SELECT t2.country FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t1.written_by = "Todd Casey"
SELECT t2.series_name , t2.country FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t1.directed_by = "Ben Jones" INTERSECT SELECT t2.series_name , t2.country FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t1.directed_by = "Michael Chang"
SELECT t2.series_name , t2.country FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t1.directed_by = "Ben Jones" INTERSECT SELECT t2.series_name , t2.country FROM cartoon as t1 JOIN tv_channel as t2 ON t1.channel = t2.id WHERE t1.directed_by = "Michael Chang"
SELECT pixel_aspect_ratio_par , country FROM tv_channel WHERE language != 'english'
SELECT pixel_aspect_ratio_par , country FROM tv_channel WHERE language != 'english'
SELECT id FROM tv_channel WHERE country IN ( SELECT country FROM tv_channel GROUP BY country HAVING COUNT(*) > 2 )
SELECT id FROM tv_channel GROUP BY series_name HAVING COUNT(*) > 2
SELECT id FROM tv_channel EXCEPT SELECT channel FROM cartoon WHERE directed_by = "Ben Jones"
SELECT id FROM tv_channel EXCEPT SELECT channel FROM cartoon WHERE directed_by = "Ben Jones"
SELECT package_option FROM tv_channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = "Ben Jones")
SELECT package_option FROM tv_channel WHERE id NOT IN (SELECT channel FROM cartoon WHERE directed_by = "Ben Jones")
SELECT COUNT(*) FROM poker_player
SELECT COUNT(*) FROM poker_player
SELECT earnings FROM poker_player ORDER BY earnings DESC
SELECT earnings FROM poker_player ORDER BY earnings DESC
SELECT final_table_made , best_finish FROM poker_player
SELECT final_table_made , best_finish FROM poker_player
SELECT AVG(earnings) FROM poker_player
SELECT AVG(earnings) FROM poker_player
SELECT money_rank FROM poker_player ORDER BY earnings DESC LIMIT 1
SELECT money_rank FROM poker_player ORDER BY earnings DESC LIMIT 1
SELECT MAX(final_table_made) FROM poker_player WHERE earnings < 200000
SELECT MAX(final_table_made) FROM poker_player WHERE earnings < 200000
SELECT t2.name FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id
SELECT t1.name FROM people as t1 JOIN poker_player as t2 ON t1.people_id = t2.people_id
SELECT t2.name FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id WHERE t1.earnings > 300000
SELECT t2.name FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id WHERE t1.earnings > 300000
SELECT t2.name FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id ORDER BY t1.final_table_made asC
SELECT t2.name FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id ORDER BY t1.final_table_made asC
SELECT t2.birth_date FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id ORDER BY t1.earnings LIMIT 1
SELECT t2.birth_date FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id ORDER BY t1.earnings LIMIT 1
SELECT t1.money_rank FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id ORDER BY t2.height DESC LIMIT 1
SELECT t1.money_rank FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id ORDER BY t2.height DESC LIMIT 1
SELECT AVG(t1.earnings) FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id WHERE t2.height > 200
SELECT AVG(t1.earnings) FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id WHERE t2.height > 200
SELECT t2.name FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id ORDER BY t1.earnings DESC
SELECT t2.name FROM poker_player as t1 JOIN people as t2 ON t1.people_id = t2.people_id ORDER BY t1.earnings DESC
SELECT nationality , COUNT(*) FROM people GROUP BY nationality
SELECT nationality , COUNT(*) FROM people GROUP BY nationality
SELECT nationality FROM people GROUP BY nationality ORDER BY COUNT(*) DESC LIMIT 1
SELECT nationality FROM people GROUP BY nationality ORDER BY COUNT(*) DESC LIMIT 1
SELECT nationality FROM people GROUP BY nationality HAVING COUNT(*) >= 2
SELECT nationality FROM people GROUP BY nationality HAVING COUNT(*) >= 2
SELECT name , birth_date FROM people ORDER BY name ASC
SELECT name , birth_date FROM people ORDER BY name
SELECT name FROM people WHERE nationality != "Russia"
SELECT name FROM people WHERE nationality != 'Russia'
SELECT name FROM people WHERE people_id NOT IN (SELECT people_id FROM poker_player)
SELECT name FROM people WHERE people_id NOT IN (SELECT people_id FROM poker_player)
SELECT COUNT(DISTINCT nationality) FROM people
SELECT COUNT(DISTINCT nationality) FROM people
SELECT COUNT(DISTINCT state) FROM area_code_state
SELECT contestant_number , contestant_name FROM contestants ORDER BY contestant_name DESC
SELECT vote_id , phone_number , state FROM votes
SELECT MAX(area_code) , MIN(area_code) FROM area_code_state
SELECT created FROM votes WHERE state = 'CA' ORDER BY created DESC LIMIT 1
SELECT contestant_name FROM contestants WHERE contestant_name != 'Jessie Alloway'
SELECT DISTINCT state , created FROM votes
SELECT t1.contestant_number , t2.contestant_name FROM votes as t1 JOIN contestants as t2 ON t1.contestant_number = t2.contestant_number GROUP BY t1.contestant_number HAVING COUNT(*) >= 2
SELECT t1.contestant_number , t2.contestant_name FROM votes as t1 JOIN contestants as t2 ON t1.contestant_number = t2.contestant_number GROUP BY t1.contestant_number ORDER BY COUNT(*) asC LIMIT 1
SELECT COUNT(*) FROM votes WHERE state = 'NY' OR state = 'CA'
SELECT COUNT(*) FROM contestants WHERE contestant_number NOT IN (SELECT contestant_number FROM votes)
SELECT t1.area_code FROM area_code_state as t1 JOIN votes as t2 ON t1.state = t2.state GROUP BY t1.area_code ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.created , t2.state , t2.phone_number FROM contestants as t1 JOIN votes as t2 ON t1.contestant_number = t2.contestant_number WHERE t1.contestant_name = 'Tabatha Gehling'
SELECT t1.area_code FROM area_code_state as t1 JOIN votes as t2 ON t1.state = t2.state JOIN contestants as t3 ON t2.contestant_number = t3.contestant_number WHERE t3.contestant_name = 'Tabatha Gehling' INTERSECT SELECT t1.area_code FROM area_code_state as t1 JOIN votes as t2 ON t1.state = t2.state JOIN contestants as t3 ON t2.contestant_number = t3.contestant_number WHERE t3.contestant_name = 'Kelly Clauss'
SELECT contestant_name FROM contestants WHERE contestant_name LIKE '%Al%'
SELECT name FROM country WHERE indepyear > 1950
SELECT name FROM country WHERE indepyear > 1950
SELECT COUNT(*) FROM country WHERE governmentform = 'Republic'
SELECT COUNT(*) FROM country WHERE governmentform = 'Republic'
SELECT SUM(surfacearea) FROM country WHERE region = 'Caribbean'
SELECT SUM(surfacearea) FROM country WHERE region = 'Caribbean'
SELECT continent FROM country WHERE name = "Anguilla"
SELECT continent FROM country WHERE name = "Anguilla"
SELECT t2.region FROM city as t1 JOIN country as t2 ON t1.countrycode = t2.code WHERE t1.name = "Kabul"
SELECT t2.region FROM city as t1 JOIN country as t2 ON t1.countrycode = t2.code WHERE t1.name = "Kabul"
SELECT t1.language FROM countrylanguage as t1 JOIN country as t2 ON t1.countrycode = t2.code WHERE t2.name = 'Aruba' ORDER BY t1.percentage DESC LIMIT 1
SELECT t2.language FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.name = "Aruba" ORDER BY t2.percentage DESC LIMIT 1
SELECT population , lifeexpectancy FROM country WHERE name = "Brazil"
SELECT population , lifeexpectancy FROM country WHERE name = "Brazil"
SELECT region , population FROM country WHERE name = 'Angola'
SELECT region , population FROM country WHERE name = 'Angola'
SELECT AVG(lifeexpectancy) FROM country WHERE region = "Central Africa"
SELECT AVG(lifeexpectancy) FROM country WHERE region = "Central Africa"
SELECT name FROM country WHERE continent = 'Asia' ORDER BY lifeexpectancy LIMIT 1
SELECT name FROM country WHERE continent = 'Asia' ORDER BY lifeexpectancy LIMIT 1
SELECT SUM(population) , MAX(gnp) FROM country WHERE continent = 'Asia'
SELECT MAX(gnp) FROM country WHERE continent = 'Asia'
SELECT AVG(lifeexpectancy) FROM country WHERE continent = 'Africa' AND governmentform = 'Republic'
SELECT AVG(lifeexpectancy) FROM country WHERE continent = 'Africa' AND governmentform = 'Republic'
SELECT SUM(surfacearea) FROM country WHERE continent = 'Asia' OR continent = 'Europe'
SELECT SUM(surfacearea) FROM country WHERE continent = 'Asia' OR continent = 'Europe'
SELECT SUM(population) FROM city WHERE district = "Gelderland"
SELECT SUM(population) FROM city WHERE district = "Gelderland"
SELECT AVG(gnp) , SUM(population) FROM country WHERE governmentform = 'US Territory'
SELECT AVG(gnp) , SUM(population) FROM country WHERE continent = 'North America'
SELECT COUNT(DISTINCT language) FROM countrylanguage
SELECT COUNT(DISTINCT language) FROM countrylanguage
SELECT COUNT(DISTINCT governmentform) FROM country WHERE continent = 'Africa'
SELECT COUNT(DISTINCT governmentform) FROM country WHERE continent = 'Africa'
SELECT COUNT(*) FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.name = 'Aruba'
SELECT COUNT(*) FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.name = 'Aruba'
SELECT COUNT(*) FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.name = 'Afghanistan' AND t2.isofficial = 't'
SELECT COUNT(*) FROM countrylanguage as t1 JOIN country as t2 ON t1.countrycode = t2.code WHERE t2.name = 'Afghanistan' AND t1.isofficial = 't'
SELECT t2.name FROM countrylanguage as t1 JOIN country as t2 ON t1.countrycode = t2.code GROUP BY t1.countrycode ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.name FROM countrylanguage as t1 JOIN country as t2 ON t1.countrycode = t2.code GROUP BY t1.countrycode ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.continent FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode GROUP BY t1.continent ORDER BY COUNT(*) DESC LIMIT 1
SELECT continent FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode GROUP BY continent ORDER BY COUNT(*) DESC LIMIT 1
SELECT COUNT(*) FROM countrylanguage WHERE language = 'English' INTERSECT SELECT COUNT(*) FROM countrylanguage WHERE language = 'Dutch'
SELECT COUNT(*) FROM countrylanguage WHERE language = 'English' INTERSECT SELECT COUNT(*) FROM countrylanguage WHERE language = 'Dutch'
SELECT t1.name FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'English' INTERSECT SELECT t1.name FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'French'
SELECT t1.name FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'English' INTERSECT SELECT t1.name FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'French'
SELECT t2.name FROM countrylanguage as t1 JOIN country as t2 ON t1.countrycode = t2.code WHERE t1.language = 'English' INTERSECT SELECT t2.name FROM countrylanguage as t1 JOIN country as t2 ON t1.countrycode = t2.code WHERE t1.language = 'French'
SELECT t2.name FROM countrylanguage as t1 JOIN country as t2 ON t1.countrycode = t2.code WHERE t1.language = 'English' INTERSECT SELECT t2.name FROM countrylanguage as t1 JOIN country as t2 ON t1.countrycode = t2.code WHERE t1.language = 'French'
SELECT COUNT(DISTINCT t1.continent) FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'Chinese'
SELECT COUNT(DISTINCT continent) FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'Chinese'
SELECT t1.region FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'English' OR t2.language = 'Dutch'
SELECT DISTINCT t1.region FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'Dutch' OR t2.language = 'English'
SELECT t1.name FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'English' OR t2.language = 'Dutch' AND t2.isofficial = 't'
SELECT t1.name FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'English' OR t2.language = 'Dutch' AND t2.isofficial = 't'
SELECT t2.language FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.continent = 'Asia' GROUP BY t2.language ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.language FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.continent = 'Asia' GROUP BY t2.language ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.language FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.governmentform = 'Republic' GROUP BY t2.language HAVING COUNT(*) = 1
SELECT t2.language FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.governmentform = 'Republic' GROUP BY t2.language HAVING COUNT(*) = 1
SELECT t1.name FROM city as t1 JOIN countrylanguage as t2 ON t1.countrycode = t2.countrycode WHERE t2.language = 'English' ORDER BY t1.population DESC LIMIT 1
SELECT t1.name FROM city as t1 JOIN countrylanguage as t2 ON t1.countrycode = t2.countrycode WHERE t2.language = 'English' ORDER BY t1.population DESC LIMIT 1
SELECT name , population , lifeexpectancy FROM country WHERE continent = 'Asia' ORDER BY surfacearea DESC LIMIT 1
SELECT name , population , lifeexpectancy FROM country WHERE continent = 'Asia' ORDER BY surfacearea DESC LIMIT 1
SELECT AVG(lifeexpectancy) FROM country WHERE code NOT IN (SELECT countrycode FROM countrylanguage WHERE language = 'English' AND isofficial = 't')
SELECT AVG(lifeexpectancy) FROM country WHERE code NOT IN (SELECT countrycode FROM countrylanguage WHERE language = 'English' AND isofficial = 't')
SELECT SUM(t1.population) FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language != 'English'
SELECT population FROM country WHERE code NOT IN ( SELECT countrycode FROM countrylanguage WHERE language = 'English' )
SELECT t2.language FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.headofstate = "Beatrix" AND t2.isofficial = "t"
SELECT t2.language FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.headofstate = "Beatrix" AND t2.isofficial = "t"
SELECT COUNT(DISTINCT t2.language) FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.indepyear < 1930 AND t2.isofficial = 't'
SELECT COUNT(DISTINCT t2.language) FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t1.indepyear < 1930 AND t2.isofficial = 't'
SELECT name FROM country WHERE surfacearea > (SELECT MAX(surfacearea) FROM country WHERE continent = 'Europe')
SELECT name FROM country WHERE surfacearea > (SELECT MAX(surfacearea) FROM country WHERE continent = 'Europe')
SELECT name FROM country WHERE continent = 'Africa' AND population < (SELECT MAX(population) FROM country WHERE continent = 'Asia')
SELECT name FROM country WHERE population < (SELECT MAX(population) FROM country WHERE continent = 'Asia') AND continent = 'Africa'
SELECT name FROM country WHERE population > (SELECT MAX(population) FROM country WHERE continent = 'Africa') AND continent = 'Asia'
SELECT name FROM country WHERE population > (SELECT MIN(population) FROM country WHERE continent = 'Africa') AND continent = 'Asia'
SELECT countrycode FROM countrylanguage EXCEPT SELECT countrycode FROM countrylanguage WHERE language = 'English'
SELECT countrycode FROM countrylanguage EXCEPT SELECT countrycode FROM countrylanguage WHERE language = 'English'
SELECT countrycode FROM countrylanguage WHERE language != 'English'
SELECT countrycode FROM countrylanguage WHERE language != 'English'
SELECT code FROM country WHERE governmentform != 'Republic' EXCEPT SELECT countrycode FROM countrylanguage WHERE language = 'English'
SELECT code FROM country WHERE governmentform != 'Republic' EXCEPT SELECT countrycode FROM countrylanguage WHERE language = 'English'
SELECT t1.name FROM city as t1 JOIN countrylanguage as t2 ON t1.countrycode = t2.countrycode JOIN country as t3 ON t1.countrycode = t3.code WHERE t2.language = 'English' AND t2.isofficial = 'F' AND t3.continent = 'Europe'
SELECT t2.name FROM countrylanguage as t1 JOIN city as t2 ON t1.countrycode = t2.countrycode JOIN country as t3 ON t3.code = t2.countrycode WHERE t3.continent = 'Europe' AND t1.language = 'English' AND t1.isofficial = 'f'
SELECT DISTINCT t2.name FROM countrylanguage as t1 JOIN city as t2 ON t1.countrycode = t2.countrycode JOIN country as t3 ON t3.code = t2.countrycode WHERE t1.language = 'Chinese' AND t1.isofficial = 't' AND t3.continent = 'Asia'
SELECT DISTINCT t2.name FROM countrylanguage as t1 JOIN city as t2 ON t1.countrycode = t2.countrycode JOIN country as t3 ON t2.countrycode = t3.code WHERE t3.continent = 'Asia' AND t1.language = 'Chinese' AND t1.isofficial = 't'
SELECT name , indepyear , surfacearea FROM country ORDER BY population LIMIT 1
SELECT name , indepyear , surfacearea FROM country ORDER BY population LIMIT 1
SELECT population , name , headofstate FROM country ORDER BY surfacearea DESC LIMIT 1
SELECT name , population , headofstate FROM country ORDER BY surfacearea DESC LIMIT 1
SELECT t2.name , COUNT(*) FROM countrylanguage as t1 JOIN country as t2 ON t1.countrycode = t2.code GROUP BY t1.countrycode HAVING COUNT(*) >= 3
SELECT t2.name , COUNT(*) FROM countrylanguage as t1 JOIN country as t2 ON t1.countrycode = t2.code GROUP BY t1.countrycode HAVING COUNT(*) > 2
SELECT COUNT(*) , district FROM city WHERE population > (SELECT AVG(population) FROM city) GROUP BY district
SELECT COUNT(*) , district FROM city WHERE population > (SELECT AVG(population) FROM city) GROUP BY district
SELECT governmentform , SUM(population) FROM country GROUP BY governmentform HAVING AVG(lifeexpectancy) > 72
SELECT governmentform , SUM(population) FROM country GROUP BY governmentform HAVING AVG(lifeexpectancy) > 72
SELECT AVG(lifeexpectancy) , SUM(population) , continent FROM country GROUP BY continent HAVING AVG(lifeexpectancy) < 72
SELECT continent , SUM(population) , AVG(lifeexpectancy) FROM country GROUP BY continent HAVING AVG(lifeexpectancy) < 72
SELECT name , surfacearea FROM country ORDER BY surfacearea DESC LIMIT 5
SELECT name , surfacearea FROM country ORDER BY surfacearea DESC LIMIT 5
SELECT name FROM country ORDER BY population DESC LIMIT 3
SELECT name FROM country ORDER BY population DESC LIMIT 3
SELECT name FROM country ORDER BY population ASC LIMIT 3
SELECT name FROM country ORDER BY population LIMIT 3
SELECT COUNT(*) FROM country WHERE continent = 'Asia'
SELECT COUNT(*) FROM country WHERE continent = 'Asia'
SELECT name FROM country WHERE population = 80000 AND continent = 'Europe'
SELECT name FROM country WHERE population = 80000 AND continent = 'Europe'
SELECT SUM(population) , AVG(surfacearea) FROM country WHERE continent = 'North America' AND surfacearea > 3000
SELECT SUM(population) , AVG(surfacearea) FROM country WHERE continent = 'North America' AND surfacearea > 3000
SELECT name FROM city WHERE population BETWEEN 160000 AND 900000
SELECT name FROM city WHERE population BETWEEN 160000 AND 900000
SELECT language FROM countrylanguage GROUP BY language ORDER BY COUNT(*) DESC LIMIT 1
SELECT language FROM countrylanguage GROUP BY language ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.name , t2.language FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.percentage = ( SELECT MAX(percentage) FROM countrylanguage )
SELECT countrycode , language FROM countrylanguage WHERE percentage = ( SELECT MAX(percentage) FROM countrylanguage )
SELECT COUNT(*) FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'Spanish' AND t2.percentage = ( SELECT MAX(percentage) FROM countrylanguage WHERE language = 'Spanish' )
SELECT COUNT(*) FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'Spanish' AND t2.percentage > 75
SELECT t1.code FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'Spanish' ORDER BY t2.percentage DESC LIMIT 1
SELECT t1.code FROM country as t1 JOIN countrylanguage as t2 ON t1.code = t2.countrycode WHERE t2.language = 'Spanish' AND t2.percentage > 75
SELECT COUNT(*) FROM conductor
SELECT COUNT(*) FROM conductor
SELECT name FROM conductor ORDER BY age ASC
SELECT name FROM conductor ORDER BY age
SELECT name FROM conductor WHERE nationality != "USA"
SELECT name FROM conductor WHERE nationality != 'USA'
SELECT record_company FROM orchestra ORDER BY year_of_founded DESC
SELECT record_company FROM orchestra ORDER BY year_of_founded DESC
SELECT AVG(attendance) FROM show
SELECT AVG(attendance) FROM show
SELECT MAX(share) , MIN(share) FROM performance WHERE type != "Live final"
SELECT MAX(share) , MIN(share) FROM performance WHERE type != "Live final"
SELECT COUNT(DISTINCT nationality) FROM conductor
SELECT COUNT(DISTINCT nationality) FROM conductor
SELECT name FROM conductor ORDER BY year_of_work DESC
SELECT name FROM conductor ORDER BY year_of_work DESC
SELECT name FROM conductor ORDER BY year_of_work DESC LIMIT 1
SELECT name FROM conductor ORDER BY year_of_work DESC LIMIT 1
SELECT t2.name , t1.orchestra FROM orchestra as t1 JOIN conductor as t2 ON t1.conductor_id = t2.conductor_id
SELECT t1.name , t2.orchestra FROM conductor as t1 JOIN orchestra as t2 ON t1.conductor_id = t2.conductor_id
SELECT t2.name FROM orchestra as t1 JOIN conductor as t2 ON t1.conductor_id = t2.conductor_id GROUP BY t1.conductor_id HAVING COUNT(*) > 1
SELECT t2.name FROM orchestra as t1 JOIN conductor as t2 ON t1.conductor_id = t2.conductor_id GROUP BY t2.name HAVING COUNT(*) > 1
SELECT t2.name FROM orchestra as t1 JOIN conductor as t2 ON t1.conductor_id = t2.conductor_id GROUP BY t1.conductor_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.name FROM orchestra as t1 JOIN conductor as t2 ON t1.conductor_id = t2.conductor_id GROUP BY t1.conductor_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.name FROM orchestra as t1 JOIN conductor as t2 ON t1.conductor_id = t2.conductor_id WHERE t1.year_of_founded > 2008
SELECT t2.name FROM orchestra as t1 JOIN conductor as t2 ON t1.conductor_id = t2.conductor_id WHERE t1.year_of_founded > 2008
SELECT record_company , COUNT(*) FROM orchestra GROUP BY record_company
SELECT record_company , COUNT(*) FROM orchestra GROUP BY record_company
SELECT major_record_format FROM orchestra GROUP BY major_record_format ORDER BY COUNT(*) ASC
SELECT major_record_format FROM orchestra GROUP BY major_record_format ORDER BY COUNT(*)
SELECT record_company FROM orchestra GROUP BY record_company ORDER BY COUNT(*) DESC LIMIT 1
SELECT record_company FROM orchestra GROUP BY record_company ORDER BY COUNT(*) DESC LIMIT 1
SELECT orchestra FROM orchestra WHERE orchestra_id NOT IN (SELECT orchestra_id FROM performance)
SELECT orchestra FROM orchestra WHERE orchestra_id NOT IN (SELECT orchestra_id FROM performance)
SELECT record_company FROM orchestra WHERE year_of_founded < 2003 INTERSECT SELECT record_company FROM orchestra WHERE year_of_founded > 2003
SELECT record_company FROM orchestra WHERE year_of_founded < 2003 INTERSECT SELECT record_company FROM orchestra WHERE year_of_founded > 2003
SELECT COUNT(*) FROM orchestra WHERE major_record_format = "CD" OR major_record_format = "DVD"
SELECT COUNT(*) FROM orchestra WHERE major_record_format LIKE "%CD%" OR major_record_format LIKE "%DVD%"
SELECT t1.year_of_founded FROM orchestra as t1 JOIN performance as t2 ON t1.orchestra_id = t2.orchestra_id GROUP BY t1.orchestra_id HAVING COUNT(*) > 1
SELECT t1.year_of_founding FROM orchestra as t1 JOIN performance as t2 ON t1.orchestra_id = t2.orchestra_id GROUP BY t1.orchestra_id HAVING COUNT(*) > 1
SELECT COUNT(*) FROM highschooler
SELECT COUNT(*) FROM highschooler
SELECT name , grade FROM highschooler
SELECT name , grade FROM highschooler
SELECT DISTINCT grade FROM highschooler
SELECT grade FROM highschooler
SELECT grade FROM highschooler WHERE name = "Kyle"
SELECT grade FROM highschooler WHERE name = 'Kyle'
SELECT name FROM highschooler WHERE grade = 10
SELECT name FROM highschooler WHERE grade = 10
SELECT id FROM highschooler WHERE name = 'Kyle'
SELECT id FROM highschooler WHERE name = "Kyle"
SELECT COUNT(*) FROM highschooler WHERE grade = 9 OR grade = 10
SELECT COUNT(*) FROM highschooler WHERE grade >= 9
SELECT COUNT(*) , grade FROM highschooler GROUP BY grade
SELECT COUNT(*) , grade FROM highschooler GROUP BY grade
SELECT grade FROM highschooler GROUP BY grade ORDER BY COUNT(*) DESC LIMIT 1
SELECT grade FROM highschooler GROUP BY grade ORDER BY COUNT(*) DESC LIMIT 1
SELECT grade FROM highschooler GROUP BY grade HAVING COUNT(*) >= 4
SELECT grade FROM highschooler GROUP BY grade HAVING COUNT(*) >= 4
SELECT student_id , COUNT(*) FROM friend GROUP BY student_id
SELECT COUNT(*) FROM friend GROUP BY student_id
SELECT t2.name , COUNT(*) FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id GROUP BY t1.student_id
SELECT t2.name , COUNT(*) FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id GROUP BY t1.student_id
SELECT t2.name FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id GROUP BY t1.student_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.name FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id GROUP BY t1.student_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.name FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id GROUP BY t1.student_id HAVING COUNT(*) >= 3
SELECT t2.name FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id GROUP BY t1.student_id HAVING COUNT(*) >= 3
SELECT t2.name FROM friend as t1 JOIN highschooler as t2 ON t1.friend_id = t2.id WHERE t1.student_id = (SELECT id FROM highschooler WHERE name = "Kyle")
SELECT t2.name FROM friend as t1 JOIN highschooler as t2 ON t1.friend_id = t2.id WHERE t1.student_id = (SELECT id FROM highschooler WHERE name = "Kyle")
SELECT COUNT(*) FROM friend as t1 JOIN highschooler as t2 ON t1.friend_id = t2.id WHERE t2.name = "Kyle"
SELECT COUNT(*) FROM friend as t1 JOIN highschooler as t2 ON t1.friend_id = t2.id WHERE t2.name = "Kyle"
SELECT id FROM highschooler EXCEPT SELECT student_id FROM friend
SELECT id FROM highschooler EXCEPT SELECT student_id FROM friend
SELECT name FROM highschooler WHERE id NOT IN (SELECT student_id FROM friend)
SELECT name FROM highschooler WHERE id NOT IN (SELECT student_id FROM friend)
SELECT t1.student_id FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id JOIN likes as t3 ON t1.friend_id = t3.liked_id
SELECT student_id FROM friend INTERSECT SELECT student_id FROM likes
SELECT t3.name FROM friend as t1 JOIN likes as t2 ON t1.student_id = t2.liked_id JOIN highschooler as t3 ON t1.student_id = t3.id INTERSECT SELECT t3.name FROM friend as t1 JOIN likes as t2 ON t1.friend_id = t2.liked_id JOIN highschooler as t3 ON t1.friend_id = t3.id
SELECT t3.name FROM friend as t1 JOIN likes as t2 ON t1.student_id = t2.liked_id JOIN highschooler as t3 ON t1.friend_id = t2.student_id
SELECT COUNT(*) , student_id FROM likes GROUP BY student_id
SELECT student_id , COUNT(*) FROM likes GROUP BY student_id
SELECT t2.name , COUNT(*) FROM likes as t1 JOIN highschooler as t2 ON t1.liked_id = t2.id GROUP BY t2.name
SELECT t2.name , COUNT(*) FROM likes as t1 JOIN highschooler as t2 ON t1.liked_id = t2.id GROUP BY t2.name
SELECT t2.name FROM likes as t1 JOIN highschooler as t2 ON t1.liked_id = t2.id GROUP BY t1.liked_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.name FROM likes as t1 JOIN highschooler as t2 ON t1.student_id = t2.id GROUP BY t1.student_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.name FROM likes as t1 JOIN highschooler as t2 ON t1.student_id = t2.id GROUP BY t1.student_id HAVING COUNT(*) >= 2
SELECT t2.name FROM likes as t1 JOIN highschooler as t2 ON t1.liked_id = t2.id GROUP BY t1.liked_id HAVING COUNT(*) >= 2
SELECT t2.name FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id WHERE t2.grade > 5 GROUP BY t1.student_id HAVING COUNT(*) >= 2
SELECT t2.name FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id WHERE t2.grade > 5 GROUP BY t1.student_id HAVING COUNT(*) >= 2
SELECT COUNT(*) FROM likes as t1 JOIN highschooler as t2 ON t1.liked_id = t2.id WHERE t2.name = "Kyle"
SELECT COUNT(*) FROM likes as t1 JOIN highschooler as t2 ON t1.liked_id = t2.id WHERE t2.name = "Kyle"
SELECT AVG(t2.grade) FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id
SELECT AVG(t2.grade) FROM friend as t1 JOIN highschooler as t2 ON t1.student_id = t2.id
SELECT MIN(grade) FROM highschooler WHERE id NOT IN (SELECT student_id FROM friend)
SELECT MIN(grade) FROM highschooler WHERE id NOT IN (SELECT student_id FROM friend)
SELECT state FROM professionals INTERSECT SELECT state FROM owners
SELECT state FROM professionals INTERSECT SELECT state FROM owners
SELECT AVG(t1.age) FROM dogs as t1 JOIN treatments as t2 ON t1.dog_id = t2.dog_id
SELECT AVG(t1.age) FROM dogs as t1 JOIN treatments as t2 ON t1.dog_id = t2.dog_id
SELECT t1.professional_id , t1.last_name , t1.cell_number FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id WHERE t1.state = "Indiana" OR t2.treatment_id > 2
SELECT t1.professional_id , t1.last_name , t1.cell_number FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id WHERE t1.state = "Indiana" OR t2.treatment_id > 2
SELECT t2.name FROM owners as t1 JOIN dogs as t2 ON t1.owner_id = t2.owner_id JOIN treatments as t3 ON t2.dog_id = t3.dog_id WHERE t1.first_name = "Nora" AND t1.last_name = "Haley" GROUP BY t2.name HAVING SUM(t3.cost_of_treatment) <= 1000
SELECT t2.name FROM owners as t1 JOIN dogs as t2 ON t1.owner_id = t2.owner_id JOIN treatments as t3 ON t2.dog_id = t3.dog_id GROUP BY t1.owner_id HAVING SUM(t3.cost_of_treatment) <= 1000
SELECT first_name FROM professionals UNION SELECT first_name FROM owners EXCEPT SELECT name FROM dogs
SELECT first_name FROM professionals UNION SELECT first_name FROM owners EXCEPT SELECT name FROM dogs
SELECT professional_id , role_code , email_address FROM professionals WHERE professional_id NOT IN (SELECT professional_id FROM treatments)
SELECT professional_id , role_code , email_address FROM professionals WHERE professional_id NOT IN (SELECT professional_id FROM treatments)
SELECT t1.owner_id , t2.first_name , t2.last_name FROM dogs as t1 JOIN owners as t2 ON t1.owner_id = t2.owner_id GROUP BY t1.owner_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.owner_id , t2.first_name , t2.last_name FROM dogs as t1 JOIN owners as t2 ON t1.owner_id = t2.owner_id GROUP BY t1.owner_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT t1.professional_id , t1.role_code , t1.first_name FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id GROUP BY t1.professional_id HAVING COUNT(*) >= 2
SELECT t1.professional_id , t1.role_code , t1.first_name FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id GROUP BY t1.professional_id HAVING COUNT(*) >= 2
SELECT t1.breed_name FROM breeds as t1 JOIN dogs as t2 ON t1.breed_code = t2.breed_code GROUP BY t1.breed_name ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.breed_name FROM dogs as t1 JOIN breeds as t2 ON t1.breed_code = t2.breed_code GROUP BY t1.breed_code ORDER BY COUNT(*) DESC LIMIT 1
SELECT t2.owner_id , t3.last_name FROM dogs as t1 JOIN owners as t2 ON t1.owner_id = t2.owner_id JOIN professionals as t4 ON t4.professional_id = t4.professional_id JOIN treatments as t3 ON t3.professional_id = t4.professional_id GROUP BY t2.owner_id ORDER BY SUM(t3.cost_of_treatment) DESC LIMIT 1
SELECT t1.owner_id , t1.last_name FROM owners as t1 JOIN treatments as t2 ON t1.owner_id = t2.owner_id GROUP BY t1.owner_id ORDER BY SUM(t2.cost_of_treatment) DESC LIMIT 1
SELECT t2.treatment_type_description FROM treatments as t1 JOIN treatment_types as t2 ON t1.treatment_type_code = t2.treatment_type_code GROUP BY t1.treatment_type_code ORDER BY SUM(t1.cost_of_treatment) LIMIT 1
SELECT t2.treatment_type_description FROM treatments as t1 JOIN treatment_types as t2 ON t1.treatment_type_code = t2.treatment_type_code GROUP BY t1.treatment_type_code ORDER BY SUM(t1.cost_of_treatment) LIMIT 1
SELECT t1.owner_id , t1.zip_code FROM owners as t1 JOIN treatments as t2 ON t1.owner_id = t2.owner_id JOIN professionals as t3 ON t2.professional_id = t3.professional_id GROUP BY t1.owner_id ORDER BY SUM(t2.cost_of_treatment) DESC LIMIT 1
SELECT t3.owner_id , t3.zip_code FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id JOIN owners as t3 ON t1.professional_id = t3.owner_id GROUP BY t3.owner_id ORDER BY SUM(t2.cost_of_treatment) DESC LIMIT 1
SELECT t1.professional_id , t1.cell_number FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id GROUP BY t1.professional_id HAVING COUNT(*) >= 2
SELECT t1.professional_id , t1.cell_number FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id GROUP BY t1.professional_id HAVING COUNT(*) >= 2
SELECT t1.first_name , t1.last_name FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id WHERE t2.cost_of_treatment < (SELECT AVG(cost_of_treatment) FROM treatments)
SELECT t1.first_name , t1.last_name FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id WHERE t2.cost_of_treatment < (SELECT AVG(cost_of_treatment) FROM treatments)
SELECT t2.date_of_treatment , t1.first_name FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id
SELECT t2.date_of_treatment , t1.first_name FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id
SELECT t1.cost_of_treatment , t2.treatment_type_description FROM treatments as t1 JOIN treatment_types as t2 ON t1.treatment_type_code = t2.treatment_type_code
SELECT t1.cost_of_treatment , t2.treatment_type_description FROM treatments as t1 JOIN treatment_types as t2 ON t1.treatment_type_code = t2.treatment_type_code
SELECT t2.first_name , t2.last_name , t1.size_code FROM dogs as t1 JOIN owners as t2 ON t1.owner_id = t2.owner_id
SELECT t2.first_name , t2.last_name , t3.size_description FROM dogs as t1 JOIN owners as t2 ON t1.owner_id = t2.owner_id JOIN sizes as t3 ON t1.size_code = t3.size_code
SELECT t2.first_name , t1.name FROM dogs as t1 JOIN owners as t2 ON t1.owner_id = t2.owner_id
SELECT t2.first_name , t1.name FROM dogs as t1 JOIN owners as t2 ON t1.owner_id = t2.owner_id
SELECT t1.name , t2.date_of_treatment FROM dogs as t1 JOIN treatments as t2 ON t1.dog_id = t2.dog_id GROUP BY t1.breed_code ORDER BY COUNT(*) asC LIMIT 1
SELECT t1.name , t2.date_of_treatment FROM dogs as t1 JOIN treatments as t2 ON t1.dog_id = t2.dog_id GROUP BY t1.breed_code ORDER BY COUNT(*) asC LIMIT 1
SELECT t1.first_name , t2.name FROM owners as t1 JOIN dogs as t2 ON t1.owner_id = t2.owner_id WHERE t1.state = "Virginia"
SELECT t1.first_name , t2.name FROM owners as t1 JOIN dogs as t2 ON t1.owner_id = t2.owner_id WHERE t1.state = "Virginia"
SELECT t1.date_arrived , t1.date_departed FROM dogs as t1 JOIN treatments as t2 ON t1.dog_id = t2.dog_id
SELECT t1.date_arrived , t1.date_departed FROM dogs as t1 JOIN treatments as t2 ON t1.dog_id = t2.dog_id
SELECT t2.last_name FROM dogs as t1 JOIN owners as t2 ON t1.owner_id = t2.owner_id ORDER BY t1.age LIMIT 1
SELECT t2.last_name FROM dogs as t1 JOIN owners as t2 ON t1.owner_id = t2.owner_id ORDER BY t1.age LIMIT 1
SELECT email_address FROM professionals WHERE state = "Hawaii" OR state = "Wisconsin"
SELECT email_address FROM professionals WHERE state = "Hawaii" OR state = "Wisconsin"
SELECT date_arrived , date_departed FROM dogs
SELECT date_arrived , date_departed FROM dogs
SELECT COUNT(DISTINCT dog_id) FROM treatments
SELECT COUNT(DISTINCT dog_id) FROM treatments
SELECT COUNT(DISTINCT professional_id) FROM treatments
SELECT COUNT(DISTINCT professional_id) FROM treatments
SELECT role_code , street , city , state FROM professionals WHERE city LIKE "%West%"
SELECT role_code , street , city , state FROM professionals WHERE city LIKE '%West%'
SELECT first_name , last_name , email_address FROM owners WHERE state LIKE '%North%'
SELECT first_name , last_name , email_address FROM owners WHERE state LIKE '%North%'
SELECT COUNT(*) FROM dogs WHERE age < (SELECT AVG(age) FROM dogs)
SELECT COUNT(*) FROM dogs WHERE age < (SELECT AVG(age) FROM dogs)
SELECT cost_of_treatment FROM treatments ORDER BY date_of_treatment DESC LIMIT 1
SELECT cost_of_treatment FROM treatments ORDER BY date_of_treatment DESC LIMIT 1
SELECT COUNT(*) FROM dogs WHERE dog_id NOT IN (SELECT dog_id FROM treatments)
SELECT COUNT(*) FROM dogs WHERE dog_id NOT IN (SELECT dog_id FROM treatments)
SELECT COUNT(*) FROM owners WHERE owner_id NOT IN (SELECT owner_id FROM dogs)
SELECT COUNT(*) FROM owners WHERE owner_id NOT IN (SELECT owner_id FROM dogs)
SELECT COUNT(*) FROM professionals WHERE professional_id NOT IN (SELECT professional_id FROM treatments)
SELECT COUNT(*) FROM professionals WHERE professional_id NOT IN (SELECT professional_id FROM treatments)
SELECT name , age , weight FROM dogs WHERE abandoned_yn = 1
SELECT name , age , weight FROM dogs WHERE abandoned_yn = 1
SELECT AVG(age) FROM dogs
SELECT AVG(age) FROM dogs
SELECT age FROM dogs ORDER BY date_of_birth LIMIT 1
SELECT age FROM dogs ORDER BY date_of_birth LIMIT 1
SELECT charge_type , SUM(charge_amount) FROM charges GROUP BY charge_type
SELECT charge_type , SUM(charge_amount) FROM charges GROUP BY charge_type
SELECT charge_amount FROM charges ORDER BY charge_amount DESC LIMIT 1
SELECT charge_amount FROM charges ORDER BY charge_amount DESC LIMIT 1
SELECT email_address , cell_number , home_phone FROM professionals
SELECT email_address , cell_number , home_phone FROM professionals
SELECT DISTINCT breed_code , size_code FROM dogs
SELECT DISTINCT breed_code , size_code FROM dogs
SELECT t1.first_name , t3.treatment_type_description FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id JOIN treatment_types as t3 ON t2.treatment_type_code = t3.treatment_type_code
SELECT t1.first_name , t3.treatment_type_description FROM professionals as t1 JOIN treatments as t2 ON t1.professional_id = t2.professional_id JOIN treatment_types as t3 ON t2.treatment_type_code = t3.treatment_type_code
SELECT COUNT(*) FROM singer
SELECT COUNT(*) FROM singer
SELECT name FROM singer ORDER BY net_worth_millions ASC
SELECT name FROM singer ORDER BY net_worth_millions ASC
SELECT birth_year , citizenship FROM singer
SELECT birth_year , citizenship FROM singer
SELECT name FROM singer WHERE citizenship != "France"
SELECT name FROM singer WHERE citizenship != 'France'
SELECT name FROM singer WHERE birth_year = 1948 OR birth_year = 1949
SELECT name FROM singer WHERE birth_year = 1948 OR birth_year = 1949
SELECT name FROM singer ORDER BY net_worth_millions DESC LIMIT 1
SELECT name FROM singer ORDER BY net_worth_millions DESC LIMIT 1
SELECT citizenship , COUNT(*) FROM singer GROUP BY citizenship
SELECT citizenship , COUNT(*) FROM singer GROUP BY citizenship
SELECT citizenship FROM singer GROUP BY citizenship ORDER BY COUNT(*) DESC LIMIT 1
SELECT citizenship FROM singer GROUP BY citizenship ORDER BY COUNT(*) DESC LIMIT 1
SELECT citizenship , MAX(net_worth_millions) FROM singer GROUP BY citizenship
SELECT MAX(net_worth_millions) , citizenship FROM singer GROUP BY citizenship
SELECT t2.title , t1.name FROM singer as t1 JOIN song as t2 ON t1.singer_id = t2.singer_id
SELECT t2.title , t1.name FROM singer as t1 JOIN song as t2 ON t1.singer_id = t2.singer_id
SELECT DISTINCT t1.name FROM singer as t1 JOIN song as t2 ON t1.singer_id = t2.singer_id WHERE t2.sales > 300000
SELECT DISTINCT t1.name FROM singer as t1 JOIN song as t2 ON t1.singer_id = t2.singer_id WHERE t2.sales > 300000
SELECT t1.name FROM singer as t1 JOIN song as t2 ON t1.singer_id = t2.singer_id GROUP BY t1.singer_id HAVING COUNT(*) > 1
SELECT t1.name FROM singer as t1 JOIN song as t2 ON t1.singer_id = t2.singer_id GROUP BY t1.singer_id HAVING COUNT(*) > 1
SELECT t1.name , SUM(t2.sales) FROM singer as t1 JOIN song as t2 ON t1.singer_id = t2.singer_id GROUP BY t1.singer_id
SELECT t1.name , SUM(t2.sales) FROM singer as t1 JOIN song as t2 ON t1.singer_id = t2.singer_id GROUP BY t1.name
SELECT name FROM singer WHERE singer_id NOT IN (SELECT singer_id FROM song)
SELECT name FROM singer WHERE singer_id NOT IN (SELECT singer_id FROM song)
SELECT citizenship FROM singer WHERE birth_year < 1945 INTERSECT SELECT citizenship FROM singer WHERE birth_year > 1955
SELECT citizenship FROM singer WHERE birth_year < 1945 INTERSECT SELECT citizenship FROM singer WHERE birth_year > 1955
SELECT COUNT(*) FROM other_available_features
SELECT feature_type_code FROM other_available_features WHERE feature_name = "AirCon"
SELECT t1.property_type_description FROM ref_property_types as t1 JOIN properties as t2 ON t1.property_type_code = t2.property_type_code
SELECT property_name FROM properties WHERE property_type_code = "House" OR property_type_code = "Apartment" AND room_count > 1
