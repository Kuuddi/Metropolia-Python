def tuplaa_alkiot(luvut: list):
    multiplied = tuple(num * 2 for num in luvut)
    return multiplied

if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)
