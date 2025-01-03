from setuptools import setup, find_packages

setup(
    name='mypkg',
    version='0.0.0',
    packages=find_packages(),
    install_requires=['setuptools', 'requests', 'beautifulsoup4'],
    zip_safe=True,
    maintainer='Takaya Mizumaki',
    maintainer_email='mizutaka2005@gmail.com',
    description='A package for practice, publishing Yahoo news.',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',  # listenerノードも必要なら>追加
            'announcer = mypkg.announcer:main',

        ],
    },

)

