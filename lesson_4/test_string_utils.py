from string_utils import StringUtils
import pytest

#позитивные кейсы для метода capitilize:
@pytest.mark.parametrize('text, result', [
    ('skypro', 'Skypro'), #Строка, в которой только одно слово
    ("it's a beautiful lie", "It's a beautiful lie"), #Строка с несколькими словами
    ('in the end     ', 'In the end     '), #Строка с пробелами в конце
    (('ВЕРХНИЙ РЕГИСТР', 'Верхний регистр')), #Все буквы в верхнем регистре
    ('1234567', '1234567'), #Числа
    ('@#$%^&*():!№;', '@#$%^&*():!№;'), #спецсимволы
    ('', ''), #Пустая строка
    ('     hi there', '     hi there'), #Строка с пробелами в начале
    ('🌸😊❤️🍕🎶', '🌸😊❤️🍕🎶'), #Эмодзи

    ])
def test_positive_capitilize(text, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(text)
    assert res == result

#негативные кейсы для метода capitilize:
@pytest.mark.xfail()
@pytest.mark.parametrize('text, result', [
    (None, None), #None, AttributeError
    (123456, None), #integer, AttributeError
    (['anna kotikova'], None) #list, AttributeError
    ])
def test_negative_capitilize(text, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(text)
    assert res == result  

#позитивные кейсы для метода trim
@pytest.mark.parametrize('text, result', [
    (' 12345%dkffkab', '12345%dkffkab'), #1 пробел в начале
    ('          111kfsslf99', '111kfsslf99'), #несколько пробелов в начале
    (' fsdfj sfdkj asdfk', 'fsdfj sfdkj asdfk'), #Строка с несколькими словами
    ('     ', ''), #Просто пробел(ы)
    (' 🌈🎉🐱‍🏍', '🌈🎉🐱‍🏍'), #эмодзи
    ('', ''), #пустая строка
    ('akjfb2      ', 'akjfb2      '), #пробелы в конце
    ])
def test_positive_trim(text, result):
    stringutils = StringUtils()
    res = stringutils.trim(text)
    assert res == result

#негативные кейсы для метода trim
@pytest.mark.xfail()
@pytest.mark.parametrize('text, result', [
    (None, None), #None AttributeError
    (1363, None), #integer AttributeError
    (['    Привет'], None) #list AttributeError
    ])
def test_negative_trim(text, result):
    stringutils = StringUtils()
    res = stringutils.trim(text)
    assert res == result

#позитивные кейсы для метода to_list
@pytest.mark.parametrize('text, delimeter, result', [
    ('123,456,789,', ',', ['123', '456', '789', '']), #строка из чисел
    ('sdf*sa*as*sFDdfd', '*', ['sdf', 'sa', 'as', 'sFDdfd']), #строка из букв
    ('123ф567ф124фsdfg', 'ф', ['123', '567', '124', 'sdfg']), #еще один вид разделителя
    ('тыц\nтыц\nтыц\nпам\nпарам', '\n', ['тыц', 'тыц', 'тыц', 'пам', 'парам']), #разделитель из нескольких символов
        ('waeufvb;a asdfdf', '123', ['waeufvb;a asdfdf']), #разделитель, которого нет
    ])
def test_positive_to_list(text, delimeter, result):
    stringutils = StringUtils()
    res = stringutils.to_list(text, delimeter)
    assert res == result

@pytest.mark.parametrize('text, result', [('esab,asf8,3777,()*737', ['esab', 'asf8', '3777', '()*737'])]) #не указан разделитель
def test_positive1_to_list(text, result):
    stringutils = StringUtils()
    res = stringutils.to_list(text)
    assert res == result

#негативные кейсы для метода to_list
@pytest.mark.xfail()
@pytest.mark.parametrize('text, delimeter, result', [
    (None, ',', None), #None
    (['anna', 'inna', 'tolya'], ',', None), #list AttributeError
    ])
def test_negative_to_list(text, delimeter, result):
    stringutils = StringUtils()
    res = stringutils.to_list(text, delimeter)
    assert res == result

#позитивные кейсы для метода contains
@pytest.mark.parametrize('text, symbol, result', [
    ('dsf sf5ncwe', '5', True), #есть 1 раз
    ('sfbksfin', 's', True), #есть несколько раз
    ('аымилд', 'мил', True), #не 1 символ, а несколько
    ('sfb№ksfin', '№', True), #спецсимвол в качестве символа
    ('kugjk', '', True), #не указать разделитель
    ('', '', True), #пустая строка
    ])
def test_positive_contains(text, symbol, result):
    stringutils = StringUtils()
    res = stringutils.contains(text, symbol)
    assert res == result

#негативные кейсы для метода contains
@pytest.mark.xfail()
@pytest.mark.parametrize('text, symbol, result', [
    (None, '', None), #None AttributeError
    ])
def test_negative_contains(text, symbol, result):
    stringutils = StringUtils()
    res = stringutils.contains(text, symbol)
    assert res == result

#позитивные кейсы для метода delete_symbol
@pytest.mark.parametrize('text, symbol, result', [
    ('wsadjkc4sfdzzzz', '4', 'wsadjkcsfdzzzz'), #удаление 1 символа
    ('wsazzdjkcz4sfdzzzz', 'z', 'wsadjkc4sfd'), #удаление 1 символа, встречается несколько раз
    ('ываи лаыаслрф флвыв', 'ваи', 'ы лаыаслрф флвыв'), #удаление нескольких символов
    ('sdflkslbca; as asfjnsl', '^', 'sdflkslbca; as asfjnsl'), #удаление символа, которого нет
    ('', 'f', ''), #пустая строка и символ для удаления
    ('ыфвлмятл  ыа с', '', 'ыфвлмятл  ыа с'), #ничего для удаления
    ('Skypro', 's', 'Skypro') #регистрочувствительность
    ])
def test_positive_delete_symbol(text, symbol, result):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(text, symbol)
    assert res == result

#негативные кейсы для метода delete_symbol
@pytest.mark.xfail()
@pytest.mark.parametrize('text, symbol, result', [('64wefh5ed', 5, None)])#TypeError
def test_negative_delete_symbol(text, symbol, result):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(text, symbol)
    assert res == result

#позитивные кейсы для метода starts_with
@pytest.mark.parametrize('text, symbol, result', [
    ('sdficbwv a sfn jzsd i', 's', True),  #1 символ
    ('43587vhsdjbv&^', '435', True), #несколько символов
    ('уасядг тоыа', 'dvjj', False), #не начинается с этих символов
    ('уасядг тоыа', 'тоыа', False), #не начинается, а заканчивается
    ('ывпмло в', '', True) #пустота вместо символа
    ])
def test_positive_starts_with(text, symbol, result):
    stringutils = StringUtils()
    res = stringutils.starts_with(text, symbol)
    assert res == result

#негативные кейсы для метода starts_with
@pytest.mark.xfail()
@pytest.mark.parametrize('text, symbol, result', [('64wefh5ed', 5, None)]) #integer TypeError
def test_negative_starts_with(text, symbol, result):
    stringutils = StringUtils()
    res = stringutils.starts_with(text, symbol)
    assert res == result

#позитивные кейсы для метода end_with
@pytest.mark.parametrize('text, symbol, result', [
    ('sdficbwv a sfn jzsd i', 'i', True),  #1 символ
    ('43587vhsdjbv&^', 'v&^', True), #несколько символов
    ('уасядг тоыа', 'dvjj', False), #не заканчивается на эти символы
    ('уасядг тоыа', 'уася', False), #не заканчивается, а начинается
    ('ывпмло в', '', True) #пустота вместо символа
    ])
def test_positive_end_with(text, symbol, result):
    stringutils = StringUtils()
    res = stringutils.end_with(text, symbol)
    assert res == result

#негативные кейсы для метода end_with
@pytest.mark.xfail()
@pytest.mark.parametrize('text, symbol, result', [('64wefh5ed', 5, None)]) #integer TypeError
def test_negative_end_with(text, symbol, result):
    stringutils = StringUtils()
    res = stringutils.end_with(text, symbol)
    assert res == result

#позитивные кейсы для метода is_empty
@pytest.mark.parametrize('text, result', [
    ('', True), #пустая строка
    ('     ', True), #только пробелы
    ('хзфлыстт3', False), #непустая строка
    (' ', True) #неразрывный пробел
    ])
def test_positive_is_empty(text, result):
    stringutils = StringUtils()
    res = stringutils.is_empty(text)
    assert res == result

#негативные кейсы для метода is_empty
@pytest.mark.xfail()
@pytest.mark.parametrize('text, result', [
    (7575, None), #integer
    ([], None), #пустой list
    (None, None) #None
    ])
def test_negative_is_empty(text, result):
    stringutils = StringUtils()
    res = stringutils.is_empty(text)
    assert res == result

#позитивные кейсы для list_to_string
@pytest.mark.parametrize('text, result', [
    (['cat', 'dog', 'horse'], 'cat, dog, horse'), #список из string
    ([1, 3, 56, 987], '1, 3, 56, 987'), #список из integer
    (['sf', 'shd', 435], 'sf, shd, 435'), #смешанный список
    ([], ''), #пустой список
    ([[1, 3], [56, 987]], '[1, 3], [56, 987]'), #матрица
    ('sdgdgvrr', 's, d, g, d, g, v, r, r') #строка
    ])
def test_positive_list_to_string(text, result):
    stringutils = StringUtils()
    res = stringutils.list_to_string(text)
    assert res == result

@pytest.mark.parametrize('text, joiner, result', [([7, 952, 991, '01', '01'], '-', '7-952-991-01-01')])
def test_positive1_list_to_string(text, joiner, result):
    stringutils = StringUtils()
    res = stringutils.list_to_string(text, joiner)
    assert res == result
