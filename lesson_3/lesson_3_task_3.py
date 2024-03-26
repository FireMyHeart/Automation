from address import Address
from mailing import Mailing

mail1 = Mailing()
address1 = Address()
mail1.to_address = address1
mail1.from_address = address1
mail1.track = 123456789
mail1.cost = 1000

print(f"Отправление {mail1.track} из {mail1.to_address.index}, {mail1.to_address.city}, {mail1.to_address.street}, {mail1.to_address.house} - {mail1.to_address.flat}.")