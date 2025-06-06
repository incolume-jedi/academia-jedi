"""Streamlit app for Academia Jedi 20250605 project."""

import streamlit as st
from ajedi20250606_acesso_openweather import auth_token
from icecream import ic
from httpx import HTTPStatusError
from http import HTTPStatus


def main():
    st.title('Web App Climatológico')
    st.write('Dados disponibilizados pela OpenWeatherMap (https://openweathermap.org/current)')

    city = st.text_input('Informe o nome da cidade', key='city', value='Brasília')

    if not city:
        st.stop()

    try:
        result = auth_token(city=city)
        result.raise_for_status()  # Raise an error for bad responses
    except HTTPStatusError:
        match result.status_code:
            case HTTPStatus.UNAUTHORIZED:
                st.error('Token inválido ou expirado. Verifique o token de acesso à API OpenWeatherMap.')
                st.stop()
            case HTTPStatus.NOT_FOUND:
                st.warning(f'Informações encontradas para a cidade "{city}".')
                st.stop()

    ic(result.json())


if __name__ == '__main__':
    main()
