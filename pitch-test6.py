from music21 import *
import inspect
tharsis = stream.Stream()
tharsis = converter.parse("12_reges2.xml")
stmpPart = stream.Stream()
newPart = stream.Part()
os = stream.Part()
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

for elem in tharsisNotes.flat:
    num = elem.offset
    print num
    slice = tharsisNotes.flat.getElementsByOffset(num, mustBeginInSpan = False, mustFinishInSpan = False)
    if len(slice) > 1:
        for everye in range(len(slice)):
            print slice[everye].offset
            if slice[everye].offset > newPart.highestOffset:
                newnote = compare_pitch_high(slice)
                if newnote != newPart.flat.getElementsByOffset(newPart.highestOffset):
                    newPart.append(newnote)
            else:
                print "Nothing to be done here."
    else:
        newPart.append(slice[0])
#        temp.offset = et.offset
#        of = temp.offset
    print "--"

#newPart.show()
#os.append(newPart)
#os.show()