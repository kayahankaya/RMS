import DAL.Sql.Db.DbManager as DbManager
from DAL.Sql.Db.Entities.ProductEntity import ProductEntity

class ProductRepository:

    def __init__(self):

        self.dbcontext = DbManager.getdbbcon()

    def get_product_by_product_name(self,product_name):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM products 
        WHERE product_name=%s""",(product_name))
        row = cur.fetchone()
        
        temp_product = ProductEntity()

        temp_product.product_id = row[0]
        temp_product.product_name = row[1]
        temp_product.product_price = row[2]
        temp_product.product_category = row[3]
        temp_product.created_at = row[4]
        temp_product.updated_at = row[5]
        
        return temp_product

    def get_product_by_product_id(self,product_id):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM products 
        WHERE product_id=%s""",(product_id))
        row = cur.fetchone()

        temp_product = ProductEntity()

        temp_product.product_id = row[0]
        temp_product.product_name = row[1]
        temp_product.product_price = row[2]
        temp_product.product_category = row[3]
        temp_product.created_at = row[4]
        temp_product.updated_at = row[5]

        return temp_product

    def get_allproducts(self):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT product_name, product_price 
        FROM products """)
        list_products = cur.fetchall()

        return list_products

    
    def get_allcategory_of_products(self):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT DISTINCT product_category 
        FROM products """)
        list_category = cur.fetchall()

        return list_category

    def insert_product(self,product_name, product_price, product_category):

        cur = self.dbcontext.cursor()
        cur.execute("""
        INSERT INTO products (product_name, product_price, product_category) 
        VALUES(%s, %s, %s)""", (product_name, product_price, product_category))

        self.dbcontext.commit()


    def get_allproducts_by_category(self,product_category):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT product_name, product_price 
        FROM products 
        WHERE product_category=%s""",(product_category))
        rows = list(cur.fetchall())

        return rows

    def update_product_price_by_product_id(self, product_price, product_id):

        cur = self.dbcontext.cursor()
        cur.execute("""
        UPDATE products 
        SET products.product_price = %s
        WHERE products.product_id = %s""", (product_price, product_id))

        self.dbcontext.commit()

    def update_product_name_by_product_id(self,product_name,  product_id):

        cur = self.dbcontext.cursor()
        cur.execute("""
        UPDATE products 
        SET products.product_name = %s
        WHERE products.product_id = %s""", (product_name, product_id))

        self.dbcontext.commit()

    def get_product_id_by_product_name(self,product_name):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT product_id
        FROM products 
        WHERE products.product_name = %s""",(product_name))
        product_id = cur.fetchone()

        return product_id











            

        


