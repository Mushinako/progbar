# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
import setuptools

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

setuptools.setup(
    name="progbar-mushinako",  # Replace with your own username
    version="2021.05",
    author="Mushinako",
    author_email="ridoedee@gmail.com",
    description="Simple progress bar for personal use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mushinako/progbar",
    packages=setuptools.find_packages(),
    package_data={
        "progbar": ["*.pyi", "py.typed"],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
