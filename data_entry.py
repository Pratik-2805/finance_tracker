from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORY = {'I': "Income", 'E': "Expence"}

#This entire def is a recursion function since until the valid date format is not pasted the function will keep on calling itself.
def get_date(prompt, allow_default=False): # promt will ask if yo want to add some another date , and default will directly add the todays date.
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy Format")
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    

def get_category():
    category = input("Enter the Category('I' for Income or 'E' for Expense.): ").upper()
    if category in CATEGORY:
        return CATEGORY[category]
    
    print("Invalid Category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()


def get_description():
    return input("Enter the description (Optional): ")