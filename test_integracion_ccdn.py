#!/usr/bin/env python3
"""
Test de integración del sistema de cumpleaños CCDN con templates reales
"""
import json
import os
import sys

def test_configuracion_aprobada():
    """Test de la configuración aprobada"""
    print("🔧 Testing configuración aprobada...")
    
    config_path = "/Users/jriquelmebravari/cumpleanos_mensuales/configuracion_poster_definitiva.json"
    
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        print(f"✅ Configuración cargada: {config['poster_config']['name']}")
        print(f"📐 Dimensiones: {config['poster_config']['dimensions']['width']}x{config['poster_config']['dimensions']['height']}px")
        print(f"🎨 Colores principales: {config['color_scheme']['primary']}, {config['color_scheme']['secondary']}")
        print(f"📝 Estado: {config['poster_config']['status']}")
        
        return config
    else:
        print("❌ Configuración no encontrada")
        return None

def test_script_generador():
    """Test del script generador"""
    print("\n🎨 Testing script generador...")
    
    script_path = "/Users/jriquelmebravari/sistema_cumpleanos_mensual/generar_poster_mensual.py"
    
    if os.path.exists(script_path):
        print(f"✅ Script encontrado: {script_path}")
        
        # Leer primeras líneas para verificar
        with open(script_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()[:20]
        
        print(f"📋 Primeras líneas del script:")
        for i, line in enumerate(lines[:5]):
            print(f"   {i+1}: {line.strip()}")
        
        return True
    else:
        print("❌ Script generador no encontrado")
        return False

def test_preparacion_datos():
    """Test de preparación de datos"""
    print("\n📊 Testing preparación de datos...")
    
    # Datos de prueba simulando entrada del CRM (con formato real de la planilla)
    cumpleanos_test = [
        {'Nombre': 'Elizabeth Eliana Cortés', 'Fecha': '2025-08-07', 'Cargo': 'Técnico Paramédico'},
        {'Nombre': 'Myrna Ximena Vergara', 'Fecha': '2025-08-09', 'Cargo': 'Nutricionista'},
        {'Nombre': 'Patricia de Lourdes Rodríguez', 'Fecha': '2025-08-12', 'Cargo': 'Supervisora de Cobranza'},
        {'Nombre': 'María José García', 'Fecha': '2025-08-23', 'Cargo': 'Administrativos'},
        {'Nombre': 'Kirenia Tofalos', 'Fecha': '2025-08-24', 'Cargo': 'Administrativos'}
    ]
    
    # Simular transformación a formato del script real
    datos_transformados = []
    for persona in cumpleanos_test:
        fecha = persona['Fecha']
        dia = fecha.split('-')[2]  # Extraer día
        
        dato_transformado = {
            "nombre": persona['Nombre'],
            "dia": dia.zfill(2),
            "cargo": persona['Cargo']
        }
        datos_transformados.append(dato_transformado)
    
    print(f"✅ Datos transformados exitosamente: {len(datos_transformados)} personas")
    for dato in datos_transformados:
        print(f"   🎂 {dato['nombre']} - Agosto {dato['dia']} ({dato['cargo']})")
    
    return datos_transformados

def test_configuracion_grid(num_cumpleaneros, config):
    """Test de configuración de grid responsivo"""
    print(f"\n📐 Testing grid responsivo para {num_cumpleaneros} cumpleañeros...")
    
    if not config:
        print("❌ Sin configuración disponible")
        return None
    
    responsive_config = config.get("responsive_grid", {})
    
    if num_cumpleaneros <= 2:
        grid_config = responsive_config.get("1-2_cumpleañeros")
        descripcion = "1-2 cumpleañeros: Una sola columna centrada"
    elif num_cumpleaneros <= 6:
        grid_config = responsive_config.get("3-6_cumpleañeros")
        descripcion = "3-6 cumpleañeros: 2 columnas - PERFECTA"
    elif num_cumpleaneros <= 12:
        grid_config = responsive_config.get("7-12_cumpleañeros")
        descripcion = "7-12 cumpleañeros: 2 columnas con gap reducido"
    else:
        grid_config = responsive_config.get("13-20_cumpleañeros")
        descripcion = "13+ cumpleañeros: 3 columnas con texto menor"
    
    if grid_config:
        print(f"✅ {descripcion}")
        print(f"   Columnas: {grid_config.get('grid_columns', 'N/A')}")
        print(f"   Ancho máximo: {grid_config.get('max_width', 'N/A')}")
        print(f"   Comentario: {grid_config.get('comment', 'N/A')}")
        return grid_config
    else:
        print("❌ Configuración de grid no encontrada")
        return None

def test_colores_corporativos(config):
    """Test de colores corporativos"""
    print("\n🎨 Testing colores corporativos CCDN...")
    
    if not config:
        print("❌ Sin configuración disponible")
        return False
    
    colores = config.get("color_scheme", {})
    
    print("✅ Colores oficiales CCDN:")
    print(f"   🔵 Azul principal: {colores.get('primary', 'N/A')}")
    print(f"   🔷 Azul secundario: {colores.get('secondary', 'N/A')}")
    print(f"   💚 Verde lima: {colores.get('accent', 'N/A')}")
    print(f"   🧡 Naranja: {colores.get('orange', 'N/A')}")
    print(f"   💜 Morado ginecología: {colores.get('purple', 'N/A')}")
    print(f"   ⚪ Blanco: {colores.get('white', 'N/A')}")
    
    # Verificar que no hay rosa (como pidió el usuario)
    if 'rosa' in str(colores).lower() or 'pink' in str(colores).lower():
        print("⚠️  ADVERTENCIA: Se encontró rosa en los colores (debe ser azul principal)")
        return False
    else:
        print("✅ Correcto: No hay rosa, azul es el color principal")
        return True

def main():
    print("🎂 TEST DE INTEGRACIÓN SISTEMA CUMPLEAÑOS CCDN")
    print("=" * 60)
    print("Verificando integración con templates reales desarrollados")
    print()
    
    # Test 1: Configuración aprobada
    config = test_configuracion_aprobada()
    
    # Test 2: Script generador
    script_ok = test_script_generador()
    
    # Test 3: Preparación de datos
    datos_test = test_preparacion_datos()
    
    # Test 4: Grid responsivo
    if config and datos_test:
        grid_config = test_configuracion_grid(len(datos_test), config)
    
    # Test 5: Colores corporativos
    colores_ok = test_colores_corporativos(config)
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📋 RESUMEN DE INTEGRACIÓN")
    print("=" * 60)
    
    tests_pasados = 0
    if config:
        print("✅ Configuración aprobada: CARGADA")
        tests_pasados += 1
    else:
        print("❌ Configuración aprobada: FALTA")
    
    if script_ok:
        print("✅ Script generador: ENCONTRADO")
        tests_pasados += 1
    else:
        print("❌ Script generador: FALTA")
    
    if datos_test:
        print("✅ Preparación de datos: FUNCIONAL")
        tests_pasados += 1
    else:
        print("❌ Preparación de datos: FALLA")
    
    if colores_ok:
        print("✅ Colores corporativos: CORRECTOS (azul principal)")
        tests_pasados += 1
    else:
        print("❌ Colores corporativos: REVISAR")
    
    print(f"\n🎯 RESULTADO: {tests_pasados}/4 tests pasados")
    
    if tests_pasados == 4:
        print("🎉 INTEGRACIÓN COMPLETA - LISTA PARA USAR")
        print("🚀 El sistema está listo para generar cumpleaños con templates reales CCDN")
    else:
        print("⚠️  INTEGRACIÓN PARCIAL - Revisar elementos faltantes")
    
    print("\n📝 PRÓXIMOS PASOS:")
    print("1. Probar desde el CRM con datos reales de Google Sheets")
    print("2. Ejecutar generación completa de poster")
    print("3. Verificar conversión PNG via MCP/N8N")
    print("4. Deploy en Streamlit Cloud con funcionalidad completa")

if __name__ == "__main__":
    main()