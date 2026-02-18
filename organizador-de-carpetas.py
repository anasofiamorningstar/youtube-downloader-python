import os
import shutil

def organizar_carpeta(ruta):
    # Definimos los tipos de archivos y sus carpetas
    extensiones = {
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Musica': ['.mp3', '.wav', '.flac'],
        'Comprimidos': ['.zip', '.rar', '.tar', '.gz']
    }

    # Cambiar al directorio deseado
    os.chdir(ruta)

    for archivo in os.listdir():
        # Saltamos si es una carpeta
        if os.path.isdir(archivo):
            continue
            
        # Extraemos la extensión
        nombre, ext = os.path.splitext(archivo)
        ext = ext.lower()

        # Buscamos a qué categoría pertenece
        movido = False
        for carpeta, lista_ext in extensiones.items():
            if ext in lista_ext:
                # Creamos la carpeta si no existe
                if not os.path.exists(carpeta):
                    os.makedirs(carpeta)
                
                # Movemos el archivo
                shutil.move(archivo, os.path.join(carpeta, archivo))
                print(f"Movido: {archivo} -> {carpeta}")
                movido = True
                break
        
        if not movido and ext != "":
            if not os.path.exists('Otros'):
                os.makedirs('Otros')
            shutil.move(archivo, os.path.join('Otros', archivo))

# --- Ejecución ---
if __name__ == "__main__":
    mi_ruta = input("Introduce la ruta de la carpeta a organizar: ")
    if os.path.exists(mi_ruta):
        organizar_carpeta(mi_ruta)
        print("\n¡Carpeta organizada con éxito!")
    else:
        print("La ruta no es válida.")
        