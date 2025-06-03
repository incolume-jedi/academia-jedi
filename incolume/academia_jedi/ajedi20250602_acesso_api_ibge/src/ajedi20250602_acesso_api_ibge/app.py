"""Web app."""

import pandas as pd
import streamlit as st
from ajedi20250602_acesso_api_ibge import get_nome
from icecream import ic

ic.configureOutput(prefix='[ajedi20250602-acesso-api-ibge] ')


def main():
    """Main function to run the Streamlit app."""
    st.title('Web App Nomes')
    st.write(
        'Dados da API IBGE (https://servicodados.ibge.gov.br/api/docs/nomes?versao=2)'
    )

    nome = st.text_input('Consulte um nome')
    if not nome:
        st.stop()

    try:
        dict_values = {}
        for x in get_nome(nome)[0]['res']:
            k, v = x.values()
            dict_values[k] = v
    except KeyError:
        st.warning(f'Nenhum dado encontradao para {nome}.')
        st.stop()

    ic(dict_values)
    df_names = pd.DataFrame.from_dict(
        dict_values, orient='index', columns=['Frequência']
    )

    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.write('Frequência por década')
        st.dataframe(df_names)
    with col2:
        st.write('Evolução por tempo')
        st.line_chart(df_names)


if __name__ == '__main__':
    main()
