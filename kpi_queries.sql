-- Supplier delivery performance
SELECT supplier_id, COUNT(*) AS purchase_orders, ROUND(100.0*AVG(on_time),2) AS on_time_delivery_pct, ROUND(AVG(delivery_days),2) AS avg_delivery_days, SUM(damaged_qty) AS damaged_units FROM purchase_orders GROUP BY supplier_id ORDER BY on_time_delivery_pct ASC;
-- Material damage rates
SELECT material_id, SUM(ordered_qty) AS ordered_units, SUM(damaged_qty) AS damaged_units, ROUND(100.0*SUM(damaged_qty)/NULLIF(SUM(ordered_qty),0),2) AS damage_pct FROM purchase_orders GROUP BY material_id ORDER BY damage_pct DESC;
-- Late or damaged orders requiring review
SELECT po_id, supplier_id, material_id, order_date, received_date, promised_days, delivery_days, damaged_qty, order_value FROM purchase_orders WHERE on_time=0 OR damaged_qty>0 ORDER BY delivery_days DESC;
