import cv2 as cv

link = r'C:\Users\suyash\Pictures/Camera Roll/imgop.jpg'
im = cv.imread(link)
img = cv.resize(im, (500,500) ,interpolation=cv.INTER_AREA)
cv.imshow('image', img)


#1. Averaging Blur Effect
avg = cv.blur(img, (5,5))  #Here the two no. is the size of cornol you want to take the bigger the sizde the larger the effect.
cv.imshow('Average', avg)


#2. Gaussian Blur Effect
gsb = cv.GaussianBlur(img, (5,5), 10)   #This is said to be natural because it gives weight to the pixels so the pixel near 
cv.imshow('gaussian', gsb)              #will have a larger effect.

gsb1 = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('gaussian1', gsb1)


#3. Median Blur Effect
median = cv.medianBlur(img, 5)   #Median blur does teh same as average except that it take the median value(smug effect).
cv.imshow('median', median)

#4. Bilateral Blur Effect
bil = cv.bilateralFilter(img, 50, 150, 150) 
cv.imshow('Bilateral', bil)
