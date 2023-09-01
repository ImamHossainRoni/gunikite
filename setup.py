from setuptools import setup, find_packages

__author__ = 'Imam Hossain Roni'


setup(
    name="gunikite",
    version="0.2.0",
    description="Utility for running Gunicorn server from a virtual environment.",
    author="Imam Hossain Roni",
    author_email="imamhossainroni95@gmail.com",
    packages=find_packages(),
    url="https://github.com/imamhossainroni/gunikite",  # Update with your project's URL
    license="MIT",  # Choose an appropriate license
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        # List your dependencies here
    ],
    keywords="gunicorn utility virtual-environment",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
)
