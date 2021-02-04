#Import methods from all pages
from .pccomponentes import check_pccomponentes
from .versusgamers import check_versusgamers
from .coolmod import check_coolmod
from .amazon import check_amazon

__services = {
	'amazon.es': check_amazon,
	'amazon.com': check_amazon,
	'vsgamers.es': check_versusgamers,
	'coolmod.com': check_coolmod,
	'pccomponentes.com': check_pccomponentes
}

def check(url):
	for key in __services.keys():
		if key in url:
			return __services[key](url)
		# else:
		# 	print(key, url)

	return None
