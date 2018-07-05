# Optical Coherence Tomography Image Reconstruction

A simple Graphical User Interface for reconstructing images from Spectral-Domain Optical Coherence Tomography (SD-OCT) data 

## Getting Started

To use this GUI, it is recommended to install a scientific computing bundle, such as [Anaconda](https://anaconda.org/anaconda/python). This software is adapted from a full, custom suite of OCT image tools built by Dr. Bizheva's OCT Lab at the University of Waterloo written in MatLab. The functionality of this software is limited, but new functions will be added in the future

### Prerequisites

Python 3.x is recommended for use, as Python 2.x has not been tested. This GUI software was built with upon many existing, fantastic packages which must be installed (many come bundled with Anaconda). The following packages are necessary:

```
matplotlib==2.1.2
scipy==1.0.0
numpy==1.14.0
Pillow==5.2.0
imageio==2.3.0
```

### Installing
To install, simply download all files to a local machine with the necessary packages. Navigate to the directory and run in a terminal:

```
python main_gui.py
```

Alternatively, the file can be run  from a Python IDE such as Anaconda


## Built With
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - Used for developing the GUI functionality
* [Scipy](https://www.scipy.org/) - Numpy, Scipy Interpolation and Signal packages, and Matplotlib are used
* [Pillow](https://pillow.readthedocs.io/en/5.2.x/) - Used for image manipulation

## Citing
If you would like to use this software, please consider citing one of our papers from the [Bizheva OCT Lab](https://scholar.google.ca/citations?user=4hgzfwgAAAAJ&hl=en) at the Univesity of Waterloo

## Customization

If you have any questions about this software or how it could be adapted to fit your needs, please don't hesitate to email the [authors](mailto:bmaclell@uwaterloo.ca)

## Authors

All software development was completed by **Benjamin MacLellan, bmaclell@uwaterloo.ca**


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* We would like to thank all past, present and future members of the research group for their help and dedication. In particular Bingyao Tan, Olivera Krajl, and Erik Mason

