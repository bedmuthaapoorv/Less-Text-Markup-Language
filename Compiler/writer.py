def writer(tags):
    Index=open("../index.html","a+")
    Index.write(tags)
    Index.close()