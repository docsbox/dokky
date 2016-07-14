from setuptools import setup

setup(**{
  "name": "dokky",
  "py_modules": ["dokky"],
  "url": "https://github.com/docsbox/dokky",
  "author": "Dmitry Veselov",
  "author_email": "d.a.veselov@yandex.ru",
  "version": "0.1.0",
  "description": "Python client for Docsbox",
  "license": "MIT",
  "classifiers": (
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
  ),
  "install_requires": [
    "requests==2.10.0",
  ],
})
