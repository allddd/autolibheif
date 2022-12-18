# autolibheif
autolibheif is a Linux CLI utility for convenient encoding and decoding of the HEIF/HEIC file format.

Supported formats: **.jpg / .png / .HEIF / .HEIC**
## Installation
### Arch-based distributions
Manual
```
git clone https://aur.archlinux.org/autolibheif.git
cd autolibheif/
makepkg -si
```
Using AUR helpers
```
yay -S autolibheif
```
### Other distributions
**Dependencies:**
[libheif](https://github.com/strukturag/libheif),
[python-setuptools](https://github.com/pypa/setuptools)

```
# create virtual environment if needed
git clone https://github.com/allddd/autolibheif.git
cd autolibheif/
python setup.py install
```
## Usage
Launch the utility from a terminal by typing `autolibheif`