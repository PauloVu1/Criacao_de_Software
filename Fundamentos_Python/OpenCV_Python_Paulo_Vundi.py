
import	cv2 # Importar a biblioteca OpenCV 

print("Estes códigos resultam de uma colaboração direta com o chatgpt da openai")
# Abrir e exibir uma imagem

img = cv2.imread('plane-343.jpg')                   # Carrega a imagem
resized = cv2.resize(img, (300, 200))
cv2.imshow('Minha Imagem', resized) 
cv2.imshow('Imagem', resized) 
cv2.waitKey(0)                                   # Espera uma tecla
cv2.destroyAllWindows()                          # Fecha todas as janelas

"""

# Ler e exibir um vídeo
import	cv2
cap = cv2.VideoCapture('video.mp4')              # Carrega o vídeo

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Vídeo', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):       # Sai ao pressionar 'q'
        break

cap.release()
cv2.destroyAllWindows()

# Converter uma imagem para escala de cinza

img = cv2.imread('imagem.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Cinza', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Redimensionar uma imagem 

img = cv2.imread('imagem.jpg')
resized = cv2.resize(img, (300, 200))           # (largura, altura)

cv2.imshow('Redimensionada', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Salvar uma imagem processada
import cv2
img = cv2.imread('imagem.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('imagem_cinza.jpg', gray)

"""