"""Streamlit app for Academia Jedi 20250605 project."""

import streamlit as st
from ajedi20250606_acesso_openweather import auth_token


def main():
    st.title('Web App Climatológico')
    st.write('Dados disponibilizados pela OpenWeatherMap (https://openweathermap.org/current)')

    st.write(auth_token())


if __name__ == '__main__':
    main()
