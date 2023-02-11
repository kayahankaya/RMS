import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
from DAL.Sql.Repository.OrderRepository import OrderRepository
from DAL.Sql.Repository.ProductRepository import ProductRepository
from DAL.Sql.Repository.BillRepository import BillRepository
from DAL.Sql.Repository.RecipeRepository import RecipeRepository
from DAL.Sql.Repository.StockRepository import StockRepository
from decimal import Decimal

class Order:

    radio_buttons = []

    table_number = OrderRepository().table_count()

    temp_list = []
    
    def __init__(self, tree_tabletab, default_db, var,selectedlabel,order_label,part3,checkentry_wo_tax,paidbycheck_ent,paidbycc_label_entry,remainingcheck_entry,tree_productstab,checkentry_amount,part1_2_rb,list_products,part1_1_2,pc_label_entry_var,pc_label_entry):
        
        self.tree_tabletab = tree_tabletab
        self.default_db = default_db
        self.selectedlabel = selectedlabel
        self.var = var
        self.order_label = order_label
        self.part3 = part3
        self.checkentry_wo_tax = checkentry_wo_tax
        self.paidbycheck_ent = paidbycheck_ent
        self.paidbycc_label_entry = paidbycc_label_entry
        self.remainingcheck_entry = remainingcheck_entry
        self.tree_productstab = tree_productstab
        self.checkentry_amount = checkentry_amount
        self.part1_2_rb = part1_2_rb
        self.list_products = list_products
        self.part1_1_2 = part1_1_2
        self.pc_label_entry_var = pc_label_entry_var
        self.pc_label_entry = pc_label_entry

    def fillcolumn(self,*args):

        order_id,product_id,created_at = args
        temp_product = ProductRepository().get_product_by_product_id(product_id)
        self.product_name,self.product_price = temp_product.product_name, temp_product.product_price

        self.tree_tabletab.insert('', tk.END, values=(order_id,self.product_name, created_at))
    
    def fillproductlist(self):

        for row in self.list_products:
            self.product_name = row[0]
            self.product_price = row[1]
            self.tree_productstab.insert('', tk.END, values=(self.product_name, self.product_price))

    def on_select(self):

        return self.default_db

    def on_select2(self):

        return self.default_db_merge

    def sel(self):
        
        selectedtable = self.var.get()
        self.tree_tabletab.delete(*self.tree_tabletab.get_children())

        selected = "You selected Table " + str(selectedtable)
        self.selectedlabel.config(text=selected)

        textvar_order = "Table " + str(selectedtable) +"'s Orders"
        self.order_label.config(text=textvar_order)



        list = []
        
        order_products = OrderRepository().get_orders_of_current_table(selectedtable)

        for row in order_products:
            order_id = row[0]
            product_id= row[1]
            created_at = row[2]
            self.fillcolumn(order_id,product_id,created_at)
            list.append(product_id)   

        listunique = set(list)
        new_list_dict = dict()

        tablegroup_label = tk.Label(self.part3,text="""-- Order Details--""")
        tablegroup_label.grid(row=0, column=0,pady=7,padx=7)

        columns_tablegroup = ('product_id','product_name','product_price', 'quantity','total_product_price')

        tree_tablegroup = ttk.Treeview(self.part3, columns=columns_tablegroup , show='headings')
        tree_tablegroup.grid(row=1, column=0, pady=7,padx=7)

        tree_tablegroup.column("#1", width=145)
        tree_tablegroup.column("#2", width=145)
        tree_tablegroup.column("#3", width=145)
        tree_tablegroup.column("#4", width=145)
        tree_tablegroup.column("#5", width=145)

        tree_tablegroup.heading('product_id',anchor=tk.CENTER, text='Product ID')
        tree_tablegroup.heading('product_name',anchor=tk.CENTER, text='Product Name')
        tree_tablegroup.heading('product_price',anchor=tk.CENTER, text='Product Price')
        tree_tablegroup.heading('quantity',anchor=tk.CENTER, text='Quantity')
        tree_tablegroup.heading('total_product_price',anchor=tk.CENTER, text='Sub Total')

        for u in listunique:
        
            count = list.count(u)
            new_list_dict[u] = count
            temp_product = ProductRepository().get_product_by_product_id(u)
            product_name, product_price = temp_product.product_name, temp_product.product_price
            total_product_price = int(product_price) * count
            tree_tablegroup.insert('', tk.END, values=(u,product_name, product_price,count,total_product_price))

        mustpay_current = BillRepository().get_mustpay_by_table_name(selectedtable)
        if not mustpay_current:
            self.checkentry_wo_tax.delete(0, tk.END)
            self.checkentry_wo_tax.insert(0, 0.00)
        else:
            self.checkentry_wo_tax.delete(0, tk.END)
            self.checkentry_wo_tax.insert(0, mustpay_current)

        temp_bill = BillRepository().get_paids_by_table_name(selectedtable)
        BillRepository().update_remain_check_by_tablename(selectedtable)

        if temp_bill:
            (paidby_cash,paidby_cc) = temp_bill
            remaining_check = BillRepository().select_remain_check_by_tablename(selectedtable)
            remaining_check_int = float(remaining_check[0])

            hc = int(BillRepository().get_head_count(selectedtable)[0])
            self.pc_label_entry.delete(0, tk.END)
            self.pc_label_entry.insert(0, hc)
        else:
            (paidby_cash,paidby_cc) = (0.00,0.00)
            remaining_check_int = 0.00

        self.paidbycheck_ent.delete(0, tk.END)
        self.paidbycheck_ent.insert(0, paidby_cash)

        self.paidbycc_label_entry.delete(0, tk.END)
        self.paidbycc_label_entry.insert(0, paidby_cc)

        self.remainingcheck_entry.delete(0, tk.END)
        self.remainingcheck_entry.insert(0, remaining_check_int)



    def delete_order(self):
        
        temp_item = self.tree_tabletab.item(self.tree_tabletab.selection()[0])['values'][0]
        temp_product_id = OrderRepository().get_order_by_order_id(temp_item)
        ingredients_list = RecipeRepository().get_recipe_by_product_id(temp_product_id.product_id)
        for ingredient in ingredients_list :
            stock_id_ingre = ingredient[1]
            stock_weight_ingre = int(ingredient[3])
            StockRepository().update_stock_by_stock_id_and_stock_weight(stock_weight_ingre,stock_id_ingre)
        OrderRepository().delete_order_by_order_id(temp_item)
        self.sel()
        self.make_rbtn()
        BillRepository().update_remain_check_by_tablename(self.var.get())
        if not OrderRepository().get_orders_of_current_table(self.var.get()):
            answer = messagebox.askquestion("Confirm","Do you want to CLOSE Table " + str(self.var.get()))
            if answer =='yes':
                BillRepository().close_bill_by_table_name(self.var.get())
            self.make_rbtn() 

    def add_order(self):

        selectedtable = self.var.get()
        howmany = int(self.on_select().get())

        self.head_count()

        for _ in range(howmany):

            bill_id_toadd = BillRepository().get_bill_id_by_table_name(selectedtable)

            if not bill_id_toadd:

                BillRepository().insert_table_name_to_bill(selectedtable)
                bill_id_toadd = BillRepository().get_bill_id_by_table_name(selectedtable)

            temp_value_tree = self.tree_productstab.item(self.tree_productstab.selection()[0])['values'][0]

            selected_product_id = ProductRepository().get_product_by_product_name(temp_value_tree)
            selected = selected_product_id.product_id
            ingredients_list = RecipeRepository().get_recipe_by_product_id(selected)
            for ingredient in ingredients_list :
                stock_id_ingre = ingredient[1]
                stock_weight_ingre = int(ingredient[3])
                StockRepository().drop_stock_by_stock_id(stock_id_ingre,stock_weight_ingre)
            OrderRepository().insert_order_by_product_id_and_bill_id(bill_id_toadd, selected)
            decimal_number = Decimal(selected_product_id.product_price).quantize(Decimal('0.00'))
            BillRepository().insert_mustpay_by_order_id(decimal_number,bill_id_toadd)
            self.sel()
            self.make_rbtn()
            

    def make_rbtn(self):

        column_table = 3
        row_table = Order.table_number // column_table # 3
        last_row = Order.table_number % column_table # 0
        if last_row >= 1:
            row_table += 1
        for k in range(0,row_table): #k 0 1 2 3 row
            if k == (row_table-1): 
                if last_row >= 1:
                    column_table = last_row      
            for i in range(1,(column_table+1)):
                input = i+3*k
                textinput = "Table "+str(input)
                radio_button = tk.Radiobutton(self.part1_2_rb, text=textinput, variable=self.var, value=input, width = 8 , command = self.sel)
                table_status =  BillRepository().get_bill_id_by_table_name(input)
                radio_button.configure(bg='green')
                if table_status:
                    radio_button.configure(bg='red')
                self.radio_buttons.append(radio_button)
                radio_button.grid(row=k, column=i)

    def add_table(self):

        Order.table_number += 1
        BillRepository().change_table_number(Order.table_number)
        self.make_rbtn()
        self.update_options2()

    def delete_table(self):

        if Order.table_number > 0:
            Order.table_number -= 1
            # loop through the radio_buttons list and destroy each one
            for rb in Order.radio_buttons:
                rb.destroy()
            BillRepository().change_table_number(Order.table_number)
            self.make_rbtn()
            self.update_options2()

    def pay_bill(self):

        if self.displaySelectedItem():
            popup = tk.Toplevel()
            popup.title("PopUp")

            info_text = tk.Label(popup,text="Selected Amount = " + str(self.checkentry_amount.get()))
            info_text.grid(row=0, column=0, columnspan=2,padx=2, pady=2)

            info_text_total = tk.Label(popup,text="Total Remaining Amount = " + str(self.remainingcheck_entry.get()))
            info_text_total.grid(row=1, column=0, columnspan=2,padx=2, pady=2)

            payby_label1 = tk.Label(popup,text="Cash =")
            payby_label1.grid(row=2, column=0, padx=2, pady=2,sticky='w')

            payby_label2 = tk.Label(popup,text="Credit Card =")
            payby_label2.grid(row=3, column=0, padx=2, pady=2,sticky='w')

            payby_cash = tk.Entry(popup, width=10)
            payby_cash.grid(row=2, column=1, padx=2, pady=2,sticky='nsew')

            payby_cc = tk.Entry(popup, width=10)
            payby_cc.grid(row=3, column=1, padx=2, pady=2,sticky='nsew')

            temp_list = self.displaySelectedItem()

            def cc_cash():
                payby_cash1 = payby_cash.get()
                payby_cc1 = payby_cc.get()
                var1 = self.var.get()

                BillRepository().update_change_by_paidcash_and_table_name(payby_cash1,var1)
                BillRepository().update_change_by_paidcc_and_table_name(payby_cc1,var1)

                payby_cash_db , payby_cc_db = BillRepository().get_paids_by_table_name(var1)
                        
                mustpay_check = BillRepository().get_mustpay_by_table_name(var1)

                if ((payby_cash_db) + (payby_cc_db)) >= float(mustpay_check[0]):

                    answer = messagebox.askquestion("Confirm","Do you want to CLOSE Table " + str(var1))
                    if answer =='yes':
                        BillRepository().close_bill_by_table_name(var1)
                    self.make_rbtn() 
                payby_cash.delete(0, tk.END)
                payby_cc.delete(0, tk.END)

                for item in temp_list:
                    OrderRepository().update_orderstatus_paid_by_orderid(int(item))
                self.sel()

                popup.destroy()

            button = tk.Button(popup, text="OK", command=cc_cash)
            button.grid(row=4, column=0, padx=2, pady=2,sticky='nsew')

            button2 = tk.Button(popup, text="Cancel", command=popup.destroy)
            button2.grid(row=4, column=1, padx=2, pady=2,sticky='nsew')

            self.sel()
        else:
            answer2 = messagebox.askquestion("Confirm", "No selected product(s) to pay.\nDo you want to continue?")
            if answer2 =='yes':
                popup = tk.Toplevel()
                popup.title("PopUp")

                info_text = tk.Label(popup,text="Selected Amount = " + str(self.checkentry_amount.get()))
                info_text.grid(row=0, column=0, columnspan=2,padx=2, pady=2)

                info_text_total = tk.Label(popup,text="Total Remaining Amount = " + str(self.remainingcheck_entry.get()))
                info_text_total.grid(row=1, column=0, columnspan=2,padx=2, pady=2)

                payby_label1 = tk.Label(popup,text="Cash =")
                payby_label1.grid(row=2, column=0, padx=2, pady=2,sticky='w')

                payby_label2 = tk.Label(popup,text="Credit Card =")
                payby_label2.grid(row=3, column=0, padx=2, pady=2,sticky='w')

                payby_cash = tk.Entry(popup, width=10)
                payby_cash.grid(row=2, column=1, padx=2, pady=2,sticky='nsew')

                payby_cc = tk.Entry(popup, width=10)
                payby_cc.grid(row=3, column=1, padx=2, pady=2,sticky='nsew')

                temp_list = self.displaySelectedItem()

                def cc_cash():
                    payby_cash1 = payby_cash.get()
                    payby_cc1 = payby_cc.get()
                    var1 = self.var.get()

                    BillRepository().update_change_by_paidcash_and_table_name(payby_cash1,var1)
                    BillRepository().update_change_by_paidcc_and_table_name(payby_cc1,var1)

                    payby_cash_db , payby_cc_db = BillRepository().get_paids_by_table_name(var1)
                            
                    mustpay_check = BillRepository().get_mustpay_by_table_name(var1)

                    if ((payby_cash_db) + (payby_cc_db)) >= float(mustpay_check[0]):

                        answer = messagebox.askquestion("Confirm","Do you want to CLOSE Table " + str(var1))
                        if answer =='yes':
                            BillRepository().close_bill_by_table_name(var1)
                        self.make_rbtn() 
                    payby_cash.delete(0, tk.END)
                    payby_cc.delete(0, tk.END)

                    for item in temp_list:
                        OrderRepository().update_orderstatus_paid_by_orderid(int(item))
                    self.sel()

                    popup.destroy()

                button = tk.Button(popup, text="OK", command=cc_cash)
                button.grid(row=4, column=0, padx=2, pady=2,sticky='nsew')

                button2 = tk.Button(popup, text="Cancel", command=popup.destroy)
                button2.grid(row=4, column=1, padx=2, pady=2,sticky='nsew')

                self.sel()


    def displaySelectedItem(self,*args):
        selectedItem = self.tree_tabletab.selection()
        total_selected_price = 0
        list_id = []

        for item in selectedItem:
            item_values = self.tree_tabletab.item(item)
            name = item_values['values'][1]
            list_id.append(item_values['values'][0])
            temp_product = ProductRepository().get_product_by_product_name(name)
            total_selected_price = total_selected_price + int(temp_product.product_price)

        self.checkentry_amount.delete(0, tk.END)
        self.checkentry_amount.insert(0, total_selected_price)

        return list_id

    def update_options2(self):

        options2 = []

        for table_name in range(1,(OrderRepository().table_count())+1):
            options2.append('Table '+str(table_name))

        self.default_db_merge = tk.StringVar(value='Table 1') 

        dropdown_merge = tk.OptionMenu(self.part1_1_2, self.default_db_merge, *options2)
        dropdown_merge.config(height=1, width=5 ,font=("Arial", 8), background="lightblue", activebackground="white")
        dropdown_merge.grid(row=0,column=1)

        dropdown_merge.bind("<<OptionMenuSelect>>", self.on_select2)
     

    def change_table(self):

        selectedItem = self.tree_tabletab.selection()
        next_table_raw = self.default_db_merge.get()
        next_table = int(next_table_raw.strip('Table '))

        bill_id_toadd = BillRepository().get_bill_id_by_table_name(next_table)
        current_bill = BillRepository().get_bill_id_by_table_name(self.var.get())

        if not bill_id_toadd:

            BillRepository().insert_table_name_to_bill(next_table)
            bill_id_toadd = BillRepository().get_bill_id_by_table_name(next_table)

        for item in selectedItem:
            item_values = self.tree_tabletab.item(item)
            order_id = item_values['values'][0]
            product_name = item_values['values'][1]
            temp_product = ProductRepository().get_product_by_product_name(product_name)
            OrderRepository().change_bill_by_order_id(bill_id_toadd,order_id)
            BillRepository().decrease_mustpay_by_order_id(temp_product.product_price,current_bill)
            BillRepository().insert_mustpay_by_order_id(temp_product.product_price,bill_id_toadd)

        if not OrderRepository().get_orders_of_current_table(self.var.get()):
            answer = messagebox.askquestion("Confirm","Do you want to CLOSE Table " + str(self.var.get()))
            if answer =='yes':
                BillRepository().close_bill_by_table_name(self.var.get()) 
        self.make_rbtn()
        self.sel()

    def head_count(self):

        bill_id = BillRepository().get_bill_id_by_table_name(self.var.get())
        BillRepository().set_head_count(int(self.pc_label_entry.get()) , bill_id)
        






