import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# --- 1. GENERATING AND MANIPULATING NDARRAYS ---
my_array = np.array([1.1, 9.2, 8.1, 4.7])
print("1D Array Shape:", my_array.shape)
print("1D Array Dimensions:", my_array.ndim)

array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])
print("2D Array Shape:", array_2d.shape)

mystery_array = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]],
                          [[7, 86, 6, 98], [5, 1, 0, 4]],
                          [[5, 36, 32, 48], [97, 0, 27, 18]]])
print("3D Array Shape:", mystery_array.shape)
print("Specific Value:", mystery_array[2, 1, 2])
print("Slicing all rows/cols on first axis:\n", mystery_array[:, :, 0])

a = np.arange(10, 30)
print("Arange 10 to 30:", a)
print("Last 3 elements:", a[-3:])
print("Elements 3 to 6:", a[3:6])
print("Elements 12 onwards:", a[12:])
print("Every other element:", a[::2])
print("Reversed Array:", np.flip(a))

b = np.array([6,0,9,0,0,5,0])
print("Indices of non-zero elements:", np.nonzero(b))

z = np.random.random((3,3,3))
print("3x3x3 Random Array:\n", z)

x = np.linspace(0, 100, num=9)
y = np.linspace(-3, 3, num=9)
plt.plot(x, y)
plt.title("Linspace Plot")
plt.show()

noise = np.random.random((128,128,3))
plt.imshow(noise)
plt.title("Random Noise Image")
plt.show()

# --- 2. BROADCASTING AND MATRIX MULTIPLICATION ---
v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
print("Vector Addition:", v1 + v2)
print("Vector Multiplication:", v1 * v2)

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])
b1 = np.array([[4, 1, 3],
               [5, 8, 5]])
print("Matrix Multiplication (Dot Product):\n", np.matmul(a1, b1))

# --- 3. MANIPULATING IMAGES AS NDARRAYS ---
img = mpimg.imread('yummy_macarons.jpg')
print("Image Shape (Height, Width, Channels):", img.shape)
print("Image Dimensions:", img.ndim)

plt.imshow(img)
plt.title("Original Image")
plt.show()

# Color Inversion (Subtracting current pixel values from max value 255)
inverted_img = 255 - img
plt.imshow(inverted_img)
plt.title("Inverted Colors")
plt.show()

# Convert to Grayscale using standard human perception weights
grey_vals = np.array([0.2126, 0.7152, 0.0722])
img_gray = np.matmul(img, grey_vals)

plt.imshow(img_gray, cmap='gray')
plt.title("Grayscale Image")
plt.show()