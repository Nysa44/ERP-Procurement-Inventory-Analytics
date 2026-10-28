# SAP S/4HANA-Inspired Procurement & Inventory Analytics
A portfolio simulation for a graduate SAP/business-process consulting application using synthetic procurement and inventory data, SQL, Python, and Excel.

**Scope honesty:** This is an independent ERP-inspired simulation, not a real SAP S/4HANA implementation and not connected to SAP software. All data is synthetic.

## Scenario
A fictional distributor wants to monitor purchase-order delivery, damaged goods, supplier performance, and inventory-count differences.

## Contents
- `data/purchase_orders.csv`: 180 synthetic purchase orders
- `data/suppliers.csv`, `data/materials.csv`: reference data
- `data/inventory_snapshot.csv`: system stock vs physical count
- `sql/schema.sql`: relational schema
- `sql/kpi_queries.sql`: supplier, damage, and exception queries
- `src/analyze_procurement.py`: KPI calculations, data-quality checks, exception reports
- `excel/Procurement_Inventory_KPI_Dashboard.xlsx`: workbook with data and KPI formulas
- `reports/`: generated CSV reports

## Run
Requires Python 3.10+:
```bash
pip install pandas
python src/analyze_procurement.py
```


## Resume entry (after running and understanding it)
**ERP Procurement & Inventory Analytics Simulation | SQL, Python, Excel, Power BI**
- Analysed 180 synthetic purchase orders to monitor supplier delivery, damaged units, order value, and inventory accuracy.
- Built SQL queries and Python checks to identify late deliveries, damaged goods, inventory variances, and data-quality issues.
- Prepared KPI summaries and exception reports to support operational review and process-improvement discussions.
