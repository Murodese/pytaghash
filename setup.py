import setuptools

setuptools.setup(
    name="pytaghash",
    version="0.1.0",
    url="https://github.com/Murodese/pytaghash",

    author="James Meneghello",
    author_email="murodese@gmail.com",

    description=" An extension of BeautifulSoup 4 Tags to provide additional XPath and feature hashing capabilities.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
