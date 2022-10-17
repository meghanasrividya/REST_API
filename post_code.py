import requests


class Api:

    def __init__(self, postcode):
        self.url = "http://api.postcodes.io/postcodes/"
        self.postcode = postcode

    def post_code_checker(self):  # Creating a function that checks if the post code is valid
        url_arg = self.url + self.postcode
        response = requests.get(url_arg)

        if response.status_code == 200:
            print("You have entered correct postcode")
        else:
            print("Please enter the correct postcode in right format")

    def latitude(self):  # display latitude
        url_arg = self.url + self.postcode
        response = requests.get(url_arg)
        response_dict = response.json()
        result = response_dict["result"]
        latitude = result["latitude"]
        return latitude

    def longitude(self):  # display longitude
        url_arg = self.url + self.postcode
        response = requests.get(url_arg)
        response_dict = response.json()
        result = response_dict["result"]
        longitude = result["longitude"]
        return longitude

    def display_url(self):  # display url together with given postcode
        url_arg = self.url + self.postcode
        return url_arg

    def data(self):
        url_arg = self.url + self.postcode
        print(url_arg)  # display url together with given postcode
        response = requests.get(url_arg)
        print("Type of data scrapped : ",
              type(response.content))  # check the type of data scrapped from the web - response

        response_dict = response.json()  # converting data type to dictionary
        print("Type of the data after converting: ", type(response.json()))
