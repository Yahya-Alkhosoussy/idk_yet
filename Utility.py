def make_account(first_name: str, last_name: str, age:int, password:str , Account_type:str):

    if Account_type == 1:

        Account_type = "Credit"

    else: 

        Account_type = "Debit"

    try:
        
        with open(f"saved_information/{first_name}_{last_name}.txt", "x") as file:
            
            file.write(f"""First name: {first_name}
Last name: {last_name}
Age: {age} years old
Password: {password}
Account type: {Account_type}""")
    
    except FileExistsError:
        
        print("File already exists.")
