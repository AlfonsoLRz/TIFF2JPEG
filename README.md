# **TIFF2JPEG (DJI ZenmuseXT2)**
Image converter from TIFF to JPEG for files captured from a **DJI Zenmuse XT2** device. Temperature values are stored in `.csv` files, whereas `.jpg` images are saved along with the `.tiff` metadata, so single viewpoints can be further processed through their metadata.

![Thermal Composition](Assets/Teaser.png)

### Methodology

From an input folder, `.tiff` images are read and converted into `.jpg`, which are subsequently saved in another folder. Temperature from each pixel is also stored in `.csv` files. Then, exiftool is launched to transfer metadata from `.tiff` images to the previously generated `.jpg` files.

### Usage

The python script only requires input and output folders as well as a boolean value indicating if the device was configured in `high_gain` mode. By default, it is false.

> High gain mode changes the multiplying factor in the formula that converts Kelvin measurements to Celsius **(img * factor - 273.15)** . High gain uses a factor of `0.04`, whereas the alternative mode uses `0.4`.

`tiff2jpeg.py --input folder --output folder --high_gain`

The script looks both for `.tiff` and `.tif` files in the input folder, so there is no need in passing the correct extension.
