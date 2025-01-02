from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
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
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',  # listenerノードも必要なら追加
        ],
    },
)

