"""Streamlit app for Academia Jedi 20250605 project."""

import os
from http import HTTPStatus

import streamlit as st
from ajedi20250606_acesso_openweather import auth_token
from httpx import HTTPStatusError
from icecream import ic


def main():
    """Main function to run the Streamlit app."""
    st.title('Web App Climatológico')
    st.write(
        'Dados disponibilizados pela OpenWeatherMap (https://openweathermap.org/current)',
    )

    city = st.text_input(
        'Informe o nome da cidade',
        key='city',
        value='Brasília',
    )
    if not os.getenv('OPEN_WEATHER_MAP_API_KEY'):
        st.text_input(
            'Informe o token de acesso à API OpenWeatherMap',
            key='token',
        )

    if not city:
        st.stop()

    try:
        result = auth_token(city=city)
        result.raise_for_status()  # Raise an error for bad responses
    except HTTPStatusError:
        ic(result.json())
        match result.status_code:
            case HTTPStatus.UNAUTHORIZED:
                st.error(
                    'Token inválido ou expirado. \n\n'
                    'Verifique o token de acesso à API OpenWeatherMap \n'
                    'e atualize a variável de'
                    ' ambiente (OPEN_WEATHER_MAP_API_KEY)'
                    ' de teu sistema operacional.',
                )
                st.stop()
            case HTTPStatus.NOT_FOUND:
                st.warning(
                    f'Informações não encontradas para a cidade "{city}".',
                )
                st.stop()
            case HTTPStatus.TOO_MANY_REQUESTS:
                st.warning(
                    'Mais de 60 requisições por minuto para API'
                    ' no plano gratuíto. Tente novamente mais tarde.',
                )
                st.stop()

    clima_atual = result.json()['weather'][0]['description']
    icon = result.json()['weather'][0]['icon']
    temperatura = result.json()['main']['temp']
    sensacao_termica = result.json()['main']['feels_like']
    umidade = result.json()['main']['humidity']
    cobertura_nuvens = result.json()['clouds']['all']

    st.subheader(f'Clima atual em {city}')
    col1, col2 = st.columns([0.4, 0.6])
    with col1:
        st.image(f'https://openweathermap.org/img/wn/{icon}@2x.png')
    with col2:
        st.metric(label='Clima', value=clima_atual)

    (
        col1,
        col2,
    ) = st.columns(2)
    with col1:
        st.metric(label='Temperatura', value=f'{temperatura} °C')
        st.metric(label='Sensação térmica', value=f'{sensacao_termica} °C')
    with col2:
        st.metric(label='Umidade', value=f'{umidade} %')
        st.metric(label='Cobertura de nuvens', value=f'{cobertura_nuvens} %')


if __name__ == '__main__':
    main()
