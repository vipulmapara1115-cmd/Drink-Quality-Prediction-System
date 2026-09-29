import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project"
AUTHOR_USER_NAME = "vipulmapara"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "vipulmapara1115@gmail.com"


setuptools.setup(
    name="mlproject",
    version="0.0.0",
    author=" Vipul Mapara",
    author_email="vipulmapara1115@gmail.com",
    description="A small python package for ml app",
    long_description="a ml experiment as on Sep 30 2026",
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)