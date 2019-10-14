from pymongo import MongoClient
class Mg:
    def __init__(self):
        self.con=MongoClient("mongodb://localhost:27017/")["book_metadata"]["metadata"]
  
    def get_all_info(self,param):
        a=self.con.find({"asin":param})
        ls=[]
        for i in a:
            ls.append(i)
        return ls
    
    def get_total(self):
        a=self.con.find().count()
        # print(a)
    
    def get_all_books(self, skip, category):
        if(category=="all"):
            param = {}
        else:
            param = {'categories':{'$elemMatch':{'$elemMatch':{'$in':[category]}}}}
        # print(param)
        a=self.con.find(param).limit(100).skip(100*(skip-1))
        # print(a)
        ls=[]
        for i in a:
            ls.append(i)
            
        return ls

    def get_all(self):
        a=self.con.distinct("asin")
        ls=[]
        for i in a:
            ls.append(i)
        return ls
    
    def get_category(self,param):
        p = {'categories':{'$elemMatch':{'$elemMatch':{'$in':[param]}}}}
        # print(p)
        a=self.con.find(p)
        # print(a)
        ls=[]
        for i in a:
            ls.append(i)
        return ls
    
    def get_sorted_title(self):
        pass

# print(Mg().get_all_books(1, "Solaris"))
# print(Mg().get_category("Solaris"))
