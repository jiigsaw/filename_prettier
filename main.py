__author__ = 'root'
import shutil
import glob
import itertools
import string
import re
from functions import Match_regex

# Configuration
music_path = "/home/user/Musik/einzelstücke/"
match_files = music_path + "*.mp3"

# Main
# Initialize class
m = Match_regex()
m.permute()
i = 0
for filename in glob.glob(match_files):    # If filename contains match then
    i += 1
    print("\n" + str(i) + " " + filename)
    m.rename_permutregex_matched(filename)
for filename in glob.glob(match_files):
    Match_regex.rename_nospace(filename)
# We use a n
for filename in glob.glob(match_files):
    Match_regex.rename_hyphen_doubles(filename)
print "finish"
