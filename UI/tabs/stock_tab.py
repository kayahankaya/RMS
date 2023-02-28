import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
from BL.stocktab_bl import Stocktabb_bl

def main(nb,tree_productstab):

    stocktab = ttk.Frame(nb)
    stocktab.pack(fill='both', expand=True)
    nb.add(stocktab, text="Stock", underline=0)

    stocklist_button = ttk.Frame(stocktab)
    stocklist_button.grid(row=0,column=0,padx=15,pady=20)

    stocklist = ttk.Frame(stocktab, borderwidth=2, relief='raised')
    stocklist.grid(row=0,column=1,padx=15,pady=20)

    columns = ('stock_name', 'stock_weight', 'stock_unit')
    tree_stocktab = ttk.Treeview(stocklist, columns=columns, show='headings')
    tree_stocktab.column("#1",anchor=tk.CENTER)
    tree_stocktab.column("#2",anchor=tk.CENTER)
    tree_stocktab.column("#3",anchor=tk.CENTER)
    tree_stocktab.pack()

    tree_stocktab.heading('stock_name', text='Stock Name')
    tree_stocktab.heading('stock_weight', text='Stock Weight')
    tree_stocktab.heading('stock_unit', text='Stock Unit')

    label_stock_name = tk.Label(stocklist_button, text='Stock Name:')
    entry_stock_name = tk.Entry(stocklist_button)

    label_stock_name.pack()
    entry_stock_name.pack()

    label_stock_weight = tk.Label(stocklist_button, text='Stock Weight:')
    entry_stock_weight = tk.Entry(stocklist_button)

    label_stock_weight.pack()
    entry_stock_weight.pack()

    label_stock_unit = tk.Label(stocklist_button, text='Stock Unit:')
    entry_stock_unit = tk.Entry(stocklist_button)

    label_stock_unit.pack()
    entry_stock_unit.pack()

    recipebuttons_frame = ttk.Frame(stocktab)
    recipebuttons_frame.grid(row=1,column=0,padx=15,pady=20)

    label_product_name = tk.Label(recipebuttons_frame, text='Product Name:')
    entry_product_name = tk.Entry(recipebuttons_frame)

    label_product_name.pack()
    entry_product_name.pack()

    label_product_price = tk.Label(recipebuttons_frame, text='Product Price:')
    entry_product_price = tk.Entry(recipebuttons_frame)

    label_product_price.pack()
    entry_product_price.pack()

    dropdownframe1 = ttk.Frame(recipebuttons_frame)
    dropdownframe1.pack()

    label_product_category = tk.Label(dropdownframe1, text='Product Category:')
    entry_product_category = tk.Entry(dropdownframe1)

    label_product_category.grid(row=0,column=0,pady=5)
    entry_product_category.grid(row=1,column=0,pady=5)

    newrecipelist = ttk.Frame(stocktab, borderwidth=2, relief='raised')
    newrecipelist.grid(row=1,column=1,padx=15,pady=20)

    newrecipelist_sub = ttk.Frame(newrecipelist)
    newrecipelist_sub.pack(side=tk.TOP)

    label_adding_stock_weight = tk.Label(newrecipelist_sub, text='Recipe Weight:')
    entry_adding_stock_weight = tk.Entry(newrecipelist_sub)

    label_adding_stock_weight.pack()
    entry_adding_stock_weight.pack()

    columns = ('Ingredients', 'Weights', 'Units')
    tree_stocktab_newrecipe = ttk.Treeview(newrecipelist, columns=columns, show='headings')
    tree_stocktab_newrecipe.column("#1",anchor=tk.CENTER)
    tree_stocktab_newrecipe.column("#2",anchor=tk.CENTER)
    tree_stocktab_newrecipe.column("#3",anchor=tk.CENTER)
    tree_stocktab_newrecipe.pack(side=tk.BOTTOM)

    tree_stocktab_newrecipe.heading('Ingredients', text='Ingredients')
    tree_stocktab_newrecipe.heading('Weights', text='Weights')
    tree_stocktab_newrecipe.heading('Units', text='Units')

    newproductlist_stock = ttk.Frame(stocktab, borderwidth=2, relief='raised')
    newproductlist_stock.grid(row=0,column=2,rowspan=2,padx=15,pady=20,sticky='nsew')

    columns_pro = ('product_name', 'product_price')
    tree_product_stock = ttk.Treeview(newproductlist_stock, columns=columns_pro, show='headings')
    tree_product_stock.column("#1",anchor=tk.CENTER, width=120)
    tree_product_stock.column("#2",anchor=tk.CENTER, width=120)
    tree_product_stock.grid(row=1, column=0, sticky='nsew')

    tree_product_stock.heading('product_name', text='Product Name')
    tree_product_stock.heading('product_price', text='Product Price')

    tree_product_stock.configure(height=18)

    label_product_stock_name = tk.Label(newproductlist_stock, text='Product Name:')
    label_product_stock_name.grid(row=2,column=0,padx=5,pady=5,sticky='nsew')

    entry_product_stock_name = tk.Entry(newproductlist_stock)
    entry_product_stock_name.grid(row=3,column=0,padx=5,pady=5,sticky='nsew')

    label_product_stock_price = tk.Label(newproductlist_stock, text='Product Price:')
    label_product_stock_price.grid(row=4,column=0,padx=5,pady=5,sticky='nsew')

    entry_product_stock_price = tk.Entry(newproductlist_stock)
    entry_product_stock_price.grid(row=5,column=0,padx=5,pady=5,sticky='nsew')

    update_product_stock = tk.Button(newproductlist_stock, text='Update Product', width=25, command=lambda: update_product())
    update_product_stock.grid(row=6,column=0,padx=5,pady=5,sticky='nsew')

    update_product_stock = tk.Button(newproductlist_stock, text='Delete Product', width=25, command=lambda: delete_product())
    update_product_stock.grid(row=7,column=0,padx=5,pady=5,sticky='nsew')

    bottom_stock = ttk.Frame(stocktab)
    bottom_stock.grid(row=2,column=0,columnspan=3,padx=5,pady=10,sticky='nsew')

    var = tk.StringVar()

    def fillcolumn(stock_name, stock_weight, stock_unit):
        
        tree_stocktab.insert('', tk.END, values=(str(stock_name).capitalize(), stock_weight, stock_unit))

    def displaySelectedItem(event):

        entry_stock_name.delete(0, tk.END)
        entry_stock_weight.delete(0, tk.END)
        entry_stock_unit.delete(0, tk.END)
        
        selectedItem = tree_stocktab.selection()

        if selectedItem:
            selectedItem = selectedItem[0]
            entry_stock_name.insert(0, tree_stocktab.item(selectedItem)['values'][0])
            entry_stock_weight.insert(0, tree_stocktab.item(selectedItem)['values'][1])
            entry_stock_unit.insert(0, tree_stocktab.item(selectedItem)['values'][2])
    
    def populate_tree():

        tree_stocktab.delete(*tree_stocktab.get_children())
        allstock = stockobj.get_all_stock()
        for row in allstock:
            fillcolumn(row[0], row[1], row[2])
        
    def add_stock():
        
        get_stock_name = entry_stock_name.get()
        get_stock_weight = entry_stock_weight.get()
        get_stock_unit = entry_stock_unit.get()

        allstock = stockobj.getallstock_by_stockname(get_stock_name)

        if allstock:
            if get_stock_weight == '':
                textvar1 = "Error for 'Adding Stock Weight'"
                textvar2 = 'Please enter a value for Adding Stock Weight'
                messagebox.showerror(textvar1,textvar2)
            else:
                stockobj.insert_exist_stock(get_stock_weight, get_stock_name)
                textvar1 = "Stock updated!"
                textvar2 = 'Stock Name: '+str(get_stock_name)+'\nStock Weight: '+str(get_stock_weight)+' '+str(get_stock_unit)+'\n\nUpdated'
                messagebox.showinfo(textvar1,textvar2)
        else:
            stockobj.insert_new_stock(get_stock_name,get_stock_weight,get_stock_unit)
            textvar1 = "New stock added!"
            textvar2 = 'Stock Name: '+str(get_stock_name)+'\nStock Weight: '+str(get_stock_weight)+' '+str(get_stock_unit)+'\n\nAdded'
            messagebox.showinfo(textvar1,textvar2)
        # refresh the tree with updated data
        populate_tree()

    def delete_stock():
        stock_name_ingre = entry_stock_name.get()
        stock_weight_ingre = entry_stock_weight.get()

        stockobj.drop_stock_by_stock_name(stock_name_ingre,stock_weight_ingre)

        populate_tree()

    def add_recipe():

        get_stock_name = entry_stock_name.get()
        get_adding_stock_weight = entry_adding_stock_weight.get()
        get_stock_unit = entry_stock_unit.get()
        
        textvar1 = "New ingredient added!"
        textvar2 = 'Igredient Name: '+str(get_stock_name)+'\nIngredient Weight: '+str(get_adding_stock_weight)+'\nIngredient Unit: '+str(get_stock_unit)
        answer = messagebox.askquestion(textvar1,textvar2)

        if answer == 'yes':
            tree_stocktab_newrecipe.insert('', tk.END, values=(str(get_stock_name).capitalize(), get_adding_stock_weight, get_stock_unit))
    
    def delete_recipe():
        tree_stocktab_newrecipe.delete(tree_stocktab_newrecipe.selection()[0])

    def add_product():

        product_name = entry_product_name.get()
        product_price = entry_product_price.get()

        if entry_product_category.get() != '':
            product_category = entry_product_category.get()
        else:
            product_category = str(var.get())

        textvar1 = "New product added!"
        textvar2 = 'Product Name: '+str(product_name)+'\nProduct Price: '+str(product_price)+'\n\nAdded'
        answer = messagebox.askquestion(textvar1,textvar2)

        if answer == 'yes':

            stockobj.insert_product(product_name, product_price, product_category)
            product_list_in_stocktab()
            update_dropdown()

            tree_productstab.delete(*tree_productstab.get_children())
            rows = stockobj.get_allproducts()
            for row in rows:
                tree_productstab.insert('', tk.END, values=(row[0], row[1]))

    def product_list_in_stocktab(*args):

        tree_product_stock.delete(*tree_product_stock.get_children())
        rows = stockobj.get_allproducts_by_category(var.get())
        for row in rows:
            tree_product_stock.insert('', tk.END, values=(row[0], row[1]))

    def update_dropdown():

        options = []
        for opt in stockobj.get_allcategory_of_products():
            options.append(opt[0])
        dropdown = tk.OptionMenu(newproductlist_stock,var, *options)
        dropdown.config(width=15 ,height=1,font=("Arial", 8), background="grey", activebackground="white")
        dropdown.grid(row=0, column=0,padx=5,pady=5)

    def display_product_stock(event):

        entry_product_stock_name.delete(0, tk.END)
        entry_product_stock_price.delete(0, tk.END)

        selectedItem = tree_product_stock.selection()

        if selectedItem:
            selectedItem = selectedItem[0]
            entry_product_stock_name.insert(0, tree_product_stock.item(selectedItem)['values'][0])
            entry_product_stock_price.insert(0, tree_product_stock.item(selectedItem)['values'][1])

    def update_product():

        product_name = entry_product_stock_name.get()
        product_id = stockobj.get_product_id_by_product_name(product_name)
        product_price = entry_product_stock_price.get()

        textvar1 = "New product added!"
        textvar2 = 'Product Name: '+str(product_name)+'\nProduct Price: '+str(product_price)+'\n\nAdded'
        answer = messagebox.askquestion(textvar1,textvar2)

        if answer == 'yes':

            pn = str(product_name)
            pp = str(product_price)
            pi = product_id[0]
            stockobj.update_product_price_and_name(pn,pp,pi)
            product_list_in_stocktab()

            entry_product_stock_name.delete(0, tk.END)
            entry_product_stock_price.delete(0, tk.END)
            tree_productstab.delete(*tree_productstab.get_children())

            rows = stockobj.get_allproducts()
            for row in rows:
                tree_productstab.insert('', tk.END, values=(row[0], row[1]))

    def delete_product():

        product_name = entry_product_stock_name.get()
        product_id = stockobj.get_product_id_by_product_name(product_name)
        product_price = entry_product_stock_price.get()

        textvar1 = "Deleting Product"
        textvar2 = '\nDo you want to DELETE this product: ?\nProduct Name: '+str(product_name)+'\nProduct Price: '+str(product_price)
        answer = messagebox.askquestion(textvar1,textvar2)

        if answer == 'yes':

            stockobj.delete_product_by_product_id(product_id)
            product_list_in_stocktab()
            entry_product_stock_name.delete(0, tk.END)
            entry_product_stock_price.delete(0, tk.END)
            tree_productstab.delete(*tree_productstab.get_children())

            rows = stockobj.get_allproducts()
            for row in rows:
                tree_productstab.insert('', tk.END, values=(row[0], row[1]))


    stockobj = Stocktabb_bl()

    add_product_b = tk.Button(bottom_stock, text='Add Product', width=15, command=lambda: add_product())
    add_product_b.pack()

    updaterecipe = tk.Button(newrecipelist_sub, text='Add Recipe', width=25, command=lambda: add_recipe())
    updaterecipe.pack(side=tk.LEFT,padx=20,pady=5)

    deleterecipe = tk.Button(newrecipelist_sub, text='Delete Recipe', width=25, command=lambda: delete_recipe())
    deleterecipe.pack(side=tk.RIGHT,padx=20,pady=5)

    updatebutton = tk.Button(stocklist_button, text='Insert', width=25, command=lambda: add_stock())
    updatebutton.pack(pady=5)

    deletebutton = tk.Button(stocklist_button, text='Delete', width=25, command=lambda: delete_stock())
    deletebutton.pack(pady=5)

    product_list_in_stocktab()

    update_dropdown()

    populate_tree()
    
    var.trace("w", product_list_in_stocktab)

    tree_product_stock.bind("<<TreeviewSelect>>", display_product_stock)

    tree_stocktab.bind("<<TreeviewSelect>>", displaySelectedItem)

if __name__ == "__main__":
    main()
