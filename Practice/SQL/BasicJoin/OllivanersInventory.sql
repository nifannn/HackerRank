select id, age, min_coins.coins, min_coins.power from
(select code, power, min(coins_needed) as coins
from wands group by code, power) as min_coins
inner join wands_property as property
on min_coins.code=property.code
inner join wands on min_coins.code=wands.code and min_coins.power=wands.power and min_coins.coins=wands.coins_needed
where is_evil=0
order by min_coins.power desc, age desc;
