-- models/staging/stg_sales.sql

with source as (

    select * from "sales_db"."data"."raw_sales"

),

renamed as (

    select
        cast("InvoiceNo" as text) as invoice_no,
        cast("StockCode" as text) as stock_code,
        initcap("Description") as description,
        cast("Quantity" as integer) as quantity,
        cast("InvoiceDate" as timestamp) as invoice_date,
        cast("UnitPrice" as numeric) as unit_price,
        cast("CustomerID" as text) as customer_id,
        initcap("Country") as country

    from source
    where "CustomerID" is not null
      and "UnitPrice" is not null

)

select * from renamed