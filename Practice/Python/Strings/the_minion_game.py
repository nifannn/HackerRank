def minion_game(string):
    # Stuart score
    s_idx = [i for i, c in enumerate(string) if c not in 'AEIOU']
    s_score = sum([len(string)-i for i in s_idx])
    # Kevin score
    k_idx = [i for i, c in enumerate(string) if c in 'AEIOU']
    k_score = sum([len(string)-i for i in k_idx])
    # final result
    if k_score > s_score:
        print("Kevin {}".format(k_score))
    elif k_score < s_score:
        print("Stuart {}".format(s_score))
    else:
        print("Draw")

if __name__ == '__main__':
    minion_game(input("Enter a string: "))
