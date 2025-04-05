def longsequence(X, Y, m, n, sequence):
   if m == 0 or n == 0:  # if one of the sequence is empty
       return 0

   if X[m - 1] == Y[n - 1]:
       sequence.append(X[m - 1])  #we add the character that is common
       return 1 + longsequence(X, Y, m - 1, n - 1, sequence) #we add one to the length of the common sequence and get to the next characters

   else:
       s1 = sequence.copy()  # X
       s2 = sequence.copy()  # Y


       # Call recursively for both branches
       result1 = longsequence(X, Y, m - 1, n, s1)
       result2 = longsequence(X, Y, m, n - 1, s2)


       # Compare results and choose the longer one
       if result1 > result2:
           sequence[:] = s1  # Update the sequence with X part
           return result1
       else:
           sequence[:] = s2  # Update the sequence with Y part
           return result2


def dynammic(X, Y, m, n):
   # Initialize the matrix with 0
   dp = [[0] * (n + 1) for _ in range(m + 1)]


   # building the matrix
   for i in range(1, m + 1):
       for j in range(1, n + 1):
           if X[i - 1] == Y[j - 1]:
               dp[i][j] = dp[i - 1][j - 1] + 1
           else:
               dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

#dp[i-1][j]: the  length if we ignore the last character of X but still consider all of Y[:j].
#dp[i][j-1]: the length if we ignore the last character of Y but still consider all of X[:i]

   print("Print the matrix:")
   for row in dp:
       print(row)

   length = dp[m][n] #the result is here (last element in the matrix,the down right corner
   #Building the aequence by going backwards in the matrix
   lcs = []
   i, j = m, n
   while i > 0 and j > 0:
       if X[i - 1] == Y[j - 1]:
           lcs.append(X[i - 1])  # If characters match, include it in LCS
           i =i- 1
           j =j- 1
       elif dp[i - 1][j] > dp[i][j - 1]:
           i =i- 1  # Move up if the value above is bigger
       else:
           j =j- 1  # Move left if the value to the left is bigger


   # Reverse the LCS list to get the correct order
   lcs.reverse()
   return length, ''.join(lcs)  # Return the length and LCS string


#X = input("The first sequence is: ")
#Y = input("The second sequence is: ")
X = "MNPNQMN"
Y = "NQPMNM"
m = len(X)
n = len(Y)
sequence = []
length_lcs = longsequence(X, Y, m, n,sequence)
print("Length of longest common subsequence:", length_lcs)
print("One of the longest common subsequences :", ''.join(reversed(sequence)))

print("---------")
print("The sequences you chose:")
print("X =", X)
print("Y =", Y)
length, lcs_sequence = dynammic(X, Y, m, n)
print("\nLength of longest common subsequence :", length)
print("One of the longest common subsequences :", lcs_sequence)