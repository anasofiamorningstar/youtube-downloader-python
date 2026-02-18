import tkinter as tk
from tkinter import messagebox, ttk
from plyer import notification
import time
import threading

def enviar_notificacion(tarea, tiempo_espera):
    """Función que corre en segundo plano para esperar y notificar."""
    # Convertimos minutos a segundos
    time.sleep(tiempo_espera * 60)
    
    try:
        notification.notify(
            title="🔔 ¡Recordatorio Importante!",
            message=f"Tarea pendiente: {tarea}",
            app_name="Bot de Recordatorios",
            timeout=10
        )
    except Exception as e:
        print(f"Error al enviar notificación: {e}")

def iniciar_hilo():
    tarea = entrada_tarea.get().strip()
    tiempo_raw = entrada_tiempo.get().strip()

    # 1. Validación de campos vacíos
    if not tarea or not tiempo_raw:
        messagebox.showwarning("Atención", "Por favor, llena ambos campos.")
        return

    # 2. Validación de número válido
    try:
        minutos = float(tiempo_raw)
        if minutos <= 0:
            messagebox.showwarning("Error", "El tiempo debe ser mayor a 0.")
            return
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido (ej: 5 o 0.5).")
        return

    # 3. Crear el hilo "Daemon" (Se cierra si cierras la app)
    hilo = threading.Thread(target=enviar_notificacion, args=(tarea, minutos))
    hilo.daemon = True 
    hilo.start()

    # 4. Feedback visual y limpieza
    messagebox.showinfo("Bot Activo", f"Ok, te recordaré: '{tarea}' en {minutos} min.")
    entrada_tarea.delete(0, tk.END)
    entrada_tiempo.delete(0, tk.END)

# --- Configuración de la Ventana (Interfaz mejorada) ---
ventana = tk.Tk()
ventana.title("Mi Bot de Recordatorios")
ventana.geometry("350x300")
ventana.configure(padx=20, pady=20)

# Estilo con Etiquetas
tk.Label(ventana, text="📌 Tarea a recordar:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
entrada_tarea = ttk.Entry(ventana, width=40)
entrada_tarea.pack(pady=(0, 15))

tk.Label(ventana, text="⏳ Tiempo (en minutos):", font=("Segoe UI", 10, "bold")).pack(anchor="w")
entrada_tiempo = ttk.Entry(ventana, width=15)
entrada_tiempo.pack(anchor="w", pady=(0, 20))

# Botón con Estilo
btn_recordar = tk.Button(
    ventana, 
    text="🔔 ACTIVAR RECORDATORIO", 
    command=iniciar_hilo, 
    bg="#2ecc71", 
    fg="white", 
    font=("Segoe UI", 10, "bold"),
    cursor="hand2",
    relief="flat",
    padx=10,
    pady=5
)
btn_recordar.pack(fill="x")

ventana.mainloop()