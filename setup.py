from setuptools import setup, find_packages

setup(
    name='webcloner',
    version='6.25.25.1',
    author='Synthfax',
    description='Offline website cloner, updater, and packager',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'tqdm',
        'flask'
    ],
    entry_points={
        'console_scripts': [
            'webcloner=webcloner.cloner:main',
        ]
    },
    license='Apache License 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
