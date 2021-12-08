import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="time_box",
    version="0.0.2",
    author="ZeroSeeker",
    author_email="zeroseeker@foxmail.com",
    description="Time processing tool collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZeroSeeker/time_box",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
