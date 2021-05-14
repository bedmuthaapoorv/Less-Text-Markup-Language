from writer import *
from trackers import *
from tagger import *
def theend():
    code=''
    for i in getPending()[::-1]:
        code=code+endtagger(i)
        addCompleted(i)
    writer(code)
