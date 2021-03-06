import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylitetouch",  # Replace with your own username
    version="0.1.0",
    author="Patrick Carr",
    author_email="patrick.carr03@gmail.com",
    description="LiteTouch 5000LC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patmann03/pylitetouch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
