#!/usr/bin/env python3
import re
import json
import xmltodict
import sys
import os
import fnmatch

# default output dir
output_dir = "en"

def mkdirs(path):
	"""Make directory, if it doesn't exist."""
	if not os.path.exists(path):
		os.makedirs(path)

# https://pythonadventures.wordpress.com/2014/12/29/xml-to-dict-xml-to-json/
def convert(xml_file, xml_attribs=True):
	with open(xml_file, "rb") as f:    # notice the "rb" mode
		d = xmltodict.parse(f, xml_attribs=xml_attribs)
		return json.dumps(d, indent=2, ensure_ascii=False)

def main():
	mkdirs(output_dir)
	
	for file in os.listdir('.'):
		if fnmatch.fnmatch(file, '*.xml'):
			# parse out all the quoted lone integers
			json_data = convert(file)
			json_data = re.sub('\"(\d+)\"', r'\1', json_data)

			# make multiple regex replace with a single pass
			# http://rc98.net/multiple_replace
			subs = {
				'"@': '"',        # remove XML artifact
				'ranLiao': 'oil', # resources in romanized Chinese
				'danYao': 'ammo',
				'gang': 'steel',
				'lv': 'bauxite',
				'RanLiao': 'Oil', # resources in romanized Chinese, uppercase
				'DanYao': 'Ammo',
				'Gang': 'Steel',
				'Lv': 'Bauxite',
				'huoLi': 'firepower', # equipment stats in romanized Chinese
				'leiZhuang': 'torpedo',
				'huiBi': 'evasion',
				'duiQian': 'antisub',
				'duiKong': 'antiair',
				'mingZhong': 'hitrate',
				'suoDi': 'lineOfSight',
				'zhuangJia': 'armor',
				'leiMing': 'leiMing', # meaning is unknown, check in app later
			}
			#compiled = re.compile('|'.join(map(re.escape, subs)))  # use to avoid regex
			compiled = re.compile('|'.join(map(re.escape, subs)))
			def lookup(match):
				return subs[match.group(0)]
			new_json_data = compiled.sub(lookup, json_data)

			# save as converted JSON
			with open(os.path.join(output_dir, os.path.splitext(file)[0] + ".json"), 'w') as f:
				f.write(new_json_data)

# display some lines

if __name__ == "__main__":
	main()
