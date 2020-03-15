from setuptools import setup, find_packages


setup(
    name="mixp", 
    version="0.0.2",
    author="Casey Ellis",
    author_email="cjellis@uchicago.edu",
    description="MSCA Class Package",
    long_description_content_type="text/markdown",
    url="https://github.com/ravescovi/mixpotatos",
    packages=find_packages(exclude=["*test*"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)