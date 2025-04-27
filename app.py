import streamlit as st


def home():
    st.title('API')


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


page_dict = {'Kapitoly': [
    introduction,
    json
]}

home_page = st.Page(home, title="O kurzu", icon=":material/info:")
contact_page = st.Page(contact, title="Kontakt", icon=":material/import_contacts:")

account_pages = [home_page, contact_page]

pg = st.navigation({"Informace": account_pages} | page_dict)
pg.run()