-- 코드를 입력하세요
SELECT MCDP_CD as '진료과 코드', count(*) as '5월예약건수'
from APPOINTMENT
where APNT_YMD between '2022-05-01' and '2022-05-31'
group by MCDP_CD
order by 2, 1;


## 2022-5에 예약한 환자 수
# 진료과 코드별로 조회
# 진료과별 예약한 환자 수 기준으로 오름차순 - 진료과 코드 기준 오름차순
