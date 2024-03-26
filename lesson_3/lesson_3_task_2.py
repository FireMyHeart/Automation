from smartphone import Smartphone
catalog = []

tel1 = Smartphone('Xiaomi', 'POCOPHONE F1', '+79529910000')
tel2 = Smartphone('Apple iPhone', '15 Pro Max', '+79107115566')
tel3 = Smartphone('Samsung', 'Galaxy S23 Ultra', '+79227631111')
tel4 = Smartphone('Xiaomi', 'Poco F5 Pro', '+79051234567')
tel5 = Smartphone('Apple iPhone', 'iPhone 13', '+79091112233')

catalog.extend([tel1, tel2, tel3, tel4, tel5])

for i in catalog:
    print(f"{i.phone_brand} - {i.phone_model}. {i.phone_number}.")