import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Proyecto Final - Dashboard", layout="wide")

@st.cache_data
def cargar_datos():
    df = pd.read_csv('Formulario_Estadistica.csv')
    df.columns = df.columns.str.strip()
    return df

df = cargar_datos()

#------------------FIGURAS------------------
df_conteo_sem = df['Semestre'].value_counts().reset_index()
df_conteo_sem.columns = ['Semestre', 'Cantidad']
fig_barras_semestre = px.bar(
    df_conteo_sem,
    x='Semestre',
    y='Cantidad',
    color='Semestre',
    title="Cantidad de alumnos por semestre:",
    text_auto=True,
)
fig_barras_semestre.update_traces(
    textfont_size=16,
    textangle=0,
    textposition="outside",
    cliponaxis=False
)

df_cont_genero = df['Género'].value_counts().reset_index()
df_cont_genero.columns = ['Género', 'Total']
fig_pastel_genero = px.pie(
    df_cont_genero,
    names="Género",
    values="Total",
    title="Género de las personas que respondieron:",
    color="Género"
)

df_cont_satis = df['Disfrutas tu carrera?'].value_counts().reset_index()
df_cont_satis.columns = ['Disfrutas tu carrera?', 'Total']
fig_anillo_satisfaccion = px.pie(
    df_cont_satis,
    names='Disfrutas tu carrera?',
    values='Total',
    hole=0.5,
    title="¿Disfrutas tu carrera?"
)

df['Fecha de nacimiento'] = pd.to_datetime(df['Fecha de nacimiento'], dayfirst=True, errors='coerce')
fecha_de_hoy = pd.Timestamp.now()
df['Edad'] = (fecha_de_hoy - df['Fecha de nacimiento']).dt.days // 365.25
df_limpio = df[df['Fecha de nacimiento'].dt.year < 2025].copy()
df_cont_edad = df_limpio['Edad'].value_counts().reset_index()
df_cont_edad.columns = ['Edad', 'Total']
fig_hist = px.histogram(
    df_cont_edad,
    x='Edad',
    y='Total',
    title="Edad de los estudiantes",
    text_auto=True
)
fig_hist.update_layout(
    xaxis_title="Edad (Años)",
    yaxis_title="Número de Alumnos",
    bargap=0.1
)

df_conteo_carr = df['Que carrera cursas?'].value_counts().reset_index()
df_conteo_carr.columns = ['Carrera', 'Total']
fig_barras_carrera = px.bar(
    df_conteo_carr,
    x='Total',
    y='Carrera',
    title="Cantidad de alumnos de cada carrera:",
    subtitle="(Solo quienes participaron en la encuesta)",
    text_auto=True
)
fig_barras_carrera.update_traces(
    textfont_size=16,
    textangle=0,
    textposition="outside",
    cliponaxis=False
)


df_conteo_obst = df['Que es lo que no te permite disfrutar de tu carrera completamente?'].value_counts().reset_index()
df_conteo_obst.columns = ['Obstaculo', 'Total']
fig_barras_obst = px.bar(
    df_conteo_obst,
    x='Total',
    y='Obstaculo',
    title="Obstáculos que impiden la satisfacción del alumnado:",
    text_auto=True
)
fig_barras_obst.update_traces(
    textfont_size=16,
    textangle=0,
    textposition="outside",
    cliponaxis=False
)

df_conteo_camb = df['Si la respuesta es si a qué area seria?'].value_counts().reset_index()
df_conteo_camb.columns = ['Alternativas', 'Total']
fig_barras_camb = px.bar(
    df_conteo_camb,
    x='Alternativas',
    y='Total',
    color='Alternativas',
    title="Alternativas populares para alumnos que se cambiarían de carrera:",
    text_auto=True,
)
fig_barras_camb.update_traces(
    textfont_size=16,
    textangle=0,
    textposition="outside",
    cliponaxis=False
)
#------------------LAYOUT------------------
st.title("¿Segur@ de tu carrera?")
st.markdown("Análisis de los datos recopilados de la encuesta")
st.subheader("Gráficos de Barras")
st.plotly_chart(fig_barras_semestre, use_container_width=True)
st.plotly_chart(fig_barras_carrera, use_container_width=True)
st.plotly_chart(fig_barras_obst, use_container_width=True)
st.plotly_chart(fig_barras_camb, use_container_width=True)
st.markdown("---")
col_izq, col_der = st.columns(2)
with col_izq:
    st.caption("Vista Pastel")
    st.plotly_chart(fig_pastel_genero, use_container_width=False)
with col_der:
    st.caption("Vista Anillo")
    st.plotly_chart(fig_anillo_satisfaccion, use_container_width=False)
st.markdown("---")
st.subheader("Histograma")
fig_hist.update_xaxes(type="category")
st.plotly_chart(fig_hist, use_container_width=True)
# --- CRÉDITOS PIE DE PÁGINA ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p><strong>Desarrollado por:</strong> Leidy M. Morayta Pérez, Ángela A. Pimienta Díaz, Victor A. Romero Minaya y Diego Valadez Almeyda</p>
        <p><em>Proyecto final para la materia de Estadística | Noviembre 2025</em></p>
    </div>
    """,
    unsafe_allow_html=True

)
