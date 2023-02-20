import tkinter as tk 
from tkinter import ttk 
from tkcalendar import DateEntry
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from BL.financetab_bl import Financetab_bl

def main(nb):

    financetab = ttk.Frame(nb)
    financetab.pack()
    nb.add(financetab, text="Finance", underline=0)

    style = ttk.Style()
    style.configure("BW.TFrame", background="white",  relief="solid", bordercolor="black")

    calendarframe = ttk.Frame(financetab, borderwidth=10, style="BW.TFrame")
    calendarframe.pack(fill=tk.X)

    financetree_fr = ttk.Frame(financetab, borderwidth=10, style="BW.TFrame")
    financetree_fr.pack(fill=tk.X)

    graphframe = ttk.Frame(financetab, borderwidth=10, style="BW.TFrame")
    graphframe.pack(fill=tk.X)

    infoframe = ttk.Frame(financetree_fr, borderwidth=10, style="BW.TFrame")
    infoframe.pack(fill=tk.Y)

    info_change_fr = ttk.Frame(financetab, borderwidth=10, style="BW.TFrame")
    info_change_fr.pack(anchor=tk.CENTER,fill=tk.X)

    columns_tablegroup = ('Name','Count','Total')

    tree_finances = ttk.Treeview(financetree_fr, columns=columns_tablegroup, show='headings')
    tree_finances.pack()

    tree_finances.column("#1",anchor=tk.CENTER, width=150)
    tree_finances.column("#2",anchor=tk.CENTER, width=150)
    tree_finances.column("#3",anchor=tk.CENTER, width=150)

    tree_finances.heading('Name',anchor=tk.CENTER, text='Name')
    tree_finances.heading('Count',anchor=tk.CENTER, text='Count')
    tree_finances.heading('Total',anchor=tk.CENTER, text='Total')

    cal1=DateEntry(calendarframe,selectmode='day',date_pattern='yyyy-MM-dd')
    cal1.pack(pady=5,padx=75,side=tk.LEFT)

    start_time_var = tk.StringVar()
    start_time_combobox = ttk.Combobox(calendarframe, textvariable=start_time_var, values=["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "23:59"])
    start_time_combobox.current(0)
    start_time_combobox.pack(pady=5,padx=75,side=tk.LEFT)

    cal2=DateEntry(calendarframe,selectmode='day',date_pattern='yyyy-MM-dd')
    cal2.pack(pady=5,padx=75,side=tk.LEFT)

    end_time_var = tk.StringVar()
    end_time_combobox = ttk.Combobox(calendarframe, textvariable=end_time_var, values=["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "23:59"])
    end_time_combobox.current(24)
    end_time_combobox.pack(pady=5,padx=75,side=tk.LEFT)

    fig = Figure(figsize=(4, 2.25))
    ax = fig.add_subplot(111)
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Amount")
    ax.bar(0, 0)

    canvas = FigureCanvasTkAgg(fig, master=graphframe)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.X)

    # Create the Tkinter canvas to display the graph
    var = tk.StringVar(value='People')

    elements = ['People','Amount']
    dropdown = tk.OptionMenu(info_change_fr , var, *elements)
    dropdown.config(width=15 ,height=1,font=("Arial", 8), background="grey", activebackground="white")
    dropdown.pack()

    def option_menu(frame,var,liste):
        return tk.OptionMenu(frame, var, *liste)

    def insert_tree(tree,*args):
        tree.insert('', tk.END, values=(args))

    financeobj = Financetab_bl(start_time_var,end_time_var,cal1,cal2,tree_finances,
    ax,canvas,info_change_fr,var,dropdown,option_menu,insert_tree)

    cal1.bind("<<DateEntrySelected>>", financeobj.update_cal2)
    cal2.bind("<<DateEntrySelected>>")

    getproduct_btn = tk.Button(financetree_fr, text='Get Products Sum', width=20, command=lambda: financeobj.sold_products())
    getproduct_btn.pack(pady=5,padx=100,side=tk.LEFT)

    gettable_btn = tk.Button(financetree_fr, text='Get Tables Sum', width=20, command=lambda: financeobj.sold_tables())
    gettable_btn.pack(pady=5,padx=100,side=tk.LEFT)

    getuser_btn = tk.Button(financetree_fr, text='Get Users Sum', width=20, command=lambda: financeobj.sold_users())
    getuser_btn.pack(pady=5,padx=100,side=tk.RIGHT)

    getdaily_graph_btn = tk.Button(graphframe, text='Get Daily Graph', width=20, command=lambda: financeobj.daily_graph())
    getdaily_graph_btn.pack(pady=5,padx=100,side=tk.LEFT)

    getweekly_graph_btn = tk.Button(graphframe, text='Get Weekly Graph', width=20, command=lambda: financeobj.weekly_graph())
    getweekly_graph_btn.pack(pady=5,padx=100,side=tk.LEFT)

    getmonthly_graph_btn = tk.Button(graphframe, text='Get Montly Graph', width=20, command=lambda: financeobj.monthly_graph())
    getmonthly_graph_btn.pack(pady=5,padx=100,side=tk.RIGHT)

    financeobj.change_input_graph()

if __name__ == "__main__":
    main()