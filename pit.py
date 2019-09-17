__version__ = "1.0"

"""
Personal Income Tax Calculator
Author: Anh Hong
File Name: pit.py

"""

base_salary = 1490000
minimum_salary_region1 = 4180000
minimum_salary_region2 = 3710000
minimum_salary_region3 = 3250000
minimum_salary_region4 = 2920000
social_insurance_rate = 0.08      
health_insurance_rate = 0.015     
unemployment_rate = 0.01
personal_deduction = 9000000
dependant_deduction = 3600000
pit_lv1 = 5000000
pit_lv1_rate = 0.05
pit_lv2 = 10000000
pit_lv2_rate = 0.1
pit_lv3 = 5000000
pit_lv3_rate = 0.15
pit_lv4 = 5000000
pit_lv4_rate = 0.2
pit_lv5 = 5000000
pit_lv5_rate = 0.25
pit_lv6 = 5000000
pit_lv6_rate = 0.3
pit_lv7 = 5000000
pit_lv7_rate = 0.35


# Define class Income
class PersonalMonthlyIncome():
    def __init__(self, gross, contract, dependant, region):      
        #Tiền lương trong hợp đồng
        self.gross = gross

        #Tiền lương làm căn cứ tính BH Xã Hội, Y tế
        self.contract = contract

        #Số người phụ thuộc
        self.dependant = dependant

        #Thông tin vùng, để xác định mức lương tối thiếu để tính BH Thất nghiệp
        self.region = region
    
    def minimum_salary(self):
        if self.region == 1:
            return minimum_salary_region1
        if self.region == 2:
            return minimum_salary_region2
        if self.region == 3:
            return minimum_salary_region3
        return minimum_salary_region4

    def insurance_based_calculation(self):
        if self.contract > (base_salary*20):
            return base_salary*20
        else:
            return self.contract
    
    def unemployment_based_calculation(self):
        if self.contract > (self.minimum_salary()*20):
            return self.minimum_salary()*20
        else:
            return self.contract

    def social_insurance(self):
        if self.contract > (base_salary*20):
            return round((base_salary*20*social_insurance_rate))
        else:
            return round(self.contract*social_insurance_rate)

    def health_insurance(self):
        if self.contract > (base_salary*20):
            return round((base_salary*20*health_insurance_rate))
        else:
            return round(self.contract*health_insurance_rate)
    
    def unemployment(self):
        temp = self.minimum_salary()*20
        if self.contract > temp:
            return round(temp*unemployment_rate)
        else:
            return round(self.contract*unemployment_rate)

    def personal_deduction(self):
        return personal_deduction

    def dependant_deduction(self):
        return self.dependant*dependant_deduction

    def taxable_income(self):
        return (self.gross)-(self.social_insurance() + self.health_insurance() + self.unemployment() + self.personal_deduction() + self.dependant_deduction())
    
    def personal_income_tax(self):
        tax = 0        
        temp = self.taxable_income()

        if temp > 80000000:
            tax += temp*pit_lv7_rate - 9850000
        else:
            if temp > 52000000:
                tax += temp*pit_lv6_rate - 5850000
            else:
                if temp > 32000000:
                    tax += temp*pit_lv5_rate - 3250000
                else:
                    if temp > 18000000:
                        tax += temp*pit_lv4_rate - 1650000
                    else:
                        if temp > 10000000:
                            tax += temp*pit_lv3_rate - 750000
                        else:
                            if temp > 5000000:
                                tax += temp*pit_lv2_rate - 250000
                            else:
                                tax += temp*pit_lv1_rate
        return round(tax)

    def net_income(self):
        return self.gross - self.social_insurance() - self.health_insurance() - self.unemployment() - self.personal_income_tax()
        