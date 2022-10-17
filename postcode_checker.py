from post_code import Api

postcode = input("Please, enter the postcode:").upper().strip()  # prompt the user to input the postcode
a = Api(postcode)
a.post_code_checker()
print(a.longitude())
print(a.latitude())
a.data()
