
  create view "sales_db"."data"."fct_daily_revenue__dbt_tmp"
    
    
  as (
    -- models/marts/fct_daily_revenue.sql

with sales as (

    select
        invoice_date,
        quantity,
        unit_price
    from "sales_db"."data"."stg_sales"

),

revenue_per_day as (

    select
        date(invoice_date) as date,
        sum(quantity * unit_price) as daily_revenue
    from sales
    group by date(invoice_date)
    order by date
)

select * from revenue_per_day
  );