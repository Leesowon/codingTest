-- 코드를 작성해주세요
select sum(score) as score, e.emp_no, e.emp_name, e.position, e.email
from HR_EMPLOYEES as e
inner join HR_GRADE as g on e.emp_no = g.emp_no
# left join HR_DEPARTMENT as d on e.dept_id = d.dept_id
group by year, g.emp_no
having g.YEAR = '2022'
order by 1 desc
limit 1;