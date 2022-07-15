from countryinfo import CountryInfo
while True:
    country_name = input("Enter name of the country in English:")
    country = CountryInfo(country_name)
    print(f"{country.capital()} is the capital of {country_name}."
          f"This country is located in {country.subregion()}.\n"
          f"The current population of {country_name} adds up to {country.population()}.\n"
          f"In case u have any friends out there in {country_name} and u want to call them,"
          f"be sure that u enter {country.calling_codes()} code first. By the way, if u are interested, \n"
          f" for the local people is: {country.demonym()}")
