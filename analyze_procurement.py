from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
orders=pd.read_csv(ROOT/'data/purchase_orders.csv')
inventory=pd.read_csv(ROOT/'data/inventory_snapshot.csv')
required=['po_id','supplier_id','material_id','ordered_qty','received_qty','damaged_qty']
checks={'Missing required cells':int(orders[required].isna().sum().sum()),'Duplicate PO IDs':int(orders.po_id.duplicated().sum()),'Invalid quantity records':int(((orders.received_qty+orders.damaged_qty)>orders.ordered_qty).sum())}
kpis=pd.DataFrame([['Purchase orders',len(orders)],['Total order value',round(orders.order_value.sum(),2)],['On-time delivery (%)',round(orders.on_time.mean()*100,2)],['Damage rate (%)',round(orders.damaged_qty.sum()/orders.ordered_qty.sum()*100,2)],['Average delivery days',round(orders.delivery_days.mean(),2)],['Average inventory accuracy (%)',round(inventory.inventory_accuracy_pct.mean(),2)],*list(checks.items())],columns=['KPI','Value'])
supplier=orders.groupby('supplier_id').agg(purchase_orders=('po_id','count'),on_time_delivery_pct=('on_time',lambda s:round(s.mean()*100,2)),avg_delivery_days=('delivery_days','mean'),damaged_units=('damaged_qty','sum'),order_value=('order_value','sum')).reset_index().sort_values('on_time_delivery_pct')
exceptions=orders[(orders.on_time==0)|(orders.damaged_qty>0)].copy()
exceptions['exception_reason']=exceptions.apply(lambda r:'Late delivery + damage' if r.on_time==0 and r.damaged_qty>0 else ('Late delivery' if r.on_time==0 else 'Damaged units'),axis=1)
out=ROOT/'reports'; out.mkdir(exist_ok=True)
kpis.to_csv(out/'kpi_summary.csv',index=False); supplier.to_csv(out/'supplier_performance.csv',index=False); exceptions.to_csv(out/'purchase_order_exceptions.csv',index=False)
print(kpis.to_string(index=False)); print('Reports saved to',out)
