-- 코드를 작성해주세요
select sum(g.score) as SCORE, e.emp_no, e.emp_name, e.position, e.email
from HR_EMPLOYEES as e join HR_GRADE as g
on e.emp_no = g.emp_no
group by g.emp_no, g.year
having g.YEAR = '2022'
order by SCORE desc
limit 1

# select e.emp_no, e.emp_name, e.position, e.email, sum(g.score), g.year
# from HR_EMPLOYEES as e join HR_GRADE as g
# on e.emp_no = g.emp_no
# group by e.emp_no, g.year