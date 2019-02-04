

import pandas as pd
import pandasql as pdsql

orders = pd.read_csv('C:/Users/User/Desktop/data/retail_db/orders/part-00000',
            names=['order_id', 'order_date', 'order_custid', 'order_status'],
            index_col = 'order_id')

#print(orders)
# new_orders = orders.groupby(['order_status'])['order_status'].count()
# print(new_orders)
# orders1 = orders.groupby(['order_status'])
# print(orders1)

orders.groupby(['order_status'])['order_status'].count()

order_items = pd.read_csv('C:/Users/User/Desktop/data/retail_db/order_items/part-00000',
                          names=['order_item_id', 'order_item_order_id', 'order_item_product_id',
                                 'order_item_quantity', 'order_item_subtotal', 'order_item_product_price'],
                          index_col='order_item_order_id')
#print(order_items)

ordersCompleted = orders.loc[(orders['order_status'] == 'COMPLETE') | (orders['order_status'] == 'CLOSED')]

final_value = ordersCompleted.join(order_items).groupby(['order_date'])['order_item_subtotal'].sum()

print(final_value)


revenue_per_day_sql = """select o.order_date, sum(oi.order_item_subtotal) daily_revenue 
from orders o join order_items oi on o.order_id = oi.order_item_order_id
where o.order_status in ('COMPLETE', 'CLOSED')
group by o.order_date
order by o.order_date"""

revenue_per_day = pdsql(revenue_per_day_sql)
