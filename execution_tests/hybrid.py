from files_utilities import *
from collections import Counter


def confront():
    llama = load_json("results_Llama.json")
    t5 = load_json("results_cleaned_ft_T5_results.json")
    gpt = load_json("results_cleaned_nlp_7_shots_gpt_results.json")
    mistral = load_json("results_Mistral.json")
    majority_results = majority_confrontation(llama, mistral, t5,  gpt)
    results = {"generated": majority_results}
    write_json("hybrid.json", results)


def normalize(item):
    try:
        return json.dumps(item, sort_keys=True)
    except TypeError:
        return str(item)


def is_error(value):
    return isinstance(value, str) and value.startswith("SPARQL query failed")


def preference_score(value):
    """Lower score = better quality."""
    if is_error(value):
        return float('inf')  # deprioritize errors unless all are errors
    if isinstance(value, str):
        return 0
    elif isinstance(value, list):
        return 1 if len(value) > 0 else 3
    elif isinstance(value, bool):
        return 1
    return 4  # worst fallback for unknowns


# def majority_confrontation(data1, data2, data3, data4):
#     g1 = data1["generated"]
#     g2 = data2["generated"]
#     g3 = data3["generated"]
#     g4 = data4["generated"]
#
#     assert len(g1) == len(g2) == len(g3) == len(g4), "Mismatch in list lengths"
#
#     majority_results = []
#     vote_counts = Counter()
#
#     for i in range(len(g1)):
#         values = [g1[i], g2[i], g3[i], g4[i]]
#         normalized = [normalize(v) for v in values]
#         counter = Counter(normalized)
#         most_common = counter.most_common()
#         top_count = most_common[0][1]
#         tied_keys = [k for k, v in most_common if v == top_count]
#         candidates = [v for v in values if normalize(v) in tied_keys]
#
#         non_error_candidates = [v for v in candidates if not is_error(v)]
#
#         if non_error_candidates:
#             best = min(non_error_candidates, key=preference_score)
#         else:
#             # All values are errors → pick the most frequent one
#             best_norm = tied_keys[0]  # already sorted by count
#             for v in values:
#                 if normalize(v) == best_norm:
#                     best = v
#                     break
#
#         majority_results.append(best)
#         vote_counts[top_count] += 1
#
#     print("Agreement breakdown:")
#     for k in sorted(vote_counts, reverse=True):
#         print(f"  {k} out of 4 models agreed: {vote_counts[k]} queries")
#
#     return majority_results

def get_equals(data):
    gold = load_json("gold_results.json").get("gold")
    new_data = []
    for i, item in enumerate(data):
        if item == "equal":
            item = gold[i]
        new_data.append(item)
    return new_data


def majority_confrontation(data1, data2, data3, data4):
    g1 = get_equals(data1["generated"])
    g2 = get_equals(data2["generated"])
    g3 = get_equals(data3["generated"])
    g4 = get_equals(data4["generated"])
    assert len(g1) == len(g2) == len(g3) == len(g4), "Mismatch in list lengths"

    majority_results = []
    vote_counts = Counter()
    one_vote_details = []

    model_names = ["LLaMA", "Mistral", "T5",  "GPT"]
    all_models = [g1, g2, g3, g4]

    for i in range(len(g1)):
        values = [g1[i], g2[i], g3[i], g4[i]]
        normalized = [normalize(v) for v in values]
        counter = Counter(normalized)
        most_common = counter.most_common()
        top_count = most_common[0][1]
        tied_keys = [k for k, v in most_common if v == top_count]
        candidates = [v for v in values if normalize(v) in tied_keys]

        non_error_candidates = [v for v in candidates if not is_error(v)]

        if non_error_candidates:
            best = min(non_error_candidates, key=preference_score)
        else:
            best_norm = tied_keys[0]
            for v in values:
                if normalize(v) == best_norm:
                    best = v
                    break

        majority_results.append(best)
        vote_counts[top_count] += 1

        if top_count == 1:
            # Find which model produced the winner
            for idx, v in enumerate(values):
                if v == best:
                    winning_model = model_names[idx]
                    break

            one_vote_details.append({
                "index": i,
                "winner_model": winning_model,
                "winner_answer": best,
                "all_values": {
                    "T5": g1[i],
                    "Mistral": g2[i],
                    "GPT": g3[i],
                    "LLaMA": g4[i]
                }
            })

    print("Agreement breakdown:")
    for k in sorted(vote_counts, reverse=True):
        print(f"  {k} out of 4 models agreed: {vote_counts[k]} queries")

    write_json("one_vote_queries.json", one_vote_details)

    return majority_results


if __name__ == '__main__':
    confront()
