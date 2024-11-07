def calculate_vehicle(v, w):
    # Check for invalid input
    if w < 2 or w % 2 != 0 or v >= w:
        return "INVALID INPUT"

    # Calculate TW and FW
    TW = (4 * v - w) // 2
    FW = v - TW

    # Check if calculations are correct
    if TW < 0 or FW < 0 or (2 * TW + 4 * FW) != w:
        return "INVALID INPUT"

    return f"TW={TW} FW={FW}"

# Reading input
try:
    v = int(input().strip())
    w = int(input().strip())
    result = calculate_vehicle(v, w)
    print(result)
except ValueError:
    print("INVALID INPUT")
