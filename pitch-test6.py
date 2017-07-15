from music21 import *
import inspect
tharsis = stream.Stream()
tharsis = converter.parse("12_reges.xml")
stmpPart = stream.Stream()
newPart = []
os = stream.Part()
tharsisNotes = tharsis.flat.getElementsByClass(note.Note)

def compare_pitch_high(slice, high):
	for each in range(len(slice)):
		if slice[each] > high:
		    high = slice[each]
		else:
		    high = high
	return high

def compare_pitch_low(slice, low):
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
    print len(slice)
    high = slice[0]
    if len(slice) > 1:
        newPart.append(compare_pitch_high(slice, high))
    else:
        newPart.append(high)
#        temp.offset = et.offset
#        of = temp.offset
    print "--"

os.append(newPart)
#os.show()