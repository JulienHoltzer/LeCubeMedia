import unittest
import cube


class TagEventTestCase(unittest.TestCase):

	class testtaghandler :
		def __init__(self):
			self.cbcalled = False
			self.ttype = None
			self.tdata = None

		def cb(self,ttype,tdata):
			self.cbcalled = True
			self.ttype = ttype
			self.tdata = tdata
			

	def setUp(self):
		self.cube = cube.Cube()
		self.tth = TagEventTestCase.testtaghandler()
		self.cube.register_tag_handler('user',self.tth.cb)

	def tearDown(self):
		self.cube = None

	def testNominalCase(self):
		self.cube.tag_detection('NFC','user:gilles')
		self.assertFalse(self.tth.cbcalled)

		self.cube.step()

		self.assertTrue(self.tth.cbcalled)
		self.assertEqual(self.tth.ttype,'user')
		self.assertEqual(self.tth.tdata,'gilles')

	def testUnknownTag(self):
		thunk = TagEventTestCase.testtaghandler()
		self.cube.tag_handler_unknown = thunk.cb

		self.cube.tag_detection('NFC','unknown:tag')
		self.cube.step()

		self.assertFalse(self.tth.cbcalled)

		self.assertTrue(thunk.cbcalled)
		self.assertEqual(thunk.ttype,'unknown')
		self.assertEqual(thunk.tdata,'tag')
		
	def testBadFormatTag(self):
		thunk = TagEventTestCase.testtaghandler()
		self.cube.tag_handler_unknown = thunk.cb

		self.cube.tag_detection('NFC','unknowntag')
		self.cube.step()

		self.assertFalse(self.tth.cbcalled)
		self.assertFalse(thunk.cbcalled)
		


