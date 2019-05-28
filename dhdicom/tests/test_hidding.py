# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-


import unittest
import numpy as np
from dhdicom.hidding.mixed import EPRHindingAndAuthentication


class PropertiesTest(unittest.TestCase):

    def setUp(self):
        self.hider = EPRHindingAndAuthentication('clavemaestra')

    def test_data_authentic(self):
        data = np.random.uniform(
            low=0, high=65537, size=(128, 128)).astype(int)
        self.hider.process(data)
        authentic, *l = self.hider.authenticate(data)
        self.assertTrue(authentic)

    def test_data_not_authentic(self):
        data = np.random.uniform(
            low=0, high=65537, size=(128, 128)).astype(int)
        self.hider.process(data)
        data[0][0] += 1
        data[127][127] += 1
        authentic, *l = self.hider.authenticate(data)
        self.assertFalse(authentic)
        self.assertListEqual(l[0], [0, 15])

    def test_get_msg(self):
        data = np.random.uniform(
            low=0, high=65537, size=(128, 128)).astype(int)
        msg = "Anier Soria Lorente"
        self.hider.process(data, msg)
        msg_extracted = self.hider.get_msg(data)
        self.assertEqual(msg, msg_extracted)
