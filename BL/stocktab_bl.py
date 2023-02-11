import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
from DAL.Sql.Repository.StockRepository import StockRepository
from DAL.Sql.Repository.ProductRepository import ProductRepository

class Stocktabb_bl: 

    def __init__(self,stocktab,tree_stocktab,entry_stock_name,entry_stock_weight,entry_stock_unit,var,tree_stocktab_newrecipe,tree_product_stock,entry_adding_stock_weight,entry_product_name,entry_product_price,entry_product_category,entry_product_stock_name,entry_product_stock_price,newproductlist_stock):
        
        self.stocktab = stocktab
        self.tree_stocktab = tree_stocktab
        self.entry_stock_name = entry_stock_name
        self.entry_stock_weight = entry_stock_weight
        self.entry_stock_unit = entry_stock_unit
        self.var = var
        self.tree_stocktab_newrecipe = tree_stocktab_newrecipe
        self.tree_product_stock = tree_product_stock
        self.entry_adding_stock_weight = entry_adding_stock_weight
        self.entry_product_name = entry_product_name
        self.entry_product_price = entry_product_price
        self.entry_product_category = entry_product_category
        self.entry_product_stock_name = entry_product_stock_name
        self.entry_product_stock_price = entry_product_stock_price
        self.newproductlist_stock = newproductlist_stock
        

    def fillcolumn(self,stock_name, stock_weight, stock_unit):
        self.tree_stocktab.insert('', tk.END, values=(str(stock_name).capitalize(), stock_weight, stock_unit))

    def displaySelectedItem(self,event):

        self.entry_stock_name.delete(0, tk.END)
        self.entry_stock_weight.delete(0, tk.END)
        self.entry_stock_unit.delete(0, tk.END)

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
                messagebox.showerror("Error for 'Adding Stock Weight'",'Please enter a value for Adding Stock Weight', parent = self.stocktab)
            else:
                StockRepository().update_stock_by_stock_name_and_stock_weight(get_stock_weight, get_stock_name)
                messagebox.showinfo("Stock updated!" , 'Stock Name: '+
                str(get_stock_name)+'\nStock Weight: '+str(get_stock_weight)+' '+str(get_stock_unit)+'\n\nUpdated' , parent = self.stocktab)
        else:
            StockRepository().insert_stock_by_stock_name_stock_weight_stock_unit(get_stock_name,get_stock_weight,get_stock_unit)
            messagebox.showinfo("New stock added!" , 'Stock Name: '+str(get_stock_name)+'\nStock Weight: '+str(get_stock_weight)+' '+str(get_stock_unit)+'\n\nAdded' , parent = self.stocktab)
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

        self.tree_stocktab_newrecipe.insert('', tk.END, values=(str(get_stock_name).capitalize(), get_adding_stock_weight, get_stock_unit))

    def delete_recipe(self):
        self.tree_stocktab_newrecipe.delete(self.tree_stocktab_newrecipe.selection()[0])

    def add_product(self):
        product_name = self.entry_product_name.get()
        product_price = self.entry_product_price.get()
        if self.entry_product_category.get() != '':
            product_category = self.entry_product_category.get()
        else:
            product_category = str(self.var.get())
        ProductRepository().insert_product(product_name, product_price, product_category)
        self.product_list_in_stocktab()
        self.update_dropdown()

    def product_list_in_stocktab(self,*args):
        self.tree_product_stock.delete(*self.tree_product_stock.get_children())
        rows = ProductRepository().get_allproducts_by_category(self.var.get())
        for row in rows:
            self.tree_product_stock.insert('', tk.END, values=(row[0], row[1]))

    def update_dropdown(self):
        options = []
        for opt in ProductRepository().get_allcategory_of_products():
            options.append(opt[0])
        dropdown = tk.OptionMenu(self.newproductlist_stock, self.var, *options)
        dropdown.config(width=15 ,height=1,font=("Arial", 8), background="grey", activebackground="white")
        dropdown.grid(row=0, column=0,padx=5,pady=5)

    def display_product_stock(self,event):

        self.entry_product_stock_name.delete(0, tk.END)
        self.entry_product_stock_price.delete(0, tk.END)

        selectedItem = self.tree_product_stock.selection()

        if selectedItem:
            selectedItem = selectedItem[0]
            self.entry_product_stock_name.insert(0, self.tree_product_stock.item(selectedItem)['values'][0])
            self.entry_product_stock_price.insert(0, self.tree_product_stock.item(selectedItem)['values'][1])
           
    def update_product(self):

        product_name = self.entry_product_stock_name.get()
        product_id = ProductRepository().get_product_id_by_product_name(product_name)
        product_price = self.entry_product_stock_price.get()
        ProductRepository().update_product_price_by_product_id(str(product_price),product_id[0])
        ProductRepository().update_product_name_by_product_id(str(product_name),product_id[0])
        self.product_list_in_stocktab()
        self.entry_product_stock_name.delete(0, tk.END)
        self.entry_product_stock_price.delete(0, tk.END)

    
    
