import random, string

def randomword(length):
    """
		Random string generator with length params
	"""
    return ''.join(random.choice(string.ascii_letters) for i in range(length))