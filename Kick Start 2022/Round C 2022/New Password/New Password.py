import sys

sys.stdin = open("New Password.txt")


# t number of test cases
# N length of the old password
# P old password

# passwords must contain:
# 1.At least 7 characters.
# 2.At least one uppercase English alphabet letter.
# 3.At least one lowercase English alphabet letter.
# 4.At least one digit.
# 5.At least one special character #, @, *, &.


# string createNewPassword(string oldPassword) {
#     bool condition2 = false;
#     bool condition3 = false;
#     bool condition4 = false;
#     bool condition5 = false;
#     string newPassword = oldPassword;
#     for (int i = 0; i < oldPassword.size(); i++) {
#         if (oldPassword[i] >= 'A' && oldPassword[i] <= 'Z')
#           condition2 = true;
#         else if (oldPassword[i] >= 'a' && oldPassword[i] <= 'z')
#           condition3 = true;
#         else if (oldPassword[i] >= '0' && oldPassword[i] <= '9')
#           condition4 = true;
#         else if (oldPassword[i] == '@' || oldPassword[i] == '#' || oldPassword[i] == '&' || oldPassword[i] == '*')
#           condition5 = true;
#     }
#
#     if (!condition2) newPassword.append("A"); // Append any uppercase English alphabet letter.
#     if (!condition3) newPassword.append("a"); // Append any lowercase English alphabet letter.
#     if (!condition4) newPassword.append("1"); // Append any digit.
#     if (!condition5) newPassword.append("#"); // Append any special character.
#
#     // Append any digit, letter, or a special character.
#     while (newPassword.size() < 7) newPassword.append("1");
#
#     return newPassword;
# }

# if not (any(x.islower() for x in P)):
# if not (any(x.isupper() for x in P)):
# if not (any(x.isdigit() for x in P)):

def createNewPassword():
    N = int(input())  # length of the old password
    # print(N)
    P = [s for s in input().split(' ')]  # old password
    # print(P)
    condition2 = False
    condition3 = False
    condition4 = False
    condition5 = False
    newPassword = P[0]
    for j in newPassword:
        if j.isupper():
            condition2 = True
        elif j.islower():
            condition3 = True
        elif j.isdigit():
            condition4 = True
        elif j == '@' or j == '#' or j == '&' or j == '*':
            condition5 = True
    n = list(newPassword)
    if not condition2:
        n.append("A")
        # n = ''.join(n)
        # print(n)
    if not condition3:
        n.append("a")
        # print(n)
    if not condition4:
        n.append("1")
        # print(n)
    if not condition5:
        n.append("#")
        # print(n)

    while len(n) < 7:
        n.append("1")

    return ''.join(n)


for case in range(int(input())):
    print('Case #%d: %s' % (case + 1, createNewPassword()))
# Passed
