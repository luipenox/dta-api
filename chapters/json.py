import streamlit as st
import json

st.title("JSON v Pythonu")

st.header("Co je JSON?")
st.write("""
JSON (JavaScript Object Notation) je lehký, textový formát pro výměnu dat.
Je nezávislý na programovacím jazyce a snadno čitelný jak pro lidi, tak pro počítače.

Základní charakteristiky:
- Jednoduchá syntaxe
- Univerzální použití
- Podporován většinou programovacích jazyků
- Běžně používaný ve webových API
""")

st.header("Struktura JSON")
st.write("""
JSON podporuje následující datové typy:
- Objekty (slovníky) `{}`
- Pole (seznamy) `[]`
- Řetězce `"text"`
- Čísla `42`, `3.14`
- Boolean hodnoty `true`, `false`
- Null `null`
""")

st.header("Práce s JSON v Pythonu")
st.code("""
# Importování JSON modulu
import json

# Příklad JSON dat
data = {
    "jméno": "Jan",
    "věk": 30,
    "město": "Praha",
    "aktivní": True,
    "koníčky": ["sport", "hudba", "čtení"]
}

# Převod Python objektu na JSON řetězec
json_string = json.dumps(data, indent=4, ensure_ascii=False)

# Převod JSON řetězce zpět na Python objekt
python_dict = json.loads(json_string)
""", language="python")

st.header("Ukládání a načítání JSON souborů")
st.code("""
# Uložení do souboru
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# Načtení ze souboru
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
""", language="python")

st.header("Ukázky formátu JSON")
st.write("### 1. Základní JSON objekty")
st.code("""
# Jednoduchý JSON objekt
{
    "jméno": "Jan Novák",
    "věk": 30,
    "aktivní": true,
    "výška": 180.5,
    "email": null
}

# JSON pole
[
    "jablko",
    "banán",
    "pomeranč"
]
""", language="json")

st.write("### 2. Vnořené struktury")
st.code("""
{
    "osoba": {
        "jméno": "Jan",
        "příjmení": "Novák",
        "adresa": {
            "ulice": "Hlavní 123",
            "město": "Praha",
            "PSČ": "12000"
        }
    },
    "koníčky": ["sport", "hudba", "čtení"],
    "kontakty": {
        "email": ["jan@example.com", "novak@firma.cz"],
        "telefon": {
            "osobní": "123456789",
            "pracovní": "987654321"
        }
    }
}
""", language="json")

st.write("### 3. Pole objektů")
st.code("""
{
    "zaměstnanci": [
        {
            "id": 1,
            "jméno": "Jan Novák",
            "pozice": "vývojář",
            "plat": 50000
        },
        {
            "id": 2,
            "jméno": "Marie Veselá",
            "pozice": "designér",
            "plat": 45000
        }
    ]
}
""", language="json")

st.write("### 4. Konfigurace aplikace")
st.code("""
{
    "databáze": {
        "host": "localhost",
        "port": 5432,
        "název": "moje_db",
        "přihlášení": {
            "uživatel": "admin",
            "heslo": "****"
        }
    },
    "api": {
        "url": "https://api.example.com",
        "klíč": "abc123",
        "timeout": 30
    },
    "nastavení": {
        "debug": true,
        "cache": {
            "povoleno": true,
            "doba_platnosti": 3600
        }
    }
}
""", language="json")

st.write("### 5. API Response")
st.code("""
{
    "status": "success",
    "code": 200,
    "data": {
        "produkty": [
            {
                "id": "p123",
                "název": "Notebook",
                "cena": 25000,
                "skladem": true,
                "specifikace": {
                    "procesor": "Intel i5",
                    "ram": "8GB",
                    "disk": "512GB SSD"
                }
            },
            {
                "id": "p124",
                "název": "Myš",
                "cena": 599,
                "skladem": false,
                "specifikace": {
                    "typ": "bezdrátová",
                    "dpi": 1600,
                    "barva": "černá"
                }
            }
        ],
        "metadata": {
            "celkem": 2,
            "stránka": 1,
            "limit": 10
        }
    }
}
""", language="json")