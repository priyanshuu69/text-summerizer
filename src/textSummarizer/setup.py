import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__="0.0.0"

REPO_NAME = "Text-Summerizer"
AUTHOR_USER_NAME = "priyanshu"

SRC_REPO = "textSummerizer"
AUTHOR_EMAIL ="priyanshujagwan143@gmail.com"


# The line `setuptools.setup(name=SRC_REPO, ...)` in the Python script is calling the `setup()`
# function from the `setuptools` module to configure the metadata for the Python package being
# developed.

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for NLP app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPOO_NAME}",
    project_urls={
        "bug tracker": f"httpd://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src")  
    
)