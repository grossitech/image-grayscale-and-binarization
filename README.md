# Manual Image Processor: Grayscale & Binary Conversion

![Language](https://img.shields.io/badge/Language-Python-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

This project is a hands-on implementation of fundamental image processing algorithms in Python. The challenge is to convert a color image into both grayscale and binary (black and white) formats by manually manipulating each pixel, without relying on high-level image processing libraries like OpenCV or Scikit-Image for the core transformations.

---

## 📖 About The Project

The main goal is to demonstrate a foundational understanding of how digital images are represented and can be manipulated programmatically. The script performs a two-step dimensionality reduction on a given image:

1.  **Color to Grayscale:** Reduces a 3-channel (RGB) image to a single-channel image representing luminosity (from 0 to 255).
2.  **Grayscale to Binary:** Further reduces the image information by converting the 256 possible shades of gray into just two values: 0 (black) and 255 (white).

The Pillow (PIL) library is used only for the essential I/O tasks of loading the source image and saving the resulting files.

---

## ✨ Features

* Downloads an image from any public URL.
* Converts the color image to grayscale using the standard luminosity method.
* Converts the grayscale image to a binary image using a fixed threshold.
* Saves the processed images with dynamic filenames based on the original source (e.g., `original.png` -> `original_grayscale.png`).
* Implemented using standard Python loops and data structures.

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python 3 installed on your system.

### Installation

1.  Clone the repository (or download the `.py` file).
2.  Install the necessary Python libraries:
    ```sh
    pip install Pillow requests
    ```

### Execution

Run the script from your terminal:
```sh
python image_processor.py
```
The script will download the source image, process it, and save the `_grayscale` and `_binary` versions in the same directory. It will also open the resulting images using your system's default image viewer.

## 🛠️ How It Works
The processing logic is implemented from scratch:

* Grayscale Conversion: Each pixel's RGB values are converted to a single grayscale value using the weighted luminosity formula, which accounts for human eye perception:
`Gray = int(0.299*R + 0.587*G + 0.114*B)`

* Binarization: A fixed threshold (127) is applied to the grayscale image. Each pixel is checked:

    * If `gray_value > 127`, the new pixel becomes `255` (white).

    * Otherwise, the new pixel becomes `0` (black).

## 👨‍💻 Author

<img 
  align=left 
  margin=10 
  width=80 
  src="https://avatars.githubusercontent.com/u/188269406"
/>
<p>&nbsp&nbsp&nbsp&nbspLuciano Grossi<br/><br/>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/grossitech"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
    <a href="https://twitter.com/lucianogrossi"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a>
    <a href="https://www.linkedin.com/in/lucianogrossi"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

---

## 📜 License

This project is under the MIT License. See the [LICENSE](LICENSE) file for more details.