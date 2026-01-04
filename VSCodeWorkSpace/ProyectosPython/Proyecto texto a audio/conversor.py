from gtts import gTTS

def convertir_texto_a_audio(texto, nombre_archivo="salida.mp3", idioma="es"):
    try:
        tts = gTTS(text=texto, lang=idioma)
        tts.save(nombre_archivo)
        print(f"✅ Audio guardado como {nombre_archivo}")
    except Exception as e:
        print(f"Error al convertir a audio: {e}")