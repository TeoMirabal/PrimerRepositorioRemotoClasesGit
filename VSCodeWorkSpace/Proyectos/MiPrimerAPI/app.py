from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hola Teo, tu API Flask está viva</h1>
    <br>
    <h2>Tu perfil:</h2>
    <ul>
        <li>Automatización con bots</li>
        <li>Calistenia</li>
        <li>Desarrollo backend</li>
        <li>Seguridad estructurada</li>
    </ul>
    """