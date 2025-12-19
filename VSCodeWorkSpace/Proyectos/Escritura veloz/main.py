import time

def prueba_velocidad():
    oracion_objetivo = "El momo vende rapidamente cantidades impresionantes de humo por segundo."
    print("Escribe la siguiente oración exactamente como aparece:")
    print(f"\n👉 {oracion_objetivo}\n")


    #Inicia la prueba
    input("Presiona Enter cuando estés listo para comenzar...")
    
    tiempo_inicio = time.time()

    entrada_usuario = input("\nEscribe aquí: ")

    tiempo_fin = time.time()
    
    #Duracion de la prueba
    tiempo_total = tiempo_fin - tiempo_inicio
    palabras = len(oracion_objetivo.split())
    velocidad_ppm = (len(entrada_usuario.split()) / tiempo_total) * 60

    # Verificar precisión
    if entrada_usuario == oracion_objetivo:
        precision = "✅ Precisión perfecta"
    else:
        errores = sum(1 for a, b in zip(entrada_usuario, oracion_objetivo) if a != b)
        errores += abs(len(entrada_usuario) - len(oracion_objetivo))
        precision = f"❌ Errores detectados: {errores}"

    print("\n📊 Resultados:")
    print(f"⏱️ Tiempo: {tiempo_total:.2f} segundos")
    print(f"💨 Velocidad: {velocidad_ppm:.2f} palabras por minuto")
    print(f"🎯 Precisión: {precision}")

# Ejecutar el programa
prueba_velocidad()