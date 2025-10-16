-- 코드를 작성해주세요
select ID, ifnull(LENGTH, 0) as LENGTH
from FISH_INFO
order by LENGTH desc, ID
limit 10;