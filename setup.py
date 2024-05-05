import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Chicken-disease-classification"
Author_User_Name = "amit4009"
SRC_REPO = "chicken_disease_classifier"
Author_email = "i2pandit@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_User_Name,
    author_email=Author_email,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected keyword
    url=f"https://github.com/{Author_User_Name}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_User_Name}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Corrected mapping
    packages=setuptools.find_packages(where="src"),
    
)
