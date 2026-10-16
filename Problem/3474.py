"""ICS"""

DIGITS = {
    "Black": 0,
    "Brown": 1,
    "Red": 2,
    "Orange": 3,
    "Yellow": 4,
    "Green": 5,
    "Blue": 6,
    "Purple": 7,
    "Grey": 8,
    "White": 9,
}

MULTIPLIERS = {
    "Black": 1,
    "Brown": 10,
    "Red": 100,
    "Orange": 1000,
    "Yellow": 10000,
    "Green": 100000,
    "Blue": 1000000,
    "Purple": 10000000,
    "Gold": 0.1,
    "Silver": 0.01,
}

TOLERANCES = {
    "Brown": 0.01,
    "Red": 0.02,
    "Green": 0.005,
    "Blue": 0.0025,
    "Purple": 0.0010,
    "Grey": 0.0005,
    "Gold": 0.05,
    "Silver": 0.10,
}

BAND_1 = input()
BAND_2 = input()
BAND_3 = input()
BAND_4 = input()

if (
    BAND_1 in DIGITS
    and BAND_2 in DIGITS
    and BAND_3 in MULTIPLIERS
    and BAND_4 in TOLERANCES
):
    BASE = (DIGITS[BAND_1] * 10 + DIGITS[BAND_2]) * MULTIPLIERS[BAND_3]
    LOWER = BASE * (1 - TOLERANCES[BAND_4])
    UPPER = BASE * (1 + TOLERANCES[BAND_4])
    print(f"{LOWER:.4f}")
    print(f"{UPPER:.4f}")
else:
    print("Error")
