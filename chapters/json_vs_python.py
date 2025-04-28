import streamlit as st

st.title("JSON vs. Python datové struktury")

st.header("Hlavní rozdíly")

# Tabulka rozdílů
st.table({
    "Vlastnost": [
        "Klíče v objektech",
        "Textové hodnoty",
        "Boolean hodnoty",
        "Null hodnota",
        "Komentáře",
        "Datové typy",
        "Trailing čárky"
    ],
    "JSON": [
        "Pouze v dvojitých uvozovkách",
        'Pouze "double quotes"',
        "true/false",
        "null",
        "Nepodporuje",
        "Omezená sada",
        "Nejsou povoleny"
    ],
    "Python": [
        "Mohou být i bez uvozovek",
        'Podporuje "double" i \'single\'',
        "True/False",
        "None",
        "Podporuje (#)",
        "Široká škála typů",
        "Jsou povoleny"
    ]
})

st.header("Ukázka rozdílů")

col1, col2 = st.columns(2)

with col1:
    st.subheader("JSON")
    st.code('''
{
    "jmeno": "Jan",
    "vek": 30,
    "aktivni": true,
    "kamaradi": ["Petr", "Pavel"],
    "adresa": {
        "mesto": "Praha",
        "psc": "12000"
    },
    "telefon": null
}
''', language="json")

with col2:
    st.subheader("Python")
    st.code('''
{
    'jmeno': "Jan",  # komentář
    "vek": 30,
    'aktivni': True,
    'kamaradi': ['Petr', 'Pavel'],
    'adresa': {
        'mesto': 'Praha',
        'psc': '12000',
    },
    'telefon': None,
}
''', language="python")

st.info("""
🔍 **Klíčové rozdíly v kostce:**
- JSON vyžaduje dvojité uvozovky, Python je flexibilnější
- Python používá True/False/None, JSON používá true/false/null
- Python podporuje více datových typů (např. tuple, set)
- Python umožňuje komentáře a trailing čárky
""")