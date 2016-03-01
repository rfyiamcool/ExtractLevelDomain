import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "ExtractLevelDomain",
        version = "2.6.3",
        author = "ruifengyun",
        author_email = "rfyiamcool@163.com",
        description = "pass url to extract domain",
        license = "MIT",
        keywords = ["extract domain","fengyun"],
        url = "https://github.com/rfyiamcool",
        long_description = read('README.md'),
        scripts = ['ExtractLevelDomain.py'],
        classifiers = [
             'Development Status :: 2 - Pre-Alpha',
             'Intended Audience :: Developers',
             'License :: OSI Approved :: MIT License',
             'Programming Language :: Python :: 2.7',
             'Programming Language :: Python :: 3.0',
             'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)

