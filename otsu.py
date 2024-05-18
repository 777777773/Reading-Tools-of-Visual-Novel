import cv2

# 读取图像
img = cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE)

# 应用Otsu阈值处理
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 将处理后的图像保存为新的文件
cv2.imwrite('1.png', thresh)


# 关闭所有窗口
cv2.destroyAllWindows()
