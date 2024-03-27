from address import Address
from mailing import Mailing

address1 = Address(214013, 'г. Смоленск', 'ул. Матросова', '5А', '37')
address2 = Address(129301, 'г. Москва', 'пр-кт Мира', '184 к1', 'оф. 123')
mail1 = Mailing(address1, address2, 7000, 900724001)

print(f"Отправление {mail1.track} из {mail1.from_address.index}, {mail1.from_address.city}, {mail1.from_address.street}, {mail1.from_address.house} - {mail1.from_address.flat}.")