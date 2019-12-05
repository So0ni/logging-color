import os
from setuptools import setup, find_packages

setup(
    name='colored_log',
    version='0.0.1',
    description='a color patch for python standard logging module',
    license='GPL Licence',
    author='Sonic Young',
    author_email='173976914@qq.com',
    url='https://github.com/So0ni/logging_color',
    packages=['logging_color'],
    include_package_data=False,
    python_requires='>=3.7',
    install_requires=[],
    data_files=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
    ],
    scripts=[],
)
