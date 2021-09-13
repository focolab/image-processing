import setuptools

setuptools.setup(
    name="image-processing",
    version="0.0.0",
    author="UCSF FOCO Lab",
    author_email="jackson.borchardt2@ucsf.edu",
    description="standalone repository for image processing algorithm implementations",
    long_description_content_type=open('README.md').read(),
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'numpy',
          'scipy',
          'opencv-python-headless',
          'scikit-image'
      ],
    python_requires='>=3.6',
)
