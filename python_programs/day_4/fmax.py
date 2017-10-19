def filemax(f):
    fm = 0
    found = False
    for line in f:
        words = line.split()
        for word in words:
            try:
                val = float(word)
                if not found:
                    found = True
                    fm = val
                elif val > fm:
                    fm = val
            except ValueError:
                pass
    if found:
        return fm
    else:
        return


def filemaxname(fname):
    f = open(fname)
    return filemax(f)
#    with open(fname,'read') as f:
#        return filemax(f)
