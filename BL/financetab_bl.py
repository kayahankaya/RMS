from DAL.Sql.Repository.ReportRepository import ReportRepository

class Financetab_bl:

    def __init__(self,*args):

        self.start_time_var = args[0]
        self.end_time_var = args[1]
        self.cal1 = args[2]
        self.cal2 = args[3]
        self.tree_finances = args[4]
        self.ax = args[5]
        self.canvas = args[6]
        self.info_change_fr = args[7]
        self.var = args[8]
        self.dropdown = args[9]
        self.option_menu = args[10]
        self.insert_tree = args[11]

    def get_date_for_table(self):

        time1 = self.start_time_var.get()+':00'
        time2 = self.end_time_var.get()+':00'
        date1 = str(self.cal1.get_date())
        date2 = str(self.cal2.get_date())

        self.tree_finances.delete(*self.tree_finances.get_children())

        return time1,time2,date1,date2

    def sold_products(self):
        
        time1,time2,date1,date2 = self.get_date_for_table()

        for i in ReportRepository().get_soldproduct_report(time1,time2,date1,date2):
            self.insert_tree(self.tree_finances,i[0],i[1],i[2])

    def sold_tables(self):

        time1,time2,date1,date2 = self.get_date_for_table()

        for i in ReportRepository().get_soldtables_report(time1,time2,date1,date2):
            self.insert_tree(self.tree_finances,i[0],i[1],i[2])

    def sold_users(self):

        time1,time2,date1,date2 = self.get_date_for_table() 

        for i in ReportRepository().get_solduser_report(time1,time2,date1,date2):
            self.insert_tree(self.tree_finances,i[0],i[1],i[2])

    def get_graph_input(self):

        self.ax.clear()
        amount_value = self.change_input_graph()

        date1 = str(self.cal1.get_date())
        date2 = str(self.cal2.get_date())

        return date1, date2, amount_value
    
    def set_graph_input(self,date_list,total_list):

        self.ax.bar(date_list, total_list)
        for i, v in enumerate(total_list):
            self.ax.text(i, v+2, str(v), ha='center')
        self.canvas.draw()
        self.ax.autoscale(enable=True, axis='both', tight=1)

    def daily_graph(self):

        date1, date2, amount_value = self.get_graph_input() 

        date_list, total_list = ReportRepository().daily_graph_report(date1,date2,amount_value)

        self.set_graph_input(date_list, total_list)

    def weekly_graph(self):

        date1, date2, amount_value = self.get_graph_input()

        date_list, total_list = ReportRepository().weekly_graph_report(date1,date2,amount_value)

        self.set_graph_input(date_list, total_list)

    def monthly_graph(self):

        date1, date2, amount_value = self.get_graph_input()     

        date_list, total_list = ReportRepository().monthly_graph_report(date1,date2,amount_value)

        self.set_graph_input(date_list, total_list)

    def update_cal2(self,event):
        selected_date = self.cal1.get_date()
        self.cal2.config(mindate=selected_date)

    def selected_element(self):

        return self.var

    def change_input_graph(self):
        self.dropdown.pack_forget()
        elements = ['People','Amount']
        self.dropdown = self.option_menu(self.info_change_fr,self.var,elements)
        self.dropdown.config(width=15 ,height=1,font=("Arial", 8), background="grey", activebackground="white")
        self.dropdown.pack()

        self.dropdown.bind("<<OptionMenuSelect>>", self.selected_element)

        return self.var.get()
     

 
        
    