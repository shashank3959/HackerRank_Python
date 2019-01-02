# You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
#
# Different sizes of alphabet rangoli are shown below:
#
# #size 3
#
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
#
# #size 5
#
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
#
# #size 10
#
# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------
# The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).
#
# Input Format
#
# Only one line of input containing , the size of the rangoli.
#
# Constraints
#
#
# Output Format
#
# Print the alphabet rangoli in the format explained above.
#
# Sample Input
#
# 5
# Sample Output
#
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def print_rangoli(num):
    #Top half
    for i in reversed(range(num)):
        alph = []
        for j in reversed(range(i, num)):
            alph.append(chr(97 + j))

        alph_reversed = "-".join(reversed(alph[:len(alph)-1]))
        alph = "-".join(alph)

        print("-"*i*2 + alph + "-"*(i != num-1) + alph_reversed + "-"*i*2)

    #Bottom half
    for i in range(num):
        alph = []
        for j in reversed(range(i, num)):
            alph.append(chr(97 + j))

        alph_reversed = "-".join(reversed(alph[:len(alph)-1]))
        alph = "-".join(alph)

        if i != 0:
            print("-"*i*2 + alph + "-"*(i != num-1) + alph_reversed + "-"*i*2)

    return


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)