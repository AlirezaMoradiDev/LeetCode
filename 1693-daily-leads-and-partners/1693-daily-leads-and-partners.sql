# Write your MySQL query statement below
Select date_id, make_name ,count(DISTINCT lead_id) AS unique_leads, count(DISTINCT partner_id) AS unique_partners from DailySales
group by date_id, make_name