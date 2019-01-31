import random




class Randomer():
	"""
	Random methods
	"""
	__MIN_INT = -2147483648
	__MAX_INT = +2147483647

	__MIN_FLOAT = 2.3 * 10 ** -308
	__MAX_FLOAT = 1.7 * 10 ** 308

	def __init__(self):
		pass

	@classmethod
	def int_get(cls, start=__MIN_INT, end=__MAX_INT):
		"""
		Gives random value of int from range [start, end]
		"""
		return random.randint(start, end)

	@classmethod
	def float_get(cls, start=__MIN_FLOAT, end=__MAX_FLOAT):
		"""
		Gives random value of float from range [start, end]
		"""
		return random.uniform(start, end)

	@classmethod
	def bool_get(cls):
		"""
		Gives random value of boolean
		"""
		return bool(random.random())
