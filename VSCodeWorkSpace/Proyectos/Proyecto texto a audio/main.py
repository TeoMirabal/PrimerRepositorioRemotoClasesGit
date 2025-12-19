from extractor import extraer_texto_desde_url
from conversor import convertir_texto_a_audio

def main():
    url = input("🔗 Ingresá la URL del artículo: ").strip()
    titulo, texto = extraer_texto_desde_url(url)

    if texto:
        print(f"\n📄 Título del artículo: {titulo}\n")
        convertir_texto_a_audio(texto, nombre_archivo="articulo.mp3")
    else:
        print("❌ No se pudo procesar el artículo.")

if __name__ == "__main__":
    main()