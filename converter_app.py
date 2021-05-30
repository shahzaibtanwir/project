import streamlit as st
from multiapp import MultiApp
from apps import home, cmtoinch, inchtofeet, nanotomicro, metertokm, kmtomile, C2F, k2c, k2f, ML2L, mg2g, g2kg, pound2ounce, gram2carrat 

app = MultiApp()

st.title("  Unit Converter App ")
st.subheader("Ceated by Shahzaib Tanwir")

app.add_app("Home", home.app)
app.add_app("Centimeter to Inch ", cmtoinch.app)
app.add_app("Inch to Feet", inchtofeet.app)
app.add_app("Nanometer  to Micrometer", nanotomicro.app)
app.add_app("Meter to Kilometer", metertokm.app)
app.add_app("Kilometer to Miles", kmtomile.app)
app.add_app("Celsius to Fahrenheit ", C2F.app)
app.add_app("Kelvin to Celsius", k2c.app)
app.add_app("Kelvin to fahrenheit", k2f.app)
app.add_app("Milliliter to Liter", ML2L.app)
app.add_app("Milligram to Gram", mg2g.app)
app.add_app("Gram to kilogram", g2kg.app)
app.add_app("Pound to Ounces", pound2ounce.app)
app.add_app("Gram to Carats", gram2carrat.app)


app.run()