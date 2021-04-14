country_dict = {}
country_number = int(input("Введите кол-во стран: "))
city_name = []
for country_num in range(0, country_number):
    stroka1 = input("Введите страну, через пробел и города: ").split()
    country_name = stroka1[0]
    for i in range(1, len(stroka1)):
        #city_name = city_name + " " + stroka1[i]
        city_name.append(stroka1[i])
    country_dict[country_name] = city_name
    #country_dict[country_name] = country_dict.get(country_name, city_name) + city_name
    #country_dict.update({country_name: city_name})
    print(country_dict)
    city_name.clear()
#ountry_dict.update({country_name : city_name})
print(country_dict)