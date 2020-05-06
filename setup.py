setup(
    name="Sorting_Algorithm_Explorer",
    version="1.0.0",
    description="Explore sorting algorithms! A project for ASWDV",
    long_description=README,
    long_description_content_type="text",
    author="Dawson Ren",
    author_email="dawsonren@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ],
    packages=["Sorting_Algorithm"],
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": ["sa=Sorting_Algorithm.__main__:main"]},
)
