def find_specific_ranks(n, k, scores):
    score_counts = {}
    result = []
    n=0
    for score in scores:
        if score in score_counts:
            score_counts[score] += 1
        else:
            score_counts[score] = 1

    unique_scores = sorted(score_counts.keys(), reverse=True)
    
    rank = 0
    for score in unique_scores:
        count = score_counts[score]
        rank += count
        if rank >= k:
            result.append(score)
            k *= 2  # Next rank is k/2th rank

    return result

# Input
n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Find specific ranks
result = find_specific_ranks(n, k, scores)

# Print the result
print(" ".join(map(str, result)))
