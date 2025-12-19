from newspaper import Article

def extraer_texto_desde_url(url):
    try:
        articulo = Article(url, language='es')
        articulo.download()
        articulo.parse()
        return articulo.title, articulo.text
    except Exception as e:
        print(f"Error al extraer el artículo: {e}")
        return None, None