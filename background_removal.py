# Importar cv2 para capturar el video.
import cv2

import numpy as np

# Establecer el índice de cámara como 0.
camera = cv2.VideoCapture(0)

# Establecer el ancho y altura del cuadro como 640 X 480.
camera.set(3 , 640)
camera.set(4 , 480)

# Cargar la imagen de la montaña.
mountain = cv2.imread('mount-everest.jpg')

# Ajustar el tamaño de la imagen de la montaña a 640 X 480.
cv2.resize(mountain, (640,480))

while True:

    # Leer el cuadro desde la cámara establecida.
    status , frame = camera.read()

    # Si obtenemos el cuadro exitosamente.
    if status:

        # Lo volteamos.
        frame = cv2.flip(frame , 1)

        # Convertir la imagen a RGB para un procesamiento sencillo.
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # Crear límites.
        lower_bound = np.array([100,100,100])
        upper_bound = np.array([255,255,255])

        # Poner límites a la imagen.
        mask_1 = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        # Invertir la máscara.
        mask_2 = cv2.bitwise_not(mask_1)

        # Operación de bit a bit y operación para extraer el primer plano / persona.
        rest_1 = cv2.bitwise_and(frame,frame, mask=mask_2)
        print(rest_1)

        # Imagen final.
        final_image = np.where(mask_2==mask_1, rest_1, mask_1)
    
        # Mostrar la imagen final.
        cv2.imshow('image' , final_image)

        # Esperar 1ms antes de mostrar otro cuadro.
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# Soltar la cámara y cerrar todas las ventanas abiertas.
camera.release()
cv2.destroyAllWindows()
