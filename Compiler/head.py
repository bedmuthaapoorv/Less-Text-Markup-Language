from trackers import *
from tagger import *
from writer import *
def head(attr):
    if(attr[0] not in getCompleted()):
        code=''
        code=tagger(attr[0])
        code=code+attr[1]
        code=code+endtagger(attr[0])
        writer(code)
        addPending("head")
