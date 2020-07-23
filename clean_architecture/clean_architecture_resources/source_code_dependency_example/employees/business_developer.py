"""
Created on 14/05/20

@author: revanth
"""


class Business_Developer:

    def __init__(self, name: str, age: int, base_salary: int):
        self.name = name
        self.age = age
        self.base_salary = base_salary

    def _get_business_developer_bonus(self):
        return 15000

    def get_total_salary(self):
        total_salary = self.base_salary + self._get_business_developer_bonus()
        print('{} - Business_Developer: {}'.format(self.name, total_salary))
        return total_salary
