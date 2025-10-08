-- 코드를 작성해주세요
select ITEM_ID, ITEM_NAME, RARITY
from ITEM_INFO
where ITEM_ID in (select t.item_id
                  from item_info as i, item_tree as t
                  where i.item_id = t.PARENT_ITEM_ID and i.RARITY = 'RARE')
order by ITEM_ID desc

