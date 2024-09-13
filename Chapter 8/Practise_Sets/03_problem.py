# Problem 03

# Write a function to convert PKR TO USD & GBP

def currency_converter():
    # change_to = input("Enter USD To Convert In United States Dollar.\nEnter GBP To Convert In Great British Pound.\n")
    change_to = input("USD or GBP\n")
    amount = int(input("Enter The Amount to calulate:"))

    if (change_to == "GBP"):
       total = amount*364.80
       print("Your Pkr",amount , "To Great Pound Is", total)

    if (change_to == "USD"):
       total = amount*278.93
       print("Your Pkr",amount , "To Great Pound Is", total)
    
    else:
       print("Just Enter USD or GBP not other than these 2\nThank You!!")

currency_converter()