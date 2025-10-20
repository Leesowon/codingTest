select p.id as ID, count(c.id) as CHILD_COUNT
from ECOLI_DATA as p left join ECOLI_DATA as c
on p.id = c.PARENT_ID
group by p.id
order by p.id