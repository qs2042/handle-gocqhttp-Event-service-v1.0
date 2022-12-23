

def analysisDoc(tmp: str):
    if tmp == None: return {}
    tmp = tmp[1:-1]
    r = {}
    for i in tmp.split("\n"):
        l = i.split(":")
        k: str = l[0]
        v: str = l[-1]
        r[k.strip()] = v.strip()
    return r