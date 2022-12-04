# spline_fitting
Draw points on an image and fit an n-degree spine

## Requirements:
- numpy
- opencv
- pygame
- argparse
- scipy

Linux:
```
pip3 install numpy opencv-python pygame argparse scipy
```
Windows/MacOS:
```
conda install -c conda-forge numpy opencv cogsci pygame argparse scipy
```

## Usage:
For help with usage:
```python3 fit.py -h```

Set input image with --image/-i
```
python3 fit.py -i img.jpg
```

Set degree of polynomial to fit with --degree/-d
```
python3 fit.py -d 3
```

Example (fit cubic spline to image: 'img.jpg'):
```
python3 fit.py -i img.jpg -d 3
```
