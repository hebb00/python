def compare(q, qq):
    l= len(q)
    ll= len(qq)
    if l != ll:
        return False
    while q :
        ele= q.pop()
        el= qq.pop()
        print(el)
        if ele != el:
            return False
    return True


if __name__ == "__main__":
    q=[4,5,6]
    qq=[4,5,6]
    print(compare(q,qq))
