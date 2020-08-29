from setuptools import setup

with open("README.md") as README:
    long_description = README.read()

setup(
    name='minesweeperPy',
    version='2.0',
    description='A simple minesweeper generator for Python 3',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Steven Shrewsbury',
    author_email='',
    url='https://github.com/stshrewsburyDev/minesweeperPy',
    packages=['minesweeper'],
    install_requires=[],
    python_requires='>=3.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)