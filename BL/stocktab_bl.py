from DAL.Sql.Repository.StockRepository import StockRepository
from DAL.Sql.Repository.ProductRepository import ProductRepository

class Stocktabb_bl(): 

    def __init__(self,*args):

        self.stocktab = args[0]
        self.tree_stocktab = args[1]
        self.entry_stock_name = args[2]
        self.entry_stock_weight = args[3]
        self.entry_stock_unit = args[4]
        self.var = args[5]
        self.tree_stocktab_newrecipe = args[6]
        self.tree_product_stock = args[7]
        self.entry_adding_stock_weight = args[8]
        self.entry_product_name = args[9]
        self.entry_product_price = args[10]
        self.entry_product_category = args[11]
        self.entry_product_stock_name = args[12]
        self.entry_product_stock_price = args[13]
        self.newproductlist_stock = args[14]
        self.ask_question = args[15]
        self.show_error = args[16]
        self.show_info = args[17]
        self.delete_entry = args[18]
        self.option_menu = args[19]
        self.insert_tree = args[20]
        self.tree_productstab = args[21]
        
    def fillcolumn(self,stock_name, stock_weight, stock_unit):
        self.insert_tree(self.tree_stocktab,str(stock_name).capitalize(), stock_weight, stock_unit)

    def displaySelectedItem(self,event):
        self.delete_entry(self.entry_stock_name)
        self.delete_entry(self.entry_stock_weight)
        self.delete_entry(self.entry_stock_unit)

        selectedItem = self.tree_stocktab.selection()

        if selectedItem:
            selectedItem = selectedItem[0]
            self.entry_stock_name.insert(0, self.tree_stocktab.item(selectedItem)['values'][0])
            self.entry_stock_weight.insert(0, self.tree_stocktab.item(selectedItem)['values'][1])
            self.entry_stock_unit.insert(0, self.tree_stocktab.item(selectedItem)['values'][2])

    def populate_tree(self):
        self.tree_stocktab.delete(*self.tree_stocktab.get_children())
        allstock = StockRepository().get_allstock()
        for row in allstock:
            self.fillcolumn(row[0], row[1], row[2])

    def add_stock(self):
        
        get_stock_name = self.entry_stock_name.get()
        get_stock_weight = self.entry_stock_weight.get()
        get_stock_unit = self.entry_stock_unit.get()

        result1 = StockRepository().get_allstock_by_stock_name(get_stock_name)

        if result1:
            if get_stock_weight == '':
                textvar1 = "Error for 'Adding Stock Weight'"
                textvar2 = 'Please enter a value for Adding Stock Weight'
                self.show_error(textvar1,textvar2)
            else:
                StockRepository().update_stock_by_stock_name_and_stock_weight(get_stock_weight, get_stock_name)
                textvar1 = "Stock updated!"
                textvar2 = 'Stock Name: '+str(get_stock_name)+'\nStock Weight: '+str(get_stock_weight)+' '+str(get_stock_unit)+'\n\nUpdated'
                self.show_info(textvar1,textvar2)
        else:
            StockRepository().insert_stock_by_stock_name_stock_weight_stock_unit(get_stock_name,get_stock_weight,get_stock_unit)
            textvar1 = "New stock added!"
            textvar2 = 'Stock Name: '+str(get_stock_name)+'\nStock Weight: '+str(get_stock_weight)+' '+str(get_stock_unit)+'\n\nAdded'
            self.show_info(textvar1,textvar2)
        # refresh the tree with updated data
        self.populate_tree()

    def delete_stock(self):
        stock_name_ingre = self.entry_stock_name.get()
        stock_weight_ingre = self.entry_stock_weight.get()
        StockRepository().drop_stock_by_stock_name(stock_name_ingre,stock_weight_ingre)

        self.populate_tree()

    def add_recipe(self):

        get_stock_name = self.entry_stock_name.get()
        get_adding_stock_weight = self.entry_adding_stock_weight.get()
        get_stock_unit = self.entry_stock_unit.get()
        
        textvar1 = "New ingredient added!"
        textvar2 = 'Igredient Name: '+str(get_stock_name)+'\nIngredient Weight: '+str(get_adding_stock_weight)+'\nIngredient Unit: '+str(get_stock_unit)
        answer = self.ask_question(textvar1,textvar2)

        if answer == 'yes':
            self.insert_tree(self.tree_stocktab_newrecipe,str(get_stock_name).capitalize(), get_adding_stock_weight, get_stock_unit)



    def delete_recipe(self):
        self.tree_stocktab_newrecipe.delete(self.tree_stocktab_newrecipe.selection()[0])

    def add_product(self):

        product_name = self.entry_product_name.get()
        product_price = self.entry_product_price.get()

        if self.entry_product_category.get() != '':
            product_category = self.entry_product_category.get()
        else:
            product_category = str(self.var.get())

        textvar1 = "New product added!"
        textvar2 = 'Product Name: '+str(product_name)+'\nProduct Price: '+str(product_price)+'\n\nAdded'
        answer = self.ask_question(textvar1,textvar2)

        if answer == 'yes':

            ProductRepository().insert_product(product_name, product_price, product_category)
            self.product_list_in_stocktab()
            self.update_dropdown()

            self.tree_productstab.delete(*self.tree_productstab.get_children())
            rows = ProductRepository().get_allproducts()
            for row in rows:
                self.insert_tree(self.tree_productstab,row[0], row[1])


    def product_list_in_stocktab(self,*args):
        self.tree_product_stock.delete(*self.tree_product_stock.get_children())
        rows = ProductRepository().get_allproducts_by_category(self.var.get())
        for row in rows:
            self.insert_tree(self.tree_product_stock,row[0], row[1])

    def update_dropdown(self):
        options = []
        for opt in ProductRepository().get_allcategory_of_products():
            options.append(opt[0])
        dropdown = self.option_menu(self.newproductlist_stock,self.var, options)
        dropdown.config(width=15 ,height=1,font=("Arial", 8), background="grey", activebackground="white")
        dropdown.grid(row=0, column=0,padx=5,pady=5)

    def display_product_stock(self,event):

        self.delete_entry(self.entry_product_stock_name)
        self.delete_entry(self.entry_product_stock_price)

        selectedItem = self.tree_product_stock.selection()

        if selectedItem:
            selectedItem = selectedItem[0]
            self.entry_product_stock_name.insert(0, self.tree_product_stock.item(selectedItem)['values'][0])
            self.entry_product_stock_price.insert(0, self.tree_product_stock.item(selectedItem)['values'][1])
           
    def update_product(self):

        product_name = self.entry_product_stock_name.get()
        product_id = ProductRepository().get_product_id_by_product_name(product_name)
        product_price = self.entry_product_stock_price.get()

        textvar1 = "New product added!"
        textvar2 = 'Product Name: '+str(product_name)+'\nProduct Price: '+str(product_price)+'\n\nAdded'
        answer = self.ask_question(textvar1,textvar2)

        if answer == 'yes':

            ProductRepository().update_product_price_by_product_id(str(product_price),product_id[0])
            ProductRepository().update_product_name_by_product_id(str(product_name),product_id[0])
            self.product_list_in_stocktab()
            self.delete_entry(self.entry_product_stock_name)
            self.delete_entry(self.entry_product_stock_price)
            self.tree_productstab.delete(*self.tree_productstab.get_children())

            rows = ProductRepository().get_allproducts()
            for row in rows:
                self.insert_tree(self.tree_productstab,row[0], row[1])

    def delete_product(self):

        product_name = self.entry_product_stock_name.get()
        product_id = ProductRepository().get_product_id_by_product_name(product_name)
        product_price = self.entry_product_stock_price.get()

        textvar1 = "Deleting Product"
        textvar2 = '\nDo you want to DELETE this product: ?\nProduct Name: '+str(product_name)+'\nProduct Price: '+str(product_price)
        answer = self.ask_question(textvar1,textvar2)

        if answer == 'yes':

            ProductRepository().delete_product_by_product_id(product_id)
            self.product_list_in_stocktab()
            self.delete_entry(self.entry_product_stock_name)
            self.delete_entry(self.entry_product_stock_price)
            self.tree_productstab.delete(*self.tree_productstab.get_children())

            rows = ProductRepository().get_allproducts()
            for row in rows:
                self.insert_tree(self.tree_productstab,row[0], row[1])




    


    
    
