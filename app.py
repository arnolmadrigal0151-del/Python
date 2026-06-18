import streamlit as st

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Ulises Pizzas", page_icon="🍕", layout="centered")

# --- 2. DATOS DEL MENÚ OFICIAL (Precios en MXN) ---
precios_tamanos = {
    "Pizza Grande (30 cm)": 239,
    "Pizza Individual": 139,
    "Micro Pizza (Máx 2 ing)": 45
}

recetas_ingredientes = {
    "Hawaiana": ["Jamón", "Piña"],
    "Veneciana": ["Salchicha", "Jamón"],
    "Clásica": ["Salami", "Champiñón"],
    "Alemana": ["Salami", "Salchicha"],
    "Carnes Frías": ["Salami", "Salchicha", "Jamón"],
    "Italiana": ["Champiñón", "Jamón", "Piña"],
    "Portuguesa": ["Carne Molida", "Jitomate", "Cebolla", "Pimiento Morrón"],
    "Ranchera": ["Chorizo", "Jitomate", "Cebolla", "Pimiento Morrón"],
    "Mexicana": ["Jamón", "Jitomate", "Cebolla", "Pimiento Morrón"],
    "Atún a la Mexicana": ["Atún", "Jitomate", "Cebolla", "Pimiento Morrón"],
    "Vegetariana": ["Champiñón", "Jitomate", "Cebolla", "Pimiento Morrón"],
    "Especial": ["Salami", "Salchicha", "Champiñón", "Carne Molida", "Chorizo", "Jamón", "Piña"],
    "¡Arma tu Pizza! (Personalizada)": []
}

ingredientes_disponibles = [
    "Jamón", "Atún", "Tocino", "Cebolla", "Elote", "Salchicha", 
    "Champiñón", "Salami", "Jitomate", "Chorizo", "Piña", 
    "Carne Molida", "Pimiento Morrón", "Pepperoni"
]

# Catálogos de precios individuales
bebidas_precios = {
    "Coca Cola original": 30,
    "Coca Cola Zero": 30,
    "Sprite": 30,
    "Sidral Mundet": 30,
    "Fanta": 30,
    "Jugo del Valle Mango": 30,
    "Jugo del Valle Manzana": 30,
    "Jugo del Valle Durazno": 30
}

aderezos_precios = {
    "Aderezo chimichurri botella grande": 60,
    "Aderezo chimichurri": 25,
    "Aderezo mango habanero": 25,
    "Aderezo ajo parmesano": 25,
    "Aderezo BBQ": 25,
    "Aderezo buffalo": 25
}

# --- 3. DISEÑO DE LA INTERFAZ VISUAL ---
st.title("🍕 Ulises Pizzas - Sistema de Pedidos")
st.markdown("---")

st.subheader("👤 Datos de la Orden")
col1, col2 = st.columns(2)
with col1:
    nombre_cliente = st.text_input("Nombre del Cliente:", placeholder="Ej. Arnol Madrigal")
with col2:
    telefono = st.text_input("Teléfono de Contacto:", placeholder="Ej. 3329893703")

st.markdown("---")

st.subheader("🍕 Configura tu Pizza")

tamano_seleccionado = st.selectbox("Selecciona el Tamaño:", list(precios_tamanos.keys()))
precio_pizza = precios_tamanos[tamano_seleccionado]

especialidad_seleccionada = st.selectbox("Selecciona la Especialidad:", list(recetas_ingredientes.keys()))

ingredientes_base = recetas_ingredientes[especialidad_seleccionada]
if especialidad_seleccionada != "¡Arma tu Pizza! (Personalizada)":
    st.info(f"**Receta base actual:** 🧀 Queso, {', '.join(ingredientes_base)}")
else:
    st.info("**Receta base actual:** ¡Tú eliges la combinación perfecta! Base de salsa y queso incluida.")

# Lógica interactiva para Quitar y Agregar ingredientes
ingredientes_quitar = []
ingredientes_agregar = []
ingredientes_finales = list(ingredientes_base)
es_micro = (tamano_seleccionado == "Micro Pizza (Máx 2 ing)")

if especialidad_seleccionada != "¡Arma tu Pizza! (Personalizada)":
    col_q, col_a = st.columns(2)
    with col_q:
        ingredientes_quitar = st.multiselect("❌ ¿Quitar ingredientes de la receta base?", ingredientes_base)
    with col_a:
        opciones_agregar = [i for i in ingredientes_disponibles if i not in ingredientes_base]
        ingredientes_agregar = st.multiselect("➕ ¿Agregar ingredientes extra?", opciones_agregar)
    
    for ing in ingredientes_quitar:
        if ing in ingredientes_finales: ingredientes_finales.remove(ing)
    for ing in ingredientes_agregar:
        ingredientes_finales.append(ing)
else:
    st.write("Elige tus ingredientes:")
    if es_micro:
        st.warning("⚠️ Recuerda: La Micro Pizza solo permite un máximo de 2 ingredientes.")
    
    cols = st.columns(3)
    ingredientes_finales = []
    for idx, ing in enumerate(ingredientes_disponibles):
        with cols[idx % 3]:
            deshabilitar = es_micro and len(ingredientes_finales) >= 2 and f"custom_{ing}" not in st.session_state
            if st.checkbox(ing, key=f"custom_{ing}", disabled=deshabilitar):
                ingredientes_finales.append(ing)

# Lógica de Queso Extra
queso_extra = False
precio_queso_extra = 0
if not es_micro:
    st.markdown(" ")
    costo_q = 30 if tamano_seleccionado == "Pizza Grande (30 cm)" else 15
    queso_extra = st.checkbox(f"🧀 ¡Agregar Queso Extra! (+${costo_q} MXN)")
    precio_queso_extra = costo_q if queso_extra else 0

precio_pizza += precio_queso_extra

st.markdown("---")

# --- NUEVA SECCIÓN DE COMPLEMENTOS DETALLADA POR CANTIDAD ---
st.subheader("🥤 Bebidas y Aderezos Extra")

col_b, col_ad = st.columns(2)

bebidas_pedido = {}
total_bebidas_costo = 0
cantidad_total_bebidas = 0

with col_b:
    with st.expander("🥤 Desplegar Menú de Bebidas", expanded=True):
        st.write("Ajusta la cantidad de cada una:")
        for bebida, precio in bebidas_precios.items():
            cant = st.number_input(f"{bebida} (${precio} c/u)", min_value=0, max_value=10, value=0, key=f"beb_{bebida}")
            if cant > 0:
                bebidas_pedido[bebida] = cant
                total_bebidas_costo += precio * cant
                cantidad_total_bebidas += cant
        if cantidad_total_bebidas > 0:
            st.success(f"Total Bebidas: {cantidad_total_bebidas} pzas | ${total_bebidas_costo} MXN")

aderezos_pedido = {}
total_aderezos_costo = 0
cantidad_total_aderezos = 0

with col_ad:
    with st.expander("🍯 Desplegar Menú de Aderezos", expanded=True):
        st.write("Ajusta la cantidad de cada uno:")
        for aderezo, precio in aderezos_precios.items():
            cant = st.number_input(f"{aderezo} (${precio} c/u)", min_value=0, max_value=10, value=0, key=f"ade_{aderezo}")
            if cant > 0:
                aderezos_pedido[aderezo] = cant
                total_aderezos_costo += precio * cant
                cantidad_total_aderezos += cant
        if cantidad_total_aderezos > 0:
            st.success(f"Total Aderezos: {cantidad_total_aderezos} pzas | ${total_aderezos_costo} MXN")

st.markdown("---")

st.subheader("✍️ Instrucciones Especiales")
notas_pedido = st.text_area("¿Alguna indicación para cocina?", placeholder="Ej. bien dorada porfa...")

st.markdown("---")

# --- 4. CÁLCULO TOTAL FINAL ---
total_a_pagar = precio_pizza + total_bebidas_costo + total_aderezos_costo

if st.button("🚀 MANDAR PEDIDO A COCINA", use_container_width=True):
    if not nombre_cliente or not telefono:
        st.error("⚠️ Por favor, llena el nombre y el teléfono antes de enviar.")
    elif es_micro and len(ingredientes_finales) > 2:
        st.error("⚠️ No se puede procesar el pedido. La Micro Pizza excede los 2 ingredientes.")
    else:
        st.success(f"🎉 ¡Pedido procesado con éxito para {nombre_cliente.lower()}!")
        
        # Desglose para el ticket (similar a la estructura de image_82d56a.png)
        cambios_texto = ""
        if especialidad_seleccionada != "¡Arma tu Pizza! (Personalizada)":
            if ingredientes_quitar: cambios_texto += f"\n        * **Sin:** {', '.join(ingredientes_quitar)}"
            if ingredientes_agregar: cambios_texto += f"\n        * **Extra:** {', '.join(ingredientes_agregar)}"
        else:
            cambios_texto = f"\n        * **Ingredientes:** {', '.join(ingredientes_finales) if ingredientes_finales else 'Solo Queso'}"

        # Formatear listas detalladas de bebidas y aderezos con sus cantidades
        lista_bebidas_txt = [f"{cant}x {bebida}" for bebida, cant in bebidas_pedido.items()]
        texto_bebidas = ", ".join(lista_bebidas_txt) if lista_bebidas_txt else "Ninguna"

        lista_aderezos_txt = [f"{cant}x {aderezo}" for aderezo, cant in aderezos_pedido.items()]
        texto_aderezos = ", ".join(lista_aderezos_txt) if lista_aderezos_txt else "Ninguno"

        st.info(f"""
        **RESUMEN ENVIADO A COCINA:**
        * **Cliente:** {nombre_cliente} ({telefono})
        * **Detalle:** {tamano_seleccionado} de {especialidad_seleccionada} {"(CON QUESO EXTRA 🧀)" if queso_extra else ""}{cambios_texto}
        * **Bebidas ({cantidad_total_bebidas}):** {texto_bebidas}
        * **Aderezos ({cantidad_total_aderezos}):** {texto_aderezos}
        * **Notas:** {notas_pedido if notas_pedido else 'Ninguna'}
        ---
        * **Total a Cobrar:** ${total_a_pagar} MXN
        """)
        