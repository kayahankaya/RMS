from DAL.Sql.Repository.StockRepository import StockRepository
from DAL.Sql.Repository.ProductRepository import ProductRepository

class Stocktabb_bl(): 
        
    def get_all_stock(self):
        return StockRepository().get_allstock()

    def getallstock_by_stockname(self,get_stock_name):
        return StockRepository().get_allstock_by_stock_name(get_stock_name)

    def insert_new_stock(self,get_stock_name,get_stock_weight,get_stock_unit):
        StockRepository().insert_stock_by_stock_name_stock_weight_stock_unit(get_stock_name,get_stock_weight,get_stock_unit)

    def insert_exist_stock(self,get_stock_weight, get_stock_name):
        StockRepository().update_stock_by_stock_name_and_stock_weight(get_stock_weight, get_stock_name)

    def drop_stock_by_stock_name(self,stock_name_ingre,stock_weight_ingre):
        StockRepository().drop_stock_by_stock_name(stock_name_ingre,stock_weight_ingre)

    def get_allproducts(self):
        return ProductRepository().get_allproducts()

    def insert_product(self,product_name, product_price, product_category):
        ProductRepository().insert_product(product_name, product_price, product_category)

    def get_allcategory_of_products(self):
        return ProductRepository().get_allcategory_of_products()
    
    def get_allproducts_by_category(self,tablename):
        return ProductRepository().get_allproducts_by_category(tablename)
    
    def get_product_id_by_product_name(self,product_name):
        return ProductRepository().get_product_id_by_product_name(product_name)
    
    def update_product_price_and_name(self, pn,pp,pi):
        ProductRepository().update_product_price_by_product_id(pp,pi)
        ProductRepository().update_product_name_by_product_id(pn,pi)

    def delete_product_by_product_id(self,product_id):
        ProductRepository().delete_product_by_product_id(product_id)


    


    
    
