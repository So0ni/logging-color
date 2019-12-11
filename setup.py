import os
from setuptools import setup

ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(ROOT, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='logging_color',
    version='0.1.2',
    description='a color patch for python standard logging module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL Licence',
    author='Sonic Young',
    author_email='173976914@qq.com',
    url='https://github.com/So0ni/logging_color',
    packages=['logging_color'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: OS Independent",
    ],
)
