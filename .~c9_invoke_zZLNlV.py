class Item:
    def __init__(self,name, price, category):
        if price<=0:
            raise ValueError(f"Invalid value for price, got {price}")
        if type(name)!=str:
            raise ValueError(f"Invalid value for name, got {type(name)}")
        if type(category)!=str:
            raise ValueError(f"Invalid value for category, got {type(category)}")
        self.name=name
        self.price=price
        self.category=category
    def ___str__(self):
        return '%s@%g-%s'%(self.name, self.price,self.category)
    
class Query:
    def __init__(self,field, operation, value):
        operations=['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        if operation not in operations:
            raise ValueError(f"Invalid value for operation, got {operation}")
        if type(field)!=str:
            raise ValueError(f"Invalid value for name, got {type(field)}")
        self.field=field
        self.operation=operation
        self.value=value
    def ___str__(self):
        return '%s %s %g'%(self.field, self.operation,self.value)

class Store(Item, Query):
    
    def __init__(self,value=None):
        if value is None or len(value)<=0:
            self.list=[]
        else:
            self.list=value
        

    def add_item(self,other):
        self.name=other.name
        self.price=other.price
        self.category=other.category
        self.list.append([other.name,other.price,other.category])
    def filter(self,other):
        self.n_list=[]
        if other.operation=="ENDS_WITH":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if self.list[j][0].endswith(other.value):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="price":
                    if str(self.list[j][1]).endswith(str(other.value)):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if self.list[j][2].endswith(other.value):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])           
                j=j+1
        elif other.operation=="STARTS_WITH":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if self.list[j][0].startswith(other.value):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="price":
                    if str(self.list[j][1]).startswith(str(other.value)):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if self.list[j][2].startswith(other.value):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                j=j+1
        elif other.operation=="EQ":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if self.list[j][0]==(other.value):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="price":
                    if self.list[j][1]==other.value:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])

                if str(other.field)=="category":
                    if self.list[j][2]==(other.value):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                j=j+1
            
        elif other.operation=="IN":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if (other.value) in self.list[j][0]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="price":
                    if str(other.value) in str(self.list[j][1]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if (other.value) in self.list[j][2]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])            
                j+=1
        elif other.operation=="CONTAINS":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if (other.value) in self.list[j][0]:
                       self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])                     
                if str(other.field)=="price":
                    if str(other.value) in str(self.list[j][1]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if (other.value) in self.list[j][2]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                j+=1
        elif other.operation=="LT":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if (other.value)>self.list[j][0]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if (other.field)=="price":
                    if str(other.value)>self.list[j][1]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])

                if str(other.field)=="category":
                    if (other.value)>self.list[j][2]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])                 
                j+=1
        elif other.operation=="GT":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if (other.value)<self.list[j][0]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])             
                if str(other.field)=="price":
                    if (other.value)<self.list[j][1]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if (other.value)<self.list[j][2]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])                     
                j+=1
        elif other.operation=="LTE":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if (other.value)>=self.list[j][1]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])               
                if str(other.field)=="price":
                    if (other.value)>=self.list[j][1]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])                 
                if str(other.field)=="category":
                    if (other.value)>=self.list[j][2]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                j+=1
        elif other.operation=="GTE":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if (other.value)<=self.list[j][0]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="price":
                    if (other.value)<=self.list[j][1]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if (other.value)<=self.list[j][2]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                j+=1
        return Store(self.n_list)
    def exclude(self,other):
        self.n_list=[]
        if (other.operation=="ENDS_WITH"):
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if not(self.list[j][0].endswith(other.value)):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="price":
                    if not(str(self.list[j][1]).endswith(str(other.value))):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if not(self.list[j][2].endswith(other.value)):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])           
                j=j+1
        elif (other.operation=="STARTS_WITH"):
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if not(self.list[j][0].startswith(other.value)):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="price":
                    if not(str(self.list[j][1]).startswith(str(other.value))):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if not(self.list[j][2].startswith(other.value)):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                j=j+1
        elif (other.operation=="EQ"):
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if (self.list[j][0]!=other.value):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="price":
                    if (self.list[j][1]!=other.value):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])

                if str(other.field)=="category":
                    if (self.list[j][2]!=other.value):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                j=j+1
            
        elif (other.operation=="IN"):
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if (other.value not in self.list[j][0]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="price":
                    if (str(other.value) not in str(self.list[j][1])):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if (other.value not in self.list[j][2]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])            
                j+=1
        elif (other.operation=="CONTAINS"):
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if (other.value not in self.list[j][0]):
                       self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])                     
                if str(other.field)=="price":
                    if (str(other.value) not in str(self.list[j][1])):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if (other.value not in self.list[j][2]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                j+=1
        elif (other.operation=="LT"):
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if not(other.value>self.list[j][0]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if (other.field)=="price":
                    if not((other.value)>self.list[j][1]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])

                if str(other.field)=="category":
                    if not(other.value>self.list[j][2]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])                 
                j+=1
        elif (other.operation=="GT"):
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if not(other.value<self.list[j][0]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])             
                if str(other.field)=="price":
                    if not(other.value<self.list[j][1]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if not(str(other.field)=="category"):
                    if (other.value)<self.list[j][2]:
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])                     
                j+=1
        elif other.operation=="LTE":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if not(other.value>=self.list[j][1]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])               
                if str(other.field)=="price":
                    if not((other.value)>=self.list[j][1]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])                 
                if str(other.field)=="category":
                    if not((other.value)>=self.list[j][2]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                j+=1
        elif other.operation=="GTE":
            j,counter=0,0
            while(j<len(self.list)):
                if str(other.field)=="name":
                    if not((other.value)<=self.list[j][0]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="price":
                    if not((other.value)<=self.list[j][1]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                if str(other.field)=="category":
                    if not((other.value)<=self.list[j][2]):
                        self.n_list.append([self.list[j][0],self.list[j][1],self.list[j][2]])
                j+=1
        return Store(self.n_list)
        
    def count(self):
        return len(self.list)
    
                    

    def __str__(self):
        if len(self.list)<=0:
            return "No items"
        else:
            self.list1=[]
            for i in range(len(self.list)):
                self.list1.append(f'{str(self.list[i][0])}@{str(self.list[i][1])}-{str(self.list[i][2])}')
            return '\n'.join(self.list1)
   
store = Store()
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item) 

item = Item(name="Oreo Biscuits", price=30, category="Foo")  
store.add_item(item)  

item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  

item = Item(name="Butter", price=10, category="Grocery")  
store.add_item(item)  
print(store)
print(store.count())
query = Query(field="name", operation="IN", value="cuits")  
result = store.filter(query)  
print(result)
print(result.count())

query = Query(field="price", operation="LT", value=30)  
results = result.exclude(query)
print(results)
print()
query = Query(field="price", operation="EQ", value=10)  
results = store.filter(query)


