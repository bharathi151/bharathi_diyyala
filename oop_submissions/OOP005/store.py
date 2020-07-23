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
    def filter(self,*args):
        temp_list=self.list
        for i in args:
            self.n_list=[]
            if i.operation=="ENDS_WITH":
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and temp_list[j][0].endswith(i.value):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="price" and str(temp_list[j][1]).endswith(str(i.value)):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and temp_list[j][2].endswith(i.value):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])         
            elif i.operation=="STARTS_WITH":
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and temp_list[j][0].startswith(i.value):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="price" and str(temp_list[j][1]).startswith(str(i.value)):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and temp_list[j][2].startswith(i.value):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
            elif i.operation=="EQ":
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and temp_list[j][0]==(i.value):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="price" and temp_list[j][1]==i.value:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and temp_list[j][2]==(i.value):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
            elif i.operation=="IN" or i.operation=="CONTAINS":
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (i.value) in temp_list[j][0]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="price" and str(i.value) in str(temp_list[j][1]):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and (i.value) in temp_list[j][2]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])        
            elif i.operation=="LT":
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (i.value)>temp_list[j][0]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if (i.field)=="price" and (i.value)>temp_list[j][1]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and (i.value)>temp_list[j][2]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])               
            elif i.operation=="GT":
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (i.value)<temp_list[j][0]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])             
                    if (i.field)=="price" and (i.value)<temp_list[j][1]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and (i.value)<temp_list[j][2]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])                     
            elif i.operation=="LTE":
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (i.value)>=temp_list[j][1]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])              
                    if (i.field)=="price" and (i.value)>=temp_list[j][1]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])                
                    if str(i.field)=="category" and (i.value)>=temp_list[j][2]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
            elif i.operation=="GTE":
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (i.value)<=temp_list[j][0]:self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if (i.field)=="price" and (i.value)<=temp_list[j][1]: self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and (i.value)<=temp_list[j][2]:self.n_list.append([temp_list[j][0],temp_list[j][1],self.list[j][2]])
            temp_list=self.n_list
        return Store(temp_list)
        
    def exclude(self,*args):
        temp_list=self.list
        for i in args:
            self.n_list=[]
            if (i.operation=="ENDS_WITH"):
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (not(temp_list[j][0].endswith(i.value))):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="price" and (not(str(temp_list[j][1]).endswith(str(i.value)))):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and (not(temp_list[j][2].endswith(i.value))):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])           
            elif (i.operation=="STARTS_WITH"):
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (not(temp_list[j][0].startswith(i.value))):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="price" and (not(str(temp_list[j][1]).startswith(str(i.value)))):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and (not(temp_list[j][2].startswith(i.value))):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
            elif (i.operation=="EQ"):
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (temp_list[j][0]!=i.value):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="price" and (temp_list[j][1]!=i.value):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and (temp_list[j][2]!=i.value):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
            elif (i.operation=="IN")or (i.operation=="CONTAINS") :
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (i.value not in temp_list[j][0]):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="price" and (str(i.value) not in str(temp_list[j][1])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and (i.value not in temp_list[j][2]):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])           
            elif (i.operation=="LT"):
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (not(i.value>temp_list[j][0])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if (i.field)=="price" and (not((i.value)>temp_list[j][1])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and (not(i.value>temp_list[j][2])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])                
            elif (i.operation=="GT"):
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (not(i.value<temp_list[j][0])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])             
                    if str(i.field)=="price" and (not(i.value<temp_list[j][1])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if (str(i.field)=="category") and (not(i.value<temp_list[j][2])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])                     
            elif i.operation=="LTE":
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (not(i.value>=temp_list[j][1])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])               
                    if str(i.field)=="price" and (not((i.value)>=temp_list[j][1])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])                 
                    if str(i.field)=="category" and (not((i.value)>=temp_list[j][2])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
            elif i.operation=="GTE":
                for j in range(len(temp_list)):
                    if str(i.field)=="name" and (not((i.value)<=temp_list[j][0])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="price" and (not((i.value)<=temp_list[j][1])):self.n_list.append([temp_list[j][0],temp_list[j][1],temp_list[j][2]])
                    if str(i.field)=="category" and (not((i.value)<=temp_list[j][2])):self.n_list.append([temp_list[j][0],temp_list[j][1],self.list[j][2]])
            temp_list=self.n_list
        return Store(temp_list)
        
    def count(self):return len(self.list)

    def __add__(self,other):
        s=[]
        for i in range(len(self.list)):s.append([self.list[i][0],self.list[i][1],self.list[i][2]])
        for i in range(len(other.list)):s.append([other.list[i][0],other.list[i][1],other.list[i][2]])
        return Store(s)
    
    def __str__(self):
        if len(self.list)<=0:return "No items"
        else:
            self.list1=[]
            for i in range(len(self.list)):self.list1.append(f'{str(self.list[i][0])}@{str(self.list[i][1])}-{str(self.list[i][2])}')
            return '\n'.join(self.list1)

