"""Main script for this module."""

import streamlit as st
from ajedi20250607_docker_subprojetos import main


def app():
    """Main function to run the Streamlit app."""
    st.title('Docker Subprojetos')
    st.markdown('---')
    st.write('This is a simple Streamlit app for Docker Subprojetos.')
    st.write(main())


if __name__ == '__main__':
    app()
