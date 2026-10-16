"""MYBAD"""

arrows = {
    "U": [
        "  *  ",
        " *** ",
        "* * *",
        "  *  ",
        "  *  ",
    ],
    "D": [
        "  *  ",
        "  *  ",
        "* * *",
        " *** ",
        "  *  ",
    ],
    "L": [
        "  *  ",
        " *   ",
        "*****",
        " *   ",
        "  *  ",
    ],
    "R": [
        "  *  ",
        "   * ",
        "*****",
        "   * ",
        "  *  ",
    ],
}

command = input().strip()

for row in range(5):
    line_parts = [arrows[char][row] for char in command]
    print(" ".join(line_parts))
