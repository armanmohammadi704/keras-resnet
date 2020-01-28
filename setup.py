import setuptools

setuptools.setup(
    name='keras_resnet',
    version='0.2.2',
    description='Keras implementation of MaskRCNN instance aware segmentation.',
    url='https://github.com/armanmohammadi704/keras_resnet',
    maintainer='Hans Gaiser',
    maintainer_email='h.gaiser@fizyr.com',
    packages=setuptools.find_packages(),
    install_requires=['keras', 'keras_resnet']
)
