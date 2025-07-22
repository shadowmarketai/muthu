
from setuptools import setup, find_packages

setup(
    name="muthu-footer",
    version="0.1.0",
    description="Streamlit sticky footer by M. Kumaran",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="M. Kumaran",
    author_email="mkumaran2931@gmail.com",
    url="https://github.com/shadowmarketai/50day_python_challenge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Streamlit",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=[
        "streamlit"
    ],
    python_requires=">=3.7",
)
