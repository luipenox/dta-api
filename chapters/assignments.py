import streamlit as st

st.title("Příklady na REST API v Pythonu")

st.markdown("""
Pro tyto příklady budeme používat následující API:
- JSONPlaceholder (https://jsonplaceholder.typicode.com)
- REST Countries (https://restcountries.com)
- Dog API (https://dog.ceo/dog-api)
""")

st.header("Příklad 1: Získání seznamu příspěvků")
st.markdown("""
**Zadání:**
Načtěte prvních 5 příspěvků z JSONPlaceholder API a vypište jejich titulky a texty.

**Nápověda:**
- Použijte endpoint `/posts`
- Použijte metodu GET
- Data přijdou ve formátu JSON
""")

with st.expander("Zobrazit řešení"):
    st.code("""
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    for post in posts[:5]:
        print(f"Titulek: {post['title']}")
        print(f"Text: {post['body']}")
        print("---")
    """, language="python")

st.header("Příklad 2: Vyhledání země podle názvu")
st.markdown("""
**Zadání:**
Vytvořte program, který načte informace o zadané zemi (název, hlavní město, populace, měna).

**Nápověda:**
- Použijte endpoint `/name/{country}`
- Zpracujte možnost, že země nebude nalezena
- Vypište základní informace o zemi
""")

with st.expander("Zobrazit řešení"):
    st.code("""
import requests

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        return {
            "název": data['name']['common'],
            "hlavní město": data['capital'][0],
            "populace": data['population'],
            "měny": list(data['currencies'].keys())
        }
    else:
        return None

# Příklad použití
info = get_country_info("czech")
if info:
    for key, value in info.items():
        print(f"{key}: {value}")
    """, language="python")

st.header("Příklad 3: Seznam komentářů k příspěvku")
st.markdown("""
**Zadání:**
Načtěte všechny komentáře k zadanému příspěvku z JSONPlaceholder API a vypište email autora a text komentáře.

**Nápověda:**
- Použijte endpoint `/posts/{id}/comments`
- Seřaďte komentáře podle emailu
- Ošetřete neexistující ID příspěvku
""")

with st.expander("Zobrazit řešení"):
    st.code("""
import requests

def get_post_comments(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
    response = requests.get(url)

    if response.status_code == 200:
        comments = response.json()
        # Seřazení podle emailu
        comments.sort(key=lambda x: x['email'])

        for comment in comments:
            print(f"Od: {comment['email']}")
            print(f"Komentář: {comment['body']}")
            print("---")
    else:
        print("Příspěvek nebyl nalezen")

# Příklad použití
get_post_comments(1)
    """, language="python")

st.header("Příklad 4: Náhodné obrázky psů podle plemene")
st.markdown("""
**Zadání:**
Vytvořte program, který zobrazí 3 náhodné obrázky zadaného plemene psa.

**Nápověda:**
- Použijte Dog API endpoint `/breed/{breed}/images/random/3`
- Ošetřete neexistující plemeno
- Vypište URL obrázků
""")

with st.expander("Zobrazit řešení"):
    st.code("""
import requests

def get_dog_images(breed, count=3):
    url = f"https://dog.ceo/api/breed/{breed}/images/random/{count}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return data['message']
        else:
            return None
    return None

# Příklad použití
breed = "husky"
images = get_dog_images(breed)
if images:
    print(f"Obrázky plemene {breed}:")
    for url in images:
        print(url)
else:
    print("Plemeno nenalezeno")
    """, language="python")

st.header("Příklad 5: Statistika příspěvků uživatele")
st.markdown("""
**Zadání:**
Vypočítejte statistiku příspěvků zadaného uživatele (počet příspěvků, nejdelší příspěvek, nejkratší příspěvek).

**Nápověda:**
- Použijte endpoint `/users/{id}/posts`
- Počítejte délku těla příspěvku
- Vytvořte přehledný výstup statistiky
""")

with st.expander("Zobrazit řešení"):
    st.code("""
import requests

def get_user_posts_stats(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        if not posts:
            return None

        stats = {
            "počet_příspěvků": len(posts),
            "nejdelší": max(posts, key=lambda x: len(x['body']))['body'],
            "nejkratší": min(posts, key=lambda x: len(x['body']))['body']
        }
        return stats
    return None

# Příklad použití
stats = get_user_posts_stats(1)
if stats:
    print(f"Počet příspěvků: {stats['počet_příspěvků']}")
    print(f"Nejdelší příspěvek: {stats['nejdelší'][:100]}...")
    print(f"Nejkratší příspěvek: {stats['nejkratší']}")
    """, language="python")

st.header("Příklad 6: Seznam zemí v regionu")
st.markdown("""
**Zadání:**
Získejte seznam všech zemí v zadaném regionu a seřaďte je podle populace.

**Nápověda:**
- Použijte endpoint `/region/{region}`
- Regiony: Africa, Americas, Asia, Europe, Oceania
- Seřaďte země sestupně podle populace
""")

with st.expander("Zobrazit řešení"):
    st.code("""
import requests

def get_countries_in_region(region):
    url = f"https://restcountries.com/v3.1/region/{region}"
    response = requests.get(url)

    if response.status_code == 200:
        countries = response.json()
        # Seřazení podle populace sestupně
        countries.sort(key=lambda x: x['population'], reverse=True)

        for country in countries:
            print(f"{country['name']['common']}: {country['population']:,} obyvatel")
    else:
        print("Region nebyl nalezen")

# Příklad použití
get_countries_in_region("Europe")
    """, language="python")

st.header("Příklad 7: Informace o uživateli a jeho úkoly")
st.markdown("""
**Zadání:**
Načtěte informace o uživateli a jeho nesplněné úkoly.

**Nápověda:**
- Použijte endpointy `/users/{id}` a `/users/{id}/todos`
- Filtrujte nesplněné úkoly (completed = False)
- Vytvořte přehledný výstup
""")

with st.expander("Zobrazit řešení"):
    st.code("""
import requests

def get_user_todos(user_id):
    # Získání informací o uživateli
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)

    # Získání úkolů uživatele
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todos_response = requests.get(todos_url)

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user = user_response.json()
        todos = todos_response.json()

        # Filtrování nesplněných úkolů
        incomplete_todos = [todo for todo in todos if not todo['completed']]

        print(f"Uživatel: {user['name']} ({user['email']})")
        print(f"Počet nesplněných úkolů: {len(incomplete_todos)}")
        print("\nNesplněné úkoly:")
        for todo in incomplete_todos:
            print(f"- {todo['title']}")
    else:
        print("Uživatel nebyl nalezen")

# Příklad použití
get_user_todos(1)
    """, language="python")
