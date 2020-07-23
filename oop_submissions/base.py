class User:
    def __init__(self, first_name, last_name, lang):
        if type(first_name)!=str:
            raise ValueError(f"Invalid value for first_name, got {type(first_name)}")
        if type(last_name)!=str:
            raise ValueError(f"Invalid value for first_name, got {type(last_name)}")
        if type(lang)!=str:
            raise ValueError(f"Invalid value for first_name, got {type(lang)}")
        self.first_name = first_name
        self.last_name = last_name
        self.lang = lang

    def __str__(self):
            return '%s %s-%s'%(self.first_name, self.last_name, self.lang)

    def __repr__(self):
        return '%s-%s'%(self.first_name, self.lang)

class Log:
    def __init__(self, time_stamp):
        self.time_stamp = time_stamp

    def __str__(self):
        return "%s"%self.time_stamp

    def __repr__(self):
        return "%s"%self.time_stamp

class GroupsUser:
    def __init__(self, firstname, lastname, group):
        self.firstname = firstname
        self.lastname = lastname
        self.group = group

    def __str__(self):
        return "%s %s %s"%(self.firstname, self.lastname, self.group)

    def __repr__(self):
        return "%s %s"%(self.firstname, self.group)

class AdminUser:
    def __init__(self, firstname, lastname, group, admin):
        self.firstname = firstname
        self.lastname = lastname
        self.group = group
        self.admin = admin

    def __str__(self):
        return "%s %s %s %s"%(self.firstname, self.lastname, self.group, self.admin)

    def __repr__(self):
        return "%s %s %s"%(self.firstname, self.group, self.admin)

class MyClass:
    def __init__(self, obj_number):
        self.obj_number = obj_number

    def __str__(self):
        return "%s"%self.obj_number

    def __repr__(self):
        return "%s"%self.obj_number
