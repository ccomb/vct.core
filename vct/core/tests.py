from doctest import DocFileSuite
import unittest, doctest, os

def tearDown(test):
    if os.path.exists('Data.fs'):
        os.remove('Data.fs')

optionflags = doctest.NORMALIZE_WHITESPACE + doctest.ELLIPSIS

def test_suite( ):
    suite = [DocFileSuite('../../docs/readme.txt', tearDown=tearDown, optionflags=optionflags),
             DocFileSuite('../../docs/core.txt', tearDown=tearDown, optionflags=optionflags),
             DocFileSuite('../../docs/database.txt', tearDown=tearDown, optionflags=optionflags),
             DocFileSuite('../../docs/issue.txt', tearDown=tearDown, optionflags=optionflags),
             DocFileSuite('../../docs/observation.txt', tearDown=tearDown, optionflags=optionflags),
             DocFileSuite('../../docs/action.txt', tearDown=tearDown, optionflags=optionflags),
             DocFileSuite('../../docs/xmlrpc.txt', tearDown=tearDown, optionflags=optionflags),
            ]
    return unittest.TestSuite(suite)
