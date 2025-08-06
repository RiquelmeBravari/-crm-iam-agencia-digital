#!/usr/bin/env python3
"""
Test del módulo de Proyectos con CRUD completo
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(__file__))

from crm_simple import CRMSimple

st.set_page_config(
    page_title="Test Proyectos CRUD",
    page_icon="🚀",
    layout="wide"
)

def main():
    st.title("🚀 TEST: Módulo Proyectos CRUD Completo")
    st.markdown("---")
    
    # Crear instancia CRM
    crm = CRMSimple()
    
    # Forzar inicialización de datos
    crm.init_data()
    
    # Mostrar estado actual de proyectos
    st.subheader("📊 Estado Actual de Proyectos")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Proyectos", len(st.session_state.proyectos))
    with col2:
        st.metric("Funciones CRUD", "✅ Implementado")
    with col3:
        st.metric("Vista Avanzada", "✅ Disponible")
    
    st.markdown("---")
    
    # Test directo del sistema de proyectos
    st.header("🔧 SISTEMA COMPLETO DE PROYECTOS")
    
    # Verificar que el sistema completo esté disponible
    if hasattr(crm, 'sistema_proyectos_completo'):
        st.success("✅ `sistema_proyectos_completo()` función disponible")
        
        # Llamar directamente al sistema completo
        crm.sistema_proyectos_completo()
        
    else:
        st.error("❌ `sistema_proyectos_completo()` función NO encontrada")
    
    # Mostrar funciones avanzadas disponibles
    st.sidebar.markdown("## 🛠️ Funciones Disponibles")
    
    funciones_avanzadas = [
        'mostrar_checklist_tareas',
        'mostrar_timeline_proyecto',
        'mostrar_control_tiempo', 
        'mostrar_alertas_proyecto',
        'agregar_timeline_entrada'
    ]
    
    for func in funciones_avanzadas:
        if hasattr(crm, func):
            st.sidebar.success(f"✅ {func}")
        else:
            st.sidebar.error(f"❌ {func}")

if __name__ == "__main__":
    main()