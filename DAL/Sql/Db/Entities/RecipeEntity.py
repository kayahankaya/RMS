import datetime

class RecipeEntity:

    def __init__(self):
        self.recipe_id = 0
        self.stock_id = 0
        self.product_id = 0
        self.recipe_weight = 0
        self.created_at = datetime.date(2002,6,12)
        self.updated_at = datetime.date(2002,6,12)

