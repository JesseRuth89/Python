# first attempt
# def safe_pawns(pawns: set) -> int:
#     count = 0
#     # easy readability but I'm sure this can be cleaned
#     for parent in pawns:
#         for children in pawns:
#             # checking whites
#             if int(parent[1]) - 1 == int(children[1]):
#                 # absolute different between positions
#                 if abs(ord(children[0]) - ord(parent[0])) == 1:
#                     count += 1
#                     # has to be a better way, always a better way
#                     break
#     return count
# second attempt
def safe_pawns(pawns: set) -> int:
    count = 0
    for pawn in pawns:
        # generating safe positions
        # convert position to an int 'ord' then back to a char 'chr'
        col_l = chr(ord(pawn[0]) - 1)
        col_r = chr(ord(pawn[0]) + 1)
        row = str(int(pawn[1]) - 1)
        # showing check
        # print(f'{pawn} can be safe via {col_r+row} or {col_l+row}')
        # using 'in' is more elegant
        if col_r+row in pawns or col_l+row in pawns:
            count += 1
    return count

if __name__ == '__main__':
    print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
    print(safe_pawns({"e4"}))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"e4"}) == 0
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
