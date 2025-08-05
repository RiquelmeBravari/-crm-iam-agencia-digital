# Assets del CRM IAM Agencia

Esta carpeta contiene los recursos estáticos necesarios para el funcionamiento del CRM en Streamlit Cloud.

## Archivos:

- **iam_banner.png** (2.87 MB): Banner principal de IAM IntegrA Marketing
  - Dimensiones: Optimizado para header completo
  - Usado en: Página principal del dashboard
  - Formato: PNG con transparencia

## Compatibilidad:

- ✅ Streamlit Cloud: Usa ruta relativa `assets/iam_banner.png`
- ✅ Localhost: Fallback a ruta local si es necesario
- ✅ Fallback HTML: Banner CSS si no encuentra las imágenes

## Notas:

- Los archivos en esta carpeta se incluyen automáticamente en el deployment
- Mantener archivos de imagen optimizados para web
- Usar rutas relativas para compatibilidad con Streamlit Cloud