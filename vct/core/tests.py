from doctest import DocFileSuite
import unittest

def test_suite( ):
    suite = [DocFileSuite('../../docs/readme.txt'),
            ]
    return unittest.TestSuite(suite)
