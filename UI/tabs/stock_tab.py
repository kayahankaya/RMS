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

    update_product_stock = tk.Button(newproductlist_stock, text='Update Product', width=25, command=lambda: stockobj.update_product())
    update_product_stock.grid(row=6,column=0,padx=5,pady=5,sticky='nsew')

    update_product_stock = tk.Button(newproductlist_stock, text='Delete Product', width=25, command=lambda: stockobj.delete_product())
    update_product_stock.grid(row=7,column=0,padx=5,pady=5,sticky='nsew')

    bottom_stock = ttk.Frame(stocktab)
    bottom_stock.grid(row=2,column=0,columnspan=3,padx=5,pady=10,sticky='nsew')

    var = tk.StringVar()

    def ask_question(textvar1,textvar2):
        return messagebox.askquestion(textvar1,textvar2)

    def show_error(textvar1,textvar2):
        messagebox.showerror(textvar1,textvar2)
    
    def show_info(textvar1,textvar2):
        messagebox.showinfo(textvar1,textvar2)

    def delete_entry(entry):
        entry.delete(0, tk.END)

    def option_menu(frame,var,liste):
        return tk.OptionMenu(frame, var, *liste)

    def insert_tree(tree,*args):
        tree.insert('', tk.END, values=(args))

    stockobj = Stocktabb_bl(stocktab,tree_stocktab,entry_stock_name,
    entry_stock_weight,entry_stock_unit,var,tree_stocktab_newrecipe,
    tree_product_stock,entry_adding_stock_weight,entry_product_name,
    entry_product_price,entry_product_category,entry_product_stock_name,
    entry_product_stock_price,newproductlist_stock,ask_question,show_error,
    show_info,delete_entry,option_menu,insert_tree,tree_productstab)

    add_product_b = tk.Button(bottom_stock, text='Add Product', width=15, command=lambda: stockobj.add_product())
    add_product_b.pack()

    updaterecipe = tk.Button(newrecipelist_sub, text='Add Recipe', width=25, command=lambda: stockobj.add_recipe())
    updaterecipe.pack(side=tk.LEFT,padx=20,pady=5)

    deleterecipe = tk.Button(newrecipelist_sub, text='Delete Recipe', width=25, command=lambda: stockobj.delete_recipe())
    deleterecipe.pack(side=tk.RIGHT,padx=20,pady=5)

    updatebutton = tk.Button(stocklist_button, text='Insert', width=25, command=lambda: stockobj.add_stock())
    updatebutton.pack(pady=5)

    deletebutton = tk.Button(stocklist_button, text='Delete', width=25, command=lambda: stockobj.delete_stock())
    deletebutton.pack(pady=5)

    stockobj.product_list_in_stocktab()

    stockobj.update_dropdown()

    stockobj.populate_tree()
    
    var.trace("w", stockobj.product_list_in_stocktab)

    tree_product_stock.bind("<<TreeviewSelect>>", stockobj.display_product_stock)

    tree_stocktab.bind("<<TreeviewSelect>>", stockobj.displaySelectedItem)

if __name__ == "__main__":
    main()
