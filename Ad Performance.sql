select 
	coalesce(i.product_id, c.product_id) as product_id, 
	coalesce(i.impressions, 0) as impressions, coalesce(i.clicks, 0) as clicks, 
	coalesce(c.click_through_conversions, 0) as click_through_conversions, 
	coalesce(c.view_through_conversions, 0) as view_through_conversions, 
	coalesce(c.click_through_client_revenue, 0) as click_through_client_revenue, 
	coalesce(c.view_through_client_revenue, 0) as view_through_client_revenue
from(
	select 
		product_id, sum(impressions) as impressions,
		sum(clicks) as clicks
	from product_ad_stat
	where campaign_id = $campaign_idand data_date >= $startdate and data_date <= $enddate
	group by product_id) i
	full outer join 
	(
	select product_id,sum(click_through) as click_through_conversions,
		sum(view_through) as view_through_conversions,
		sum(click_through_client_revenue) as click_through_client_revenue,
		sum(view_through_client_revenue) as view_through_client_revenue
	from product_sales_stat
	where campaign_id = $campaign_id and data_date >= $startdate and data_date <= $enddate
	group by product_id) c 
	on (i.product_id = c.product_id)
)