from setuptools import setup, find_packages

setup(
    name="simple_cicd_demo",   # Name of your project/package
    version="0.1",             # Version number
    packages=find_packages(where="src"),  # Find all packages inside src/
    package_dir={"": "src"},   # Maps the root package to src/
)
