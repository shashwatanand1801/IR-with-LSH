import random
import numpy as np
from itertools import permutations
import json
import time


begin = time.time()

def tokenize_document(document, k=8):
    """Tokenize a document into k-shingles"""
    shingles = set()
    for i in range(len(document) - k + 1):
        shingle = document[i:i+k]
        shingles.add(shingle)
    return shingles


def generate_signature_matrix(documents, num_hashes):
    """Generate a signature matrix for a set of documents"""
    num_documents = len(documents)
    singles = set()

    for document in documents:
        single = tokenize_document(document)
        singles.update(single)

    num_singles = len(singles)

    single_list = list(singles)

    incident_matrix = np.zeros((num_singles, num_documents))


    for i in range(len(documents)):
        single = tokenize_document(documents[i])
        for j, tok in enumerate(singles):
            if tok in single:
                incident_matrix[j][i] = 1
    ar = list(range(1,num_singles+1))
    # print(ar)

    # lst = permutations(ar)
    # abc = list(lst)
    # print(lst)

    # for x in (lst):
    #     print(type(x))

    count = 0
    permute = []
    while count<num_hashes:
        lst = permutations(ar)
        # print(list(lst))
        for item in lst :
            if count>=num_hashes :
                break
            permute.append(item)
            # print("HHHHHHHHEEEEEEELLLLLLLLLLLLLLLLOOOOOOOOO")
            count += 1


    final_permutations = random.sample(permute, num_hashes)


    signature_matrix = np.full((num_hashes, num_documents), np.inf)

    for i, permutes in enumerate(final_permutations):
        key = -1
        for j in range(len(documents)):
            for idx in permutes:
                if(incident_matrix[idx-1][j]==1 and idx < signature_matrix[i][j]):
                    signature_matrix[i][j] = idx

    # print(signature_matrix)

    return signature_matrix

def compute_jaccard_similarity_set(set1, set2):
    """Compute Jaccard similarity between two sets"""
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0


def compute_jaccard_similarity_list(set1, set2):
    """Compute Jaccard similarity between two sets"""
    # intersection = len(set1 & set2)
    # union = len(set1 | set2)
    num = 0
    deno = len(set1)
    for i in range(len(set1)):
        if(set1[i] == set2[i]):
            num += 1

    # print(f"num -> {num}  &  deno -> {deno}")
    return num/deno

def compute_signature_similarity(signature_matrix, doc1, doc2):
    """Compute Jaccard similarity between two documents"""
    list1 = signature_matrix[:, doc1]
    list2 = signature_matrix[:, doc2]

    set1 = set(list1)
    set2 = set(list2)

    return compute_jaccard_similarity_list(list1, list2)




def lsh_plagiarism_detector(documents, num_hashes, threshold=0.5):
    """LSH-based plagiarism detector"""
    signature_matrix = generate_signature_matrix(documents, num_hashes)
    matches = []
    false_pos = 0
    false_neg =0

    num_documents = len(documents)
    candidate_pairs = [(i, j) for i in range(num_documents) for j in range(i+1, num_documents)]


    for pair in candidate_pairs:
        i, j = pair
        set1 = tokenize_document(documents[i])
        set2 = tokenize_document(documents[j])
        jaccard_similarity = compute_jaccard_similarity_set(set1, set2)

        # print(f"Similarity (Jacardian) of Documents {i} and {j} = {jaccard_similarity}")

        signature_similarity = compute_signature_similarity(signature_matrix, i, j)

        # print(f"Similarity (Signature) of Documents {i} and {j} = {signature_similarity}")

        if signature_similarity >= threshold:
            matches.append((i, j, signature_similarity, jaccard_similarity))

        if (signature_similarity>=0.5) and (jaccard_similarity<0.5):
            false_pos += 1
        
        if (signature_similarity<0.5) and (jaccard_similarity>=0.5):
            false_neg += 1
        


    return matches ,false_pos, false_neg


def evaluate_lsh_plagiarism_detector(documents, num_hashes, threshold=0.5, num_runs=5):
    false_positives = []
    false_negatives = []
    matches = []

    for i in range(num_runs):
        matches, false_pos, false_neg = lsh_plagiarism_detector(documents, num_hashes, threshold=0.5)
        false_positives.append(false_pos)
        false_negatives.append(false_neg)
    
    avg_false_positive = sum(false_positives)/num_runs
    avg_false_negative = sum(false_negatives)/num_runs

    return matches, avg_false_negative, avg_false_positive




# Getting the documents

f = open('data.json')

data = json.load(f)

f.close()






# Define documents


# Dummy Testing data
# documents = [
#     "The quick brown fox jumps over the lazy dog",
#     "A quick brown dog jumps over the lazy cat",
#     "The quick brown fox jumps over the lazy cat",
#     "A quick brown fox jumps over the lazy dog",
#     "The quick brown cat jumps over the lazy dog",
#     "A quick brown dog jumps over the lazy fox",
#     "The quick brown fox jumps over the lazy elephant",
#     "A quick brown elephant jumps over the lazy cat"
# ]

documents = []

plays = list(data.keys())

for key in data.keys() :
    documents.append(data[key])

print(len(documents))





# Define parameters
num_hashes_list = [50, 100, 200]
bands_list = [5, 10, 40]
rows_list = [10, 10, 5]

matches = []
avg_false_negative = 0
avg_false_positive = 0

for num_hashes in num_hashes_list:
    matches, avg_false_negative, avg_false_positive = evaluate_lsh_plagiarism_detector(
        documents, 
        num_hashes, 
        threshold=0.5, 
        num_runs=5
    )

    print(f"\n\nSimilar Documents with similarity values are (No of hash functions = {num_hashes}) :\n")
    for item in matches:
        print(f"Documents -->  {plays[item[0]]}  &  {plays[item[1]]}   | Signature = {item[2]}  | Jaccard = {item[3]}")
    print('\n-------------------------------------------------------------------')
    print(f"\nAverage number of false negatives = {avg_false_negative}")
    print(f"Average number of false positives = {avg_false_positive}")

end = time.time()

print(f"\nTime taken = {end-begin}")




    