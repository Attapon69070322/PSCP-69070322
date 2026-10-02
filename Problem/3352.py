"""laststand"""
import json
def main():
    """laststand"""
    n = json.loads(input())
    for i in n:
        print(str(i)[-1])

main()
