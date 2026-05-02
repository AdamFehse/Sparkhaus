def getDeployablePairs(performance, resourceCost):
    balances = [p - c for p, c in zip(performance, resourceCost)] # compute balance of i,j pairs
    balances.sort() # sort and use two pointers, left and right, to count valid j values for each i

    counter = 0
    n = len(balances)
    left = 0
    right = n - 1

    while left < right:
        if balances[left] + balances[right] > 0:
            counter += right - left
            right -= 1
        else:
            left += 1

    return counter


def getTriangleArea(x, y):
    x0, y0 = x[0], y[0]
    x1, y1 = x[1], y[1]
    x2, y2 = x[2], y[2]

    if y0 == y1:
        return abs(x1 - x0) * abs(y2 - y0) // 2
    if x0 == x1:
        return abs(y1 - y0) * abs(x2 - x0) // 2

    if y1 == y2:
        return abs(x2 - x1) * abs(y0 - y1) // 2
    if x1 == x2:
        return abs(y2 - y1) * abs(x0 - x1) // 2

    if y2 == y0:
        return abs(x0 - x2) * abs(y1 - y0) // 2
    if x2 == x0:
        return abs(y0 - y2) * abs(x1 - x0) // 2

    # Fallback for non-axis-aligned triangles.
    area2 = abs(
        x0 * (y1 - y2)
        + x1 * (y2 - y0)
        + x2 * (y0 - y1)
    )
    return area2 // 2
