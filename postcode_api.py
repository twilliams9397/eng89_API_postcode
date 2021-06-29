# first iteration

# import requests
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/SY38JA")
#
#
# if check_response_postcode.status_code == 200:
#
#     print(f"The postcode is valid and returned status code {check_response_postcode.status_code}.")
# else:
#     print("Oops something went wrong, please try again later.")

# second iteration
# import requests
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/sy38ja")
#
# if check_response_postcode: # all code and functionality is abstracted from the user
#     print(f"Success with status code {check_response_postcode}")
# else:
#     print("Unavailable")

# third iteration
# import requests
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/SY38JA")
#
# # print(type(check_response_postcode.content)) # bytes
# # print(type(check_response_postcode.headers)) # CaseInsensitiveDict
#
# # how can we parse/get data from dictionary
#
# # print(check_response_postcode.json()) # converts to json file and displays
#
# # let's store this data into a variable
#
# response_dict = check_response_postcode.json()
# # print(type(response_dict)) # now stored as dict
# # print(response_dict)
#
# result_dict = response_dict['result']
# # print(result_dict)
#
# for key in result_dict.keys():
#     print(f"The name of the key is {key} and the value inside is {result_dict[key]}.")

# TASK
# Prompt user to input postcode
# validate the postcode
# present the location back to the user with required message
# apply OOP - DRY where possible

import requests

def check_postcode():

    input_code = str(input("Please enter your postcode with no spaces:  ").lower())

    if input_code.isspace() == True:
        api_code = ("https://api.postcodes.io/postcodes/" + input_code)
    else:
        api_code = ("https://api.postcodes.io/postcodes/" + input_code.replace(" ", ""))

    check_response_postcode = requests.get(api_code)

    if check_response_postcode:
        response_dict = check_response_postcode.json()
        result_dict = response_dict['result']
        return f"Your postcode is {result_dict['postcode']} and you live in {result_dict['parish']}."

    else:
        return "Oops something went wrong, please try again later."

print(check_postcode())
