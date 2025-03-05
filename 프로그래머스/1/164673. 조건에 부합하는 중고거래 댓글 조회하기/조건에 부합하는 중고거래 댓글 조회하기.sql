-- 코드를 입력하세요
SELECT  b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, 
date_format(r.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD as b inner join USED_GOODS_REPLY as r
on b.BOARD_ID = r.BOARD_ID
where b.CREATED_DATE between '2022-10-01' and '2022-10-31'
order by r.CREATED_DATE, b.TITLE;