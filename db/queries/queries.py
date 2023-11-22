def select_all(table_name: str):
    return f"SELECT * FROM {table_name};"


def select_all_sales():
    return """
select t.region,
       t.country,
       s.order_date,
       p.model_name,
       p.product_price,
       s.order_quantity,
       p.product_price * s.order_quantity as total_price
from advworksterritories t
left join advworkssales s on t.territory_key = s.territory_key
join advworksproducts p on p.product_key = s.product_key
"""


def select_aggr_sales_data():
    return """
select s.order_date,
       t.country,
       t.region,
       sum(p.product_price * s.order_quantity) as days_receipts,
       t.latitude,
       t.longitude
from advworksterritories t
left join advworkssales s on t.territory_key = s.territory_key
join advworksproducts p on p.product_key = s.product_key
group by t.region, t.country, s.order_date, t.latitude, t.longitude
order by s.order_date
"""


def select_geo_coordinates():
    return """
    select latitude, longitude from advworksterritories
    """


def select_min_max_date():
    return """select min(order_date) as min_date, max(order_date) as  max_date from advworkssales"""

def select_aggr_sales_data_for_period(aggr_sales_data_query: str, date_from: str, date_to: str):
    return f"select * from ({aggr_sales_data_query}) where order_date > '{date_from}' and order_date < '{date_to}'"


def select_count_for(sub_query: str):
    return f'select count(*) from ( {sub_query} )'


def select_page_for(sub_query: str, page_number: int = 0, page_size: int = 10):
    return f'{sub_query} limit {page_size} offset {page_number * page_size}'


def select_min_and_max_sales_date():
    return f'select min(order_date) as min_sales_date, max(order_date) as min_sales_date from advworkssales'
