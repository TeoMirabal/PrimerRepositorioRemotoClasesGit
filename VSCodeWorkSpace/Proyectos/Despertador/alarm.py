import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
import time
import random
import webbrowser
from datetime import datetime, timedelta
from pystray import Icon, MenuItem, Menu
from PIL import Image
import os
import platform
import subprocess

# Configuración
ARCHIVO_LINKS = "youtube_links.txt"
SONIDO_LOCAL = "alarma.mp3"  # Opcional: sonido local para reproducir junto al video

# Leer enlaces desde archivo
def leer_links(ruta):
    try:
        with open(ruta, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

# Reproducir sonido local
def reproducir_sonido_local():
    if not os.path.exists(SONIDO_LOCAL):
        return
    if platform.system() == "Windows":
        import winsound
        winsound.PlaySound(SONIDO_LOCAL, winsound.SND_FILENAME)
    else:
        subprocess.call(["afplay", SONIDO_LOCAL])  # macOS
        # En Linux podrías usar mpg123 o aplay

# Esperar hasta la hora programada
def esperar_y_reproducir(hora_objetivo, links):
    while True:
        ahora = datetime.now()
        if ahora >= hora_objetivo:
            if links:
                video = random.choice(links)
                webbrowser.open(video)
                reproducir_sonido_local()
            else:
                print("⚠️ No hay enlaces disponibles.")
            # Repetir al día siguiente
            hora_objetivo += timedelta(days=1)
        time.sleep(30)

# GUI principal
class AlarmaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⏰ Reloj Despertador YouTube")
        self.root.geometry("350x250")
        self.root.protocol("WM_DELETE_WINDOW", self.minimizar_a_bandeja)

        # Widgets
        tk.Label(root, text="Hora de la alarma (HH:MM):").pack(pady=5)
        self.entrada_hora = tk.Entry(root, justify='center', font=("Arial", 14))
        self.entrada_hora.pack()

        tk.Label(root, text="Fecha (YYYY-MM-DD) [opcional]:").pack(pady=5)
        self.entrada_fecha = tk.Entry(root, justify='center', font=("Arial", 12))
        self.entrada_fecha.pack()

        tk.Button(root, text="Activar Alarma", command=self.activar_alarma).pack(pady=10)
        tk.Button(root, text="Ver enlaces cargados", command=self.mostrar_links).pack()

        self.icono_bandeja = None

    def activar_alarma(self):
        hora = self.entrada_hora.get()
        fecha = self.entrada_fecha.get().strip()

        if not hora or len(hora) != 5 or ":" not in hora:
            messagebox.showerror("Error", "Formato de hora inválido. Usa HH:MM.")
            return

        try:
            if fecha:
                fecha_hora = datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
            else:
                ahora = datetime.now()
                fecha_hora = datetime.strptime(f"{ahora.date()} {hora}", "%Y-%m-%d %H:%M")
                if fecha_hora < ahora:
                    fecha_hora += timedelta(days=1)
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Usa YYYY-MM-DD.")
            return

        links = leer_links(ARCHIVO_LINKS)
        if not links:
            messagebox.showwarning("Sin enlaces", "No se encontraron enlaces en el archivo.")
            return

        threading.Thread(target=esperar_y_reproducir, args=(fecha_hora, links), daemon=True).start()
        messagebox.showinfo("Alarma activada", f"La alarma sonará a las {fecha_hora.strftime('%Y-%m-%d %H:%M')}.")
        self.minimizar_a_bandeja()

    def mostrar_links(self):
        links = leer_links(ARCHIVO_LINKS)
        if not links:
            messagebox.showinfo("Enlaces", "No se encontraron enlaces.")
        else:
            vista = "\n".join(links)
            messagebox.showinfo("Enlaces cargados", vista)

    def minimizar_a_bandeja(self):
        self.root.withdraw()
        imagen = Image.open("icon.png")
        menu = Menu(MenuItem("Mostrar", self.mostrar_ventana), MenuItem("Salir", self.salir))
        self.icono_bandeja = Icon("Alarma", imagen, "Reloj Despertador", menu)
        threading.Thread(target=self.icono_bandeja.run, daemon=True).start()

    def mostrar_ventana(self, icon, item):
        self.root.after(0, self.root.deiconify)
        icon.stop()

    def salir(self, icon, item):
        icon.stop()
        self.root.quit()

# Ejecutar app
if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmaApp(root)
    root.mainloop()