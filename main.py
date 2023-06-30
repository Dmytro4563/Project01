print("test")
userName = Dima Bulba
print(tempText.replace("D" "B"))
print(D)if __name__ == "__main__":

    someArray = [1, "test", True, 1.6, "hello"]
    # get element by index
    print(someArray[4])
    # lenght arrey
    print(len(someArray))
    print(someArray[-1])
    # add elements to array
    someArray.append(2)
    print(someArray)
    # remove elements
    someArray.pop(1)
    print(someArray)
    someArray.remove('hello')
    print(someArray)
    # find element in array
    targetElement = someArray.index(1.6)
    print(targetElement)
    # replace
    targetElementIndex = someArray.index(1.6)
    someArray[targetElementIndex] = "test3"
    print(someArray)
    # reverce array
    someArray.reverse()
    print(someArray)
    # clear array
    someArray.clear()
    print(len(someArray))

    #a = 1
    #b = a
    #a[0] += 1
    #print(a)
    #print(b)

    # tempDict = {
    #     "name": "test"
    # }
    # print(type(tempDict))
    # ### personal data
    # name = input("Введіть ім'я")
    # surname = input("Введіть прізвище")
    # fathers_name = input("Введіть по-батькові")
    # ### format
    # name = name .title()
    # surname = surname.title()
    # fathers_name =  fathers_name.title()
    # ### create data frame
    # personal_data = {
    #     "name": name,
    #     "surname": surname,
    #     "fathers_name": fathers_name,
    #     "pib": f"{surname} {name} {fathers_name}"
    # }
    # personal_data["age"] = 24
    # print(personal_data)

    tempDict = {
        "adress": "test"
    }
    print(type(tempDict))
    city = input("Введіть місто")
    street = input("Введіть вулицю")
    number = input("Введіть номер будинку")
    index = input("Введіть індекс населеного пункту")

    city = city.title()
    street = street.title()
    number = number.title()
    index = index.title()

    personal_data = {
        "city": city,
        "street": street,
        "number": number,
        "index": index,
        "adress": f"{city} {street} {number} {index}"
    }