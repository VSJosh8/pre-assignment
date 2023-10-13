from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="web_checker",
    version="1.0",
    description="A web checker that checks that status of a given url and returns response information",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VSJosh8/pre-assignment",
    author="Vincent Joshua Skinner",
    author_email="vsjoshua98@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests","validators"],
)