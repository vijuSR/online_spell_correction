# TODO: stemming, lemmatization, normalization
import numpy as np

INSERTION_COST = 0.2


def get_prefix_distance(input_string, candidate_string):
    input_string = input_string.lower()
    prefix_len = len(input_string)

    candidate_string = candidate_string.lower()[:prefix_len]
    candidate_len = len(candidate_string)

    row_num = prefix_len + 1
    col_num = candidate_len + 1

    distance_matrix = np.zeros((row_num, col_num))

    distance_matrix[0, 1:] = [x for x in range(1, col_num)]
    distance_matrix[1:, 0] = [x for x in range(1, row_num)]

    for i in range(1, row_num):
        for j in range(1, col_num):
            if input_string[i-1] == candidate_string[j-1]:
                distance_matrix[i, j] = distance_matrix[i-1, j-1]
            else:
                distance_matrix[i, j] = min(distance_matrix[i-1,j-1],
                                            distance_matrix[i-1,j],
                                            distance_matrix[i,j-1]) + 1
    return distance_matrix[-1,-1]


def get_insert_distance(input_string, candidate_string):
    insert_ops = len(candidate_string) - len(input_string)
    return INSERTION_COST*insert_ops


def get_edit_distance(input_string, candidate_string):
    pdistance = get_prefix_distance(input_string, candidate_string)
    idistance = get_insert_distance(input_string, candidate_string)    
    return pdistance + idistance


def get_candidates_with_distance(query, candidates):
    rank = {}

    for candidate in candidates:
        edist = get_edit_distance(query, candidate)

        # if edist > 3:
        #     continue

        if rank.get(edist):
            rank[edist].append(candidate)
        else:
            rank[edist] = [candidate]

    return rank


def generate_rank(query, candidates):
    result = get_candidates_with_distance(query, candidates)
    ranked_candidates = []
        
    for k in sorted(list(result.keys())):
        ranked_candidates.extend(list(result[k]))

    return ranked_candidates
