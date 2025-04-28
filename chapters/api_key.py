import streamlit as st

st.title("API Autentizace - Token a API Key")

st.header("1. API Key")
st.write("""
**API Key** je jednoduchý způsob autentizace pomocí unikátního klíče.

#### Charakteristiky:
- Jednoduchý na implementaci
- Statický klíč
- Často používaný pro veřejná API
- Méně bezpečný než tokeny

#### Použití v hlavičce požadavku:
""")

st.code("""
headers = {
    'X-Api-Key': 'vaš_api_klíč_zde',
    'Content-Type': 'application/json'
}

response = requests.get('https://api.příklad.cz/data', headers=headers)
""", language="python")

st.write("#### Použití jako URL parametr:")
st.code("""
url = 'https://api.příklad.cz/data?api_key=vaš_api_klíč_zde'
response = requests.get(url)
""", language="python")

st.header("2. Token (Bearer Token)")
st.write("""
**Token** je modernější způsob autentizace, často používaný ve formě JWT (JSON Web Token).

#### Charakteristiky:
- Časově omezená platnost
- Může obsahovat additional informace (claims)
- Běžně používaný v OAuth 2.0
- Bezpečnější než API Key

#### Použití v hlavičce požadavku:
""")

st.code("""
headers = {
    'Authorization': 'Bearer váš_token_zde',
    'Content-Type': 'application/json'
}

response = requests.get('https://api.příklad.cz/data', headers=headers)
""", language="python")

st.header("3. Rozdíly mezi Token a API Key")

col1, col2 = st.columns(2)

with col1:
    st.subheader("API Key")
    st.write("""
    ✅ Jednoduchý na použití
    ✅ Trvalá platnost
    ✅ Vhodný pro jednoduché API
    ❌ Méně bezpečný
    ❌ Obtížná revokace
    ❌ Žádné dodatečné informace
    """)

with col2:
    st.subheader("Token")
    st.write("""
    ✅ Vyšší bezpečnost
    ✅ Časově omezená platnost
    ✅ Může nést další data
    ❌ Složitější implementace
    ❌ Nutnost obnovy
    ❌ Větší režie
    """)

st.header("4. Praktické příklady")

st.subheader("OpenWeatherMap API (API Key)")
st.code("""
import requests

api_key = 'váš_api_klíč_zde'
city = 'Prague'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
data = response.json()
""", language="python")

st.subheader("GitHub API (Bearer Token)")
st.code("""
import requests

token = 'váš_github_token'
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(
    'https://api.github.com/user/repos',
    headers=headers
)
repos = response.json()
""", language="python")