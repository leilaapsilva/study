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
