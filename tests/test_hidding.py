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
        msg = "Anier Soria Lorente"
        watermarked = self.hider.process(data, msg)
        authentic, *l = self.hider.authenticate(watermarked)
        self.assertTrue(authentic)

    def test_data_not_authentic(self):
        data = np.random.uniform(
            low=0, high=65537, size=(128, 128)).astype(int)
        msg = "Anier Soria Lorente"
        watermarked = self.hider.process(data, msg)
        watermarked[0][0] += 1
        watermarked[127][127] += 1
        authentic, *l = self.hider.authenticate(watermarked)
        self.assertFalse(authentic)
        self.assertListEqual(l[0], [0, 15])

    def test_get_msg(self):
        import os

        data = np.random.uniform(
            low=0, high=65537, size=(128, 128)).astype(int)
        base = os.path.dirname(__file__)
        file = open(os.path.join(base, 'messages/Message_01.txt'), "r")
        msg = file.read()
        file.close()
        watermarked = self.hider.process(data, msg)
        msg_extracted = self.hider.get_msg(watermarked)

        self.assertEqual(msg, msg_extracted)

    def test_msg_greather_than_capacity(self):
        import os
        from dhdicom.exceptions import ExceededCapacity

        data = np.random.uniform(
            low=0, high=65537, size=(128, 128)).astype(int)
        base = os.path.dirname(__file__)
        filepath = os.path.join(base, 'messages/Message_00.txt')
        file = open(filepath, "r", encoding="utf-8")
        msg = file.read()
        file.close()
        with self.assertRaises(ExceededCapacity):
            self.hider.process(data, msg)


if __name__ == '__main__':
    unittest.main()