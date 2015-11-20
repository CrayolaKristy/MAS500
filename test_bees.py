import mediacloud
import logging
import unittest
import bees


class TestMediacloudAPI(unittest.TestCase):
	def TestMediacloudAPI (self):
		result = bees.callMediaCloud()
		assert result != None 

if __name__ == "__main__":
    unittest.main()

# Code ideas from Penny W. and Yasmin R.


#Old
#logging.basicConfig(filename="bees.log", level=logging.DEBUG)

#my_api_key = 'a8031b00764a869d4af49778c040cdc38e170b76331a4a53c97afd0f5be3ae8b'
#mc = mediacloud.api.MediaCloud(my_api_key)

#logging.debug('Connection Made!')