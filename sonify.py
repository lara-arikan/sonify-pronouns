
# POEM SONIFICATION BY PRONOUN USE

#This program takes in a poem as text file and converts
#each occurrence of the pronoun 'I' in the specified language
#to the tonic of a specified key. All other words are assigned
#to a note randomly chosen within the key.
#'I' will sound longer than the other words, and will be
#an octave higher.

languageDict = {'turkish': 'ben',
                'english': 'i',
                'german': 'ich',
                'spanish': 'yo'}

keyDict = {
           'C': ['C', 'E', 'F', 'G', 'A', 'B'],
           'Db': ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'],
           'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
           'Eb': ['Eb',	'F', 'G', 'Ab', 'Bb', 'C', 'D'],
           'F': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
           'F#': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#'],
           'Gb': ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F'],
           'G': ['G', 'A', 'B', 'C', 'D', 'E','F#'],
           'Ab': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],
           'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
           'Bb': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
           'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']}


from music21 import *
import random
import sys

def find_i(filename, language, key_name, octave):
    """
    For text 'filename' in a particular language,
    this function isolates the pronoun 'I' and appends
    the tonic note to a stream whenever it occurs. All
    other words are assigned a random note in the specified
    octave of the specified key.

    """
    with open(filename, 'r') as f:
        i = languageDict.get(language)
        stream1 = stream.Stream()
        text = f.read()
        words = text.split()
        key = keyDict.get(key_name)
        count = 0
        for word in words:
            if word.lower() == i:
                note_name = key[0] + str(octave+1)
                note_i = note.Note(note_name, type='whole')
                stream1.append(note_i)
            else:
                if count % 9 == 0:
                    r = note.Rest() # every ninth object will be a rest, for easier listening
                    stream1.append(r)
                else:
                    note_name = random.choice(key) + str(octave)
                    note_else = note.Note(note_name)
                    note_else.quarterLength = 0.5
                    stream1.append(note_else)
                count += 1

    return stream1


def main():
    args = sys.argv[1:]

    # To run from terminal:
    # filename language key octave

    filename = str(args[0])
    language = str(args[1])
    key_name = str(args[2])
    octave = int(args[3])

    stream1 = find_i(filename, language, key_name, octave)
    stream1.show('midi')

    # To save midi output:

    if len(args) == 5:
        track_name = filename + key_name + str(octave)
        stream1.write("midi", track_name)

if __name__ == '__main__':
    main()


