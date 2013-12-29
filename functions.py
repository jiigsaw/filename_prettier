__author__ = 'root'
import shutil
import glob
import itertools
import string
import re


class Match_regex():
    def permute(self):    # Builds a regex for match. Using permutations to get all combinations possibilities. In the end match1 to match6 are put together in one regex match.
        match61=match62=match63=match64=match65=match66=match51=match52=match53=match54=match55=match41=''
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[A-Z]+','[a-z]+','[0-9]+'],6): # 2*A 2*0 2*a
            match61+=''.join(i)+'|'       # print(''.join(i))
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[A-Z]+','[a-z]+','[A-Z]+'],6): # 3*A 1*0 2*a
            match62+=''.join(i)+'|'
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[a-z]+','[a-z]+','[A-Z]+'],6): # 2*A 1*0 3*a
            match63+=''.join(i)+'|'
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[A-Z]+','[A-Z]+','[0-9]+'],6): # 3*A 2*0 1*a
            match64+=''.join(i)+'|'
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[a-z]+','[a-z]+'+'[0-9]+'],6): # 1*A 2*0 3*a
            match65+=''.join(i)+'|'
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[a-z]+','[0-9]+'+'[0-9]+'],6): # 1*A 3*0 2*a
            match66+=''.joins(i)+'|'
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[A-Z]+','[a-z]+'],5): # 2*A 1*0 2*a
            match51+=''.join(i)+'|'
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[a-z]+','[a-z]+'],5): # 1*A 1*0 3*a
            match52+=''.join(i)+'|'
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[A-Z]+','[A-Z]+'],5): # 3*A 1*0 1*a
            match53+=''.join(i)+'|'
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[a-z]+','[0-9]+'],5): # 1*A 2*0 2*a
            match54+=''.join(i)+'|'
        for i in itertools.permutations(['[A-Z]+','[A-Z]+','[0-9]+','[a-z]+','[0-9]+'],5): # 2*A 2*0 1*a
            match55+=''.join(i)+'|'
        for i in itertools.permutations(['[A-Z]+','[a-z]+','[0-9]+','[A-Z]+','[a-z]+'],5): # 2*A 1*0 1*a
            match41+=''.join(i)+'|'
        # It is probably safer not do add matched with just one [A-Z] to the regex.
        self.match60=match61+match62+match63+match64+match65+match66+'[A-Z]+[a-z]+[0-9]+[A-Z]+[0-9]+[a-z]+'     # 6-tuple regex match
        self.match50=match51+match52+match53+match54+match55+'[A-Z]+[a-z]+[0-9]+[A-Z]+[0-9]+'                   # 5-tuple regex match, which is rather likely than the 6-tupel match.
        self.match40=match41+'[A-Z]+[a-z]+[0-9]+[A-Z]'                                                          # 4-tuple regex, just with match41 (with two [A-Z], because else it could match actual titles, which happen to contain one of [0-9] and [A-Z] and [a-z])

    def rename_permutregex_matched(self, filename):
        if re.search(self.match60, filename):                                               # Checking first "6-tuple" regex match for the filename
            cleaned_filename_with_spaces = ''.join(re.split(self.match60, filename))        # print(re.sub('_','', cleaned_filename_with_spaces))
            cleaned_filename_no_spaces = re.sub('_', '', cleaned_filename_with_spaces)      # Removes spaces to further clean up the filename.
            shutil.move(filename, cleaned_filename_no_spaces)
        elif re.search(self.match50, filename):                                             # Checking "t-tuple"
            cleaned_filename_with_spaces = ''.join(re.split(self.match50, filename))
            cleaned_filename_no_spaces = re.sub('_', '', cleaned_filename_with_spaces)
            shutil.move(filename, cleaned_filename_no_spaces)
        elif re.search(self.match40, filename):
            cleaned_filename_with_spaces = ''.join(re.split(self.match40, filename))
            cleaned_filename_no_spaces = re.sub('_', '', cleaned_filename_with_spaces)
            shutil.move(filename, cleaned_filename_no_spaces)
        else:
            pass

    @staticmethod
    def rename_hyphen_doubles(filename):
        cleaned_filename_no_triple_hyphens = re.sub('---', '-', filename)
        cleaned_filename_no_double_hyphens = re.sub('--', '-', cleaned_filename_no_triple_hyphens)
    # If no self.variable is used (like self.match60, then the class can be set to a staticmethod with the decorator
    # @staticmethod. This is useful, because since it is now a staticmethod and no more an 'instancemethod', we
    # could now call this method without creating an instance of the class first. E.g.
    # Match_regex.rename_hyphen_doubles() should work now, rather than using m = Match_regex() and then
    # m.rename_hyphen_doubles().
        shutil.move(filename, cleaned_filename_no_double_hyphens)

    @staticmethod
    def rename_nospace(filename):
        cleaned_filename_no_spaces = re.sub(' ','', filename)
        shutil.move(filename, cleaned_filename_no_spaces)

