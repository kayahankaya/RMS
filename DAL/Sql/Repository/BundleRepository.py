import DAL.Sql.Db.DbManager as DbManager
from DAL.Sql.Db.Entities.BundleEntity import BundleEntity

class BundleRepository:

    def __init__(self):

        self.dbcontext = DbManager.getdbbcon()

    def get_bundle_by_bundle_id(self,bundle_id):

        cur = self.dbcontext.cursor()
        cur.execute("select * from bundles where bundle_id=%s",(bundle_id))
        row = cur.fetchone()
        
        temp_bundle = BundleEntity()

        temp_bundle.bundle_id = row[0]
        temp_bundle.product_id = row[1]
        temp_bundle.bundle_name = row[2]
        temp_bundle.element_1 = row[3]
        temp_bundle.element_2 = row[4]
        temp_bundle.element_3 = row[5]
        temp_bundle.element_4 = row[6]
        temp_bundle.element_5 = row[7]
        temp_bundle.element_6 = row[8]
        temp_bundle.element_7 = row[9]
        temp_bundle.element_8 = row[10]
        temp_bundle.element_9 = row[11]
        temp_bundle.element_10 = row[12]
        temp_bundle.created_at = row[13]
        temp_bundle.updated_at = row[14]

        return temp_bundle

    def get_bundle_by_product_id(self,product_id):

        cur = self.dbcontext.cursor()
        cur.execute("select * from bundles where product_id=%s",(product_id))
        row = cur.fetchone()
        
        temp_bundle = BundleEntity()

        temp_bundle.bundle_id = row[0]
        temp_bundle.product_id = row[1]
        temp_bundle.bundle_name = row[2]
        temp_bundle.element_1 = row[3]
        temp_bundle.element_2 = row[4]
        temp_bundle.element_3 = row[5]
        temp_bundle.element_4 = row[6]
        temp_bundle.element_5 = row[7]
        temp_bundle.element_6 = row[8]
        temp_bundle.element_7 = row[9]
        temp_bundle.element_8 = row[10]
        temp_bundle.element_9 = row[11]
        temp_bundle.element_10 = row[12]
        temp_bundle.created_at = row[13]
        temp_bundle.updated_at = row[14]

        return temp_bundle

    def get_bundle_by_bundle_name(self,bundle_name):

        cur = self.dbcontext.cursor()
        cur.execute("select * from bundles where product_id=%s",(bundle_name))
        row = cur.fetchone()
        
        temp_bundle = BundleEntity()

        temp_bundle.bundle_id = row[0]
        temp_bundle.product_id = row[1]
        temp_bundle.bundle_name = row[2]
        temp_bundle.element_1 = row[3]
        temp_bundle.element_2 = row[4]
        temp_bundle.element_3 = row[5]
        temp_bundle.element_4 = row[6]
        temp_bundle.element_5 = row[7]
        temp_bundle.element_6 = row[8]
        temp_bundle.element_7 = row[9]
        temp_bundle.element_8 = row[10]
        temp_bundle.element_9 = row[11]
        temp_bundle.element_10 = row[12]
        temp_bundle.created_at = row[13]
        temp_bundle.updated_at = row[14]

        return temp_bundle





            

        


