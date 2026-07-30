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

        fila.append(str(valor))

    archivo.write(" ".join(fila))

    if y != 59:
        archivo.write("\n")

print("✅ Archivo generado correctamente:", NOMBRE_SALIDA)
