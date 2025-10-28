# 🚀 GUÍA DE DESPLIEGUE EN STREAMLIT CLOUD

## 📋 PASOS PARA DEPLOYMENT

### 1. 📁 **SUBIR A GITHUB**

#### Opción A: Crear repositorio nuevo en GitHub
1. Ve a [GitHub.com](https://github.com)
2. Click "New repository"
3. Nombre: `crm-iam-agencia-digital`
4. Descripción: `CRM completo para IAM Agencia Digital`
5. ✅ Público (o privado si prefieres)
6. Click "Create repository"

#### Opción B: Comandos para terminal
```bash
# En el directorio del CRM
git add .
git commit -m "🏢 CRM IAM Agencia Digital - Primera versión"

# Conectar con tu repositorio GitHub
git remote add origin https://github.com/TU-USUARIO/crm-iam-agencia-digital.git
git branch -M main
git push -u origin main
```

### 2. ☁️ **CONECTAR STREAMLIT CLOUD**

1. **Ve a:** [streamlit.io/cloud](https://streamlit.io/cloud)
2. **Sign up/Login** con tu cuenta GitHub
3. **Click "New app"**
4. **Configurar:**
   - Repository: `TU-USUARIO/crm-iam-agencia-digital`
   - Branch: `main`
   - Main file path: `crm_simple.py`
   - App URL: `crm-iam-agencia` (personalizable)

### 3. 🔐 **CONFIGURAR SECRETS**

1. **En tu app de Streamlit Cloud:**
   - Click "⚙️ Settings" 
   - Click "🔐 Secrets"
   - Copia y pega el contenido de `.streamlit/secrets.toml`

2. **Secrets a configurar:**
```toml
[api_keys]
openrouter_api_key = "API aqui"

[google_sheets]
sheet_id = "xxxxxxxxxxxxxxxxx"

[app_config]
admin_password = "xxxxxx"
app_name = "CRM IAM Agencia Digital"
```

### 4. 🎯 **DEPLOY AUTOMÁTICO**

¡Eso es todo! Streamlit Cloud:
- ✅ Detectará automáticamente `requirements.txt`
- ✅ Instalará dependencias
- ✅ Ejecutará `crm_simple.py`
- ✅ Te dará una URL pública

## 🌐 **TU CRM ESTARÁ DISPONIBLE EN:**
```
https://crm-iam-agencia.streamlit.app
```

## 🔄 **DESARROLLO CONTINUO**

### Para hacer cambios:
```bash
# Hacer cambios en el código
git add .
git commit -m "Nueva funcionalidad X"
git push origin main
```

**⚡ Deploy automático en 2-3 minutos!**

## 🛠️ **TROUBLESHOOTING**

### Si hay errores:
1. **Check logs** en Streamlit Cloud
2. **Verificar requirements.txt** - todas las dependencias
3. **Revisar secrets** - claves correctas
4. **File paths** - usar rutas relativas

### Comandos útiles:
```bash
# Ver status del repositorio
git status

# Ver diferencias
git diff

# Revertir cambios
git checkout -- archivo.py
```

## 🎉 **¡LISTO!**

Tu CRM estará disponible 24/7 en internet con:
- ✅ URL permanente
- ✅ SSL/HTTPS automático  
- ✅ Deploy automático con Git
- ✅ Escalabilidad automática
- ✅ 99.9% uptime

---

**🏢 Desarrollado para IAM Agencia Digital**  
**📅 Agosto 2025**
