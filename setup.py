from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="innovation-sandbox",
    version="2.2.1",
    description="Python package for Innovation Sandbox",
    # long_description=open("README.rst").read(),
    packages=find_packages(),
    url = "https://github.com/enyata/innovation-sandbox-python",
    license='MIT',
    setup_requires=['wheel'],
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'aes==1.0.0',
        'pycryptodome==3.9.4',
        'pytest',
        'requests',
        'Sphinx',
        'urljoin==1.0.0',
        'urllib3==1.25.7',
        'setuptools',
        'wheel',
        'faker==4.0.0'
    ]

)
