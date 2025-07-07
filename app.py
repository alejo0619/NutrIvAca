
import streamlit as st

st.set_page_config(page_title="NutrIvAca - Nutrición", layout="centered")

st.title("🐄 NutrIvAca - Módulo de Nutrición")

st.markdown("Calcula el área de potrero necesaria por día según peso, animales y época del año.")

epoca = st.selectbox("Época del año", ["Alta producción (invierno)", "Verano (baja producción)"])
peso = st.number_input("Peso promedio del animal (kg)", min_value=100, max_value=900, step=50)
animales = st.number_input("Número de animales en el lote", min_value=1, step=1)

if st.button("Calcular área necesaria"):
    if epoca == "Alta producción (invierno)":
        aforo = 1.3
    else:
        aforo = 0.8
    perdida = 0.4
    ms_kikuyo = 0.15
    consumo_ms = peso * 0.025  # 2.5% del peso vivo
    consumo_fm = consumo_ms / ms_kikuyo
    disponible_real = aforo * (1 - perdida)
    m2_por_animal = consumo_fm / disponible_real
    m2_totales = m2_por_animal * animales

    st.success(f"✅ Cada animal necesita aproximadamente **{m2_por_animal:.1f} m²/día**.")
    st.info(f"📏 Para {int(animales)} animales, el potrero debe tener al menos **{m2_totales:.1f} m²** por día.")

st.markdown("---")
st.caption("Versión básica - NutrIvAca 2025")
