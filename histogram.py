import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt

# Memuat gambar berwarna (RGB)
image_path = r"C:\Users\HP\Documents\Tugas Kampus Unsp\Semester 5\Pengolahan Citra Digital\PCD\rgb.jpeg"
image = iio.imread(image_path)

# Mengonversi gambar RGB ke Grayscale
gray_image = np.dot(image[..., :3], [0.299, 0.587, 0.114])

# Menghitung histogram (jumlah piksel untuk setiap intensitas 0-255)
histogram, bins = np.histogram(gray_image, bins=256, range=(0, 255))

# Menampilkan histogram
plt.figure(figsize=(10, 5))
plt.bar(bins[:-1], histogram, width=1, color='black')
plt.xlabel("Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.title("Histogram Gambar Grayscale")
plt.tight_layout()
plt.show()

# Menampilkan hasil grayscale
plt.figure(figsize=(5, 5))
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.title("Gambar Grayscale")
plt.tight_layout()
plt.show()
