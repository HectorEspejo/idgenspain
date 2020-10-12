import random
while True:
    print("GENID SPAIN")
    input("Press ENTER to create your new identity...")
    #NAME GENERATOR
    name_list = ["antonio", "manuel", "martin", "carlos", "alberto", "javier", "jose", "roberto", "fabio",
                 "maria", "lucia", "sara", "andrea", "isabel", "carmen", "susana", "rosa"]
    surname_list = ["garcia", "gonzalez", "moreno", "navarro", "torres", "ramos", "gil", "serrano",
                    "ortega", "delgado", "castro", "ortiz", "rubio", "medina", "garrido", "cortes"]
    name = random.choice(name_list)
    surname1 = random.choice(surname_list)
    surname2 = random.choice(surname_list)
    print(f"FULL NAME: {surname1} {surname2}, {name}")
    #ID GENERATOR
    dni_number = random.randrange(10000000, 99999999)
    dni_letter = random.choice("ABCDEFGHIJKLMNOPQRST")
    print(f"DNI NUMBER = {dni_number}{dni_letter}")
    #BORN DATE
    day_born = random.randrange(1, 31)
    month_born = random.randrange(1, 12)
    year_born = random.randrange(1945, 1999)
    print(f"DATE BORN: {day_born}/{month_born}/{year_born}")
    #AGE
    age = 2020 - year_born
    print(f"AGE: {age}")
    #LOCATION
    city_list = ["madrid", "barcelona", "valencia", "sevilla", "san sebastian", "malaga"]
    city = random.choice(city_list)
    if city == "madrid":
        print(f"LOCATION: {city} (Comunidad de Madrid)")
    elif city == "barcelona":
        print(f"LOCATION: {city} (Cataluña)")
    elif city == "valencia":
        print(f"LOCATION: {city} (Comunidad Valenciana")
    elif city == "sevilla" or "malaga":
        print(f"LOCATION: {city} (Andalucia)")
    elif city == "san sebastian":
        print(f"LOCATION: {city} (Euskadi / Pais Vasco")
    #CIVIL STATUS
    civil_status_list = ["single", "married", "widow"]
    civil_status = random.choice(civil_status_list)
    print(f"CIVIL STATUS: {civil_status}")
    #YEARS FOR RETIRMENT
    if age < 65:
        retirement = 65 - age
        print(f"YEARS FOR RETIREMENT: {retirement}")
    elif age >= 65:
        print(f"STATUS: RETIRED")
    #PHONE NUMBER
    phone_number = random.randrange(600000000, 699999999)
    print(f"PHONE NUMBER: {phone_number}")
    #PHONE OPERATOR
    phone_operator_list = ["orange", "movistar", "vodafone"]
    phone_operator = random.choice(phone_operator_list)
    print(f"PHONE OPERATOR: {phone_operator}")
    #EMAIL
    email_providers_list = ["gmail", "outlook", "yahoo"]
    email_provider = random.choice(email_providers_list)
    print(f"EMAIL: {name}.{surname1}@{email_provider}.com")
    #PASSWORD
    password_easy_list = [name, "toby", "realmadrid", "fcbarcelona", "contrasena", "agua"]
    password_easy = random.choice(password_easy_list)
    password_hard_number = random.randrange(10, 100)
    password_hard_number2 = random.randrange(10, 100)
    password_hard_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    password_hard_letter2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    password_hard_symbol