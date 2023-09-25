import setuptools
import os
import sys

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
#     print (long_description)
# cwd = os.getcwd()
# os.system(f'ls {cwd}')


setuptools.setup(
    name="pyHDR",
    author="Health Data Research UK",
    version="0.1",
    author_email="calum.macdonald@hdruk.ac.uk",
    description="",
    long_description=None,
    long_description_content_type="text/markdown",
    url="https://github.com/HDRUK/schemata-2",
    packages=setuptools.find_packages(),
    install_requires=[
        "pydantic",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
