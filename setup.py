from setuptools import setup, find_packages

setup(
    name="flty",
    version="0.1",
    packages=find_packages(),
    py_modules=["flty.cli"],  # Make sure this matches your package structure
    install_requires=[],
    entry_points={
        "console_scripts": [
            "flty=flty.cli:main",  # CLI command mapping
        ],
    },
    python_requires=">=3.6",
)
