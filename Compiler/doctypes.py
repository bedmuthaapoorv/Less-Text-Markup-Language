from writer import *
flags={
    "doctype":0
}
def doctype(dctype):
    dctypes={
        "5":'<!DOCTYPE HTML>'
        ,"4Strict":'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN""http://www.w3.org/TR/html4/strict.dtd">'
        ,"4Trans":'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN""http://www.w3.org/TR/html4/loose.dtd">'
        ,"4Frameset":'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN""http://www.w3.org/TR/html4/frameset.dtd">'
        ,"XStrict":'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
        ,"XTrans":'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'
        ,"XFrameset":'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">'
        ,"XDtd":'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN""http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'
        ,"XBasic":'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN""http://www.w3.org/TR/xhtml-basic/xhtml-basic11.dtd">'
        ,"Math2Dtd":'<!DOCTYPE math PUBLIC "-//W3C//DTD MathML 2.0//EN""http://www.w3.org/Math/DTD/mathml2/mathml2.dtd">'
        ,"Math1Dtd":'<!DOCTYPE math SYSTEM"http://www.w3.org/Math/DTD/mathml1/mathml.dtd">'
        ,"Compound":'<!DOCTYPE html PUBLIC"-//W3C//DTD XHTML 1.1 plus MathML 2.0 plus SVG 1.1//EN""http://www.w3.org/2002/04/xhtml-math-svg/xhtml-math-svg.dtd">'
    }
    if(flags["doctype"]==0):
        flags["doctype"]=1
        writer(dctypes[dctype[1]])

