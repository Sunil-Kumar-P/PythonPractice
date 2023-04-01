# Python Program to check if given array is Monotonic

# Check if given array is Monotonic


def isMonotonic(A):

	return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
			all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


# Driver program
A = [6, 6, 7, 7]

# Print required result
print(isMonotonic(A))

# This code is written by
# Sanjit_Prasad
