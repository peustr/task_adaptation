# coding=utf-8
# Copyright 2019 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Install task_adaptation."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='task_adaptation',
    version='0.1',
    description=(
        'Task Adaptation - a package for evaluating visual models.'),
    author='Google LLC',
    author_email='task-adaptation@google.com',
    url='https://github.com/google/task_adaptation',
    license='Apache 2.0',
    packages=find_packages(),
    package_data={},
    scripts=['task_adaptation/adapt_and_eval.py'],
    install_requires=[
        'absl-py==1.3.0',
        'numpy==1.23.4',
        'scipy==1.9.3',
        'opencv-python==4.6.0.66',
        'six==1.16.0',
        'mock==4.0.3',
        'tensorflow==2.10.0',
        'tensorflow-hub==0.12.0',
        'tensorflow_addons==0.18.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords=('tensorflow machine transfer learning '
              'visual task adaptation benchmark vtab computer vision'),
)
