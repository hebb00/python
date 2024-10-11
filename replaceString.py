# replace a string in an array
def replaceG(l):
    res = [sub.replace('g','_').replace('_','e') for sub in l]
    return res
if __name__ == "__main__":
    print(replaceG(['egt','tte','gg']))