"""
Tests for src/common/convet
"""
import unittest
from src.common import conversions

class ConversionsTest(unittest.TestCase):

    def test_cpu_share_to_cores(self):
        self.assertEqual(conversions.cpu_share_to_cores(0), 0)
        self.assertEqual(conversions.cpu_share_to_cores(1), 1)
        self.assertEqual(conversions.cpu_share_to_cores(999), 999)

        self.assertEqual(conversions.cpu_share_to_cores("0"), 0)
        self.assertEqual(conversions.cpu_share_to_cores("1"), 1)
        self.assertEqual(conversions.cpu_share_to_cores("999"), 999)

        self.assertEqual(conversions.cpu_share_to_cores("1M"), 0.001)
        self.assertEqual(conversions.cpu_share_to_cores("1m"), 0.001)

        self.assertEqual(conversions.cpu_share_to_cores("0m"), 0)
        self.assertEqual(conversions.cpu_share_to_cores("999m"), 0.999)
        self.assertEqual(conversions.cpu_share_to_cores("1000m"), 1)
        self.assertEqual(conversions.cpu_share_to_cores("1500m"), 1.5)
        self.assertEqual(conversions.cpu_share_to_cores("1000000000m"), 1000000)

        with self.assertRaises(Exception):
            conversions.cpu_share_to_cores(None)
        
        with self.assertRaises(Exception):
            conversions.cpu_share_to_cores(True)

    def test_mem_share_to_bytes(self):
        self.assertEqual(conversions.mem_share_to_bytes(0), 0)
        self.assertEqual(conversions.mem_share_to_bytes(1), 1)
        self.assertEqual(conversions.mem_share_to_bytes(999999), 999999)

        self.assertEqual(conversions.mem_share_to_bytes("0"), 0)
        self.assertEqual(conversions.mem_share_to_bytes("1"), 1)
        self.assertEqual(conversions.mem_share_to_bytes("1b"), 1)
        self.assertEqual(conversions.mem_share_to_bytes("999999"), 999999)
     
        self.assertEqual(conversions.mem_share_to_bytes("1Ki"), 1024)
        self.assertEqual(conversions.mem_share_to_bytes("1kI"), 1024)
        self.assertEqual(conversions.mem_share_to_bytes("1ki"), 1024)
        self.assertEqual(conversions.mem_share_to_bytes("1KI"), 1024)

        self.assertEqual(conversions.mem_share_to_bytes("1k"), 1000)
        self.assertEqual(conversions.mem_share_to_bytes("1Ki"), 1024)
        self.assertEqual(conversions.mem_share_to_bytes("1m"), 10**6)
        self.assertEqual(conversions.mem_share_to_bytes("1Mi"), 2**20)
        self.assertEqual(conversions.mem_share_to_bytes("1g"), 10**9)
        self.assertEqual(conversions.mem_share_to_bytes("1Gi"), 2**30)
        self.assertEqual(conversions.mem_share_to_bytes("1t"), 10**12)
        self.assertEqual(conversions.mem_share_to_bytes("1Ti"), 2**40)
        self.assertEqual(conversions.mem_share_to_bytes("1p"), 10**15)
        self.assertEqual(conversions.mem_share_to_bytes("1Pi"), 2**50)
        self.assertEqual(conversions.mem_share_to_bytes("1e"), 10**18)
        self.assertEqual(conversions.mem_share_to_bytes("1Ei"), 2**60)
        self.assertEqual(conversions.mem_share_to_bytes("1z"), 10**21)
        self.assertEqual(conversions.mem_share_to_bytes("1zi"), 2**70)

        with self.assertRaises(Exception):
            conversions.mem_share_to_bytes(None)
        
        with self.assertRaises(Exception):
            conversions.mem_share_to_bytes(True)

    def test_mem_bytes_to_mi(self):
        self.assertEqual(conversions.mem_bytes_to_mi(1024), 1/1024)
        self.assertEqual(conversions.mem_bytes_to_mi(2**20), 1)
        self.assertEqual(conversions.mem_bytes_to_mi(2**30), 1024)

        self.assertEqual(conversions.mem_bytes_to_mi(str(2**20)), 1)

        with self.assertRaises(Exception):
            conversions.mem_bytes_to_mi(None)
        
        with self.assertRaises(Exception):
            conversions.mem_bytes_to_mi(True)
