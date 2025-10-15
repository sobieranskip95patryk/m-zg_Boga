
from setuptools import setup, find_packages

setup(
    name="gokai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click","rich","numpy","pandas","pyyaml","matplotlib","networkx"
    ],
    python_requires=">=3.9",
    license="MIT",
    author="GOK:AI Contributors",
    description="Silnik GOK:AI: S = (W+M+D+C+A) * E * T",
)
