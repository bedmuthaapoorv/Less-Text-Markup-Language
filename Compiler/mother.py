from doctypes import *
keywords={
    "doctype":doctype
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
lFile=open("../test.lhtml")
breakdown(lFile)