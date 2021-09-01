# VIRTUAL DRAWING PAD USING OPENCV

**Vdp or virtual drawing pad** is a opencv implementation which follows two important operations:
1. To find the upper and lower ranges of HSV values to detect the object which is to be used as Stylus.
2. To find the contours of the object and finally finding out its centroid which will be tracked to draw on the drawing pad.

### THRESHOLDING
![](https://i.imgur.com/MLi6Liw.gif)

### RESULTS
![](https://i.imgur.com/HumIH0y.gif)

#### IMPORTANT CONSIDERATION:
1. Thresholding is performed on HSV and not on RGB because HSV, it separates the image intensity, from the color information.
2. Morphological transformation like dilation and closing are performed in order to remove the noise.
3. Unnecessary contour can be removed by the selecting the maximum area.

### Concepts Used:
1. Guassian Blurring.
2. Image Thresholding.
3. Morphological operation.
4. Contour detection.
5. Finding centroid by momemts.
 
