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

        fila = []

        for x in range(60):

            r, g, b = imagen.getpixel((x, y))

            suma = r + g + b

            fila.append(str(suma))

        archivo.write(" ".join(fila))

        if y != 59:
            archivo.write("\n")

print("✅ Archivo generado correctamente:", NOMBRE_SALIDA)
