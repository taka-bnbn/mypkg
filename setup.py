#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki
# SPDX-License-Identifier: BSD-3-Clause


from setuptools import setup, find_packages
package_name = 'mypkg'

setup(
    name='mypkg',
    version='0.0.0',
    packages=find_packages(),
     data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
    ],
    install_requires=['setuptools', 'requests', 'beautifulsoup4'],
    zip_safe=True,
    maintainer='Takaya Mizumaki',
    maintainer_email='mizutaka2005@gmail.com',
    description='A package for practice, publishing Yahoo news.',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'announcer = mypkg.announcer:main',

        ],
    },

)

