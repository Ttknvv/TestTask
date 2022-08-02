from dadata import Dadata
from SettingsPO import InpSet, OutSet, DelSet

print("\nПрограмма для определения координат заданного адреса\n"
      "")

token = input("Введите ваш API ключ: ")
secret = input("Введите ваш секретный ключ: ")
language = input('Введите язык на котором будет производиться поиск, "ru" или "eng": ').lower()
if language != "ru" and language != "eng": language = "ru"

##Запись настроек в базу данных
InpSet(token, secret, language)

while True:
    inAdress = input("Введите адрес дома для определения ее координат (можете записать в произвольном формате): ")
    if inAdress == "exit":
        break
    else:
        ##Получение данных их БД
        df = OutSet()

        ##Обращение к Dadata
        dadata = Dadata(df[0][0], df[0][1])
        result = dadata.suggest("address", inAdress, language = df[0][2])

        ##Формирование выпадающего списка
        num = 1
        for i in result:
            print("|{} - {}|".format(num, i['value']))
            num += 1

        numLine =input('Введите число от 1 до 10 подходящего вам варианта из выпавшего списка ')
        if numLine == "exit":
            break
        else:
            numLine = int(numLine) - 1
            ##Получение координат из сформированного обращения
            print("Широта: {}".format(result[numLine]['data']['geo_lat']))
            print("Долгота: {}".format(result[numLine]['data']['geo_lon']))
            print('\nДля выхода из программы введите "exit"\n')
DelSet()

