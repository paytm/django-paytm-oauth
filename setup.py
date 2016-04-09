import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='paytm-oauth',
    version='0.1',
    packages=['paytmoauth'],
    include_package_data=True,
    license='MIT License',
    description='Consumer for paytm oauth',
    long_description=README,
    url='https://github.com/paytm/django-paytm-oauth',
    author='Shrey Agarwal',
    author_email='shrey.agarwal@paytm.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django :: 1.8',
        'Topic :: Internet :: WWW/HTTP',
    ],
)