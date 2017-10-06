from setuptools import setup


setup(
    name='maff',
    version='0.1',
    description='Python convenience functions that I wish were in the math module',
    long_description=open('README.md').read(),
    url='https://github.com/cosmologicon/maff',
    author='Christopher Night',
    author_email='cosmologicon@gmail.com',
    py_modules=['maff'],
    test_suite="maff_test",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
    ]
)
