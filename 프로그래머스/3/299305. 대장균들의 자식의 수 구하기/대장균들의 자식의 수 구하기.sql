-- 코드를 작성해주세요
select p.id as ID, count(c.id) as CHILD_COUNT
from ECOLI_DATA as p left join ECOLI_DATA as c
on p.id = c.parent_id
group by p.id
order by p.id