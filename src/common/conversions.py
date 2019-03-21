"""
Various conversion helper functions.
"""
import re

def cpu_share_to_cores(share):
	"""
	Convert CPU shares to core fractions
	"""
	number = float(re.findall(r"[0-9\.]+|$", str(share))[0])
	unit = re.findall(r"[a-zA-Z]+|$", str(share))[0]
	
	if unit == "":
		return float(number)
	elif unit.lower() == "m":
		return float(number)/1000.0

def mem_share_to_bytes(share):
	"""
	Calculcates mem share with ui
	"""
	number = int(float(re.findall(r"[0-9\.]+|$", str(share))[0]))
	unit = re.findall(r"[a-zA-Z]+|$", str(share))[0]
	
	if unit == "" or unit.lower() == "b":
		return float(number)
	elif unit.lower() == "k":
		return float(number)*(10**3)
	elif unit.lower() == "m":
		return float(number)*(10**6)
	elif unit.lower() == "g":
		return float(number)*(10**9)
	elif unit.lower() == "t":
		return float(number)*(10**12)
	elif unit.lower() == "p":
		return float(number)*(10**15)
	elif unit.lower() == "e":
		return float(number)*(10**18)
	elif unit.lower() == "z":
		return float(number)*(10**21)
	elif unit.lower() == "ki":
		return float(number)*(2**10)
	elif unit.lower() == "mi":
		return float(number)*(2**20)
	elif unit.lower() == "gi":
		return float(number)*(2**30)
	elif unit.lower() == "ti":
		return float(number)*(2**40)
	elif unit.lower() == "pi":
		return float(number)*(2**50)
	elif unit.lower() == "ei":
		return float(number)*(2**60)
	elif unit.lower() == "zi":
		return float(number)*(2**70)

def mem_bytes_to_mi(bytes):
    """
    Coverts bytes to megabytes.
    """
    return float(bytes)/(2**20)