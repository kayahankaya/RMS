import DAL.Sql.Db.DbManager as DbManager
from DAL.Sql.Db.Entities.RecipeEntity import RecipeEntity

class RecipeRepository:

    def __init__(self):

        self.dbcontext = DbManager.getdbbcon()

    def get_recipe_by_recipe_id(self,stock_id):

        cur = self.dbcontext.cursor()
        cur.execute("select * from recipes where stock_id=%s",(stock_id))
        row = cur.fetchone()

        temp_recipe = RecipeEntity()

        temp_recipe.recipe_id = row[0]
        temp_recipe.stock_id = row[1]
        temp_recipe.product_id = row[2]
        temp_recipe.recipe_weight = row[3]
        temp_recipe.created_at = row[4]
        temp_recipe.updated_at = row[5]

        return temp_recipe

    def get_recipe_by_product_id(self,product_id):

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT * 
        FROM recipes 
        WHERE product_id=%s""",(product_id))
        row = cur.fetchall()

        return row

    def insert_product(self,product_name, product_price, product_category):

        cur = self.dbcontext.cursor()
        cur.execute("""
        INSERT INTO recipe (product_name, product_price, product_category) 
        VALUES(%s, %s, %s)""", (product_name, product_price, product_category))
        
        self.dbcontext.commit()

    







            

        


