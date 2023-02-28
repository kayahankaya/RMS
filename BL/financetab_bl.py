from DAL.Sql.Repository.ReportRepository import ReportRepository

class Financetab_bl:

    def get_soldproduct_report(self,time1,time2,date1,date2):
        return ReportRepository().get_soldproduct_report(time1,time2,date1,date2)
    
    def get_soldtables_report(self,time1,time2,date1,date2):
        return ReportRepository().get_soldtables_report(time1,time2,date1,date2)
    
    def get_solduser_report(self,time1,time2,date1,date2):
        return ReportRepository().get_solduser_report(time1,time2,date1,date2)
    
    def daily_graph_report(self,date1,date2,amount_value):
        return ReportRepository().daily_graph_report(date1,date2,amount_value)
    
    def weekly_graph_report(self,date1,date2,amount_value):
        return ReportRepository().weekly_graph_report(date1,date2,amount_value)
    
    def monthly_graph_report(self,date1,date2,amount_value):
        return ReportRepository().monthly_graph_report(date1,date2,amount_value)


 
        
    