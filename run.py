import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('credentials.json')

SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Corrected method for authentication
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    get sales input from the user
    """
    while True:
        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid")
            return sales_data

def validate_data(values):
    """
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    return True

def update_sales_worsheet(data):
    """
    update sales worksheet add new row with data list provided
    """
    print("Updating sales data...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully...\n")

def update_surplus_worsheet(data):
    """
    update sales worksheet add new row with data list provided
    """
    print("Updating surplus data...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated successfully...\n")
    
def calculate_surplus_data(sales_row):
    """
    calculate surplus by comparing stock and sales"""
    
    print("Calculating surplus...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    
    surplus_data = []
    for stock,sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data
  
     

def main():
    """Runn all program function"""
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worsheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worsheet(new_surplus_data)
    print(new_surplus_data)
print("Welcome to Love Sandwiches Automation")
   
main()