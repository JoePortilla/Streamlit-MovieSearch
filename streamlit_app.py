# https://youtu.be/az2WnfmqOwo
import streamlit as st
import requests

title = st.text_input('Escribe el título y presiona enter')

if title:
    try:
        # Hacer una request a la API de el titulo de la pelicula
        url = f'http://www.omdbapi.com/?t={title}&apikey={st.secrets.key}'
        re = requests.get(url)
        # Recibir JSON
        re = re.json()

        # Construir Interfaz
        col1, col2 = st.columns([1, 2])
        # Columna 1
        with col1:
            st.image(re['Poster'])
        # Columna 2
        with col2:
            st.subheader(re['Title'])
            st.caption(f"Género: {re['Genre']} Año: {re['Year']}")
            st.write(re['Plot'])
            st.text(f"Calificación: {re['imdbRating']}")
            st.progress(float(re['imdbRating'])/10)
    except:
        st.error('No se ha encontrado alguna pelicula con ese titulo.')
