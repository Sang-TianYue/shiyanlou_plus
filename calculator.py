#!/usr/bin/env python3


import sys

wageAmount_dict = {}
tax_threshold = 5000

# split the arg from commandline
def get_jobNum_and_wageAmount(arg):
    key, value = arg.split(':')
    wageAmount_dict[key] = value
    return wageAmount_dict
    
def get_income_after_tax(salary):
    taxable_amount = 0
    income_after_tax = 0
    taxable_income = int(salary) - 0.165 * int(salary) - tax_threshold
    if taxable_income < 0:
        taxable_amount = 0
    elif taxable_income >= 0 and taxable_income < 3000:
        taxable_amount = taxable_income * 0.03 - 0
    elif taxable_income >= 3000 and taxable_income < 12000:
        taxable_amount = taxable_income * 0.10 - 210
    elif taxable_income >= 12000 and taxable_income < 25000:
        taxable_amount = taxable_income * 0.20 - 1410 
    elif taxable_income >= 25000 and taxable_income < 35000:
        taxable_amount = taxable_income * 0.25 - 2660
    elif taxable_income >= 35000 and taxable_income < 55000:
        taxable_amount = taxable_income * 0.30 - 4410
    elif taxable_income >= 55000 and taxable_income < 80000:
        taxable_amount = taxable_income * 0.35 - 7160
    else:
        taxable_amount = taxable_income * 0.45 - 15160
        
    income_after_tax = int(salary) - 0.165 * int(salary) - taxable_amount
    return income_after_tax




if __name__ == '__main__':
    try:
        for arg in sys.argv[1:]:
            get_jobNum_and_wageAmount(arg)
    # 若参数异常，则捕获异常
    except Exception:
        print("Parameter Error")
    else:
        for key, value in wageAmount_dict.items():
            wageAmount_dict[key] = get_income_after_tax(value)

        output_list = []
        for key, value in wageAmount_dict.items():
            # 税后工资格式化，保留小数点2位
            value = "{:.2f}".format(value)
            output_list.append("{}:{}".format(key, value))
        # 排序输出
        output_list.sort()
        for i in output_list:
            print(i)
