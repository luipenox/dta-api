import streamlit as st
import json

st.title("JSON v Pythonu - Kompletní průvodce")

st.header("Co je JSON?")
st.write("""
JSON (JavaScript Object Notation) je lehký, textový formát pro výměnu dat. Je nezávislý na programovacím jazyce 
a snadno čitelný jak pro lidi, tak pro počítače [[1]](https://www.datacamp.com/tutorial/json-data-python).

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
        #
        Uložení do souboru
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# Načtení ze souboru
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
        """, language="python")

st.header("Praktické příklady použití")

st.subheader("1. Konfigurace aplikace")
st.code("""
# config.json
{
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    },
    "api_key": "xxx-xxx-xxx",
    "debug_mode": true
}
""", language="json")

st.subheader("2. API Response")
st.code("""
# Příklad práce s API odpovědí
import requests

response = requests.get('https://api.example.com/data')
json_data = response.json()  # Automatická konverze JSON odpovědi
""", language="python")

st.header("Tipy a triky")
st.write("""
1. **Práce s velkými JSON soubory** [[2]](https://realpython.com/python-json/):
   ```python
   import ijson  # Pro velké soubory

   with open('large_file.json', 'rb') as f:
       parser = ijson.parse(f)
       for prefix, event, value in parser:
           # Zpracování dat po částech
           pass
   ```

2. **Formátování JSON výstupu:**
   ```python
   # Hezky formátovaný výstup
   json_string = json.dumps(data, 
                          indent=4, 
                          sort_keys=True, 
                          ensure_ascii=False)
   ```

3. **Ošetření chyb:**
   ```python
   try:
       data = json.loads(json_string)
   except json.JSONDecodeError as e:
       print(f"Chyba při parsování JSON: {e}")
   ```
""")

st.header("Nejlepší praktiky")
st.write("""
✅ Vždy používejte proper encoding (UTF-8)
✅ Ošetřujte možné chyby při parsování
✅ Pro velké soubory používejte streamování
✅ Používejte indent pro čitelnost
✅ Validujte JSON data před zpracováním
""")

st.header("Časté problémy a řešení")
problems = {
    "Problém s českými znaky": "Použijte ensure_ascii=False",
    "Velké JSON soubory": "Použijte knihovnu ijson",
    "Nevalidní JSON": "Použijte online JSON validátor",
    "Složité vnořené struktury": "Použijte knihovnu jmespath"
}

for problem, solution in problems.items():
    st.write(f"**{problem}:** {solution}")

st.header("Užitečné nástroje")
st.write("""
- **jsonlint**: Online validátor JSON
- **jq**: Nástroj pro práci s JSON v příkazové řádce
- **jmespath**: Knihovna pro dotazování JSON dat
- **json.tool**: Vestavěný nástroj Pythonu pro formátování JSON
""")

# Interaktivní demo
st.header("Interaktivní JSON validátor")
user_input = st.text_area("Vložte JSON k validaci:", "{\"příklad\": \"data\"}")
if st.button("Validovat"):
    try:
        parsed = json.loads(user_input)
        st.success("JSON je validní!")
        st.json(parsed)
    except json.JSONDecodeError as e:
        st.error(f"Nevalidní JSON: {str(e)}")