-- 코드를 작성해주세요
select c.id as ID, c.GENOTYPE as GENOTYPE, p.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA as p right join ECOLI_DATA as c
on p.id = c.PARENT_ID
where (c.GENOTYPE & p.GENOTYPE) = p.GENOTYPE
order by c.id