import DAL.Sql.Db.DbManager as DbManager
from DAL.Sql.Db.Entities.StockEntity import StockEntity

class StockRepository:

    def __init__(self):

        self.dbcontext = DbManager.getdbbcon()

    def get_allstock(self):

        all_stock_list = []

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM stock""")
        rows = cur.fetchall()

        for row in rows:

            temp_stock = StockEntity()

            temp_stock.stock_id = row[0]
            temp_stock.stock_name = row[1]
            temp_stock.stock_weight = row[2]
            temp_stock.stock_unit = row[3]
            temp_stock.created_at = row[4]
            temp_stock.updated_at = row[5]

            all_stock_list.append((temp_stock.stock_name,temp_stock.stock_weight,temp_stock.stock_unit))
        
        return all_stock_list

    def delete_stock_by_stock_name(self,selecteditem):
        cur = self.dbcontext.cursor()
        cur.execute("""
        DELETE 
        FROM stock 
        WHERE stock_name = %s""", (selecteditem))
        self.dbcontext.commit()

    def get_allstock_by_stock_name(self,get_stock_name):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM stock 
        WHERE stock_name = %s""", get_stock_name)
        result1 = cur.fetchall()

        return result1

    def get_stockunit_by_stock_name(self,get_stock_name):
        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT stock_unit 
        FROM stock 
        WHERE stock_name = %s""", get_stock_name)
        result2 = cur.fetchone()

        return result2

    def get_stock_by_stock_id(self,stock_id):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM stock 
        WHERE stock_id=%s""",(stock_id))
        row = cur.fetchone()

        temp_stock = StockEntity()

        temp_stock.stock_id = row[0]
        temp_stock.stock_name = row[1]
        temp_stock.stock_weight = row[2]
        temp_stock.stock_unit = row[3]
        temp_stock.created_at = row[4]
        temp_stock.updated_at = row[5]
        
        return temp_stock

    def get_stock_by_stock_name(self,stock_name):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM stock 
        WHERE stock_name=%s""",(stock_name))
        row = cur.fetchone()

        temp_stock = StockEntity()

        temp_stock.stock_id = row[0]
        temp_stock.stock_name = row[1]
        temp_stock.stock_weight = row[2]
        temp_stock.stock_unit = row[3]
        temp_stock.created_at = row[4]
        temp_stock.updated_at = row[5]

        return temp_stock

    def update_stock_by_stock_name_and_stock_weight(self,get_stock_weight, get_stock_name):

        cur = self.dbcontext.cursor()
        cur.execute("""
        UPDATE stock 
        SET stock_weight = stock_weight + %s 
        WHERE stock_name = %s;""", (get_stock_weight, get_stock_name))
        self.dbcontext.commit()

    def update_stock_by_stock_name_and_stock_unit(self,get_stock_unit, get_stock_name):

        cur = self.dbcontext.cursor()
        cur.execute("""
        UPDATE stock 
        SET stock_unit = %s 
        WHERE stock_name = %s;""", (get_stock_unit, get_stock_name))
        self.dbcontext.commit()

    def insert_stock_by_stock_name_stock_weight_stock_unit(self,get_stock_name, get_stock_weight, get_stock_unit):

        cur = self.dbcontext.cursor()
        cur.execute("""
        INSERT INTO stock (stock_name, stock_weight, stock_unit) 
        VALUES(%s, %s, %s)""", (get_stock_name, get_stock_weight, get_stock_unit))
        self.dbcontext.commit()

    def drop_stock_by_stock_id(self,stock_id_ingre,stock_weight_ingre):

        cur = self.dbcontext.cursor()
        cur.execute("""
        UPDATE stock 
        SET stock_weight = stock_weight - %s 
        WHERE stock_id = %s;""", (stock_weight_ingre, stock_id_ingre))

        self.dbcontext.commit()

    def drop_stock_by_stock_name(self,stock_name_ingre,stock_weight_ingre):

        cur = self.dbcontext.cursor()
        cur.execute("""
        UPDATE stock 
        SET stock_weight = stock_weight - %s 
        WHERE stock_name = %s;""", (stock_weight_ingre, stock_name_ingre))

        self.dbcontext.commit()

    def update_stock_by_stock_id_and_stock_weight(self,get_stock_weight, get_stock_id):

        cur = self.dbcontext.cursor()
        cur.execute("""
        UPDATE stock 
        SET stock_weight = stock_weight + %s 
        WHERE stock_id = %s;""", (get_stock_weight, get_stock_id))
        self.dbcontext.commit()





            

        


