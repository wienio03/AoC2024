import sys
from collections import defaultdict
# TOP DOWN MERGE SORT
def merge_sort(A):
   B = A.copy()
   split_and_merge(A, 0, len(A), B)
   # A = B.copy() CHANGES REFERENCE SO IT DOESNT WORK, RETURNING B DOESNT WORK EITHER BECAUSE A IS NOT MODIFIED 
   A[:] = B
   return

def split_and_merge(A, start, end, B):
    # RECURSION BASE CASE (ONE ELEMENT ARRAY IS ALREADY SORTED
    if end - start <= 1:
        return
    mid = (start + end) // 2
    split_and_merge(B, start, mid, A)
    split_and_merge(B, mid, end, A)
    merge(A, start, mid, end, B)

def merge(A, start, mid, end, B):
    # MERGING ARRAYS INTO B (TEMPORARY TO STORE SORTED INSTANCE OF SPLIT UP A) 
    L = start
    R = mid

    for k in range(start, end):
        # IF THERE ARE ANY ELEMENTS TO BE PROCESSED IN LEFT SUBARRAY AND THERE ARE NONE IN RIGHT OR THE ELEMENT IN LEFT SUBARRAY IS <= TO THE ELEMENT IN RIGHT SUBARRAY PUT IT IN B
        if L < mid and (R >= end or A[L] <= A[R]):
            B[k] = A[L]
            L = L + 1
        else:
            B[k] = A[R]
            R = R + 1
def calculate_total_distance(left_list, right_list):
    merge_sort(left_list)
    merge_sort(right_list)
    total_distance = 0
    for left, right in zip(left_list, right_list):
        distance = abs(left - right)
        total_distance += distance

    return total_distance
def parse_file(file_path):
    left_list = []
    right_list = []
    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            stripped_line = line.strip()
            split_parts = line.split()
            first_val = int(split_parts[0])
            second_val = int(split_parts[1])
            left_list.append(first_val)
            right_list.append(second_val)
    return left_list, right_list

def count_frequencies_and_similarity_score(left_list, right_list):
    frequencies = defaultdict(int)
    for i in range(0, len(right_list)):
        frequencies[right_list[i]] = frequencies[right_list[i]] + 1
    return calculate_similarity_score(left_list, frequencies)
            

def calculate_similarity_score(left_list, frequencies):
    total_score = 0
    for i in range(0, len(left_list)):
        total_score = total_score + (left_list[i] * frequencies[left_list[i]])
    return total_score


if __name__ == "__main__":
    def main():
        input_file = sys.argv[1]
        left_list, right_list = parse_file(input_file)
        merge_sort(left_list)
        merge_sort(right_list)
        total_distance = calculate_total_distance(left_list, right_list)
        print(count_frequencies_and_similarity_score(left_list, right_list))
    main()
    


