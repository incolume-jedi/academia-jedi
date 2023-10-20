import requests


def tratativa1(session: requests.Session, city_name: str):
    """https://www.hashtagtreinamentos.com/previsao-do-tempo-com-python
    link do open_weather: https://openweathermap.org/.
    """
    API_KEY = 'coloque sua API aqui'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang=pt_br'

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    print(descricao, f'{temperatura}ºC')


def tratativa2(session: requests.Session, city_name: str):
    """From https://youtu.be/CJjSOzb0IYs."""
    API_KEY = ''
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang=pt_br'
    result = session.get(url)
    return result.json()


def run():
    cities_names = [
        'São Paulo',
        'rio de janeiro',
        'London',
        'Brasília',
        'Manchester',
    ]
    s = requests.Session()
    for city_name in cities_names:
        tratativa2(s, city_name)
