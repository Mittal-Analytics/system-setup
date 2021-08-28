import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="system_setup",
    version="0.0.1",
    author="Pratyush Mittal",
    author_email="pratyush@hey.com",
    description="Simple functions for common bash commands",
    long_description=long_description,
    url="https://github.com/arocketman/git-and-pip",
    # searches for packages within the project
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
