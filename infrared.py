import cv2
import numpy as np

# Kamera akışını başlat
cap = cv2.VideoCapture(0)  # 0, varsayılan kamerayı ifade eder

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü gri tonlamaya çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Infrared işleme (örneğin, belirli bir eşik değerini geçme)
    threshold_value = 250  # Örnek eşik değeri
    _, thresholded = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    # Eşik değeri geçen bölgeleri işaretle
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)  # Çerçeve rengi yeşil

    # İşlenmiş frame'i göster
    cv2.imshow('Infrared Processed Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
