from PIL import Image

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

NOMBRE_IMAGEN = "imagen.png"
NOMBRE_SALIDA = "salida.txt"
NOMBRE_VISION = "vision.png"

# -----------------------------
# ABRIR IMAGEN
# -----------------------------

imagen = Image.open(NOMBRE_IMAGEN).convert("RGB")

# Verificar tamaño
if imagen.size != (60, 60):
    print("❌ Error: tamaño de imagen incorrecto.")
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
                valor = 7
            elif suma <= 191:
                valor = 6
            elif suma <= 287:
                valor = 5
            elif suma <= 382:
                valor = 4
            elif suma <= 478:
                valor = 3
            elif suma <= 574:
                valor = 2
            elif suma <= 670:
                valor = 1
            else:
                valor = 0

            archivo.write(f"-{valor}-\t")

        # Salto de línea al terminar la fila de píxeles
        archivo.write("\n")

        # Línea en blanco como separador
        archivo.write("\n")

print("✅ Archivo generado correctamente:", NOMBRE_SALIDA)

# -----------------------------
# GENERAR IMAGEN AMPLIADA
# -----------------------------

vision = Image.new("RGB", (360, 360))

for y in range(60):
    for x in range(60):

        color = imagen.getpixel((x, y))

        # Dibujar un bloque de 6x6
        for dy in range(6):
            for dx in range(6):
                vision.putpixel((x * 6 + dx, y * 6 + dy), color)

vision.save(NOMBRE_VISION)

print("✅ Imagen generada correctamente:", NOMBRE_VISION)
