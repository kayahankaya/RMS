from DAL.Sql.Repository.OrderRepository import OrderRepository
from DAL.Sql.Repository.ProductRepository import ProductRepository
from DAL.Sql.Repository.BillRepository import BillRepository
from DAL.Sql.Repository.RecipeRepository import RecipeRepository
from DAL.Sql.Repository.StockRepository import StockRepository

class Order:

    radio_buttons = []

    table_number = OrderRepository().table_count()

    temp_list = []

    def __init__(self,*args):
        
        self.tree_tabletab = args[0]
        self.default_db = args[1]
        self.var = args[2]
        self.remainingcheck_entry = args[3]
        self.tree_productstab = args[4]
        self.checkentry_amount = args[5]
        self.pc_label_entry = args[6]
        self.tabletab = args[7]
        self.pop_up_table_first = args[8]
        self.pop_up_table_second = args[9]
        self.make_rbtn = args[10]
        self.ask_question = args[11]
        self.show_error = args[12]
        self.option_menu = args[13]
        self.decimal_price = args[14]
        self.entry_update = args[15]
        self.sel = args[16]

    def table_status_func(self,input):
        table_status =  BillRepository().get_bill_id_by_table_name(input)

        return table_status
                
    def on_select(self):

        return self.default_db

    def on_select2(self):

        return self.default_db_merge

    def set_productlist(self):

        liste = []

        list_products = ProductRepository().get_allproducts()

        for row in list_products:

            product_name = row[0]
            product_price = row[1]
            liste.append((product_name,product_price))

        return liste

    def table_list(self):

        liste = []

        selectedtable = self.var.get()

        order_products = OrderRepository().get_orders_of_current_table(selectedtable)

        for row in order_products:
            order_id = row[0]
            product_id = row[1]
            created_at = row[2]
            temp_product = ProductRepository().get_product_by_product_id(product_id)
            liste.append((order_id,temp_product.product_name,created_at,product_id))

        return liste

    def ordertable(self):

        liste = []

        result = []

        for row in self.table_list():
            product_id = row[-1]
            liste.append(product_id)   

        listunique = set(liste)
        new_list_dict = dict()

        for u in listunique:
        
            count = liste.count(u)
            new_list_dict[u] = count
            temp_product = ProductRepository().get_product_by_product_id(u)
            product_name, product_price = temp_product.product_name, temp_product.product_price
            total_product_price = float(product_price) * count
            result.append((u,product_name,product_price,count,total_product_price))

        result 
        
        return result

    def get_paid(self):
        selectedtable = self.var.get()
        mustpay_current = BillRepository().get_mustpay_by_table_name(selectedtable)
        temp_bill = BillRepository().get_paids_by_table_name(selectedtable)
        BillRepository().update_remain_check_by_tablename(selectedtable)
        remaining_check = BillRepository().select_remain_check_by_tablename(selectedtable)
        return (mustpay_current,temp_bill,remaining_check)
                

    def get_head_count(self):
        selectedtable = self.var.get()
        hc = int(BillRepository().get_head_count(selectedtable)[0])
        return hc

    def delete_order(self):

        if self.tree_tabletab.selection():

            temp_item = self.tree_tabletab.item(self.tree_tabletab.selection()[0])['values'][0]
            temp_product_id = OrderRepository().get_order_by_order_id(temp_item)
            ingredients_list = RecipeRepository().get_recipe_by_product_id(temp_product_id.product_id)
            temp_item_ = ProductRepository().get_product_by_product_id(temp_product_id.product_id)
            
            for ingredient in ingredients_list :
                stock_id_ingre = ingredient[1]
                stock_weight_ingre = int(ingredient[3])
                StockRepository().update_stock_by_stock_id_and_stock_weight(stock_weight_ingre,stock_id_ingre)
            OrderRepository().delete_order_by_order_id(temp_item)
            BillRepository().decrease_mustpay_by_order_id(temp_item_.product_price,temp_product_id.bill_id )
            self.sel()
            self.make_rbtn() 
            BillRepository().update_remain_check_by_tablename(self.var.get())
            if not OrderRepository().get_orders_of_current_table(self.var.get()):
                textvar1 = "Confirm"
                textvar2 = "Do you want to CLOSE Table " + str(self.var.get())
                answer = self.ask_question(textvar1,textvar2)
                if answer =='yes':
                    BillRepository().close_bill_by_table_name(self.var.get())
                self.make_rbtn() 

        else:
            textvar1 = 'Error by deleting order'
            textvar2 = 'There is no selected order. Please select a order first!'
            self.show_error(textvar1,textvar2,self.tabletab)

    def add_order(self):
        
        if self.tree_productstab.selection():
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
                decimal_number = self.decimal_price(selected_product_id.product_price)
                BillRepository().insert_mustpay_by_order_id(decimal_number,bill_id_toadd)
                self.sel()
        else:
            textvar1 = 'Error by adding order!'
            textvar2 = 'There is no selected order. Please select a product first!'
            self.show_error(textvar1,textvar2,self.tabletab)
            
    def update_table_repo(self):
        result = BillRepository().change_table_number(Order.table_number)
        return result

    def remain_table(self):

        remaining_check = BillRepository().select_remain_check_by_tablename(Order.table_number)
        return remaining_check

    def pay_bill(self):

        if self.displaySelectedItem():

            payby_cash, payby_cc, popup = self.pop_up_table_first(self.checkentry_amount.get(),self.remainingcheck_entry.get())

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
                    textvar1 = "Confirm"
                    textvar2 = "Do you want to CLOSE Table " + str(var1)
                    answer = self.ask_question(textvar1, textvar2)
                    if answer =='yes':
                        BillRepository().close_bill_by_table_name(var1)
                    self.make_rbtn()  

                payby_cash.delete(0, 'end')
                payby_cc.delete(0, 'end')

                for item in temp_list:
                    OrderRepository().update_orderstatus_paid_by_orderid(int(item))
                self.sel()

                popup.destroy()

            self.pop_up_table_second(popup,cc_cash)

            self.sel()
        else:

            textvar1 = "Confirm"
            textvar2 = "No selected product(s) to pay.\nDo you want to continue?"
            answer = self.ask_question(textvar1, textvar2)

            if answer =='yes':

                payby_cash,payby_cc, popup = self.pop_up_table_first(self.checkentry_amount.get(),self.remainingcheck_entry.get())

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
                        textvar1 = "Confirm"
                        textvar2 = "Do you want to CLOSE Table " + str(self.var.get())
                        answer =  self.ask_question(textvar1,textvar2)
                        if answer =='yes':
                            BillRepository().close_bill_by_table_name(var1)
                        self.make_rbtn() 

                    payby_cash.delete(0, 'end')
                    payby_cc.delete(0, 'end')

                    for item in temp_list:
                        OrderRepository().update_orderstatus_paid_by_orderid(int(item))
                    self.sel()

                    popup.destroy()
                    

                self.pop_up_table_second(popup,cc_cash)

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
            total_selected_price = total_selected_price + float(temp_product.product_price)

        self.entry_update(self.checkentry_amount,total_selected_price)

        return list_id

    def update_options2(self):

        options2 = []

        for table_name in range(1,(OrderRepository().table_count())+1):
            options2.append('Table '+str(table_name))
        
        dropdown_merge = self.option_menu(options2)
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
            textvar1 = "Confirm"
            textvar2 = "Do you want to CLOSE Table " + str(self.var.get())
            answer =  self.ask_question(textvar1,textvar2)
            if answer =='yes':
                BillRepository().close_bill_by_table_name(self.var.get()) 

        self.make_rbtn() 

    def head_count(self):

        bill_id = BillRepository().get_bill_id_by_table_name(self.var.get())
        BillRepository().set_head_count(int(self.pc_label_entry.get()) , bill_id)
        






