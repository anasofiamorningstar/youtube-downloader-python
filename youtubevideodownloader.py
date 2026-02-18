import tkinter as tk
from tkinter import messagebox, ttk
import yt_dlp
import threading

def descargar_video():
    url = entrada_url.get().strip()
    if not url:
        messagebox.showwarning("Atención", "Pega un link de YouTube")
        return

    def proceso_descarga():
        try:
            btn_descargar.config(state="disabled")
            status_label.config(text="📥 Descargando... por favor espera.", fg="blue")
            
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s',
                'noplaylist': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            messagebox.showinfo("Éxito", "¡Video descargado correctamente!")
            status_label.config(text="✅ ¡Listo!", fg="green")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo descargar: {e}")
            status_label.config(text="❌ Error", fg="red")
        finally:
            btn_descargar.config(state="normal")
            entrada_url.delete(0, tk.END)

    threading.Thread(target=proceso_descarga, daemon=True).start()

# --- Funciones para habilitar el Pegado ---
def pegar_texto(event=None):
    try:
        texto = ventana.clipboard_get()
        entrada_url.insert(tk.INSERT, texto)
    except tk.TclError:
        pass

# --- Interfaz Gráfica ---
ventana = tk.Tk()
ventana.title("Python YT Downloader")
ventana.geometry("450x250")
ventana.configure(padx=20, pady=20)

tk.Label(ventana, text="Enlace de YouTube:", font=("Arial", 10, "bold")).pack()

# Usamos Entry normal para evitar conflictos de estilos
entrada_url = tk.Entry(ventana, width=50, font=("Arial", 10))
entrada_url.pack(pady=10)

# Habilitar Ctrl+V explícitamente
entrada_url.bind("<Control-v>", pegar_texto)
entrada_url.bind("<Control-V>", pegar_texto)

# Menú de clic derecho para pegar
menu_contextual = tk.Menu(ventana, tearoff=0)
menu_contextual.add_command(label="Pegar", command=pegar_texto)

def mostrar_menu(event):
    menu_contextual.post(event.x_root, event.y_root)

entrada_url.bind("<Button-3>", mostrar_menu) # Clic derecho

btn_descargar = tk.Button(
    ventana, 
    text="⬇ Descargar Video", 
    command=descargar_video, 
    bg="#FF0000", 
    fg="white", 
    font=("Arial", 10, "bold"),
    pady=5
)
btn_descargar.pack(pady=10)

status_label = tk.Label(ventana, text="Esperando enlace...", fg="gray")
status_label.pack()

ventana.mainloop()
