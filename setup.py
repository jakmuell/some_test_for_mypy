from setuptools import setup, find_packages

setup(
    name="some_test_for_mypy",
    version="1.36",
    packages=find_packages(where=".", include=["some_test_for_mypy*"]),
    include_package_data=True,
    package_data={
        "some_test_for_mypy": ["py.typed", "sql/*.sql"],
    },
    author="TennisProjekt",
    description="Tennis Database",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jakmuell/some_test_for_mypy",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "sqlalchemy",
        "pandas",
        "psycopg2",
        "weather_rp5",
        "timezonefinder",
        "country_converter",
    ],
)
