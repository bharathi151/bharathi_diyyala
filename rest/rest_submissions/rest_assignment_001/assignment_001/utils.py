from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from assignment_001.constants import EmployeeTypes
class Employee(object):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired,
                 is_best_employee=None, last_name=None
                 ):
        self.employee_id = employee_id
        self.age = age
        self.date_of_joining = date_of_joining
        self.last_logged_in = last_logged_in
        self.salary_in_inr = salary_in_inr
        self.employee_type = employee_type
        self.first_name = first_name
        self.last_name = last_name
        self.is_retired = is_retired
        self.is_best_employee = is_best_employee

class Company(object):
    def __init__(self, name, registration_id):
        self.name = name
        self.registration_id = registration_id

class EmployeeWithCompanyDetails(Employee):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired, company,
                 is_best_employee=None, last_name=None):
        super().__init__(employee_id, age, date_of_joining, last_logged_in,
                         salary_in_inr, employee_type, first_name, is_retired,
                         is_best_employee, last_name)
        self.company = company

class CompanyWithEmployeesDetails(Company):
    def __init__(self, name, registration_id, employees):
        super().__init__(name, registration_id)
        self.employees = employees


class EmployeeSerializer(serializers.Serializer):
    employee_id = serializers.UUIDField()
    age = serializers.IntegerField()
    date_of_joining = serializers.DateField()
    last_logged_in = serializers.DateTimeField()
    salary_in_inr = serializers.FloatField()
    employee_type = serializers.ChoiceField(choices=EmployeeTypes.values)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100, allow_null=True, required=False)
    is_retired = serializers.BooleanField()
    is_best_employee = serializers.NullBooleanField(required=False)

    def create(self, validated_data):
        return Employee(**validated_data)

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    registration_id = serializers.UUIDField()

    def create(self, validated_data):
        return Company(**validated_data)

class EmployeeWithCompanyDetailsSerializer(EmployeeSerializer):
    company = CompanySerializer()

    def create(self, validated_data):
        company_data = validated_data.pop('company')
        company = Company(**company_data)
        return EmployeeWithCompanyDetails(company=company, **validated_data)

class CompanyWithEmployeeDetailsSerializer(CompanySerializer):
    employees = EmployeeSerializer(many=True)

    def create(self, validated_data):
        employees_data = validated_data.pop('employees')
        employees = [Employee(**employee_data) for employee_data in employees_data]
        return CompanyWithEmployeesDetails(employees=employees, **validated_data)


def serialize_employee_object(employee_object):
    serializer_of_obj = EmployeeSerializer(employee_object)
    return serializer_of_obj.data

def deserialize_data_to_employee_object(employee_data):
    deserializer_of_employee_data = EmployeeSerializer(data=employee_data)
    is_valid_data = deserializer_of_employee_data.is_valid()
    if is_valid_data:
        employee_obj = deserializer_of_employee_data.save()
        return employee_obj
    return deserializer_of_employee_data.errors

def serialize_list_of_employee_objects(list_of_employee_objects):
    serializer_of_objs_list = EmployeeSerializer(list_of_employee_objects,
                                                 many=True)
    return serializer_of_objs_list.data

def deserialize_data_to_list_of_employee_objects(employees_data):
    deserializer_of_employees_data = EmployeeSerializer(data=employees_data,
                                                   many=True)
    is_valid_data = deserializer_of_employees_data.is_valid()
    if is_valid_data:
        employees_objs = deserializer_of_employees_data.save()
        return employees_objs
    return deserializer_of_employees_data.errors

def serialize_employee_with_company_object(employee_with_company_object):
    serializer_of_obj = EmployeeWithCompanyDetailsSerializer(employee_with_company_object)
    return serializer_of_obj.data

def deserialize_data_to_employee_with_company_object(employee_with_company_data):
    deserialize_employee_with_company_data = EmployeeWithCompanyDetailsSerializer(data=employee_with_company_data)
    is_valid_data = deserialize_employee_with_company_data.is_valid()
    if is_valid_data:
        employee_with_company_details_obj = deserialize_employee_with_company_data.save()
        return employee_with_company_details_obj
    return deserialize_employee_with_company_data.errors

def serialize_company_with_employees_object(company_with_employees_object):
    serializer_of_obj = CompanyWithEmployeeDetailsSerializer(company_with_employees_object)
    return serializer_of_obj.data

def deserialize_data_to_company_with_employees_object(company_with_employees_data):
    deserialize_company_with_employees_data = CompanyWithEmployeeDetailsSerializer(data=company_with_employees_data)
    is_valid_data = deserialize_company_with_employees_data.is_valid()
    if is_valid_data:
        company_with_employees_details_obj = deserialize_company_with_employees_data.save()
        return company_with_employees_details_obj
    return deserialize_company_with_employees_data.errors
