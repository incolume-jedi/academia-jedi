"""Streamlit app for Academia Jedi 20250605 project."""

import streamlit as st
from ajedi20250606_acesso_openweather import auth_token


def main():
    st.title('Web App Climatológico')
    st.write('Dados disponibilizados pela OpenWeatherMap (https://openweathermap.org/current)')

    city = st.text_input('Informe o nome da cidade', key='city', value='Brasília')

    if not city:
        st.stop()

    try:
        result = auth_token(city=city, token='2126063e2374e8abb4c56139559f6f79')
    except Exception as e:
        raise
        st.warning(f'Informações não disponíveis para a cidade "{city}".')
        st.stop()

    ic(result.json())


if __name__ == '__main__':
    main()
