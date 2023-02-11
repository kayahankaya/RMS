import tkinter as tk 
from tkinter import ttk 
from DAL.Sql.Repository.ProductRepository import ProductRepository
from DAL.Sql.Repository.OrderRepository import OrderRepository
from BL.tabletab_bl import Order

def main(nb):

    tabletab1 = ttk.Frame(nb)
    tabletab1.pack(fill=tk.BOTH, expand=True)
    nb.add(tabletab1, text="Tables", underline=0)

    tabletab = tk.Frame(tabletab1)
    tabletab.pack()

    part1 = tk.Frame(tabletab,bd=2,relief="ridge")
    part1.grid(row=0, column=0, rowspan=2, columnspan=2, pady=15, sticky='nsew')

    part1_1 = tk.Frame(part1)
    part1_1.grid(row=0, column=0, rowspan=2, columnspan=2,padx=15,sticky='nsew')

    order_label = tk.Label(part1_1)
    order_label.pack(padx=7, pady=7)

    columns_table = ('order_id','product_name', 'created_at')

    tree_tabletab = ttk.Treeview(part1_1, columns=columns_table, show='headings')

    tree_tabletab.column("#1",anchor=tk.CENTER, width=100)
    tree_tabletab.column("#2",anchor=tk.CENTER, width=150)
    tree_tabletab.column("#3",anchor=tk.CENTER, width=150)
    tree_tabletab.pack(padx=7, pady=7)

    tree_tabletab.heading('order_id', text='ID')
    tree_tabletab.heading('product_name', text='Product Name')
    tree_tabletab.heading('created_at', text='Created At')

    tree_tabletab.columnconfigure(0, weight=1)
    tree_tabletab.rowconfigure(0, weight=1)

    part1_1_2 = tk.Frame(part1_1)
    part1_1_2.pack(padx=7, pady=7)

    part1_2 = tk.Frame(part1,bd=2,relief="raised")
    part1_2.grid(row=0, column=2, rowspan=2, columnspan=2, padx=15,pady=7, sticky='nsew')

    part1_2_tn = tk.Frame(part1_2)
    part1_2_tn.pack(side=tk.TOP, padx=7, pady=7)

    part1_2_rb = tk.Frame(part1_2)
    part1_2_rb.pack(padx=7, pady=7)

    part1_2_ob = tk.Frame(part1_2)
    part1_2_ob.pack(padx=7, pady=7)

    selectedlabel = tk.Label(part1_2)
    selectedlabel.pack(padx=7, pady=7)

    part2 = tk.Frame(tabletab,bd=2,relief="ridge")
    part2.grid(row=0, column=2, rowspan=2, columnspan=2,padx=15, pady=15,sticky='nsew')

    products_label = tk.Label(part2,text="Menu")
    products_label.pack(padx=7, pady=7)

    columns_products = ('product_name', 'product_price')
    tree_productstab = ttk.Treeview(part2, columns=columns_products, show='headings')
    tree_productstab.column("#1",anchor=tk.CENTER, width=140)
    tree_productstab.column("#2",anchor=tk.CENTER, width=90)
    tree_productstab.pack(padx=7, pady=7)

    tree_productstab.heading('product_name', text='Product_Name')
    tree_productstab.heading('product_price', text='Product_Price')

    part3 = tk.Frame(tabletab,bd=2,relief="ridge")
    part3.grid(row=2, column=0, rowspan=2, columnspan=2, pady=15,sticky='nsew')

    part4 = tk.Frame(tabletab,bd=2,relief="ridge")
    part4.grid(row=2, column=2, rowspan=2, columnspan=1,padx=15, pady=15,sticky='nsew')

    tablecheck_label = ttk.Label(part4,text='--Check Details--\n')
    tablecheck_label.grid(row=0, column=0,columnspan=2,padx=7,pady=7)

    text_checkamount1 = 'Total Amount  = '
    checkamount_label = ttk.Label(part4,text=text_checkamount1)
    checkamount_label.grid(row=1, column=0, padx=7, pady=7,sticky='w')

    checkentry_wo_tax = tk.Entry(part4,width=10)
    checkentry_wo_tax.grid(row=1, column=1, padx=7, pady=7,sticky='nsew')

    remainingcheck_text = 'Remaining Check  = '
    remainingcheck_label = ttk.Label(part4,text=remainingcheck_text)
    remainingcheck_label.grid(row=2, column=0, padx=7, pady=7,sticky='w')

    remainingcheck_entry = tk.Entry(part4,width=10)
    remainingcheck_entry.grid(row=2, column=1, padx=7, pady=7,sticky='nsew')

    selected_amount_text = 'Selected Items Amount   = '
    selected_amount = ttk.Label(part4,text=selected_amount_text)
    selected_amount.grid(row=3, column=0, padx=7, pady=7, sticky='nsew')

    checkentry_amount = tk.Entry(part4,width=10)
    checkentry_amount.grid(row=3, column=1, padx=7, pady=7,sticky='nsew')

    paidbycheck_label = ttk.Label(part4,text='Paid by Check  = ')
    paidbycheck_label.grid(row=7, column=0, padx=7, pady=7,sticky='w')

    paidbycheck_ent = tk.Entry(part4,width=10)
    paidbycheck_ent.grid(row=7, column=1, padx=7, pady=7,sticky='nsew')

    paidbycc_label = ttk.Label(part4,text='Paid by Card  = ')
    paidbycc_label.grid(row=8, column=0, padx=7, pady=7,sticky='w')

    paidbycc_label_entry = tk.Entry(part4,width=10)
    paidbycc_label_entry.grid(row=8, column=1, padx=7, pady=7,sticky='nsew')

    pc_label = ttk.Label(part1_1_2,text='People count  = ')
    pc_label.grid(row=0, column=2, padx=2, pady=2,sticky='nsew')

    pc_label_entry_var = tk.IntVar(part1_1_2, value=1)

    pc_label_entry = tk.Entry(part1_1_2,width=10, textvariable=pc_label_entry_var)
    pc_label_entry.grid(row=0, column=3, padx=2, pady=2,sticky='nsew')

    default_db = tk.StringVar(value='1')

    options = ['1','2','3','4','5','6','7','8','9','10']
    dropdown = tk.OptionMenu(part1_2_ob, default_db, *options)
    dropdown.config(height=1, width=2 ,font=("Arial", 8), background="lightblue", activebackground="white")
    dropdown.pack(side=tk.LEFT)

    list_products = ProductRepository().get_allproducts()

    var = tk.IntVar()
        
    orderobj = Order(tree_tabletab, default_db, var, selectedlabel,order_label,part3,checkentry_wo_tax,paidbycheck_ent,paidbycc_label_entry,remainingcheck_entry,tree_productstab,checkentry_amount,part1_2_rb,list_products,part1_1_2,pc_label_entry_var,pc_label_entry)
    
    orderobj.update_options2()

    transfer_table = tk.Button(part1_1_2, text='Transfer to >>>',height=1, width=15, command=lambda: orderobj.change_table())
    transfer_table.grid(row=0,column=0)

    closetable = tk.Button(part4, text='Paid!',height=3, width=10, command=lambda: orderobj.pay_bill())
    closetable.grid(row=6, column=0, columnspan=2,padx=7, pady=7,sticky='nsew')

    add_table = tk.Button(part1_2_tn, text='+Table', width=5, command=lambda: orderobj.add_table())
    add_table.pack(side=tk.LEFT)

    delete_table = tk.Button(part1_2_tn, text='-Table', width=5, command=lambda: orderobj.delete_table())
    delete_table.pack(side=tk.RIGHT)

    addorder = tk.Button(part1_2_ob, text='Add Order',height=1, width=10, command=lambda: orderobj.add_order())
    addorder.pack(side=tk.LEFT)

    deleteorder = tk.Button(part1_2_ob, text='Delete Order',height=1, width=10, command=lambda: orderobj.delete_order())
    deleteorder.pack(side=tk.RIGHT)

    dropdown.bind("<<OptionMenuSelect>>", orderobj.on_select)

    tree_tabletab.bind("<<TreeviewSelect>>", orderobj.displaySelectedItem)

    orderobj.make_rbtn()
    orderobj.sel()

    for i in orderobj.fillproductlist():
        tree_productstab.insert('', tk.END, values=(i))

if __name__ == "__main__":
    main()