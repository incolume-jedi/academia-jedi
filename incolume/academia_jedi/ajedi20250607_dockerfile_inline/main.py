"""APP Module."""

import streamlit as st
from ajedi20250607_dockerfile_inline import main


def app():
    """Main function to run the Streamlit app."""
    st.title('Academia Jedi 20250607 Dockerfile Inline')
    st.markdown('---')

    st.write('This is a simple Streamlit app running inline with Dockerfile.')
    st.write(main())
    st.write(
        'This app is designed to demonstrate how to run a'
        ' Streamlit app inline with a Dockerfile.',
    )


if __name__ == '__main__':
    app()
