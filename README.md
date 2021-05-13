# Less-Text-Markup-Language
* Author : Apoorv Bedmutha

Less Text Markup Language is project with the motivation of creating an alternative to HTML without all the nonsense syntax.

traditional HTML has too much redundant and unnecessary strcturing that developer shouldn't be concerned with,
It affects development speed as well as large HTML files become very difficult to understand
Let us be honest here, nobody has ever been a fan of using  angular brackets and <br /> for new line.

LTML stands for Less Text Markup Language

and as the name states it writes large HTML codes with as less code as possible

for example

in ltml
```
doctype:4Strict
```

is equivalent to 

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN""http://www.w3.org/TR/html4/strict.dtd">
```
in HTML

In similar fashion LTML considerably reduces syntactical load on the developer and helps him focus on more important stuff

Latest Modules Added :
- Doctypes

# Doctypes

First thing to consider are doctype declarations in html,they are a pain to remember,The most common and reliable doctype to use is 

<!DOCTYPE html>

hence we will keep it as default i.e. it will be implemented if no doctype is specified.
though the user must have a functionality to specify which doctype should he use,hence he can do it using the following syntax
```
doctype:5 
```
which can be used for specifying HTML5 doctype i.e.`<DOCTYPE html>`

similarly,
for HTML 4.01 Strict user can use 
```
doctype:4Strict
```
for HTML 4.01 Transitional user can use 
```
doctype:4Trans
```
for HTML 4.01 Frameset user can use 
```
doctype:4Frameset
```
for XHTML 1.0 Strict user can use 
```
doctype:XStrict
```
for XHTML 1.0 Transitional user can use 
```
doctype:XTrans
```
for XHTML 1.0 Frameset user can use 
```
doctype:XFrameset
```
for XHTML 1.1 - DTD user can use 
```
doctype:XDtd
```
for XHTML Basic 1.1 user can use 
```
doctype:XBasic
```

for MathML 2.0 - DTD user can use 
```
doctype:Math2Dtd
```
for MathML 1.01 - DTD user can use 
```
doctype:Math1Dtd
```
for XHTML + MathML + SVG - DTD user can use 
```
doctype:Compound
```
