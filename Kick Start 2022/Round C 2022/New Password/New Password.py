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

keys = ['#', '@', '*', '&']


def spec_ch(a):
    key = ['#', '@', '*', '&']
    for j in key:
        if j in a:
            return True
        return False


t = int(input())
for i in range(1, t + 1):
    N = [int(s) for s in input().split(' ')]
    P = [s for s in input().split(' ')]
    print(N[0], type(N[0]))
    print(P[0], type(P[0]))
    if not (any(x.islower() for x in P)):
        print('no1')
    if not (any(x.isupper() for x in P)):
        print('no2')
    if not (any(x.isdigit() for x in P)):
        print('no3')
    print(spec_ch(P))

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
