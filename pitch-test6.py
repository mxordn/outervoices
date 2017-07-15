from music21 import *
import inspect
tharsis = stream.Stream()
tharsis = converter.parse("12_reges2.xml")
stmpPart = stream.Stream()
newPartHigh = stream.Part()
newPartLoW = stream.Part()
os = stream.Stream()
tharsisNotes = tharsis.flat.getElementsByClass(note.Note)

def compare_pitch_high(slice):
    high = slice[0]
    for each in range(len(slice)):
        if slice[each] > high:
            high = slice[each]
        else:
            high = high
    print high
    return high

def compare_pitch_low(slice):
    low = slice[0]
    for each in range(len(slice)):
		if slice[each] < low:
		    low = slice[each]
		else:
		    low = low
    return low

#HIGHEST VOICE
for elem in tharsisNotes.flat:
    num = elem.offset
    print num
    slice = tharsisNotes.flat.getElementsByOffset(num, mustBeginInSpan = False, mustFinishInSpan = False)
    if len(slice) > 1:
        for everye in range(len(slice)):
            print slice[everye].offset
            if slice[everye].offset > newPartHigh.highestOffset:
                newnote = compare_pitch_high(slice)
                exnote1 = newPartHigh.flat.getElementsByOffset(newPartHigh.highestOffset, classList= note.Note)
                exnote2 = exnote1[0]
#                print exnote2
#                print newnote, exnote[0].pitch
                if newnote != exnote2:
                    newPartHigh.append(newnote)
            else:
                print "Nothing to be done here."
    else:
        newPartHigh.append(slice[0])
#        temp.offset = et.offset
#        of = temp.offset
    print "--"


#LOWEST VOICE

os.insert(newPartHigh)
#os.insert(newPartLow)
os.show()