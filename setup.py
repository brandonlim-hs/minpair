import os
from setuptools import find_packages, setup
from io import open
from minpair import __version__

with open("README.md") as readme_file:
    long_description = readme_file.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    install_requires = f.read().splitlines()

with open(os.path.join(os.path.dirname(__file__), 'test_requirements.txt')) as f:
    tests_require = f.read().splitlines()

setup(
    name="minpair",
    version=__version__,
    author="Brandon Lim",
    author_email="brandonlim.lim@gmail.com",
    description="Generate minimal pairs (and minimal sets).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brandonlim-hs/minpair",
    packages=find_packages(),
    license="MIT License",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="runtests.start"
)
