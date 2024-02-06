import gspread
from google.oauth2.service_account import Credentials

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

  

    data_str = input("Enter your data here: ")

    sales_data = data_str.split(",")
    validate_data(sales_data)
def validate_data(values):
    """
    """
    try:
        if len(values) != 6:
          raise ValueError(
            f"Exactly 6 values required, you provided {len(values)}"
        )
    except ValueError as e:
       print(f"Invalid data:{e}")
get_sales_data()