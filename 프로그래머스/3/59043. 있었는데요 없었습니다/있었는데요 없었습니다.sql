# 보호 시작일 보다 입양일이 더 빠른 동물의 아이디와 이름 조회

-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.NAME
from ANIMAL_INS as i join ANIMAL_OUTS as o
on i.ANIMAL_ID = o.ANIMAL_ID
where i.DATETIME > o.DATETIME
order by i.DATETIME