def count_bits(n):
    x = str(bin(n))
    one_count = 0
    for i in x:
        if i == "1":
            one_count+=1
    return one_count