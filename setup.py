import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="indodax",
    version="1.1",
    author="Mame29",
    author_email="evanr0240@gmail.com",
    description="paket ini untuk jual beli di indodax",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mame29/Indodax",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
