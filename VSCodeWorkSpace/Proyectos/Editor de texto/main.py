import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from spellchecker import SpellChecker
import re

class EditorTexto:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Mini Editor de Texto con Corrector")
        self.archivo_actual = None
        self.spell = SpellChecker(language='es')

        # Área de texto
        self.texto = ScrolledText(root, wrap=tk.WORD, font=("Consolas", 12))
        self.texto.pack(expand=True, fill='both')

        # Barra de botones
        barra_botones = tk.Frame(root)
        barra_botones.pack(fill='x')

        tk.Button(barra_botones, text="📂 Abrir", command=self.abrir_archivo).pack(side='left')
        tk.Button(barra_botones, text="💾 Guardar", command=self.guardar_archivo).pack(side='left')
        tk.Button(barra_botones, text="🔍 Revisar ortografía", command=self.revisar_ortografia).pack(side='left')
        tk.Button(barra_botones, text="🚪 Salir", command=self.salir).pack(side='right')

        # Etiqueta de estado
        self.estado = tk.Label(root, text="Archivo no guardado", anchor='w')
        self.estado.pack(fill='x')

    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if ruta:
            try:
                with open(ruta, 'r', encoding='utf-8') as archivo:
                    contenido = archivo.read()
                self.texto.delete(1.0, tk.END)
                self.texto.insert(tk.END, contenido)
                self.archivo_actual = ruta
                self.estado.config(text=f"📄 Abierto: {ruta}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")

    def guardar_archivo(self):
        if not self.archivo_actual:
            ruta = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Archivos de texto", "*.txt")])
            if not ruta:
                return
            self.archivo_actual = ruta
        try:
            with open(self.archivo_actual, 'w', encoding='utf-8') as archivo:
                archivo.write(self.texto.get(1.0, tk.END))
            self.estado.config(text=f"💾 Guardado: {self.archivo_actual}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")

    def revisar_ortografia(self):
        contenido = self.texto.get(1.0, tk.END)
        # Extraer solo palabras alfabéticas (incluye acentos y ñ)
        palabras = re.findall(r'\b[a-zA-ZáéíóúñÁÉÍÓÚÑüÜ]+\b', contenido)
        errores = self.spell.unknown(palabras)

        if not errores:
            messagebox.showinfo("Ortografía", "✅ No se encontraron errores ortográficos.")
        else:
            sugerencias = ""
            for palabra in errores:
                correcciones = self.spell.candidates(palabra)
                if correcciones and isinstance(correcciones, (set, list)):
                    sugerencias += f"❌ {palabra} → {', '.join(correcciones)}\n"
                else:
                    sugerencias += f"❌ {palabra} → (sin sugerencias)\n"
            messagebox.showwarning("Errores ortográficos encontrados", sugerencias)

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
            self.root.destroy()

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = EditorTexto(root)
    root.geometry("700x500")
    root.mainloop()