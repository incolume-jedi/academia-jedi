"""Streamlit app for Academia Jedi 20250605 project."""

import streamlit as st
from ajedi20250605_streamlit_docker import main

st.title("Academia Jedi 20250605")
st.write("Streamlit App")

st.write(main())
