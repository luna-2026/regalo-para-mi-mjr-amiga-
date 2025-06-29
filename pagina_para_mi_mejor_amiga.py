
import streamlit as st
import base64

# Configuración de la página
st.set_page_config(page_title="Para mi mejor amiga 💖", layout="centered")

# Título principal
st.title("🌸 Para mi mejor amiga 🌸")

# Reproductor de música con autoplay (YouTube embed con autoplay activado)
st.markdown("""
<iframe width="0" height="0" src="https://www.youtube.com/watch?v=1ZOcGs0Ift8&list=RD1ZOcGs0Ift8&start_radio=1&ab_channel=%F0%9D%98%8E%C3%B8%F0%9D%98%A5%F0%9D%98%97%F0%9D%98%A9%F0%9D%98%A2%F0%9D%98%AF%F0%9D%98%B5%C3%B8%F0%9D%98%AE" 
frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
""", unsafe_allow_html=True)

# Carta personalizada
st.markdown("""
### 💌 Una carta para ti

> Querida amiga,  
> Quería dedicarte este pequeño rincón en la web para recordarte lo especial que eres para mí.  
> Cada momento compartido, cada risa, cada conversación ha dejado una huella imborrable en mi corazón.  
> Gracias por ser tú, por estar siempre, por tu luz y tu cariño.  
> Espero que esta página te saque una sonrisa y te recuerde cuánto te aprecio.  
>   
> Con todo mi cariño,  
> Tu mejor amigo 💖
""")

# Galería de imágenes
st.markdown("### 🐾 Galería de Gatitos y Perritos")
st.write("Puedes subir tus imágenes favoritas para verlas aquí:")

uploaded_images = st.file_uploader("Sube tus imágenes aquí", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_images:
    for img in uploaded_images:
        st.image(img, use_column_width=True)
else:
    st.info("Aún no se han subido imágenes. ¡Sube algunas para llenar esta galería de ternura!")

# Mensaje final
st.markdown("---")
st.markdown("Hecho con mucho cariño 💖")
