import re

def clean_words(text) :
  # remove html markup
  text = re.sub("(<.*.>)", "", text)
  # remove non-ascii and digits
  text = re.sub("(\W|\d+)", "", text)
  # remove whitespace
  text = text.strip()
  return text

raw = ["..python", ]