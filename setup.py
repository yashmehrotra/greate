try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='greate',
    version='0.1',
    author='Yash Mehrotra',
    author_email='yashmehrotra95@gmail.com',
    packages=['greate'],
    scripts=['bin/greate'],
    url='https://pypi.python.org/pypi/greate',
    license='Apache 2.0',
    description='',
    long_description=open('README.rst').read(),
    install_requires=[
        'requests==2.9.1',
        'soldier==0.0.2',
    ],
)
