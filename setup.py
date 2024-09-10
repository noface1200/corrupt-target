from setuptools import setup, find_packages

setup(
    name='corruptfile',            
    version='0.1',                     
    packages=find_packages(),          
    description='A Python package to corrupt files in a folder',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='noface',
    author_email='vfbgnfdntjyrku@gmail.com',
    url='https://github.com/noface1200/corrupt-target',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows11',
    ],
    python_requires='>=3.6',
    install_requires=[], 
)
