import streamlit as st
import requests

st.title("Základy práce s API v Pythonu - Příklady")

st.header("1. Získání dat pomocí GET")

st.subheader("Příklad: Náhodný fakt o kočce")
st.code("""
import requests

# Jednoduchý GET požadavek
url = "https://catfact.ninja/fact"
response = requests.get(url)

# Kontrola úspěšnosti požadavku
if response.status_code == 200:
    data = response.json()
    print(f"Citát: {data['fact']}")
""", language="python")

# Live ukázka
if st.button("Získat náhodný citát"):
    try:
        response = requests.get("https://catfact.ninja/fact")
        if response.status_code == 200:
            data = response.json()
            st.success(f"{data['fact']}")
    except:
        st.error("Nepodařilo se získat citát")

st.header("2. Práce s parametry v URL")

st.subheader("Příklad: Informace o zemi")
st.code("""
# GET požadavek s parametrem v URL
country = "czech"
url = f"https://restcountries.com/v3.1/name/{country}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()[0]  # Bereme první výsledek
    print(f"Název: {data['name']['common']}")
    print(f"Hlavní město: {data['capital'][0]}")
    print(f"Populace: {data['population']:,}")
""", language="python")

# Live ukázka
country_input = st.text_input("Zadejte název země v angličtině:", "czech")
if st.button("Získat informace o zemi"):
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country_input}")
        if response.status_code == 200:
            data = response.json()[0]
            st.write(f"**Název:** {data['name']['common']}")
            st.write(f"**Hlavní město:** {data['capital'][0]}")
            st.write(f"**Populace:** {data['population']:,}")
            st.image(data['flags']['png'], width=200)
    except:
        st.error("Nepodařilo se získat informace o zemi")

st.header("3. Zpracování chyb")

st.subheader("Příklad: Ošetření chyb při požadavku")
st.code("""
try:
    response = requests.get(url, timeout=5)  # Timeout po 5 sekundách

    if response.status_code == 200:
        data = response.json()
        print("Data úspěšně získána")
    elif response.status_code == 404:
        print("Požadovaný zdroj nebyl nalezen")
    elif response.status_code == 500:
        print("Chyba na straně serveru")
    else:
        print(f"Neočekávaná chyba: {response.status_code}")

except requests.exceptions.Timeout:
    print("Požadavek vypršel")
except requests.exceptions.ConnectionError:
    print("Problém s připojením")
except requests.exceptions.RequestException as e:
    print(f"Nastala chyba: {e}")
""", language="python")

st.header("4. Práce s JSONPlaceholder API")

st.subheader("Příklad: Seznam příspěvků")
st.code("""
# Získání seznamu příspěvků
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    for post in posts[:5]:  # Zobrazíme prvních 5 příspěvků
        print(f"Titulek: {post['title']}")
        print(f"Text: {post['body'][:100]}...")
        print("---")
""", language="python")

# Live ukázka
if st.button("Zobrazit příspěvky"):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            posts = response.json()
            for post in posts[:5]:
                st.subheader(post['title'])
                st.write(post['body'])
                st.markdown("---")
    except:
        st.error("Nepodařilo se načíst příspěvky")

st.info("""
💡 **Tipy pro práci s API:**
- Vždy kontrolujte návratové kódy
- Používejte try-except pro ošetření chyb
""")