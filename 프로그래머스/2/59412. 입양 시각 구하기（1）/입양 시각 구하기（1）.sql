SELECT HOUR(DATETIME) AS hour, count(*) as count 
from animal_outs
group by hour
having hour > 8 and hour < 20
order by hour;