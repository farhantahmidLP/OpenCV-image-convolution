import numpy as np
import cv2
import os
from tkinter import *
from tkinter.filedialog import askopenfilename


#prompt user to select image
Tk().withdraw() 
image = askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png")])
img = cv2.imread(image)
window_name='Image Processor'
directory = os.path.dirname(image)
counter=0


#show image in window
def show(before, after):
    global window_name, result_img
    result_img=cv2.filter2D(img,0,conv_kernel)
    view = np.concatenate((before, result_img), axis=1)
    cv2.imshow(window_name, view)


#button functions
def close():
   root.quit()
   cv2.destroyAllWindows()

def sharpen_img():
    global conv_kernel
    print("sharpen")
    conv_kernel=sharpen
    show(img, result_img)

def laplacian_img():
    global conv_kernel
    print("laplacian")
    conv_kernel=laplacian
    show(img, result_img)

def ridge_img():
    global conv_kernel
    print("laplacian ridge")
    conv_kernel=ridge
    show(img, result_img)

def sobel_x_img():
    global conv_kernel
    print("Sobel X")
    conv_kernel=sobel_x
    show(img, result_img)

def sobel_y_img():
    global conv_kernel
    print("Sobel Y")
    conv_kernel=sobel_y
    show(img, result_img)

def box_blur_img():
    global conv_kernel
    print("box blur")
    conv_kernel=box_blur
    show(img, result_img)

def gauss_blur_img():
    global conv_kernel
    print("gauss blur")
    conv_kernel=gaussian_blur
    show(img, result_img)

def identity_img():
    global conv_kernel
    print("identity")
    conv_kernel=identity
    show(img, result_img)

def new_img():
    global image, img, window_name, directory
    cv2.destroyAllWindows()
    Tk().withdraw() 
    image = askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png")])
    img = cv2.imread(image)
    directory = os.path.dirname(image)
    window_name='Image Processor'
    view = np.concatenate((img, result_img), axis=1)
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, view)

def save_img():
    global result_img, directory, img, counter
    os.chdir(directory) 
    cv2.imwrite('processed_img'+str(counter)+'.jpg', result_img)
    counter+=1
    print('Image saved at '+directory)


#kernels
sharpen=np.array([[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]])

laplacian=np.array([[0, -1, 0],
                    [-1, 4, -1],
                    [0, -1, 0]])

sobel_x=np.array([[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]])

sobel_y=np.array([[-1, -2, -1],
                  [0, 0, 0],
                  [1, 2, 1]])

ridge=np.array([[-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]])

box_blur=(1/9)*np.array([[1, 1, 1],
                         [1, 1, 1],
                         [1, 1, 1]])

gaussian_blur=(1/16)*np.array([[1, 2, 1],
                               [2, 4, 2],
                               [1, 2, 1]])

identity=np.array([[0, 0, 0],
                   [0, 1, 0],
                   [0, 0, 0]])



#applying the kernels
conv_kernel=laplacian #default
result_img=cv2.filter2D(img,0,conv_kernel)


#create and show window
view = np.concatenate((img, result_img), axis=1)
cv2.namedWindow(window_name)
cv2.imshow(window_name, view)


#create the main window and buttons
root = Tk()
root.geometry("250x320")
root.title("Kernels ")

sharp_button=Button(root, text= "Sharpen", command=sharpen_img)
laplace_button=Button(root, text= "Laplacian", command=laplacian_img)
sobel_x_button=Button(root, text= "Sobel X", command=sobel_x_img)
sobel_y_button=Button(root, text= "Sobel Y", command=sobel_y_img)
ridge_button=Button(root, text= "Laplacian Ridge", command=ridge_img)
box_bl_button=Button(root, text= "Box Blur", command=box_blur_img)
gauss_bl_button=Button(root, text= "Gaussian Blur", command=gauss_blur_img)
identity_button=Button(root, text= "Identity", command=identity_img)
exit_button=Button(root, text= "Close", command=close)
new_img_button=Button(root, text= "New Image", command=new_img)
save_img_button=Button(root, text= "Save Image", command=save_img)

exit_button.pack()
sharp_button.pack()
laplace_button.pack()
sobel_x_button.pack()
sobel_y_button.pack()
ridge_button.pack()
box_bl_button.pack()
gauss_bl_button.pack()
identity_button.pack()
new_img_button.pack()
save_img_button.pack()

root.mainloop()
root.destroy()
cv2.destroyAllWindows()
