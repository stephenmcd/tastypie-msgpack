
from setuptools import setup, find_packages


setup(
    name="tastypie-msgpack",
    version="0.0.3",
    author="Stephen McDonald",
    author_email="stephen.mc@gmail.com",
    description="MsgPack support for Django Tastypie.",
    long_description=open("README.rst").read(),
    license="BSD",
    url="https://github.com/stephenmcd/tastypie-msgpack",
    install_requires=["msgpack-python"],
    packages=['tastypie_msgpack'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
