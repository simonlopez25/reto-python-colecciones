import streamlit as st
from catalog import *

# Configuración de la página
st.set_page_config(page_title="Catálogo de Coleccionables", page_icon="🏛️", layout="wide")

# Inicializar el catálogo en la memoria de la sesión si no existe
if "catalog" not in st.session_state:
    st.session_state.catalog = []

st.title("🏛️ Catálogo de Coleccionables")

# Menú lateral para navegación
menu = st.sidebar.radio(
    "Navegación",
    ["Ver Catálogo", "Agregar Pieza", "Buscar / Filtrar", "Estadísticas"]
)

# --- OPCIÓN 1: VER CATÁLOGO ---
if menu == "Ver Catálogo":
    st.header("Lista de Piezas")
    if not st.session_state.catalog:
        st.info("El catálogo está vacío actualmente.")
    else:
        st.dataframe(st.session_state.catalog, use_container_width=True)

# --- OPCIÓN 2: AGREGAR PIEZA ---
elif menu == "Agregar Pieza":
    st.header("Agregar Nueva Pieza")

    with st.form("add_piece_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            piece_id = st.text_input("ID de la pieza")
            name = st.text_input("Nombre de la pieza")
            category = st.text_input("Categoría")
        with col2:
            price = st.number_input("Precio ($)", min_value=0.0, step=10.0)
            status = st.selectbox("Estado", ["disponible", "reservada", "vendida"])
            description = st.text_input("Descripción (debe incluir 'usada' o 'certificada')")

        submitted = st.form_submit_button("Guardar Pieza")

        if submitted:
            try:
                new_piece = add_piece(
                    st.session_state.catalog,
                    piece_id,
                    name,
                    category,
                    price,
                    status,
                    description
                )
                st.success(f"¡Pieza '{new_piece['name']}' agregada con éxito!")
            except ValueError as error:
                st.error(f"Error de validación: {error}")

# --- OPCIÓN 3: BUSCAR / FILTRAR ---
elif menu == "Buscar / Filtrar":
    st.header("Buscar o Filtrar Piezas")

    tab1, tab2 = st.tabs(["Buscar por ID", "Filtrar por Estado"])

    with tab1:
        search_id = st.text_input("Ingrese ID a buscar")
        if search_id:
            piece = find_piece_by_id(st.session_state.catalog, search_id)
            if piece:
                st.json(piece)
            else:
                st.warning(f"No se encontró ninguna pieza con el ID '{search_id}'.")

    with tab2:
        selected_status = st.selectbox("Seleccione Estado", ["disponible", "reservada", "vendida"])
        filtered = filter_by_status(st.session_state.catalog, selected_status)
        st.write(f"Piezas encontradas ({len(filtered)}):")
        st.table(filtered)

# --- OPCIÓN 4: ESTADÍSTICAS ---
elif menu == "Estadísticas":
    st.header("Métricas del Catálogo")
    avg_price = get_average_price(st.session_state.catalog)
    summary = get_catalog_summary(st.session_state.catalog)

    col1, col2 = st.columns(2)
    col1.metric("Precio Promedio", f"${avg_price:.2f}")
    col2.write("**Piezas por Categoría:**")
    col2.json(summary)