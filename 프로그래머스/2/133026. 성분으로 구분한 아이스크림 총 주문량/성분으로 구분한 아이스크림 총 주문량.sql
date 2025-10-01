select i.INGREDIENT_TYPE, sum(TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF as f inner join ICECREAM_INFO as i
on f.flavor = i.flavor
group by i.INGREDIENT_TYPE
order by f.TOTAL_ORDER;