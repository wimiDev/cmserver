import hashlib

import os

class TokenMaker:

	def createToken(self, exkey):
		_token = ''
		_token = hashlib.sha1(os.urandom(31))
		_token.update(('_' + exkey).encode('utf-8'))
		# print('----------------------TOKEN>>>>>>' + _token)
		return _token.hexdigest()

	#not use
	def createKey(self):
		_key = hashlib.sha1(os.urandom(31)).hexdigest()
		# print('----------------------TOKEN KEY>>>>>>' + _key)
		return _key