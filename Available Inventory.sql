-- this is for avails: 
select
m.campaign_id,
m.data_date,
sum(m.conversions)
from alien_modeling_mv_v3 m 
where m.data_date >= 20150201 and m.campaign_id in (48257) and m.conversions > 0
group by
m.campaign_id,
m.data_date
 
 
-- and this is for total conversions: 
 
select
m.conversion_action_id,
m.data_date,
sum(1)
from actions m 
where m.data_date >= 20150201 and m.conversion_action_id in (20617073, 20585997, 20629441, 20575861, 20565409, 20574257, 20531037)
group by
m.conversion_action_id,
m.data_date
in
 
--the latter, you need to find conversion action ids for campaigns queried in the first query