from doctypes import *
from tagger import *
from trackers import *
from head import *
from end import *
keywords={
    "doctype":doctype,
    "title":head
}
def breakdown(lFile):
    nslices=lFile.read().split("\n")
    for i in nslices:
        colSlice=i.split(":")
        cmd=colSlice[0]
        if cmd in keywords:
            keywords[cmd](colSlice)
    if(flags["doctype"]==0):
        doctype(["doctype","5"])
    theend()
lFile=open("../test.ltml")
breakdown(lFile)