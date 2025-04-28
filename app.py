import streamlit as st


def home():
    st.title('API')

def tools():
    st.title("Užitečné nástroje")
    st.write(
        "[JSONParser](https://jsonparser.org/) - online JSON parser")
    st.write(
        "[REQBIN](https://reqbin.com/) - online nástroj na testování API")

def contact():
    st.title('Kontaktní informace')
    col1, col2 = st.columns(2)

    with col1:
        st.info('Luděk Reif', icon=":material/signature:")
        st.info('+420 720 116 008', icon=":material/call:")
        st.info('luipenox@gmail.com', icon=":material/mail:")
        st.info('https://www.linkedin.com/in/luipenox/', icon=":material/link:")

    with col2:
        st.image('assets/images/luipenox.jpg', width=272)


introduction = st.Page(
    "chapters/introduction.py",
    title="Úvod do API",
    icon=":material/counter_0:")

json = st.Page(
    "chapters/json.py",
    title="JavaScript Object Notation",
    icon=":material/counter_1:")

json_vs_python = st.Page(
    "chapters/json_vs_python.py",
    title="JSON vs. Python",
    icon=":material/counter_2:")

api = st.Page(
    "chapters/api.py",
    title="Základy REST API",
    icon=":material/counter_3:")

api_examples = st.Page(
    "chapters/api_examples.py",
    title="Příklady API",
    icon=":material/counter_4:")

api_python = st.Page(
    "chapters/api_python.py",
    title="REST API v Pythonu",
    icon=":material/counter_5:")

api_key = st.Page(
    "chapters/api_key.py",
    title="Klíč API",
    icon=":material/counter_6:")

assignments = st.Page(
    "chapters/assignments.py",
    title="Cvičení",
    icon=":material/counter_7:")

page_dict = {'Kapitoly': [
    introduction,
    json,
    json_vs_python,
    api,
    api_examples,
    api_python,
    api_key,
    assignments
]}

home_page = st.Page(home, title="O kurzu", icon=":material/info:")
tools_page = st.Page(tools, title="Užitečné nástroje", icon=":material/favorite:")
contact_page = st.Page(contact, title="Kontakt", icon=":material/import_contacts:")

account_pages = [home_page, tools_page, contact_page]

pg = st.navigation({"Informace": account_pages} | page_dict)
pg.run()
