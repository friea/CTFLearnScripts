CipherText = "ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB"
reverse_alphabet = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'K', 10: 'L',
    11: 'M', 12: 'N', 13: 'O', 14: 'P', 15: 'Q', 16: 'R', 17: 'S', 18: 'T', 19: 'U', 20: 'W',
    21: 'X', 22: 'Y', 23: 'Z'
}
BinaryCipherText =""
PlainText = ""
for char in CipherText:
    if char=="A":
        BinaryCipherText += "0"
    else:
        BinaryCipherText += "1"
print(BinaryCipherText)
for i in range(int(len(BinaryCipherText)/5)):
    PlainText += reverse_alphabet[int(BinaryCipherText[i*5:(i+1)*5],2)]
print(PlainText)