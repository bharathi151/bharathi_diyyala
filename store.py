class Item:
    
    def __init__(self,name, price, category):
        if price<=0:raise ValueError(f"Invalid value for price, got {price}")
        self._name,self._price,self._category=name, price, category
    
    def __str__(self):return f'{self._name}@{self._price}-{self._category}' 

class Query:
    
    _operations=["IN","EQ","GT","GTE","LT","LTE","STARTS_WITH","ENDS_WITH","CONTAINS"]
    
    def __init__(self,field, operation, value):
        if operation not in type(self)._operations:raise ValueError(f"Invalid value for operation, got {operation}")
        self._field,self._operation,self._value=field, operation, value
    
    def __str__(self):return f'{self._field} {self._operation} {self._value}'

class Store:
   
    def __init__(self,list=None):
        if list is None or len(list)<=0:self._list=[]
        else:self._list=list
        
    def add_item(self,item):self._list.append([item._name,item._price,item._category])
    
    def count(self):return len(self._list)
    
    def filter(self,query):
        _temp_list=[]
        if query._operation=="STARTS_WITH":
            for i in range(len(self._list)):
                if query._field=="name" and (self._list[i][0].startswith(query._value)):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="category" and (self._list[i][2].startswith(query._value)):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="ENDS_WITH":
            for i in range(len(self._list)):
                if query._field=="name" and (self._list[i][0].endswith(query._value)):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="category" and self._list[i][2].endswith(query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="EQ":
            for i in range(len(self._list)):
                if query._field=="name" and (self._list[i][0]==query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="price" and (self._list[i][1]==query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="category" and (self._list[i][2]==query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="LT":
            for i in range(len(self._list)):
                if query._field=="price" and (self._list[i][1]<query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="GT":
            for i in range(len(self._list)):
                if query._field=="price" and (self._list[i][1]>query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="LTE":
            for i in range(len(self._list)):
                if query._field=="price" and (self._list[i][1]<=query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="GTE":
            for i in range(len(self._list)):
                if query._field=="price" and (self._list[i][1]>=query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="CONTAINS":
            for i in range(len(self._list)):
                if query._field=="name" and ((query._value in self._list[i][0])):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="category" and (query._value in self._list[i][2]):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])  
        elif query._operation=="IN":
            for i in range(len(self._list)):
                if query._field=="name" and (self._list[i][0] in query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="price" and (self._list[i][1] in query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="category" and (self._list[i][2] in query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        return Store(_temp_list)
    
    def exclude(self,query):
        _temp_list=[]
        if query._operation=="STARTS_WITH":
            for i in range(len(self._list)):
                if query._field=="name" and not (self._list[i][0].startswith(query._value)):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="category" and not (self._list[i][2].startswith(query._value)):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="ENDS_WITH":
            for i in range(len(self._list)):
                if query._field=="name" and not (self._list[i][0].endswith(query._value)):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="category" and not (self._list[i][2].endswith(query._value)):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="EQ":
            for i in range(len(self._list)):
                if query._field=="name" and (self._list[i][0]!=query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="price" and (self._list[i][1]!=query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="category" and (self._list[i][2]!=query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="LT":
            for i in range(len(self._list)):
                if query._field=="price" and not (self._list[i][1]<query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="GT":
            for i in range(len(self._list)):
                if query._field=="price" and not (self._list[i][1]>query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="LTE":
            for i in range(len(self._list)):
                if query._field=="price" and not (self._list[i][1]<=query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="GTE":
            for i in range(len(self._list)):
                if query._field=="price" and not (self._list[i][1]>=query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        elif query._operation=="CONTAINS":
            for i in range(len(self._list)):
                if query._field=="name" and  ((query._value not in self._list[i][0])):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="category" and (query._value not in self._list[i][2]):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])  
        elif query._operation=="IN":
            for i in range(len(self._list)):
                if query._field=="name" and (self._list[i][0] not in query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="price" and (self._list[i][1] not in query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
                if query._field=="category" and (self._list[i][2] not in query._value):
                    _temp_list.append([self._list[i][0],self._list[i][1],self._list[i][2]])
        return Store(_temp_list)
    
    def __str__(self):
        _new_list=[]
        if len(self._list)<=0:return "No items"
        else:
            for i in range(len(self._list)):
                _new_list.append(f'{self._list[i][0]}@{self._list[i][1]}-{self._list[i][2]}')
        return "\n".join(_new_list)
    
# store = Store()
# item = Item(name="Oreo Biscuits", price=30, category="Food")  
# store.add_item(item) 
# item = Item(name="Oreo Biscuits", price=15, category="Foo")  
# store.add_item(item)  

# item = Item(name="Boost Biscuits", price=20, category="Food")  
# store.add_item(item)  

# item = Item(name="Butter", price=10, category="Grocery")  
# store.add_item(item)  
# print(store)

# print(store.count())
# query = Query(field="name", operation="ENDS_WITH", value="cuits")
# print(query)
# result = store.filter(query)  
# print(result)
# print(result.count())
# query = Query(field="price", operation="GT", value=30) 
# query1 = Query(field="price", operation="EQ", value=20)  
# print(f'{query}{query1}')
# results = result.exclude(query)
# print(results)
# print(results.count())
# query = Query(field="price", operation="EQ", value=20)  
# results = results.filter(query)
# print(results)
# print(results.count())