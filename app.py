import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

email_contact = 'estebanmm.3112@gmail.com'

st.set_page_config(page_title='AutoAnalitica', page_icon='./imagenes/LOGOS-06.png', layout='wide')

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

css_load('./style/main.css')

# Función para cargar una animación Lottie desde una URL
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Lanza un error si la solicitud no fue exitosa
        return r.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error en la solicitud: {e}")
        return None
    except ValueError as e:
        st.error(f"Error al decodificar JSON: {e}")
        return None

# URL de ejemplo para una animación Lottie
lottie_url = "https://lottie.host/f904ba32-bc82-4275-ac07-4434012f56a1/fNyJyQLZMR.json"
lottie_json = load_lottieurl(lottie_url)

# URL de ejemplo para una animación Lottie de WhatsApp
lottie_whatsapp_url = "https://lottie.host/d862f405-df38-4859-8f72-e92d784f3df6/yONCFU56dC.json"
lottie_whatsapp_json = load_lottieurl(lottie_whatsapp_url)

#Intro
with st.container():
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>AutoAnalitica</h1>
        </div>
        """,
        unsafe_allow_html=True
    )


# Abre la imagen
image = Image.open('./imagenes/R1.jpg')

# Usamos un contenedor para el contenido centrado
with st.container():
    # Utilizamos st.image para cargar la imagen
    st.image(image, use_column_width=True)

    # Centramos el resto del contenido con HTML y CSS
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Conectando datos, impulsando negocios</h1>
            <p>Somos apasionados por los datos, la automatización y la eficiencia en el trabajo.</p>
            <a href="https://wa.me/573059246318?text=Hola%20AutoAnalitica!%0AQuiero%20mas%20informacion" target="_blank">Saber mas ></a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Sobre nosotros
with st.container():
    st.write('-----')
    text_colum, animacion_colum = st.columns(2)
    with text_colum:
        st.header('Sobre nosotro 🔍')
        st.write(
            """
            AutoAnalitica es una empresa dedicada a transformar la manera en que las organizaciones acceden, analizan y utilizan sus datos. 
            Especializada en Business Intelligence (BI) y Visualización de Datos,AutoAnalitica ofrece soluciones a medida para la 
            optimización de bases de datos y la consolidación de información dispersa, permitiendo análisis eficientes y decisiones 
            estratégicas acertadas. A través de la implementación de tecnologías avanzadas de automatización y servicios en la nube con AWS, 
            nuestra empresa garantiza la mejora continua de los procesos operativos y administrativos, asegurando escalabilidad, seguridad y eficiencia. 
            Con un enfoque particular en el análisis de demanda y distribución, AutoAnalitica proporciona a sus clientes las herramientas necesarias 
            para anticipar tendencias de mercado, planificar la producción y optimizar la distribución. Creemos en el poder de los datos para 
            transformar negocios y estamos aquí para ayudarte a navegar el futuro de tu empresa con confianza y claridad.
            """
        )
        st.write('[Mas sobre nosotros>](https://wa.me/573059246318?text=Hola%20AutoAnalitica!%0AQuiero%20mas%20informacion)')
    with animacion_colum:
        st_lottie(lottie_json,height=400)

# Servicio
with st.container():
    st.write('-----')
    st.markdown(
        """
        <h2 style='text-align: center;'>
            Nuestros Servicios
        </h2>
        """,
        unsafe_allow_html=True
    )
    st.write('##')
    image_colum, text_colum = st.columns((0.5,2))
    with image_colum:
        image = Image.open('./imagenes/LOGOS-07.png')
        st.image(image, use_column_width=True)
    with text_colum:
        st.subheader('Integración de Datos para Análisis Empresarial')
        st.write("""
                    Diseñamos y desarrollamos bases de datos optimizadas para análisis como parte de nuestros servicios de 
                    Business Intelligence (BI) y Visualización de Datos. Además, nos especializamos en la consolidación de 
                    datos dispersos en una sola fuente para un análisis eficiente y preciso, y creamos tableros de información 
                    interactivos utilizando Power BI y otras herramientas de visualización.
                """)
        st.write('⭐⭐⭐⭐⭐')
        
with st.container():
    st.write('-----')
    st.write('##')
    image_colum, text_colum = st.columns((0.5,2))
    with image_colum:
        image = Image.open('./imagenes/LOGOS-08.png')
        st.image(image, use_column_width=True)
    with text_colum:
        st.subheader('Automatización y Optimización de Procesos Empresariales')
        st.write("""
                    Ofrecemos soluciones integrales para la automatización de procesos y la optimización de tareas administrativas. 
                    Nuestros servicios incluyen:
                    Automatización de Procesos: Implementamos soluciones tecnológicas que permiten automatizar tareas repetitivas 
                    y mejorar la eficiencia operativa de tu empresa.
                    Desarrollos Ejecutables para Procesos Administrativos: Diseñamos y desarrollamos soluciones ejecutables a medida 
                    para diferentes procesos administrativos, adaptadas a las necesidades específicas de tu empresa.
                    Implementación y Gestión de Servicios en la Nube (AWS): Ofrecemos servicios especializados en la implementación y 
                    gestión de servicios en la nube a través de AWS (Amazon Web Services), garantizando escalabilidad, seguridad y 
                    eficiencia en la gestión de tus aplicaciones y datos
                """)
        st.write('⭐⭐⭐⭐⭐')
        
with st.container():
    st.write('-----')
    st.write('##')
    image_colum, text_colum = st.columns((0.5,2))
    with image_colum:
        image = Image.open('./imagenes/LOGOS-11.png')
        st.image(image, use_column_width=True)
    with text_colum:
        st.subheader('Análisis de Demanda y Distribución')
        st.write("""
                    Ofrecemos un análisis de la demanda de tus productos que te permite anticiparse a las ventas, planificar de manera 
                    más efectiva tu producción y optimizar la distribución en diversos clientes, canales y puntos de venta. 
                """)
        st.write('⭐⭐⭐⭐⭐')

# contacto
with st.container():
    st.write('-----')
    st.write('##')
    st.header('Contáctanos 📩')
    st.write('##')
    contact_form = f"""
    <form action="https://formsubmit.co/{email_contact}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="nombre" placeholder="Digita tu nombre completo" required>
        <input type="email" name="correo electrónico" placeholder="Digita tu correo electrónico" required>
        <textarea name="mensaje" placeholder="Déjanos tu mensaje" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    L_column, R_column = st.columns(2)
    with L_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with R_column:
        if lottie_whatsapp_json:
            # Mostrar la animación Lottie
            st_lottie(lottie_whatsapp_json, height=200, key="whatsapp_lottie")
            # Botón de WhatsApp
            st.markdown(
            """
            <div style="text-align: center;">
                <a href="https://wa.me/573059246318?text=Hola%20AutoAnalitica!%0AQuiero%20mas%20informacion" target="_blank">WhatsApp</a>
            </div>
            """,
            unsafe_allow_html=True
            )

