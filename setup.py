"""
Project setup file
"""
import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='sageintacctsdk',
    version='1.4.0',
    author='Ashwin T',
    author_email='ashwin.t@fyle.in',
    description='Python SDK for accessing Sage Intacct APIs',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['sage-intacct', 'sage', 'fyle', 'api', 'python', 'sdk'],
    url='https://github.com/fylein/sageintacct-sdk-py',
    packages=setuptools.find_packages(),
    install_requires=['requests==2.22.0', 'xmltodict==0.12.0'],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
