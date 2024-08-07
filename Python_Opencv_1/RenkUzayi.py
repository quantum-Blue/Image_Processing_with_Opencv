import cv2


img=cv2.imread("rei.png")
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow("rei",img)
cv2.imshow("rgb",img1)
cv2.imshow("HSV",img2)
cv2.imshow("grey",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()








