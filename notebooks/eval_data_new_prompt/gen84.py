def solve(N):
    # Convert N to binary and return the last two digits
    return bin([int(i) for i in str(N)][-1])[2:]