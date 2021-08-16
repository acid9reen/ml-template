from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="ml-template",
    install_requires=[
        "matplotlib >= 3.4.3",
        "notebook >= 6.4.3",
        "numpy >= 1.21.2",
        "pandas >= 1.3.2",
    ],
)
