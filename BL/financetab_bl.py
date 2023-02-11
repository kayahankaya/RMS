import tkinter as tk 
import matplotlib
matplotlib.use("TkAgg")
from DAL.Sql.Repository.ReportRepository import ReportRepository

class Financetab_bl:
    def __init__(self,start_time_var,end_time_var,cal1,cal2,tree_finances,ax,canvas,info_change_fr,var,dropdown):

        self.start_time_var = start_time_var
        self.end_time_var = end_time_var
        self.cal1 = cal1
        self.cal2 = cal2
        self.tree_finances = tree_finances
        self.ax = ax
        self.canvas = canvas
        self.info_change_fr = info_change_fr
        self.var = var
        self.dropdown = dropdown

    def sold_products(self):
        
        time1 = self.start_time_var.get()+':00'
        time2 = self.end_time_var.get()+':00'
        date1 = str(self.cal1.get_date())
        date2 = str(self.cal2.get_date())

        self.tree_finances.delete(*self.tree_finances.get_children())

        for i in ReportRepository().get_soldproduct_report(time1,time2,date1,date2):
            self.tree_finances.insert('', tk.END, values=(i))

    def sold_tables(self):

        time1 = self.start_time_var.get()+':00'
        time2 = self.end_time_var.get()+':00'
        date1 = str(self.cal1.get_date())
        date2 = str(self.cal2.get_date())

        self.tree_finances.delete(*self.tree_finances.get_children())

        for i in ReportRepository().get_soldtables_report(time1,time2,date1,date2):
            self.tree_finances.insert('', tk.END, values=(i))

    def sold_users(self):
        
        time1 = self.start_time_var.get()+':00'
        time2 = self.end_time_var.get()+':00'
        date1 = str(self.cal1.get_date())
        date2 = str(self.cal2.get_date())
        
        self.tree_finances.delete(*self.tree_finances.get_children())

        for i in ReportRepository().get_solduser_report(time1,time2,date1,date2):
            self.tree_finances.insert('', tk.END, values=(i))

    def daily_graph(self):

        self.ax.clear()
        amount_value = self.change_input_graph()

        date1 = str(self.cal1.get_date())
        date2 = str(self.cal2.get_date())

        date_list, total_list = ReportRepository().daily_graph_report(date1,date2,amount_value)

        self.ax.bar(date_list, total_list)
        self.canvas.draw()
        self.ax.autoscale(enable=True, axis='both', tight=1)

    def weekly_graph(self):

        self.ax.clear()
        amount_value = self.change_input_graph()

        date1 = str(self.cal1.get_date())
        date2 = str(self.cal2.get_date())

        date_list, total_list = ReportRepository().weekly_graph_report(date1,date2,amount_value)

        self.ax.bar(date_list, total_list)
        self.canvas.draw()
        self.ax.autoscale(enable=True, axis='both', tight=1)

    def monthly_graph(self):

        self.ax.clear()
        amount_value = self.change_input_graph()

        date1 = str(self.cal1.get_date())
        date2 = str(self.cal2.get_date())

        date_list, total_list = ReportRepository().monthly_graph_report(date1,date2,amount_value)

        self.ax.bar(date_list, total_list)
        self.canvas.draw()
        self.ax.autoscale(enable=True, axis='both', tight=1)

    def update_cal2(self,event):
        selected_date = self.cal1.get_date()
        self.cal2.config(mindate=selected_date)


    def selected_element(self):

        return self.var

    def change_input_graph(self):
        self.dropdown.pack_forget()
        elements = ['People','Amount']
        self.dropdown = tk.OptionMenu(self.info_change_fr , self.var, *elements)
        self.dropdown.config(width=15 ,height=1,font=("Arial", 8), background="grey", activebackground="white")
        self.dropdown.pack()

        self.dropdown.bind("<<OptionMenuSelect>>", self.selected_element)

        return self.var.get()
     

 
        
    