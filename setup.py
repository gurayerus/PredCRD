"""Setup tool for PredCRD."""

from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="PredCRD",
    version="0.0.1",
    description="PredCRD - Predict Continuous Representation of Disease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kyunglok Baik, Di Wu",
    author_email="software@cbica.upenn.edu",
    maintainer="Kyunglok Baik",
    maintainer_email="kyunglok.baik@pennmedicine.upenn.edu",
    download_url="https://github.com/CBICA/PredCRD/",
    url="https://github.com/CBICA/PredCRD/",
    packages=find_packages(exclude=["tests", ".github","tabular_data"]),
    python_requires=">=3.8",
    install_requires=required,
    entry_points={"console_scripts": ["PredCRD = PredCRD.__main__:main"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    license="By installing/using PredCRD, the user agrees to the following license: See https://www.med.upenn.edu/cbica/software-agreement-non-commercial.html",
    keywords=[
        "deep learning",
        "image segmentation",
        "semantic segmentation",
        "medical image analysis",
        "medical image segmentation",
        "nnU-Net",
        "nnunet",
    ],
    package_data={"PredCRD": ["VERSION"]},
)