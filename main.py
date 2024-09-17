import Account_management as am
import Show_details as ad
import Utility as u
import Validation as v

print("""Hello there! 
Do you want to create an account, review your account, or update your account? 
    1. To create an account 
    2. To review your account 
    3. To update your account""")

purpose = int(input())

match purpose:

    case 1:  # Create an account
        
        am.create_account()

        