import streamlit as st

st.title("Úvod do API")

st.header("Co je API?")
st.write("""
API (Application Programming Interface) je sada standardizovaných pravidel a protokolů, které umožňují různým softwarovým 
aplikacím vzájemně komunikovat. 

**Představte si API jako číšníka v restauraci**:
- Vy (klient) si objednáváte jídlo
- Číšník (API) přijme vaši objednávku
- Předá ji do kuchyně (server)
- A přinese vám hotové jídlo zpět
""")

st.header("REST API")
st.write("""
   - Nejrozšířenější typ API
   - Používá HTTP metody (GET, POST, PUT, PATCH, DELETE)
   - Jednoduchá a standardizovaná komunikace
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
   - Obsahuje stavový kód HTTP (např. 200 pro úspěch)
""")

st.header("Příklady využití API")
st.write("""
# Příklady využití REST API

### 1. Sociální sítě
- **Správa obsahu**
  - Získávání příspěvků a komentářů
  - Publikování nového obsahu
  - Správa profilů
- **Interakce**
  - Lajkování
  - Sdílení
  - Komentování

### 2. E-commerce
- **Produktový management**
  - Správa katalogu
  - Aktualizace cen
  - Správa skladových zásob
- **Objednávky**
  - Vytváření objednávek
  - Sledování stavu
  - Správa plateb

### 3. Finanční služby
- **Bankovnictví**
  - Platební transakce
  - Kontrola zůstatku
  - Historie transakcí
- **Investice**
  - Kurzovní data
  - Správa portfolia
  - Obchodování s akciemi

### 4. Geolokační služby
- **Mapy**
  - Vyhledávání míst
  - Navigace
  - Výpočet tras
- **Počasí**
  - Aktuální počasí
  - Předpověď
  - Meteorologická data

### 5. IoT (Internet věcí)
- **Správa zařízení**
  - Monitoring stavu
  - Ovládání zařízení
  - Aktualizace firmware
- **Data**
  - Sběr dat ze senzorů
  - Analýza dat
  - Reporting

### 6. Streamovací služby
- **Obsah**
  - Katalog médií
  - Správa playlistů
  - Doporučení
- **Uživatelé**
  - Historie sledování
  - Hodnocení
  - Preference

### 7. Rezervační systémy
- **Ubytování**
  - Dostupnost pokojů
  - Rezervace
  - Správa pobytů
- **Doprava**
  - Letecké rezervace
  - Jízdenky
  - Pronájem vozidel

### 8. Mobilní aplikace
- **Uživatelé**
  - Registrace
  - Autentizace
  - Správa profilů
- **Data**
  - Synchronizace
  - Push notifikace
  - Zálohování

### 9. Cloud computing
- **Infrastruktura**
  - Správa serverů
  - Monitoring služeb
  - Škálování
- **Storage**
  - Ukládání souborů
  - Zálohování
  - Sdílení dat

### 10. CMS systémy
- **Obsah**
  - Publikování článků
  - Správa médií
  - Kategorizace
- **Interakce**
  - Komentáře
  - Hodnocení
  - SEO nástroje
""")

st.header("Výhody používání API")
st.write("""
### 1. Standardizace
- **Jednotné rozhraní**
  - Konzistentní způsob komunikace
  - Předvídatelné chování
  - Snadná integrace
- **Dokumentace**
  - Jasně definované endpointy
  - Popis parametrů a odpovědí
  - Příklady použití

### 2. Bezpečnost
- **Řízení přístupu**
  - Autentizace uživatelů
  - Autorizace požadavků
  - API klíče a tokeny
- **Ochrana dat**
  - Šifrování komunikace
  - Validace vstupů
  - Rate limiting

### 3. Škálovatelnost
- **Výkon**
  - Rozdělení zátěže
  - Cachování
  - Optimalizace dotazů
- **Flexibilita**
  - Horizontální škálování
  - Load balancing
  - Mikroslužby architektura

### 4. Efektivita vývoje
- **Znovupoužitelnost**
  - Sdílení funkcionalit
  - Modulární přístup
  - Oddělení zodpovědností
- **Údržba**
  - Snadné aktualizace
  - Verzování API
  - Monitoring a logování

### 5. Multiplatformní přístup
- **Nezávislost**
  - Různé programovací jazyky
  - Různé operační systémy
  - Různá zařízení
- **Kompatibilita**
  - Webové aplikace
  - Mobilní aplikace
  - Desktop aplikace

### 6. Integrace služeb
- **Propojení systémů**
  - Třetí strany
  - Interní služby
  - Cloud služby
- **Automatizace**
  - Webhooky
  - Události
  - Workflow

### 7. Byznys přínosy
- **Monetizace**
  - Placený přístup k API
  - Freemium model
  - Pay-as-you-go
- **Partnerství**
  - B2B integrace
  - Marketplace
  - Ekosystém

### 8. Testovatelnost
- **Kvalita**
  - Automatické testy
  - Dokumentované chování
  - Simulace chyb
- **Vývoj**
  - Sandbox prostředí
  - Mock služby
  - API testing tools

### 9. Monitoring
- **Výkonnost**
  - Metriky
  - Alerting
  - Diagnostika
- **Využití**
  - Statistiky používání
  - Analýza trendů
  - ROI měření

### 10. Inovace
- **Agilnost**
  - Rychlé změny
  - A/B testování
  - Feature flags
- **Experimentování**
  - Prototypování
  - Beta testing
  - Zpětná vazba
""")