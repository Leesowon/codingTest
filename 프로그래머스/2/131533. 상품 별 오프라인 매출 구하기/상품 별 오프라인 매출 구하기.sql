
SELECT p.PRODUCT_CODE, sum(p.PRICE * o.SALES_AMOUNT) as SALES
from PRODUCT as p join OFFLINE_SALE as o
on p.PRODUCT_ID = o.PRODUCT_ID
group by p.PRODUCT_CODE
order by SALES desc, p.PRODUCT_CODE asc

# select p.PRODUCT_ID, p.price, o.sales_amount, o.OFFLINE_SALE_ID
# from PRODUCT as p inner join OFFLINE_SALE as o
# on p.PRODUCT_ID = o.PRODUCT_ID
# order by PRODUCT_ID