from setuptools import setup, find_packages

setup(
    name='qni-core',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'python==3.9.7',
        'numpy==1.22.3',
        'scipy==1.8.0',
        'pandas==1.4.2',
        'matplotlib==3.5.1',
        'seaborn==0.11.2',
        'scikit-learn==1.0.2',
        'joblib==1.1.0',
        'qutip==4.7.1',
        'pytest==6.2.5'
    ],
    author='KOSASIH',
    description='Quantum Computing and Machine Learning Framework',
    url='https://github.com/KOSASIH/qni-core',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: Apache 2.0 License'
    ]
)
