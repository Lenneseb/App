import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date

# Set page configuration
st.set_page_config(page_title="My Contacts", page_icon="🎂", layout="wide")

def init_dataframe():
    """Initialize or load the dataframe."""
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame(columns=['Name', 'Birth Date', 'Age'])

def calculate_age(birth_date):
    """Calculate age given the birth date."""
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def add_entry(name, birth_date):
    """Add a new entry to the DataFrame using pd.concat and calculate age."""
    age = calculate_age(birth_date)
    new_entry = pd.DataFrame([{'Name': name, 'Birth Date': birth_date, 'Age': age}])
    st.session_state.df = pd.concat([st.session_state.df, new_entry], ignore_index=True)

def display_dataframe():
    """Display the DataFrame in the app."""
    if not st.session_state.df.empty:
        st.dataframe(st.session_state.df)
    else:
        st.write("No data to display.")

def plot_data():
    """Plot the age data using Pandas' plotting capabilities."""
    if not st.session_state.df.empty:
        df = st.session_state.df
        ax = df.plot(kind='barh', x='Name', y='Age', title = "Age", legend=False)
        st.pyplot(ax.figure)
    else:
        st.write("No data to display.")

def main():
    st.title("My Contacts App")

    init_dataframe()

    with st.sidebar:
        st.header("Add New Entry")
        name = st.text_input("Name")
        birth_date = st.date_input("Birth Date",min_value=date(1950, 1, 1),format="DD.MM.YYYY")
        add_button = st.button("Add")

    if add_button and name:  # Check if name is not empty
        add_entry(name, birth_date)

    display_dataframe()
    plot_data()

st.title('Willkommen zum Age Calculator')
st.text('Gib links dein Name und dein Geburtsdatum ein und wir berechen wie alt du bist.')
st.write('Du bist der erst Besucher heute* :sunglasses:')

st.title('Probieren wir mal ein Data Element aus')
st.text('Spielen wir mal etwas mit Zahlen rum.')
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)

st.title('Probieren wir mal ein Chart Element aus')
st.text('Keine Ahnung was das Darstellen soll aber es sieht cool aus.')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

st.title('Jetzt versuchen wir mal ein Input Element')
st.text('Sei so lieb und unterstütze den Entwickler: Mich :)')

st.button("Erneut versuchen", type="primary")
if st.button('Liebe Grüsse an den Entwickler'):
    st.write('Danke schön')
else:
    st.write('Vielleicht ein anderes Mal')

st.title('Nun eine Sidebar und einen Container')
add_selectbox = st.sidebar.selectbox(
    "Wie findest du diese Website?",
    ("Genial", "Super", "Toll")
)

add_selectbox = st.sidebar.selectbox(
    "Wie ist das Programmieren so?",
    ("Spanned", "Langweilig", "Super")
)

container = st.container(border=True)
container.write("Das ist drin")
st.write("Das ist nicht mehr drin")

container.write("Das ist auch noch drin")

st.text('So das war jetzt viel rumspielen,hier gehts endlich zum deinem Alter und dem Graphen dazu. Viel Spass!')

if __name__ == "__main__":
    main()
