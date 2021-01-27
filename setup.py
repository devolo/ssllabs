import shlex
from subprocess import check_call

import pkg_resources
from setuptools import find_packages, setup
from setuptools.command.develop import develop


# Create post develop command class for hooking into the python setup process
# This command will run after dependencies are installed
class PostDevelopCommand(develop):

    def run(self):
        try:
            check_call(shlex.split("pre-commit install"))
        except Exception:
            print("Unable to run 'pre-commit install'")
        develop.run(self)


pkg_resources.require('setuptools>=46.4.0')
setup(
    name="ssllabs",
    author="Markus Bong, Guido Schmitz",
    author_email="m.bong@famabo.de, guido.schmitz@fedaix.de",
    description="Qualys SSL Labs API in Python",
    long_description_content_type="text/markdown",
    url="https://github.com/devolo/ssllabs",
    packages=find_packages(exclude=("tests*",
                                    )),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "dacite",
        "httpx",
    ],
    extras_require={
        "dev": [
            "pre-commit",
        ],
        "test": [
            "asynctest;python_version<'3.8'",
            "pytest",
            "pytest-asyncio",
            "pytest-cov",
            "pytest-mock",
        ],
    },
    cmdclass={"develop": PostDevelopCommand},
    python_requires=">=3.7",
)
