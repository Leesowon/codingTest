-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.NAME
# select *
from ANIMAL_INS as i right join ANIMAL_OUTS as o
on o.ANIMAL_ID = i.ANIMAL_ID
where i.INTAKE_CONDITION is null
# where o.ANIMAL_ID is null
# order by o.ANIMAL_ID, o.NAME