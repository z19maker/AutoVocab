import json
from pathlib import Path

def ja_to_en(vocab: list):
	def translate(word):
		translation = lookup.get(word)
		return translation

	complete_vocab = {}
	for word in vocab:
		# trnslate japanese to english
		translation = translate(word)
		complete_vocab[word]=translation

	return complete_vocab

print("loading jmdict.json and creating lookup table")
with open(Path(__file__).parent / "jmdict.json", "r") as f:
	jmdict = json.load(f)

def build_lookup(jmdict):
	lookup = {}
	for word in jmdict["words"]:
		glosses = []
		for sense in word["sense"]: #?
			for g in sense["gloss"]: #?
				if g["lang"] == "eng":
					glosses.append(g["text"])
		# index by kanji text
		for k in word["kanji"]:
			if k["common"] and glosses:
				lookup[k["text"]] = glosses[0]
		# also index by kana (fallback for kana only words)
		for k in word["kana"]:
			if k["common"] and k["text"] not in lookup and glosses:
				lookup[k["text"]] = glosses[0]
	return lookup

lookup = build_lookup(jmdict)


