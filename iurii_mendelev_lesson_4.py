import sys
from requests import get, utils
response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


chr = input('Введите код валюты: ')

def currency_rates(chr):

    response_list = []
    response_list.append(content.split('><'))
    response_list_1 = response_list[0]
    for i in response_list_1:
        if i == 'CharCode>' + chr + '</CharCode':
            ind = response_list_1.index(i)
            value = ''.join(response_list_1[ind + 3].strip('eVaulave/<>'))
            nominal = ''.join(response_list_1[ind + 1].strip('<>NloanmimalN/<>'))
            print('За {} {} сегодня дают {} рублей'.format(nominal, chr, value))
            print('Сегодня за {} рублей можно купить {} {}'.format(value, nominal, chr))


currency_rates(chr)


