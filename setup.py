import setuptools

setuptools.setup(
    name='keras-resnet',
    version='0.1.0',
    description='Keras implementation of MaskRCNN instance aware segmentation.',
    url='https://github.com/armanmohammadi704/keras-resnet',
    maintainer='Hans Gaiser',
    maintainer_email='h.gaiser@fizyr.com',
    packages=setuptools.find_packages(),
    install_requires=['keras']
)
