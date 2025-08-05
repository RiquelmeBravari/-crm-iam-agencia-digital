#!/bin/bash
# 🌐 SCRIPT PARA DESPLIEGUE PÚBLICO DEL CRM
# ========================================

echo "🌐 Configurando CRM para acceso público..."

# Opción 1: Usar ngrok para túnel público
setup_ngrok() {
    echo "🔗 Configurando túnel ngrok..."
    
    # Verificar si ngrok está instalado
    if ! command -v ngrok &> /dev/null; then
        echo "📥 Instalando ngrok..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            # macOS
            if command -v brew &> /dev/null; then
                brew install ngrok
            else
                echo "❌ Por favor instala Homebrew o descarga ngrok desde: https://ngrok.com/download"
                exit 1
            fi
        else
            echo "❌ Por favor descarga ngrok desde: https://ngrok.com/download"
            exit 1
        fi
    fi
    
    echo "✅ ngrok instalado"
    echo ""
    echo "🚀 Para crear túnel público:"
    echo "   1. Ejecuta el CRM: ./ejecutar_crm.sh"
    echo "   2. En otra terminal: ngrok http 8501"
    echo "   3. Usa la URL pública que aparece"
    echo ""
}

# Opción 2: Configurar para Streamlit Cloud
setup_streamlit_cloud() {
    echo "☁️ Configurando para Streamlit Cloud..."
    
    # Crear archivo de configuración para Streamlit Cloud
    mkdir -p ".streamlit"
    
    cat > .streamlit/config.toml << EOL
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false

[theme]
base = "light"
primaryColor = "#2e8b57"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8f9fa"
textColor = "#262730"
EOL

    # Crear archivo secrets para Streamlit Cloud
    cat > .streamlit/secrets.toml << EOL
# Configurar tus secrets aquí
# openrouter_api_key = "your-key-here"
# google_sheet_id = "your-sheet-id"
EOL

    echo "✅ Configuración para Streamlit Cloud creada"
    echo ""
    echo "📋 Pasos para desplegar en Streamlit Cloud:"
    echo "   1. Sube este proyecto a GitHub"
    echo "   2. Ve a https://streamlit.io/cloud"
    echo "   3. Conecta tu repositorio"
    echo "   4. Configura secrets.toml con tus claves"
    echo "   5. ¡Deploy automático!"
    echo ""
}

# Opción 3: Docker para VPS
setup_docker() {
    echo "🐳 Creando configuración Docker..."
    
    cat > Dockerfile << EOL
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \\
    build-essential \\
    curl \\
    software-properties-common \\
    git \\
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos
COPY . .

# Instalar dependencias Python
RUN pip3 install -r requirements.txt

# Exponer puerto
EXPOSE 8501

# Variables de entorno
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLE_CORS=false
ENV STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false

# Comando de inicio
CMD ["streamlit", "run", "crm_simple.py", "--server.port=8501", "--server.address=0.0.0.0"]
EOL

    cat > docker-compose.yml << EOL
version: '3.8'

services:
  crm:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./crm_data:/app/crm_data
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
    restart: unless-stopped
EOL

    echo "✅ Archivos Docker creados"
    echo ""
    echo "🚀 Para usar Docker:"
    echo "   docker-compose up -d"
    echo ""
}

# Menú principal
echo "Selecciona opción de despliegue:"
echo "1) 🔗 Túnel ngrok (rápido, para pruebas)"
echo "2) ☁️  Streamlit Cloud (gratis, recomendado)"
echo "3) 🐳 Docker (para VPS/servidor propio)"
echo "4) 📋 Ver todas las opciones"

read -p "Opción (1-4): " option

case $option in
    1)
        setup_ngrok
        ;;
    2)
        setup_streamlit_cloud
        ;;
    3)
        setup_docker
        ;;
    4)
        echo ""
        echo "🌐 OPCIONES DE DESPLIEGUE DISPONIBLES:"
        echo ""
        echo "1. 🔗 NGROK (Recomendado para pruebas)"
        echo "   • Rápido y fácil"
        echo "   • Túnel temporal"
        echo "   • Ideal para demos"
        echo ""
        echo "2. ☁️ STREAMLIT CLOUD (Recomendado para producción)"
        echo "   • Gratis hasta cierto uso"
        echo "   • Deploy automático desde GitHub"  
        echo "   • URL persistente"
        echo "   • Fácil de mantener"
        echo ""
        echo "3. 🐳 DOCKER + VPS"
        echo "   • Control total"
        echo "   • DigitalOcean: ~$5/mes"
        echo "   • AWS EC2: Variable"
        echo "   • Google Cloud: Variable"
        echo ""
        echo "4. 🔥 OTRAS OPCIONES:"
        echo "   • Heroku (con adaptaciones)"
        echo "   • Railway"
        echo "   • Render"
        echo "   • Vercel (con limitaciones)"
        echo ""
        ;;
    *)
        echo "❌ Opción inválida"
        exit 1
        ;;
esac