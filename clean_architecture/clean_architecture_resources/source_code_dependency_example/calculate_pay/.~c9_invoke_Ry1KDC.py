"""
Created on 14/05/20

@author: revanth
"""
from typing import List, Union
from source_code_dependency_example.employees.designer import Designer
from source_code_dependency_example.employees.developer import Developer
from source_code_dependency_example.employees.business_ developer import Business_Developer


class PayoutCalculator:

    @classmethod
    def calculate_payout(cls, employees: List[Union[Developer, Designer,Business_Developer]]):
        total_payout = 0
        for each_employee in employees:
            total_payout += each_employee.get_total_salary()

        print('Total payout: {}'.format(total_payout))



