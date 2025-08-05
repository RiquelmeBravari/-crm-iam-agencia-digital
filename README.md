# 🏢 CRM IAM AGENCIA DIGITAL - SISTEMA DEFINITIVO

Sistema CRM completo para gestión integral de agencia digital con funcionalidades avanzadas.

## 🚀 CARACTERÍSTICAS PRINCIPALES

### ✅ Módulos Incluidos:
- **👥 Gestión de Clientes** - Base de datos completa de clientes
- **💰 Sistema de Cotizaciones** - Gestión de propuestas y seguimiento
- **🧮 Cotizador Automático** - Generación automática de cotizaciones
- **📊 Carta Gantt** - Cronograma visual de proyectos
- **🧾 Sistema de Facturas** - Facturación y control de pagos
- **📋 Gestión de Tareas** - Seguimiento de actividades
- **📁 Carpetas de Clientes** - Organización de documentos
- **🔍 Proyectos SEO** - Gestión especializada SEO
- **🤖 Integración MCP** - Conexión con agentes inteligentes

### 💾 Persistencia de Datos:
- **Formato:** Archivos JSON en carpeta `crm_data/`
- **Backup Automático:** Cada 10 guardados
- **Sincronización:** Google Sheets opcional

## 🛠️ INSTALACIÓN Y USO

### Requisitos:
```bash
Python 3.8+
pip3
```

### Instalación:
```bash
# Instalar dependencias
pip3 install -r requirements.txt

# Ejecutar CRM
./ejecutar_crm.sh
```

### Acceso:
```
URL: http://localhost:8501
```

## 📁 ESTRUCTURA DE ARCHIVOS

```
CRM_IAM_AGENCIA_DEFINITIVO/
├── crm_simple.py              # Sistema principal
├── crm_agencia_completo.py    # Versión extendida
├── cotizaciones_manager.py    # Gestor de cotizaciones
├── requirements.txt           # Dependencias
├── ejecutar_crm.sh           # Script de ejecución
├── README.md                 # Este archivo
└── crm_data/                 # Datos persistentes
    ├── clientes.json
    ├── cotizaciones.json
    ├── facturas.json
    ├── proyectos.json
    ├── tareas.json
    ├── carpetas_clientes.json
    ├── keywords_data.json
    ├── proyectos_seo.json
    └── agentes_disponibles.json
```

## 🌐 DESPLIEGUE PARA ACCESO REMOTO

### Opción 1: Túnel ngrok (Recomendado para pruebas)
```bash
# Instalar ngrok
brew install ngrok  # macOS
# o descargar desde https://ngrok.com

# Ejecutar túnel
ngrok http 8501
```

### Opción 2: Servidor VPS/Cloud
- **DigitalOcean Droplet**
- **AWS EC2**  
- **Google Cloud Compute**
- **Heroku** (con adaptaciones)

### Opción 3: Streamlit Cloud
```bash
# Subir a GitHub y conectar con Streamlit Cloud
# https://streamlit.io/cloud
```

### Opción 4: Docker + Cloud
```dockerfile
# Dockerfile incluido para despliegue
```

## 🔒 CONFIGURACIÓN DE SEGURIDAD

### Para Acceso Público:
1. **Autenticación de usuarios**
2. **HTTPS obligatorio**
3. **Variables de entorno para secrets**
4. **Base de datos externa**

## 📊 DATOS INCLUIDOS

- **Clientes reales:** HISTOCELL, DR PRIETO, INTEGRAMARKETING
- **Cotizaciones:** Sistema completo de seguimiento
- **Proyectos:** Cronogramas Gantt funcionales
- **SEO:** Tracking de keywords y rankings

## 🚀 PRÓXIMAS MEJORAS

- [ ] Base de datos PostgreSQL
- [ ] Sistema de usuarios múltiples
- [ ] API REST
- [ ] Notificaciones automáticas
- [ ] Integración con WhatsApp
- [ ] Reportes PDF automáticos

---

**Desarrollado por IAM Agencia Digital**  
**Versión:** 1.0 Definitiva  
**Fecha:** Agosto 2025