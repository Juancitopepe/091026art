from PIL import Image

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

NOMBRE_IMAGEN = "imagen.png"
NOMBRE_SALIDA = "salida.txt"

# -----------------------------
# ABRIR IMAGEN
# -----------------------------

imagen = Image.open(NOMBRE_IMAGEN).convert("RGB")

# Verificar tamaño
if imagen.size != (60, 60):
    print("❌ Error: la imagen debe ser de 60x60 píxeles.")
    exit()

# -----------------------------
# GENERAR ARCHIVO
# -----------------------------

with open(NOMBRE_SALIDA, "w") as archivo:

    for y in range(60):

        # Línea con el número de fila
        archivo.write(f"-{y + 1}-\n")

        # Línea con los 60 valores
        for x in range(60):

            r, g, b = imagen.getpixel((x, y))

            suma = r + g + b

            if suma <= 95:
                valor = 0
            elif suma <= 191:
                valor = 1
            elif suma <= 287:
                valor = 2
            elif suma <= 382:
                valor = 3
            elif suma <= 478:
                valor = 4
            elif suma <= 574:
                valor = 5
            elif suma <= 670:
                valor = 6
            else:
                valor = 7

            archivo.write(f"-{valor}-     ")

        # Salto de línea al terminar la fila de píxeles
        archivo.write("\n")

        # Línea en blanco como separador
        archivo.write("\n")

print("✅ Archivo generado correctamente:", NOMBRE_SALIDA)
