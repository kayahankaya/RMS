import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
from decimal import Decimal
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

    tree_productstab.heading('product_name', text='Product Name')
    tree_productstab.heading('product_price', text='Product Price')

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

    default_db_merge = tk.StringVar() 

    options = ['1','2','3','4','5','6','7','8','9','10']
    dropdown = tk.OptionMenu(part1_2_ob, default_db, *options)
    dropdown.config(height=1, width=2 ,font=("Arial", 8), background="lightblue", activebackground="white")
    dropdown.pack(side=tk.LEFT)

    var = tk.IntVar()

    tablegroup_label = ttk.Label(part3,text="""-- Order Details--""")
    tablegroup_label.grid(row=0, column=0,pady=7,padx=7)

    columns_tablegroup = ('product_id','product_name','product_price', 'quantity','total_product_price')
    tree_tablegroup = ttk.Treeview(part3,columns=columns_tablegroup, show='headings')
    tree_tablegroup.grid(row=1, column=0, pady=7,padx=7)

    tree_tablegroup.column("#1", width=145)
    tree_tablegroup.column("#2", width=145)
    tree_tablegroup.column("#3", width=145)
    tree_tablegroup.column("#4", width=145)
    tree_tablegroup.column("#5", width=145)

    tree_tablegroup.heading('product_id', text='Product ID')
    tree_tablegroup.heading('product_name', text='Product Name')
    tree_tablegroup.heading('product_price', text='Product Price')
    tree_tablegroup.heading('quantity', text='Quantity')
    tree_tablegroup.heading('total_product_price', text='Sub Total')

    def pop_up_table_first(var1,var2):   

        popup = tk.Toplevel()
        popup.title("PopUp")

        info_text = tk.Label(popup,text="Selected Amount = " + str(var1))
        info_text.grid(row=0, column=0, columnspan=2,padx=2, pady=2)

        info_text_total = tk.Label(popup,text="Total Remaining Amount = " + str(var2))
        info_text_total.grid(row=1, column=0, columnspan=2,padx=2, pady=2)

        payby_label1 = tk.Label(popup,text="Cash =")
        payby_label1.grid(row=2, column=0, padx=2, pady=2,sticky='w')

        payby_label2 = tk.Label(popup,text="Credit Card =")
        payby_label2.grid(row=3, column=0, padx=2, pady=2,sticky='w')

        payby_cash = tk.Entry(popup, width=10)
        payby_cash.grid(row=2, column=1, padx=2, pady=2,sticky='nsew')

        payby_cc = tk.Entry(popup, width=10)
        payby_cc.grid(row=3, column=1, padx=2, pady=2,sticky='nsew')

        return (payby_cash,payby_cc,popup)

    def pop_up_table_second(popup,cc_cash):

        button = tk.Button(popup, text="OK", command=cc_cash)
        button.grid(row=4, column=0, padx=2, pady=2,sticky='nsew')

        button2 = tk.Button(popup, text="Cancel", command=popup.destroy)
        button2.grid(row=4, column=1, padx=2, pady=2,sticky='nsew')

    def update_ord_list():

        liste = orderobj.ordertable()
        tree_tablegroup.delete(*tree_tablegroup.get_children())
        for i in liste:
            u,product_name,product_price,count,total_product_price = i
            tree_tablegroup.insert('', tk.END, values=(u,product_name,product_price,count,total_product_price))

    def update_table_list():

            liste = orderobj.table_list()
            tree_tabletab.delete(*tree_tabletab.get_children())
            for i in liste:
                order_id = i[0]
                product_name = i[1]
                created_at = i[2]
                tree_tabletab.insert('', tk.END, values=(order_id, product_name ,created_at))

    def entry_update(entry,var):
        entry.delete(0, tk.END)
        entry.insert(0, var)

    def decimal_price(price):
        result = Decimal(price).quantize(Decimal('0.00'))
        return float(result)

    def option_menu(options2):
        return tk.OptionMenu(part1_1_2, default_db_merge, *options2)

    def ask_question(textvar1,textvar2):
        return messagebox.askquestion(textvar1,textvar2)

    def show_error(textvar1,textvar2):
        messagebox.showerror(textvar1,textvar2)

    def sel():

        update_table_list()
        selectedtable = var.get()
        selected = "You selected Table " + str(selectedtable)
        selectedlabel.config(text=selected)
        textvar_order = "Table " + str(selectedtable) +"'s Orders"
        order_label.config(text=textvar_order)
        update_ord_list()
        mustpay_current,temp_bill,remaining_check = orderobj.get_paid()


        if not mustpay_current:

            checkentry_wo_tax.delete(0, tk.END)
            checkentry_wo_tax.insert(0, 0.00)
        else:

            checkentry_wo_tax.delete(0, tk.END)
            checkentry_wo_tax.insert(0, mustpay_current)

        if temp_bill:

            (paidby_cash,paidby_cc) = temp_bill
            remaining_check_int = float(remaining_check[0])

            hc = orderobj.get_head_count()
            
            pc_label_entry.delete(0, tk.END)
            pc_label_entry.insert(0, hc)

            paidbycheck_ent.delete(0, tk.END)
            paidbycheck_ent.insert(0, paidby_cash)

            paidbycc_label_entry.delete(0, tk.END)
            paidbycc_label_entry.insert(0, paidby_cc)

        else:
            (paidby_cash,paidby_cc) = (0.00,0.00)
            remaining_check_int = 0.00

            paidbycheck_ent.delete(0, tk.END)
            paidbycheck_ent.insert(0, paidby_cash)

            paidbycc_label_entry.delete(0, tk.END)
            paidbycc_label_entry.insert(0, paidby_cc)
        
        remainingcheck_entry.delete(0, tk.END)
        remainingcheck_entry.insert(0, remaining_check_int)

    def make_rbtn():

        column_table = 3
        row_table = Order.table_number // column_table 
        last_row = Order.table_number % column_table 
        if last_row >= 1:
            row_table += 1
        for k in range(0,row_table): 
            if k == (row_table-1): 
                if last_row >= 1:
                    column_table = last_row      
            for i in range(1,(column_table+1)):
                input = i+3*k
                textinput = "Table "+str(input)
                radio_button = tk.Radiobutton(part1_2_rb, text=textinput, variable=var, value=input, width = 8 , command = sel)
                table_status =  orderobj.table_status_func(input)
                radio_button.configure(bg='green')
                if table_status:
                    radio_button.configure(bg='red')
                Order.radio_buttons.append(radio_button)
                radio_button.grid(row=k, column=i)

    orderobj = Order(tree_tabletab, default_db, var, 
    remainingcheck_entry,tree_productstab,checkentry_amount,
    pc_label_entry,tabletab,pop_up_table_first,pop_up_table_second,
    make_rbtn,ask_question,show_error,option_menu,decimal_price,entry_update,sel)
    
    dropdown.bind("<<OptionMenuSelect>>", orderobj.on_select)

    tree_tabletab.bind("<<TreeviewSelect>>", orderobj.displaySelectedItem)

    def add_table():
        textvar1 = "Adding Table"
        textvar2 = f"Do you want to add Table {Order.table_number + 1}?"
        answer = ask_question(textvar1,textvar2)
        if answer == 'yes':
            Order.table_number += 1
            orderobj.update_table_repo()
            make_rbtn()
            orderobj.update_options2()
            sel()
    
    def delete_table():
        remaining_check = orderobj.remain_table()
        textvar1 = "Deleting Table"
        textvar2 = f"Do you want to delete Table {Order.table_number}?"
        answer = ask_question(textvar1,textvar2)
    
        if answer == 'yes':

            if remaining_check == 0.0 or remaining_check == None :
                if Order.table_number > 0:
                    Order.table_number -= 1
                    # loop through the radio_buttons list and destroy each one
                    last_rb = Order.radio_buttons.pop()
                    last_rb.destroy()
                    orderobj.update_table_repo()
                    make_rbtn()
                    sel()

            else:
                textvar1 = "Deleting Table"
                textvar2 = f"Orders in Table {Order.table_number} should be pay or delete!\nYou cannot delete table which has orders"
                messagebox.showerror(textvar1, textvar2,tabletab)

    def update_pro_list():
        liste=[]
        liste = orderobj.set_productlist()
        for i in liste:
            product_name, product_price = i
            tree_productstab.insert('', tk.END, values=(product_name, product_price))
    
    for i in orderobj.set_productlist():
        tree_productstab.insert('', tk.END, values=(i))

    make_rbtn()

    #update_ord_list()

    update_pro_list()

    #update_table_list()

    orderobj.update_options2()

    #sel()
        
    transfer_table = tk.Button(part1_1_2, text='Transfer to >>>',height=1, width=15, command=lambda: orderobj.change_table())
    transfer_table.grid(row=0,column=0)

    closetable = tk.Button(part4, text='Paid!',height=3, width=10, command=lambda: orderobj.pay_bill())
    closetable.grid(row=6, column=0, columnspan=2,padx=7, pady=7,sticky='nsew')

    add_table_but = tk.Button(part1_2_tn, text='+Table', width=5, command=lambda: add_table())
    add_table_but.pack(side=tk.LEFT)

    delete_table_but = tk.Button(part1_2_tn, text='-Table', width=5, command=lambda: delete_table())
    delete_table_but.pack(side=tk.RIGHT)

    addorder = tk.Button(part1_2_ob, text='Add Order',height=1, width=10, command=lambda: orderobj.add_order())
    addorder.pack(side=tk.LEFT)

    deleteorder = tk.Button(part1_2_ob, text='Delete Order',height=1, width=10, command=lambda: orderobj.delete_order())
    deleteorder.pack(side=tk.RIGHT)

    return tree_productstab

if __name__ == "__main__":
    main()