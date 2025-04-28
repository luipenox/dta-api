import streamlit as st
import requests
import json

st.title("Základy práce s API v Pythonu")

st.header("Co je REST API?")
st.write("""
**REST** je zkratka pro **RE**presentational **S**tate **T**ransfer

🔍 **Co jednotlivá slova znamenají:**

- **Representational** (Reprezentační):
  - Data jsou reprezentována v určitém formátu (nejčastěji JSON nebo XML)
  - Reprezentace zdrojů je oddělena od jejich skutečné podoby na serveru

- **State** (Stav):
  - Každý požadavek obsahuje všechny informace potřebné k jeho zpracování
  - Server si nepamatuje stav mezi jednotlivými požadavky (bezstavovost)

- **Transfer** (Přenos):
  - Přenos dat mezi klientem a serverem
  - Využívá standardní HTTP metody (GET, POST, PUT, PATCH, DELETE)
""")

st.info("""
💡 **Zjednodušeně řečeno:**
REST API je způsob, jakým webové služby komunikují přes internet pomocí standardizovaných pravidel pro přenos dat a stavů mezi systémy.
""")

st.header("HTTP Metody")
st.write("""
Základní HTTP metody používané v REST API:

- **GET**: Získání dat
- **POST**: Vytvoření nových dat  
- **PUT**: Kompletní aktualizace existujících dat
- **PATCH**: Částečná aktualizace dat
- **DELETE**: Smazání dat
""")

st.header("HTTP Stavové kódy")
st.write("""
Nejčastější stavové kódy:

- **2xx** - Úspěch
  - 200: OK
  - 201: Vytvořeno
  - 204: Žádný obsah

- **4xx** - Chyba klienta
  - 400: Špatný požadavek
  - 401: Neautorizováno
  - 403: Zakázáno
  - 404: Nenalezeno

- **5xx** - Chyba serveru
  - 500: Interní chyba serveru
  - 503: Služba nedostupná
""")

st.info("""
Pro vysvětlení stavových kódu můžeme použít třeba [http.cat](https://http.cat), kde je vše vysvětleno pomocí koček..""")