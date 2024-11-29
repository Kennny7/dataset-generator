#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

setup(
    name="dataset-generator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A dataset generator tool to create realistic datasets for practice.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/dataset-generator",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.1",
        "faker>=18.5.0",
        "tkinter>=8.6.12"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

