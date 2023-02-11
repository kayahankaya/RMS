import DAL.Sql.Db.DbManager as DbManager
from DAL.Sql.Db.Entities.OrderEntity import OrderEntity

class OrderRepository:

    def __init__(self):

        self.dbcontext = DbManager.getdbbcon()

    def get_order_by_order_id(self,order_id):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM orders 
        WHERE order_id=%s""",(order_id))
        row = cur.fetchone()

        temp_order = OrderEntity()

        temp_order.user_id = row[0]
        temp_order.product_id = row[1]
        temp_order.bill_id = row[2]
        temp_order.created_at = row[3]
        temp_order.updated_at = row[4]
   
        return temp_order

    def get_order_by_product_id(self,product_id):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM orders 
        WHERE product_id=%s""",(product_id))
        row = cur.fetchone()

        temp_order = OrderEntity()
        
        temp_order.user_id = row[0]
        temp_order.product_id = row[1]
        temp_order.bill_id = row[2]
        temp_order.created_at = row[3]
        temp_order.updated_at = row[4]

        return temp_order
    
    def get_order_by_bill_id(self,bill_id):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM orders 
        WHERE bill_id=%s""",(bill_id))
        row = cur.fetchone()

        temp_order = OrderEntity()

        temp_order.user_id = row[0]
        temp_order.product_id = row[1]
        temp_order.bill_id = row[2]
        temp_order.created_at = row[3]
        temp_order.updated_at = row[4]

        return temp_order

    def get_order_by_user_id(self,user_id):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM orders 
        WHERE user_id=%s""",(user_id))
        row = cur.fetchone()

        temp_order = OrderEntity()

        temp_order.user_id = row[0]
        temp_order.product_id = row[1]
        temp_order.bill_id = row[2]
        temp_order.created_at = row[3]
        temp_order.updated_at = row[4]

        return temp_order

    def table_count(self):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT table_count 
        FROM others 
        WHERE others.other_id = 1""")
        table_number = cur.fetchone()[0]

        return table_number

    def get_orders_of_current_table(self,selectedtable):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT order_id, product_id ,created_at 
        FROM orders 
        WHERE orders.bill_id = (SELECT bill_id 
        FROM bills 
        WHERE table_name = %s AND bill_status = 'Open' AND orders.order_status = 'Unpaid' )""", (selectedtable))
        order_products = cur.fetchall()

        return order_products

    def delete_order_by_order_id(self,temp_item):

        cur = self.dbcontext.cursor()
        cur.execute("""
        DELETE 
        FROM orders 
        WHERE order_id = %s""", (temp_item))
        self.dbcontext.commit()

    def insert_order_by_product_id_and_bill_id(self,bill_id_toadd, selected_product_id):
        cur = self.dbcontext.cursor()
        cur.execute("""
        INSERT INTO orders (bill_id, product_id) 
        VALUES(%s, %s)""", (bill_id_toadd, selected_product_id))
        self.dbcontext.commit()

    def update_orderstatus_paid_by_orderid(self,order_id):
        cur = self.dbcontext.cursor()   
        cur.execute("""
        UPDATE orders 
        SET orders.order_status = 'Paid' 
        WHERE order_id = %s""", (order_id))
        self.dbcontext.commit()

    def change_bill_by_order_id(self,bill_id,order_id):
        cur = self.dbcontext.cursor()   
        cur.execute("""
        UPDATE orders 
        SET orders.bill_id = %s 
        WHERE orders.order_id = %s;""", (bill_id,order_id))
        self.dbcontext.commit()
    
    



        






            

        


