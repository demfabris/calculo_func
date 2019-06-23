import setuptools

with open("README.md", "w+") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calculo_func",
    version="0.0.1",
    author="fabricio7p",
    author_email="fabricio7p@gmail.com",
    description="This program calculates stuff",
    long_description="Program made by fabricio7p",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
