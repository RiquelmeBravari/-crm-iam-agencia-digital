#!/usr/bin/env python3
"""
📋 GESTOR DE COTIZACIONES - Marketing a tu Puerta
=================================================
Sistema para gestionar cotizaciones rechazadas y seguimiento
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json
import os

class CotizacionesManager:
    def __init__(self):
        """Inicializar gestor de cotizaciones"""
        self.cotizaciones_rechazadas = {
            'CLINICENTRO': {
                'valor_propuesto': 25000,
                'fecha_rechazo': '28 Julio 2025',
                'motivo_rechazo': 'Presupuesto muy alto para su budget actual',
                'contacto': 'Dr. Martinez - direccion@clinicentro.cl',
                'observaciones': 'Mostraron interés pero necesitan una propuesta más económica',
                'oportunidad_reconversion': 85,
                'propuesta_alternativa': 'Plan básico por $15,000',
                'fecha_recontacto': '15 Agosto 2025'
            },
            'PLASTICA LASER': {
                'valor_propuesto': 18000,
                'fecha_rechazo': '30 Julio 2025', 
                'motivo_rechazo': 'Timeline de desarrollo muy extenso (12 semanas)',
                'contacto': 'Dra. Fernandez - contacto@plasticalaser.cl',
                'observaciones': 'Urgencia por lanzar antes de septiembre',
                'oportunidad_reconversion': 70,
                'propuesta_alternativa': 'MVP en 6 semanas por $12,000',
                'fecha_recontacto': '10 Agosto 2025'
            },
            'NUEVA MASVIDA': {
                'valor_propuesto': 22000,
                'fecha_rechazo': '01 Agosto 2025',
                'motivo_rechazo': 'Requieren menos funcionalidades que las propuestas',
                'contacto': 'Sr. Rodriguez - gerencia@nuevamasvida.cl',
                'observaciones': 'Solo necesitan landing page + formularios básicos',
                'oportunidad_reconversion': 90,
                'propuesta_alternativa': 'Landing optimizada por $8,000',
                'fecha_recontacto': '05 Agosto 2025'
            }
        }
    
    def mostrar_resumen_cotizaciones(self):
        """Mostrar resumen de cotizaciones rechazadas"""
        st.subheader("📋 Resumen de Cotizaciones Rechazadas")
        
        # Métricas generales
        col1, col2, col3, col4 = st.columns(4)
        
        total_rechazadas = len(self.cotizaciones_rechazadas)
        valor_total_perdido = sum(
            [cot['valor_propuesto'] for cot in self.cotizaciones_rechazadas.values()]
        )
        if total_rechazadas:
            oportunidad_promedio = (
                sum(
                    [
                        cot['oportunidad_reconversion']
                        for cot in self.cotizaciones_rechazadas.values()
                    ]
                )
                / total_rechazadas
            )
        else:
            oportunidad_promedio = 0
        valor_potencial_recuperacion = sum(
            [
                int(cot['propuesta_alternativa'].split('$')[1].split(',')[0].replace('.', ''))
                for cot in self.cotizaciones_rechazadas.values()
                if '$' in cot['propuesta_alternativa']
            ]
        )
        
        with col1:
            st.metric("❌ Total Rechazadas", total_rechazadas)
        
        with col2:
            st.metric("💸 Valor Perdido", f"${valor_total_perdido:,}")
        
        with col3:
            st.metric("🎯 Oportunidad Promedio", f"{oportunidad_promedio:.0f}%")
        
        with col4:
            st.metric("💰 Recuperación Potencial", f"${valor_potencial_recuperacion:,}")
    
    def mostrar_detalle_cotizaciones(self):
        """Mostrar detalle de cada cotización rechazada"""
        st.subheader("🔍 Detalle de Cotizaciones Rechazadas")
        
        for cliente, datos in self.cotizaciones_rechazadas.items():
            with st.expander(f"🔴 {cliente} - ${datos['valor_propuesto']:,}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**📅 Información General:**")
                    st.write(f"• **Fecha rechazo:** {datos['fecha_rechazo']}")
                    st.write(f"• **Valor propuesto:** ${datos['valor_propuesto']:,}")
                    st.write(f"• **Contacto:** {datos['contacto']}")
                    
                    st.write("**❌ Motivo del Rechazo:**")
                    st.write(f"• {datos['motivo_rechazo']}")
                    
                    st.write("**📝 Observaciones:**")
                    st.write(f"• {datos['observaciones']}")
                
                with col2:
                    st.write("**🎯 Oportunidad de Reconversión:**")
                    st.progress(datos['oportunidad_reconversion'] / 100)
                    st.write(f"{datos['oportunidad_reconversion']}% probabilidad")
                    
                    st.write("**💡 Propuesta Alternativa:**")
                    st.info(datos['propuesta_alternativa'])
                    
                    st.write("**📞 Fecha Recontacto:**")
                    fecha_recontacto = datetime.strptime(datos['fecha_recontacto'], '%d %B %Y')
                    dias_para_recontacto = (fecha_recontacto - datetime.now()).days
                    
                    if dias_para_recontacto <= 0:
                        st.error(f"⚠️ RECONTACTAR HOY")
                    elif dias_para_recontacto <= 3:
                        st.warning(f"⏰ Recontactar en {dias_para_recontacto} días")
                    else:
                        st.success(f"📅 Recontactar en {dias_para_recontacto} días")
                
                # Acciones
                st.write("**⚡ Acciones:**")
                col_acc1, col_acc2, col_acc3 = st.columns(3)
                
                with col_acc1:
                    if st.button(f"📞 Recontactar {cliente}", key=f"call_{cliente}"):
                        st.success(f"📋 Recordatorio creado para contactar a {cliente}")
                
                with col_acc2:
                    if st.button(f"✏️ Nueva Propuesta", key=f"proposal_{cliente}"):
                        st.info(f"📄 Preparando nueva propuesta para {cliente}")
                
                with col_acc3:
                    if st.button(f"📧 Enviar Email", key=f"email_{cliente}"):
                        st.success(f"✉️ Email programado para {cliente}")
    
    def mostrar_plan_seguimiento(self):
        """Plan de seguimiento para reconversión"""
        st.subheader("📈 Plan de Seguimiento y Reconversión")
        
        # Calendario de recontactos
        st.write("**📅 Calendario de Recontactos:**")
        
        recontactos = []
        for cliente, datos in self.cotizaciones_rechazadas.items():
            fecha_recontacto = datetime.strptime(datos['fecha_recontacto'], '%d %B %Y')
            recontactos.append({
                'Cliente': cliente,
                'Fecha Recontacto': datos['fecha_recontacto'],
                'Días Restantes': (fecha_recontacto - datetime.now()).days,
                'Oportunidad': f"{datos['oportunidad_reconversion']}%",
                'Propuesta Alternativa': datos['propuesta_alternativa'],
                'Prioridad': 'ALTA' if datos['oportunidad_reconversion'] >= 85 else 'MEDIA'
            })
        
        df_recontactos = pd.DataFrame(recontactos)
        df_recontactos = df_recontactos.sort_values('Días Restantes')
        
        st.dataframe(df_recontactos, use_container_width=True)
        
        # Estrategias específicas
        st.write("**🎯 Estrategias de Reconversión:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **NUEVA MASVIDA (90% oportunidad):**
            • ✅ Propuesta simplificada lista
            • 🎯 Enfoque en landing + formularios
            • 💰 Reducción precio: $22k → $8k
            • ⏰ Contactar: 05 Agosto
            """)
            
            st.markdown("""
            **CLINICENTRO (85% oportunidad):**
            • ✅ Plan básico preparado  
            • 🎯 Funcionalidades esenciales
            • 💰 Reducción precio: $25k → $15k
            • ⏰ Contactar: 15 Agosto
            """)
        
        with col2:
            st.markdown("""
            **PLASTICA LASER (70% oportunidad):**
            • ✅ MVP rápido propuesto
            • 🎯 Entrega en 6 semanas
            • 💰 Reducción precio: $18k → $12k  
            • ⏰ Contactar: 10 Agosto
            """)
    
    def mostrar_metricas_conversion(self):
        """Métricas de conversión y recuperación"""
        st.subheader("📊 Métricas de Conversión")
        
        # Potencial de recuperación
        valor_original = sum([cot['valor_propuesto'] for cot in self.cotizaciones_rechazadas.values()])
        valor_alternativo = 35000  # 15k + 12k + 8k
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("💸 Valor Original Perdido", f"${valor_original:,}")
            st.metric("💰 Potencial Recuperación", f"${valor_alternativo:,}")
            st.metric("📈 % Recuperación", f"{(valor_alternativo/valor_original)*100:.1f}%")
        
        with col2:
            # Gráfico de oportunidades
            clientes = list(self.cotizaciones_rechazadas.keys())
            oportunidades = [datos['oportunidad_reconversion'] for datos in self.cotizaciones_rechazadas.values()]
            
            import plotly.express as px
            
            fig = px.bar(x=clientes, y=oportunidades,
                        title="Oportunidad de Reconversión por Cliente",
                        labels={'x': 'Cliente', 'y': 'Oportunidad (%)'})
            
            fig.update_traces(marker_color=['#ff4444' if x < 75 else '#ffaa44' if x < 85 else '#44ff44' for x in oportunidades])
            
            st.plotly_chart(fig, use_container_width=True)

def main():
    """Función principal del gestor de cotizaciones"""
    st.set_page_config(
        page_title="📋 Gestor de Cotizaciones",
        page_icon="📋",
        layout="wide"
    )
    
    st.title("📋 Gestor de Cotizaciones Rechazadas")
    st.markdown("**Marketing a tu Puerta** - Seguimiento y Reconversión")
    
    manager = CotizacionesManager()
    
    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Resumen", "🔍 Detalle", "📈 Seguimiento", "📊 Métricas"])
    
    with tab1:
        manager.mostrar_resumen_cotizaciones()
    
    with tab2:
        manager.mostrar_detalle_cotizaciones()
    
    with tab3:
        manager.mostrar_plan_seguimiento()
    
    with tab4:
        manager.mostrar_metricas_conversion()

if __name__ == "__main__":
    main()