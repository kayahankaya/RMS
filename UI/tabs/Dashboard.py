import tkinter as tk 
from tkinter import ttk
import UI.tabs.finance_tab as finance_tab
import UI.tabs.stock_tab as stock_tab
import UI.tabs.table_tab as table_tab

class Dashboard:

    def dash_admin(self):
        root = tk.Tk()
        root.title("RMS")

        nb = ttk.Notebook(root)
        nb.pack(pady=10, expand=True)
        
        var = table_tab.main(nb)
        stock_tab.main(nb,var)
        finance_tab.main(nb)

        root.mainloop()

    def dash_user(self):
        root = tk.Tk()
        root.title("RMS")

        nb = ttk.Notebook(root)
        nb.pack(pady=10, expand=True)

        finance_tab.main(nb)

        root.mainloop()







