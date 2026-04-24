"""Setup script for audb."""
import os

from setuptools import find_packages, setup


def read(fname):
    """Read a file relative to the setup.py location."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_version():
    """Read version from audb/core/version.py."""
    version = {}
    with open(os.path.join("audb", "core", "version.py")) as f:
        exec(f.read(), version)
    return version["__version__"]


setup(
    name="audb",
    version=read_version(),
    description=(
        "Tool for managing and sharing audio datasets, "
        "a fork of audeering/audb."
    ),
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    url="https://github.com/your-org/audb",
    author="Your Organization",
    author_email="contact@your-org.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "audeer>=1.20.0",
        "audformat>=1.0.0",
        "audiofile>=1.1.0",
        "oyaml>=1.0",
        "pandas>=1.1.5",
        "pyarrow>=6.0.0",
        "requests>=2.25.0",
        "tqdm>=4.62.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "sphinx>=5.0.0",
            "sphinx-audeering-theme>=1.3.0",
            "pre-commit>=2.20.0",
        ],
    },
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "audb=audb.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    zip_safe=False,
)
