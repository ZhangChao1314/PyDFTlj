import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydftlj",
    version="0.0.1",
    author="Elvis Soares", #<<<
    author_email="elvis.asoares@gmail.com", #<<<
    description="A DFT package for LJ fluids in Python", #<<<
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elvissoares/PyDFTlj",  #<<<
    install_requires=[         
        'pandas',         
        'numpy',
        'matplotlib',
        'scipy',
        'scienceplots',
        'torch',
    ],
    packages=setuptools.find_packages(
        where='.',
        include=['pydftlj*'],  # alternatively: `exclude=['additional*']`
        ),
    classifiers=[
        "Programming Language :: Python :: 3", 
        "Operating System :: OS Independent",
    ],
)
