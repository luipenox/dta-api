import streamlit as st
import requests

st.title("Veřejně dostupná API - Příklady")

st.header("1. Jednoduché API bez autentizace")

# ČNB
st.subheader("Kurz ČNB")
st.code("""
# Kurzy ČNB k 31.10.2022
"https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt?date=31.10.2022"
""")

# Kočky
st.subheader("Cat API")
st.code("""
# Náhodný obrázek kočky
"https://api.thecatapi.com/v1/images/search"
""")

# Země
st.subheader("REST Countries")
st.code("""
# Informace o České republice
"https://restcountries.com/v3.1/name/czech"

# Všechny země v Evropě
"https://restcountries.com/v3.1/region/europe"
""")

# Citáty
st.subheader("Quotable")
st.code("""
# Náhodný citát
"https://api.quotable.io/random"

# Seznam autorů
"https://api.quotable.io/authors"
""")

st.header("2. API pro vývojáře")

# GitHub
st.subheader("GitHub API")
st.code("""
# Seznam repozitářů uživatele
"https://api.github.com/users/USERNAME/repos"

# Informace o konkrétním repozitáři
"https://api.github.com/repos/OWNER/REPO"
""")

# JSON Placeholder
st.subheader("JSONPlaceholder (testovací API)")
st.code("""
# Seznam příspěvků
"https://jsonplaceholder.typicode.com/posts"

# Konkrétní příspěvek
"https://jsonplaceholder.typicode.com/posts/1"

# Komentáře k příspěvku
"https://jsonplaceholder.typicode.com/posts/1/comments"
""")