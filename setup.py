from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

    name='autolibheif',
    author='allddd',
    author_email='allddd@proton.me',
    version='1.0.2',
    description='CLI utility for encoding and decoding the HEIF/HEIC file format',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/allddd/autolibheif',
    packages=find_packages(),
    entry_points={
        'console_scripts':  [
            'autolibheif = src.autolibheif:main',
        ],
    },

)
