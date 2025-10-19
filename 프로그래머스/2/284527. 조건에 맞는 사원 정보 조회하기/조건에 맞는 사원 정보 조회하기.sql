-- 코드를
select sum(g.score) as SCORE, g.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from HR_EMPLOYEES as e inner join HR_GRADE as g
on e.emp_no = g.emp_no
group by g.emp_no, g.year
having g.year = '2022'
order by 1 desc # score => 1
limit 1