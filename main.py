# Step 1:
from pathlib import Path

# Step 2:
import re

# Step 1:
# Create a root directory which points to files that are present in a folder
root_dir = Path('files')

# Step 1:
#create a list
filenames = root_dir.iterdir()

# Step 1:
# above logic gives the filenames in the format of posixpaths
# to get the filenames in the string format, use below list comprehension
filenames_str = [filename.name for filename in filenames]
filenames_str

# Step 2:
# Find the files that are from Nov-1 to Nov-20
# re.IGNORE is used to ignore the case-sensitivity.
# [a-z] is used as meta character as we need to find nov, November and november
# * is used to indicate that one or more times(November and november are used twice]
# - is used becase we have a -(hyphen) after November, november and nov
# (?:[1-9]|1[0-9]|20) - as we need to search from nov-1 to nov-20
# [1-9] is for the index position, 
# 1[0-9] is used for tenth position i.e 10, 11, 12,.... 19 and
# [20] is used for just 20
# .txt is because we have .txt after the filename
pattern = re.compile("nov[a-z]*-(?:[1-9]|1[0-9]|20).txt", re.IGNORECASE)

# Step 2:
# Iterate over the filenames_str & find the pattern in the latest iterated filenames
matches = [filename for filename in filenames_str if pattern.findall(filename)]
print(matches)