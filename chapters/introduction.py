import streamlit as st

st.title("API - Aplikační programové rozhraní")

st.header("Co je API?")
st.write("""
API (Application Programming Interface) je sada standardizovaných pravidel a protokolů, které umožňují různým softwarovým 
aplikacím vzájemně komunikovat [[1]](https://www.redhat.com/en/topics/api/what-is-a-rest-api). 

Představte si API jako číšníka v restauraci:
- Vy (klient) si objednáváte jídlo
- Číšník (API) přijme vaši objednávku
- Předá ji do kuchyně (server)
- A přinese vám hotové jídlo zpět
""")

st.header("Typy API")
st.write("""
1. **REST API**
   - Nejrozšířenější typ API
   - Používá HTTP metody (GET, POST, PUT, DELETE)
   - Jednoduchá a standardizovaná komunikace

2. **SOAP API**
   - Starší, ale stále používaný protokol
   - Složitější než REST
   - Vysoká bezpečnost

3. **GraphQL**
   - Moderní přístup k API
   - Klient si přesně určuje, jaká data chce získat
   - Používají ho společnosti jako GitHub, Shopify nebo The New York Times [[2]](https://www.altexsoft.com/blog/what-is-api-definition-types-specifications-documentation/)
""")

st.header("Jak API funguje?")
st.write("""
1. **Požadavek (Request)**
   - Klient pošle požadavek na server
   - Obsahuje metodu (GET, POST, atd.)
   - Může obsahovat data nebo parametry

2. **Zpracování**
   - Server přijme požadavek
   - Zpracuje ho podle definovaných pravidel

3. **Odpověď (Response)**
   - Server pošle zpět odpověď
   - Obvykle ve formátu JSON nebo XML
   - Obsahuje stavový kód (např. 200 pro úspěch)
""")

st.header("Příklady využití API")
st.write("""
- Platební brány
- Sociální sítě (sdílení obsahu)
- Předpověď počasí
- Mapové služby
- Rezervační systémy
- Streamovací služby
""")

st.header("Výhody používání API")
st.write("""
✅ Znovupoužitelnost kódu
✅ Standardizace
✅ Bezpečnost
✅ Škálovatelnost
✅ Flexibilita
✅ Efektivita vývoje
""")

st.header("Nejlepší praktiky při práci s API")
st.write("""
1. **Dokumentace**
   - Vždy čtěte a udržujte aktuální dokumentaci

2. **Zabezpečení**
   - Používejte autentizaci a autorizaci
   - Šifrujte citlivá data

3. **Verzování**
   - Udržujte kompatibilitu se staršími verzemi

4. **Monitoring**
   - Sledujte výkon a chyby

5. **Cachování**
   - Implementujte chytré cachování pro lepší výkon
""")

st.header("Závěr")
st.write("""
API je klíčovou technologií moderního softwaru, která umožňuje efektivní propojení různých aplikací a služeb. 
Díky API můžeme vytvářet modulární, škálovatelné a udržitelné aplikace.
""")