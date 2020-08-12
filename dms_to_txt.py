from collections import Counter
from os import listdir
from os.path import isfile, join

##################
# Get the files. #
##################

# In what folder are the closed captioned files you got 
# from Microsoft Streams?
mypath = 'path/to/folder/with/captioned/files'

# This gathers the files in that folder, assuming their format is
# 'filename_1.dms'
filenames = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f)) and (f[-2:]=='_1' or f[-3:]=='dms')]
filenames.sort()

######################
# Process each file. #
######################

# Loop through files.
for filename in filenames:

    # Read lines into a list.
    with open(filename) as fp:
        text = fp.readlines()

    # Make sure all the lines are formatted as strings.
    textstring = [str(elem) for elem in text]

    # Remove the five header lines
    del textstring[:5]

    # Find only text elements by
    # Removing lines that are notes, timestamps, or blank.
    textstring = [elem for elem in textstring if not elem.startswith("NOTE")]
    textstring = [elem for elem in textstring if not elem.startswith("00:")]
    textstring = [elem for elem in textstring if not elem =="\n"]
    textstring = [elem for elem in textstring if not (len(elem)>22 and elem[8] =="-" and elem[13]=="-" and elem[18]=="-" and elem[23]=="-")]

    # Join the text together as one long string.
    together = " ".join([str(elem) for elem in textstring])

    # Remove newlines to get one long paragraph.
    together = together.replace("\r","")
    together = together.replace("\n","")

    # Change double spaces that occur between lines to single spaces.
    for i in range(5): together = together.replace("  "," ")
    if together[0]==" ": together = together[1:]

    # Replace common auto-transcription errors with correct words.
    together = together.replace("alot","a lot")
    together = together.replace("'cause","because")
    together = together.replace("connect- the-dots","connect-the-dots")
    together = together.replace("dew point","dewpoint")
    together = together.replace("El Nino","El Niño")
    together = together.replace("extra- tropical","extratropical")
    together = together.replace("high- precipitation","high-precipitation")
    together = together.replace("kilometres","kilometers")
    together = together.replace("La Nina","La Niña")
    together = together.replace("low- precipitation","low-precipitation")
    together = together.replace("occuring","occurring")
    together = together.replace("occured","occurred")
    together = together.replace("tored","toward")
    together = together.replace("untill","until")

    ##################
    # Output results #
    ##################

    # Show the beginning of the file as an initial sanity check.
    print('\n\n')
    print(together[:200])
    print()

    #################################
    # Output trends and             #
    # look for other common issues. #
    #################################
    words = together.replace('.',"")
    words = words.replace(',',"")
    words = words.replace('?',"")
    words = words.replace('!',"")

    # Find and display what may be british spellings.
    british_endings = ['re','our','ise','yse','lled','lling','ller','ence','ogue']

    # Find words with these endings.
    for ending in british_endings:
        found_words = [word for word in set(words.split()) if word.endswith(ending)]
        # Report any words you found.
        if len(found_words):
            print(f'\nCheck these words ending in -{ending}')
            found_words.sort()
            for fw in found_words:
                print(f'  {fw}')

    # Find and display what were hyphenated words at the end of the line.
    dashes = [word for word in set(words.split()) if word[-1:]=='-']
    if len(dashes):
        print("\nCheck these hyphens:")
        dashes.sort()
        for dash in dashes:
            print(dash)
    else: print("\nNo hyphens found")

    # Find and print 10 most common words.
    frequent = []
    common = Counter(words.split()).most_common(10)
    print(f'\nTotal Words: {len(together)}')
    print(f'Unique Words: {len(set(words.split()))}')
    print('10 most common words')
    for key in common:
        print(f'{key[1]}\t{key[0]}')

    ###############################
    # Create new text file.       #
    # Name removes MS formatting. #
    ###############################

    # Modify filename.
    filename = filename.replace("Modified_AutoTranscript_","")
    if filename[-6:]=='_1.dms': filename = filename.replace("_1.dms",".dms")
    elif filename[-2:]=='_1': filename = filename.replace("_1",".dms")

    # Open new file...
    with open(f"{filename[:-4]}.txt","w") as newfile:
        # ...write the file.
        newfile.write(together)

