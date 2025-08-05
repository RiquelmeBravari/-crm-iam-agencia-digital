#!/bin/bash
# 🏢 EJECUTAR CRM IAM AGENCIA DIGITAL - SISTEMA DEFINITIVO
# ======================================================

echo "🏢 Iniciando CRM IAM Agencia Digital - Sistema Definitivo"
echo "========================================================"
echo ""

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

print_success() {
    echo -e "${GREEN}[✓]${NC} ✅ $1"
}

# Variables
BASE_DIR="/Users/jriquelmebravari/CRM_IAM_AGENCIA_DEFINITIVO"
CRM_PORT="8501"

# Ir al directorio
cd "$BASE_DIR" || {
    echo "❌ No se pudo acceder al directorio: $BASE_DIR"
    exit 1
}

print_success "Verificando CRM definitivo..."

# Verificar archivo principal
if [ -f "crm_simple.py" ]; then
    print_success "CRM principal encontrado"
else
    echo "❌ Archivo crm_simple.py no encontrado"
    exit 1
fi

# Instalar dependencias
print_success "Verificando dependencias..."
pip3 install -r requirements.txt > /dev/null 2>&1

# Liberar puerto si está ocupado
if lsof -ti:$CRM_PORT &>/dev/null; then
    echo "⚠️ Puerto $CRM_PORT ocupado. Liberando..."
    lsof -ti:$CRM_PORT | xargs kill -9
    sleep 2
fi

echo ""
echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║                🏢 CRM IAM AGENCIA DIGITAL                    ║${NC}"
echo -e "${CYAN}║                    SISTEMA DEFINITIVO                        ║${NC}"
echo -e "${CYAN}╠══════════════════════════════════════════════════════════════╣${NC}"
echo -e "${CYAN}║                                                              ║${NC}"
echo -e "${CYAN}║  🌐 URL: http://localhost:$CRM_PORT                          ║${NC}"
echo -e "${CYAN}║                                                              ║${NC}"
echo -e "${CYAN}║  🏢 FUNCIONALIDADES:                                        ║${NC}"
echo -e "${CYAN}║  ✅ Gestión de Clientes                                     ║${NC}"
echo -e "${CYAN}║  ✅ Sistema de Cotizaciones                                 ║${NC}"
echo -e "${CYAN}║  ✅ Cotizador Automático                                    ║${NC}"
echo -e "${CYAN}║  ✅ Carta Gantt de Proyectos                               ║${NC}"
echo -e "${CYAN}║  ✅ Sistema de Facturas                                     ║${NC}"
echo -e "${CYAN}║  ✅ Gestión de Tareas                                       ║${NC}"
echo -e "${CYAN}║  ✅ Carpetas de Clientes                                    ║${NC}"
echo -e "${CYAN}║  ✅ Proyectos SEO                                           ║${NC}"
echo -e "${CYAN}║  ✅ Integración MCP                                         ║${NC}"
echo -e "${CYAN}║                                                              ║${NC}"
echo -e "${CYAN}║  💾 PERSISTENCIA: Datos guardados en JSON                   ║${NC}"
echo -e "${CYAN}║  🔒 ACCESO: Solo localhost por defecto                      ║${NC}"
echo -e "${CYAN}║                                                              ║${NC}"
echo -e "${CYAN}║  ⚠️ Para detener: Presiona Ctrl+C                          ║${NC}"
echo -e "${CYAN}║                                                              ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

print_success "Iniciando CRM definitivo..."

# Ejecutar CRM
streamlit run crm_simple.py \
    --server.port $CRM_PORT \
    --server.address localhost \
    --server.headless false \
    --server.runOnSave true \
    --theme.base "light" \
    --theme.primaryColor "#2e8b57" \
    --theme.backgroundColor "#ffffff" \
    --theme.secondaryBackgroundColor "#f8f9fa" \
    --theme.textColor "#262730" \
    --server.fileWatcherType "poll" \
    --browser.gatherUsageStats false

print_success "CRM definitivo finalizado"