# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Tests for Visual Domain Decathlon datasets."""

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import visual_domain_decathlon


class VisualDomainDecathlonGenericTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = visual_domain_decathlon.VisualDomainDecathlon
  BUILDER_CONFIG_NAMES_TO_TEST = ['aircraft']
  SPLITS = {
      'train': 2,
      'test': 1,
      'validation': 1,
  }
  DL_EXTRACT_RESULT = ['', '']


class VisualDomainDecathlonImagenetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = visual_domain_decathlon.VisualDomainDecathlon
  BUILDER_CONFIG_NAMES_TO_TEST = ['imagenet12']
  SPLITS = {
      'train': 3,
      'test': 2,
      'validation': 1,
  }
  DL_EXTRACT_RESULT = ['', 'imagenet12.tar']


if __name__ == '__main__':
  testing.test_main()
