from distutils.core import setup
from setuptools import find_packages

VERSION = __import__("kpl").__version__

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
]

install_requires = [
    'suds==0.4'
]

setup(
    name="kpl",
    packages=find_packages(exclude=["tests"]),
    description="Application and library to integrate with KPL ABACOS",
    version=VERSION,
    author="Mateus Vanzo de Padua",
    author_email="mateuspaduaweb@gmail.com",
    license='MIT License',
    platforms=['OS Independent'],
    url="https://github.com/mateuspadua/django-admin-report",
    keywords=['KPL', 'ABACOS', 'mercado pago'],
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)
