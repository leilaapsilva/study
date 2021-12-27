[Revising the select query](https://www.hackerrank.com/challenges/revising-the-select-query/problem)

~~~sql
select * from city where population > 100000 and countrycode = 'USA';
~~~

[Revising the select query II](https://www.hackerrank.com/challenges/revising-the-select-query-2/problem)

~~~sql
select name from city where population > 120000 and countrycode = 'USA';
~~~

[Weather Observation Station 4](https://www.hackerrank.com/challenges/weather-observation-station-4/problem?h_r=next-challenge&h_v=zen)

~~~sql
SELECT count(city) - count(distinct city) 
FROM station;
~~~

[Weather Observation Station 6](https://www.hackerrank.com/challenges/weather-observation-station-6/problem)

~~~sql
SELECT city 
FROM station 
WHERE city LIKE 'a%' 
or city like 'e%'
or city like 'i%'
or city like 'o%'
or city like 'u%';
~~~

[Weather Observation Station 8](https://www.hackerrank.com/challenges/weather-observation-station-8/problem?h_r=next-challenge&h_v=zen)

~~~sql
SELECT DISTINCT city
FROM   station
WHERE  city RLIKE '^[aeiouAEIOU].*[aeiouAEIOU]$';
~~~

[Average Population of Each Continent](https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true)

~~~sql
select co.continent, floor(avg(ci.population))
from city ci inner join country co on ci.countrycode = co.code
group by 1;
~~~

[More than 75 marks](https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true)

~~~sql
SELECT name
FROM students
WHERE marks > 75
ORDER BY right(name, 3), id ASC;
~~~

[Employee Names](https://www.hackerrank.com/challenges/name-of-employees/problem?isFullScreen=true)

~~~sql
select name from employee order by name;
~~~

[Employee Salary](https://www.hackerrank.com/challenges/salary-of-employees/problem?isFullScreen=true&h_r=next-challenge&h_v=zen)

~~~sql
SELECT name FROM employee 
WHERE salary > 2000 and months < 10
ORDER BY employee_id ASC;
~~~

WRONG
[Challenges](https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen)

~~~sql
SELECT h.hacker_id, h.name, count(c.challenge_id) as number_challenges
FROM hackers h; 
--INNER JOIN challenges c
--ON h.hacker_id = c.hacker_id
--ORDER BY count(c.challenge_id), hacker_id;
~~~

[African Cities](https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true)

~~~sql
SELECT ci.name FROM city ci
INNER JOIN country co
ON ci.countrycode = co.code
WHERE co.continent = 'Africa';
~~~

[Ollivander's Inventory](https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true)

~~~sql
SELECT w.id, wp.age, w.coins_needed, w.power 
FROM wands w
INNER JOIN wands_property wp
ON w.code = wp.code
WHERE wp.is_evil = 0
AND w.coins_needed = (
    SELECT MIN(coins_needed) 
    FROM wands w1 INNER JOIN wands_property p1 
    ON w1.code = p1.code 
    WHERE w1.power = w.power AND p1.age = wp.age)
ORDER BY w.power DESC, wp.age DESC;
~~~

WRONG
[Placements](https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true)

~~~ sql
SELECT s.name, p.salary
FROM students s
INNER JOIN packages p ON (s.id = p.id)
WHERE p.salary > (SELECT p1.salary 
                  FROM friends f 
                  INNER JOIN packages p1 ON (f.friend_id = p1.id)
                  WHERE f.id = s.id); 
~~~

[Weather Observation Station 9](https://www.hackerrank.com/challenges/weather-observation-station-9) 

~~~sql
SELECT city FROM station 
WHERE city not like "a%"
AND city not like "e%"
AND city not like "i%"
AND city not like "o%"
AND city not like "u%"
GROUP BY city
ORDER BY city;
~~~

[Weather Observation Station 10](https://www.hackerrank.com/challenges/weather-observation-station-10) 

~~~sql
SELECT city FROM station 
WHERE city not like "%a"
AND city not like "%e"
AND city not like "%i"
AND city not like "%o"
AND city not like "%u"
GROUP BY city
ORDER BY city;
~~~

[Revising Aggregations](https://www.hackerrank.com/challenges/revising-aggregations-the-count-function)

~~~sql
SELECT count(id)
FROM city
WHERE population > 100000;
~~~

[Revising Aggregations - Sum](https://www.hackerrank.com/challenges/revising-aggregations-sum)

~~~sql
SELECT sum(population)
FROM CITY
WHERE district = 'California';
~~~

[Average Population](https://www.hackerrank.com/challenges/average-population)

~~~sql
SELECT round(avg(population))
FROM city;
~~~

[Japan Population](https://www.hackerrank.com/challenges/japan-population)

~~~sql
SELECT sum(population)
FROM city
WHERE countrycode = 'JPN';
~~~

[Population Density](https://www.hackerrank.com/challenges/population-density-difference)

~~~sql
SELECT max(population)-min(population)
FROM city;
~~~

[The Blunder](https://www.hackerrank.com/challenges/the-blunder)

~~~sql
SELECT ceil(avg(salary) - avg(replace(salary, '0', '')))
FROM employees;
~~~


[Top Earners](https://www.hackerrank.com/challenges/earnings-of-employees)

~~~sql
SELECT salary * months as earnings, count(*)
FROM employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;
~~~

[Weather Observation Station 2](https://www.hackerrank.com/challenges/weather-observation-station-2/)

~~~sql
SELECT round(sum(LAT_N), 2), round(sum(LONG_W), 2)
FROM station;
~~~

[Weather Observation Station 13](https://www.hackerrank.com/challenges/weather-observation-station-13)

~~~sql
SELECT round(sum(LAT_N), 4)
FROM station
WHERE (LAT_N > 38.7880) AND (LAT_N < 137.2345);
~~~

[Weather Observation Station 14](https://www.hackerrank.com/challenges/weather-observation-station-14)

~~~sql
SELECT round(max(LAT_N), 4)
FROM station
WHERE LAT_N < 137.2345;
~~~

[Population Census](https://www.hackerrank.com/challenges/asian-population)

~~~sql
SELECT sum(city.population)
FROM city
INNER JOIN country
ON city.countrycode = country.code
WHERE country.continent = 'Asia';
~~~

[Type of triangle](https://www.hackerrank.com/challenges/what-type-of-triangle)

~~~sql
SELECT CASE 
    WHEN (a+b > c) AND (a+c > b) AND (b+c > a) THEN
    CASE
        WHEN a = b AND b = c THEN 'Equilateral'
        WHEN a = b  OR a = c OR b = c THEN 'Isosceles'
        ELSE 'Scalene'
    END
    ELSE 'Not A Triangle'
END
FROM triangles;
~~~

[Revising Aggregations - Averages](https://www.hackerrank.com/challenges/revising-aggregations-the-average-function)

~~~sql
SELECT avg(population)
FROM city
WHERE district = 'California';
~~~

[Weather Observation Station 15](https://www.hackerrank.com/challenges/weather-observation-station-15)

~~~sql
SELECT round(long_w, 4)
FROM station
WHERE lat_n < 137.2345
ORDER BY lat_n DESC
LIMIT 1;
~~~

[Weather Observation Station 16](https://www.hackerrank.com/challenges/weather-observation-station-16)

~~~sql
SELECT round(lat_n, 4)
FROM station
WHERE lat_n > 38.7780
ORDER BY lat_n
LIMIT 1;
~~~

[Weather Observation Station 17](https://www.hackerrank.com/challenges/weather-observation-station-17)

~~~sql
SELECT round(long_w, 4)
FROM station
WHERE lat_n > 38.7780
ORDER BY lat_n
LIMIT 1;
~~~

[Weather Observation Station 11](https://www.hackerrank.com/challenges/weather-observation-station-11)

~~~sql
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[^aeiou]|[^aeiou]$';
~~~

[Weather Observation Station 18](https://www.hackerrank.com/challenges/weather-observation-station-18/)

~~~sql

ERRADO

SELECT ROUND(
                 min(LAT_N) -
                 max(LAT_N)
             + 
                min(LONG_W) -
                max(LONG_W)
        , 4)
FROM station 

--|x1 - x2| + |y1 - y2|
-- x1 = min LAT_N
-- x2 = min LONG_W
-- y1 = nax LAT_N 
-- y2 = max LONG_w
~~~

[]()

~~~sql

~~~

[]()

~~~sql

~~~

[]()

~~~sql

~~~

[]()

~~~sql

~~~