from setuptools import setup
import glob
import os

setup(
    name="dense_basis",
    version="0.1.2",
    author="Kartheik Iyer",
    author_email="kartheik.iyer@dunlap.utoronto.ca",
    url = "https://github.com/kartheikiyer/dense_basis",
    packages=["dense_basis"],
    description="SED fitting with non-parametric star formation histories",
    long_description=open("README.md").read(),
    package_data={"": ["README.md", "LICENSE"], "dense_basis": ["train_data/*.mat", "pregrids/*.mat", "filters/*.dat", "filters/filter_curves/goods_s/*.txt","filters/filter_curves/goods_n/*.txt", "filters/filter_curves/cosmos/*.txt", "filters/filter_curves/egs/*.txt", "filters/filter_curves/uds/*.txt"]},
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    install_requires=["matplotlib", "numpy", "scipy", "george", "sklearn"]
)