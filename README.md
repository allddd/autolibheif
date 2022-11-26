# autolibheif
autolibheif is a Linux CLI utility used to conveniently encode and decode HEIF/HEIC file format, based on [libheif](https://github.com/strukturag/libheif).

Supported formats: **.jpg / .png / .HEIF / .HEIC**
## Installation
### AUR
```
git clone https://aur.archlinux.org/autolibheif.git
cd autolibheif/
makepkg -si
```
or
```
yay -S autolibheif
```
### Manual installation
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
Open the terminal and type `autolibheif` to launch the utility.
