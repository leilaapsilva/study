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

