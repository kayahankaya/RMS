import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
from BL.tabletab_bl import Order

def main(nb):

    tabletab1 = ttk.Frame(nb)
    tabletab1.pack(fill=tk.BOTH, expand=True)
    nb.add(tabletab1, text="Tables", underline=0)

    tabletab = tk.Frame(tabletab1)
    tabletab.pack()

    orderobj = Order()

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

    default_db_merge = tk.StringVar() 

    default_db = tk.StringVar(value='1')

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

    table_cat = tk.StringVar(value='Starters')

    part2_2 = tk.Frame(part2)
    part2_2.pack()

    def pay_popup(var1,var2):
        
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
        
        temp_list = displaySelectedItem()

        def cc_cash():

            payby_cash1 = payby_cash.get()
            payby_cc1 = payby_cc.get()
            var1 = var.get()

            orderobj.update_bill(var1,payby_cash1,payby_cc1)

            payby_cash_db , payby_cc_db = orderobj.get_paids_by_table_name(var1)
                    
            mustpay_check = orderobj.get_mustpay_by_table_name(var1)

            if ((payby_cash_db) + (payby_cc_db)) >= float(mustpay_check[0]):
                textvar1 = "Confirm"
                textvar2 = "Do you want to CLOSE Table " + str(var.get())
                answer = messagebox.askquestion(textvar1, textvar2)
                if answer =='yes':
                    orderobj.close_bill_by_table_name(var1)
                make_rbtn() 

            payby_cash.delete(0, 'end')
            payby_cc.delete(0, 'end')

            for item in temp_list:
                orderobj.update_orderstatus_paid_by_orderid(int(item))

            sel()

            popup.destroy()

        sel()

        button = tk.Button(popup, text="OK", command=cc_cash)
        button.grid(row=4, column=0, padx=2, pady=2,sticky='nsew')

        button2 = tk.Button(popup, text="Cancel", command=popup.destroy)
        button2.grid(row=4, column=1, padx=2, pady=2,sticky='nsew')
    
    def update_dropdown_table_cat():

        options = []

        for opt in orderobj.get_allcategory_of_products():
            options.append(opt[0])
        dropdown = tk.OptionMenu(part2_2, table_cat, *options)
        dropdown.config(width=15 ,height=1,font=("Arial", 8), background="grey", activebackground="white")
        dropdown.grid(row=0,column=0)

        return table_cat
        
    def update_ord_list():

        liste = []

        result = []

        t_liste = []

        selectedtable = var.get()

        order_products = orderobj.get_orders_of_current_table(selectedtable)

        for row in order_products:
            order_id = row[0]
            product_id = row[1]
            created_at = row[2]
            temp_product = orderobj.get_product_by_product_id(product_id)
            t_liste.append((order_id,temp_product.product_name,created_at,product_id))

        for row in t_liste:
            product_id = row[-1]
            liste.append(product_id)   

        listunique = set(liste)
        new_list_dict = dict()

        for u in listunique:
        
            count = liste.count(u)
            new_list_dict[u] = count
            temp_product = orderobj.get_product_by_product_id(u)
            product_name, product_price = temp_product.product_name, temp_product.product_price
            total_product_price = float(product_price) * count
            result.append((u,product_name,product_price,count,total_product_price))
            
        resultliste = result   

        tree_tablegroup.delete(*tree_tablegroup.get_children())
        for i in resultliste:
            u,product_name,product_price,count,total_product_price = i
            tree_tablegroup.insert('', tk.END, values=(u,product_name,product_price,count,total_product_price))

    def update_table_list():

            liste = []
            selectedtable = var.get()
            order_products = orderobj.get_orders_of_current_table(selectedtable)

            for row in order_products:
                order_id = row[0]
                product_id = row[1]
                created_at = row[2]
                temp_product = orderobj.get_product_by_product_id(product_id)
                liste.append((order_id,temp_product.product_name,created_at,product_id))
                
            tree_tabletab.delete(*tree_tabletab.get_children())

            for i in liste:
                order_id = i[0]
                product_name = i[1]
                created_at = i[2]
                tree_tabletab.insert('', tk.END, values=(order_id, product_name ,created_at))

    def update_pro_list(*args):

        tree_productstab.delete(*tree_productstab.get_children())
        liste = []
        cat = update_dropdown_table_cat()
        list_products = orderobj.get_allproducts_by_category(cat.get())

        for row in list_products:

            product_name = row[0]
            product_price = row[1]
            liste.append((product_name,product_price))

        for i in liste:
            product_name, product_price = i
            tree_productstab.insert('', tk.END, values=(product_name, product_price))

    def sel():

        update_table_list()
        selectedtable = var.get()
        selected = "You selected Table " + str(selectedtable)
        selectedlabel.config(text=selected)
        textvar_order = "Table " + str(selectedtable) +"'s Orders"
        order_label.config(text=textvar_order)
        update_ord_list()
        selectedtable = var.get()
        mustpay_current,temp_bill,remaining_check = orderobj.get_paid(selectedtable)


        if not mustpay_current:

            checkentry_wo_tax.delete(0, tk.END)
            checkentry_wo_tax.insert(0, 0.00)
        else:

            checkentry_wo_tax.delete(0, tk.END)
            checkentry_wo_tax.insert(0, mustpay_current)

        if temp_bill:

            (paidby_cash,paidby_cc) = temp_bill
            remaining_check_int = float(remaining_check[0])

            hc = orderobj.get_head_count(var.get())
            
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

    def on_select_howmany():

        return default_db
    
    def add_order():

        temp_value_tree = tree_productstab.item(tree_productstab.selection()[0])['values'][0]
    
        if tree_productstab.selection():
            selectedtable = var.get()
            howmany = int(on_select_howmany().get())
            orderobj.add_order_func(howmany,selectedtable,temp_value_tree)
            sel()
        else:
            textvar1 = 'Error by adding order!'
            textvar2 = 'There is no selected order. Please select a product first!'
            messagebox.showerror(textvar1,textvar2)
        make_rbtn()

    def delete_order():

        if tree_tabletab.selection():

            temp_item = tree_tabletab.item(tree_tabletab.selection()[0])['values'][0]
            orderobj.delete_order_func(temp_item)

            sel()
            make_rbtn() 
            orderobj.update_remain_check_by_tablename(var.get())

            if not orderobj.get_orders_of_current_table(var.get()):
                textvar1 = "Confirm"
                textvar2 = "Do you want to CLOSE Table " + str(var.get())
                answer = messagebox.askquestion(textvar1,textvar2)
                if answer =='yes':
                    orderobj.close_bill_by_table_name(var.get())
                make_rbtn() 
        else:
            textvar1 = 'Error by deleting order'
            textvar2 = 'There is no selected order. Please select a order first!'
            messagebox.showerror(textvar1,textvar2)

    def displaySelectedItem(*args):

        selectedItem = tree_tabletab.selection()
        total_selected_price = 0
        list_id = []

        for item in selectedItem:
            item_values = tree_tabletab.item(item)
            name = item_values['values'][1]
            list_id.append(item_values['values'][0])
            temp_product_price = orderobj.get_pro_price_by_product_name(name)
            total_selected_price = total_selected_price + float(temp_product_price)

        checkentry_amount.delete(0, tk.END)
        checkentry_amount.insert(0, total_selected_price)

        return list_id

    def pay_bill():

        if displaySelectedItem():
            pay_popup(checkentry_amount.get(),remainingcheck_entry.get())
        else:

            textvar1 = "Confirm"
            textvar2 = "No selected product(s) to pay.\nDo you want to continue?"
            answer = messagebox.askquestion(textvar1, textvar2)

            if answer =='yes':
                pay_popup(checkentry_amount.get(),remainingcheck_entry.get())

    def change_table():

        selectedItem = tree_tabletab.selection()
        next_table_raw = default_db_merge.get()
        next_table = int(next_table_raw.strip('Table '))

        bill_id_toadd = orderobj.get_bill_bytablename(next_table)
        current_bill = orderobj.get_bill_bytablename(var.get())

        if not bill_id_toadd:

            orderobj.insert_bill_bytablename(next_table)
            bill_id_toadd = orderobj.get_bill_bytablename(next_table)

        for item in selectedItem:
            item_values = tree_tabletab.item(item)
            order_id = item_values['values'][0]
            product_name = item_values['values'][1]
            orderobj.change_product_table(order_id,product_name,current_bill,bill_id_toadd)

        if not orderobj.get_orders_of_current_table(var.get()):
            textvar1 = "Confirm"
            textvar2 = "Do you want to CLOSE Table " + str(var.get())
            answer =  messagebox.askquestion(textvar1,textvar2)
            if answer =='yes':
                orderobj.close_bill_by_table_name(var.get()) 

        make_rbtn()
        sel()

    def on_select_table():

        return default_db_merge

    def update_options_table():

        options2 = []

        for table_name in range(1,(orderobj.table_count())+1):
            options2.append('Table '+str(table_name))
        
        dropdown_merge = tk.OptionMenu(part1_1_2, default_db_merge,*options2)
        dropdown_merge.config(height=1, width=5 ,font=("Arial", 8), background="lightblue", activebackground="white")
        dropdown_merge.grid(row=0,column=1)

        dropdown_merge.bind("<<OptionMenuSelect>>", on_select_table)

    def make_rbtn():

        for child in part1_2_rb.winfo_children():
            child.destroy()

        radio_buttons = []

        table_number = orderobj.table_count()
        column_table = 3
        row_table = table_number // column_table 
        last_row = table_number % column_table 
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
                radio_buttons.append(radio_button)
                radio_button.grid(row=k, column=i)

        return radio_buttons

    def add_table():
        table_number = orderobj.table_count()
        textvar1 = "Adding Table"
        textvar2 = f"Do you want to add Table {table_number + 1}?"
        answer = messagebox.askquestion(textvar1,textvar2)
        if answer == 'yes':
            table_number += 1
            orderobj.update_table_repo(table_number)
            make_rbtn()
            update_options_table()
            sel()
    
    def delete_table():
        table_number = orderobj.table_count()
        remaining_check = orderobj.remain_table()
        textvar1 = "Deleting Table"
        textvar2 = f"Do you want to delete Table {table_number}?"
        answer = messagebox.askquestion(textvar1,textvar2)
    
        if answer == 'yes':

            if remaining_check == 0.0 or remaining_check == None :
                if table_number > 0:
                    table_number -= 1
                    # loop through the radio_buttons list and destroy each one
                    radio_buttons = make_rbtn()
                    last_rb = radio_buttons[-1]
                    last_rb.destroy()
                    orderobj.update_table_repo(table_number)
                    make_rbtn()
                    sel()

            else:
                textvar1 = "Deleting Table"
                textvar2 = f"Orders in Table {table_number} should be pay or delete!\nYou cannot delete table which has orders"
                messagebox.showerror(textvar1, textvar2)
        update_options_table()

    transfer_table = tk.Button(part1_1_2, text='Transfer to >>>',height=1, width=15, command=lambda: change_table())
    transfer_table.grid(row=0,column=0)

    closetable = tk.Button(part4, text='Paid!',height=3, width=10, command=lambda: pay_bill())
    closetable.grid(row=6, column=0, columnspan=2,padx=7, pady=7,sticky='nsew')

    add_table_but = tk.Button(part1_2_tn, text='+Table', width=5, command=lambda: add_table())
    add_table_but.pack(side=tk.LEFT)

    delete_table_but = tk.Button(part1_2_tn, text='-Table', width=5, command=lambda: delete_table())
    delete_table_but.pack(side=tk.RIGHT)

    addorder = tk.Button(part1_2_ob, text='Add Order',height=1, width=10, command=lambda: add_order())
    addorder.pack(side=tk.LEFT)

    deleteorder = tk.Button(part1_2_ob, text='Delete Order',height=1, width=10, command=lambda: delete_order())
    deleteorder.pack(side=tk.RIGHT)

    table_cat.trace("w", update_pro_list)

    make_rbtn()

    update_pro_list()

    update_options_table()

    dropdown.bind("<<OptionMenuSelect>>", on_select_howmany)

    tree_tabletab.bind("<<TreeviewSelect>>", displaySelectedItem)

    return tree_productstab

if __name__ == "__main__":
    main()