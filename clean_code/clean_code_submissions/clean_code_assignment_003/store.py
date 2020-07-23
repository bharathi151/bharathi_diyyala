class Item:
    def __init__(self, name, price, category):
        if price <= 0:
            raise ValueError(f"Invalid value for price, got {price}")
        self._name, self._price, self._category = name, price, category

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def category(self):
        return self._category

    def __str__(self):
        return f'{self._name}@{self._price}-{self._category}'

class Query:
    def __init__(self, field, operation, value):
        operations = ["IN", "EQ", "GT", "GTE", "LT",
                      "LTE", "STARTS_WITH", "ENDS_WITH", "CONTAINS"]
        if operation not in operations:
            raise ValueError(f"Invalid value for operation, got {operation}")
        self._field, self._operation, self._value = field, operation, value

    @property
    def field(self):
        return self._field

    @property
    def value(self):
        return self._value

    @property
    def operation(self):
        return self._operation

    def __str__(self):
        return f'{self.field} {self.operation} {self.value}'

class Store:
    def __init__(self, list=None):
        if list:
            self._list = list
        else:
            self._list = []

    def add_item(self, item):
        self._list.append(item)

    @property
    def list(self):
        return self._list

    def count(self):
        return len(self.list)

    def filter(self, query):
        temp_list = Store()
        operations = ["IN", "EQ", "GT", "GTE", "LT", "LTE",
                      "STARTS_WITH", "ENDS_WITH", "CONTAINS"]
        for item in self.list:
            if query.operation not in operations:
                value_error(query.operation)
            value = getattr(item, query.field)
            temp_list = string_operations_filter(query.operation, query.value,
                                                 item, value, temp_list)
            temp_list = arithamtic_operations_filter(query.operation,
                                                     query.value,
                                                     item, value, temp_list)
        return temp_list

    def exclude(self, query):
        temp_list = Store()
        filter_list = self.filter(query)
        for item in self.list:
            if item not in filter_list.list:
                temp_list.add_item(item)
        return temp_list

    def __str__(self):
        if len(self.list) <= 0:
            return "No items"
        return "\n".join(map(str, self.list))

def string_operations_filter(query_operation, query_value, item,
                             value, temp_list):
    if query_operation == "STARTS_WITH":
        if value.startswith(query_value):
            temp_list.add_item(item)
    if query_operation == "ENDS_WITH":
        if value.endswith(query_value):
            temp_list.add_item(item)
    if query_operation == "CONTAINS":
        if query_value in value:
            temp_list.add_item(item)
    return temp_list

def arithamtic_operations_filter(query_operation, query_value, item,
                                 value, temp_list):
    if query_operation == "EQ":
        if value == query_value:
            temp_list.add_item(item)
    if query_operation == "LT":
        if value < query_value:
            temp_list.add_item(item)
    if query_operation == "GT":
        if value > query_value:
            temp_list.add_item(item)
    if query_operation == "LTE":
        if value <= query_value:
            temp_list.add_item(item)
    if query_operation == "GTE":
        if value >= query_value:
            temp_list.add_item(item)
    if query_operation == "IN":
        if value in query_value:
            temp_list.add_item(item)
    return temp_list

def value_error(string):
    raise ValueError(f"ValueError: Invalid value for operation, got {string}")

