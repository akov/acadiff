# a usc ref is a tuple with a number for the title and a
# string for the section

import re

refs_text = open("usc_refs_online.txt").readline()

usc_re = re.compile('(\d+)\sU\.S\.C\.\s([a-z0-9\-])+')
print usc_re.search(refs_text).groups(100)


