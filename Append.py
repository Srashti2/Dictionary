travel_log= [{"country":"France","visits":12,"cities":["paris","lille","djone"]},{"country":"Germany","visits":10,"cities":["Berlin","Munich","Frankfurt"]}]

#need to define a funtion that could add new country to the list

def add_new_country(country,visits,cities):
    travel_log.append({"country":country,"visits":visits,"cities":cities})

add_new_country("Russia",15,["Moscow","Kazan"])
print(travel_log)