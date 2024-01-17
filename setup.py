"""Classic UNIX-style real-time text formatter with unicode and pipe support

This file allows to install PyColumnizer using pip

This program is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Fern Lane"
__copyright__ = "Copyright 2024, Fern Lane"
__date__ = "2024/01/17"
__deprecated__ = False
__license__ = "GPLv3"
__maintainer__ = "developer"
__version__ = "1.0.0"

from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="PyColumnizer",
    version=__version__,
    license="Apache License 2.0",
    author="Fern Lane",
    description="Classic UNIX-style real-time text formatter with unicode and pipe support",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/F33RNI/PyColumnizer",
    project_urls={"Bug Report": "https://github.com/F33RNI/PyColumnizer/issues/new"},
    entry_points={
        "console_scripts": ["columnizer = pycolumnizer.main:main"],
    },
    install_requires=[],
    long_description=Path.open(Path("README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["PyColumnizer"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Topic :: Documentation",
        "Topic :: File Formats",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Editors :: Text Processing",
        "Topic :: Utilities",
    ],
)
