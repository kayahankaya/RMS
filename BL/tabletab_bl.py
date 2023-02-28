from DAL.Sql.Repository.OrderRepository import OrderRepository
from DAL.Sql.Repository.ProductRepository import ProductRepository
from DAL.Sql.Repository.BillRepository import BillRepository
from DAL.Sql.Repository.RecipeRepository import RecipeRepository
from DAL.Sql.Repository.StockRepository import StockRepository
from decimal import Decimal

class Order:

    def table_status_func(self,input):

        table_status =  BillRepository().get_bill_id_by_table_name(input)

        return table_status

    def get_paid(self,selectedtable):

        mustpay_current = BillRepository().get_mustpay_by_table_name(selectedtable)
        temp_bill = BillRepository().get_paids_by_table_name(selectedtable)
        BillRepository().update_remain_check_by_tablename(selectedtable)
        remaining_check = BillRepository().select_remain_check_by_tablename(selectedtable)
        return (mustpay_current,temp_bill,remaining_check)      

    def delete_order_func(self,temp_item):

            temp_product_id = OrderRepository().get_order_by_order_id(temp_item)
            ingredients_list = RecipeRepository().get_recipe_by_product_id(temp_product_id.product_id)
            temp_item_ = ProductRepository().get_product_by_product_id(temp_product_id.product_id)
            
            for ingredient in ingredients_list :
                stock_id_ingre = ingredient[1]
                stock_weight_ingre = int(ingredient[3])
                StockRepository().update_stock_by_stock_id_and_stock_weight(stock_weight_ingre,stock_id_ingre)
            OrderRepository().delete_order_by_order_id(temp_item)
            BillRepository().decrease_mustpay_by_order_id(temp_item_.product_price,temp_product_id.bill_id )

    def add_order_func(self,howmany,selectedtable,temp_value_tree):
        
        for _ in range(howmany):

            bill_id_toadd = BillRepository().get_bill_id_by_table_name(selectedtable)

            if not bill_id_toadd:

                BillRepository().insert_table_name_to_bill(selectedtable)
                bill_id_toadd = BillRepository().get_bill_id_by_table_name(selectedtable)

            selected_product_id = ProductRepository().get_product_by_product_name(temp_value_tree)
            selected = selected_product_id.product_id
            ingredients_list = RecipeRepository().get_recipe_by_product_id(selected)
            for ingredient in ingredients_list :
                stock_id_ingre = ingredient[1]
                stock_weight_ingre = int(ingredient[3])
                StockRepository().drop_stock_by_stock_id(stock_id_ingre,stock_weight_ingre)
            OrderRepository().insert_order_by_product_id_and_bill_id(bill_id_toadd, selected)
            decimal_number = float(Decimal(selected_product_id.product_price).quantize(Decimal('0.00')))
            BillRepository().insert_mustpay_by_order_id(decimal_number,bill_id_toadd)

    #bill

    def get_bill_bytablename(self,tablename):
    
        return BillRepository().get_bill_id_by_table_name(tablename)

    def insert_bill_bytablename(self,tablename):

        BillRepository().insert_table_name_to_bill(tablename)

    def close_bill_by_table_name(self,tablename):

        BillRepository().close_bill_by_table_name(tablename)

    def update_remain_check_by_tablename(self,tablename):

        BillRepository().update_remain_check_by_tablename(tablename)

    def get_orders_of_current_table(self,tablename):

        return OrderRepository().get_orders_of_current_table(tablename)

    def update_orderstatus_paid_by_orderid(self,item):

        OrderRepository().update_orderstatus_paid_by_orderid(int(item))

    def get_mustpay_by_table_name(self,tablename):

        return BillRepository().get_mustpay_by_table_name(tablename)

    def update_bill(self,tablename,payby_cash1,payby_cc1):

        BillRepository().update_change_by_paidcash_and_table_name(payby_cash1,tablename)
        BillRepository().update_change_by_paidcc_and_table_name(payby_cc1,tablename)

    def get_paids_by_table_name(self,tablename):

        return BillRepository().get_paids_by_table_name(tablename)
    
    def update_table_repo(self,newtablecount):

        result = BillRepository().change_table_number(newtablecount)
        return result

    def remain_table(self):

        lasttable = self.table_count()
        remaining_check = BillRepository().select_remain_check_by_tablename(lasttable)
        return remaining_check

    #product

    def get_pro_price_by_product_name(self,name):
        temp_product = ProductRepository().get_product_by_product_name(name)
        return temp_product.product_price
    
    def get_product_by_product_id(self,id):

        return ProductRepository().get_product_by_product_id(id)

    def change_product_table(self,order_id,product_name,current_bill,bill_id_toadd):

        temp_product = ProductRepository().get_product_by_product_name(product_name)
        OrderRepository().change_bill_by_order_id(bill_id_toadd,order_id)
        BillRepository().decrease_mustpay_by_order_id(temp_product.product_price,current_bill)
        BillRepository().insert_mustpay_by_order_id(temp_product.product_price,bill_id_toadd)

    def get_allcategory_of_products(self):

        return ProductRepository().get_allcategory_of_products()
    
    def get_allproducts_by_category(self,cat):

        return ProductRepository().get_allproducts_by_category(cat)

    #head count

    def head_count(self):

        bill_id = BillRepository().get_bill_id_by_table_name(self.var.get())
        BillRepository().set_head_count(int(self.pc_label_entry.get()) , bill_id)

    def get_head_count(self,tablename):
        hc = int(BillRepository().get_head_count(tablename)[0])
        return hc

    #table count

    def table_count(self):
        return OrderRepository().table_count()



    


        






