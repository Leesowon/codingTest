-- 코드를 작성해주세요
select count(*) as FISH_COUNT, FISH_NAME
from FISH_INFO as i left join FISH_NAME_INFO as n
on i.FISH_TYPE = n.FISH_TYPE
group by i.fish_type, n.fish_name
order by 1 desc;