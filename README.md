# 🍃 Leaf Area Density Estimation Using OpenCV

This project estimates the **leaf area density** of rubber plant images using image processing techniques in **OpenCV**. The approach involves detecting green leaf areas in an image, segmenting them using color and edge-based filtering, and calculating the **percentage of leaf coverage** relative to the total image area. The method can help in automating plant growth monitoring in rubber nurseries.

---

##  Key Features

- Detects leaf regions using Canny edge detection and contour filling
- Enhances leaf visibility by adjusting intensity
- Segments green regions using RGB color thresholding
- Applies morphological operations to refine segmentation
- Calculates **Leaf Area Density (%)**
- Supports real-time visual inspection with `cv2.imshow`

---

##  Methodology

1. **Image Reading**: Loads a nursery image (e.g., `Nursery/r1.png`)
2. **Preprocessing**: Converts to grayscale and applies Gaussian blur
3. **Edge Detection**: Uses Canny edge detection to identify leaf boundaries
4. **Contour Extraction**: Fills leaf contours to build a binary leaf mask
5. **Intensity Adjustment**: Enhances intensity inside detected leaf areas
6. **Green Color Detection**: Uses RGB thresholding to isolate green leaf areas
7. **Morphological Processing**: Applies closing operation to clean the green mask
8. **Density Calculation**: Computes the proportion of green pixels to total pixels

---

##  Sample Output

- Original nursery image with enhanced leaf regions
- Binary mask showing detected leaf shapes
- Final masked image highlighting green leaf area
- Leaf Area Density printed as a percentage

---

##  File Structure
Leaf-Area-Density/
│
├── Nursery/
│ └── r1.png # Sample input image
├── leaf_area_density.py # Main script for leaf detection
└── README.md # Project documentation
