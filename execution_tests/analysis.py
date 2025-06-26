from files_utilities import *
from hybrid import get_equals

def save_gold_data():
    data = load_json("results_Llama.json")
    original = load_json("Llama.json")
    gold = {
        "questions": original["questions"],
        "sparql": original["sparql"],
        "gold": data["gold"]
    }
    results = {
        "ok": 0,
        "error": 0,
        "empty": 0
    }
    result_list = []
    for result in gold["gold"]:
        if isinstance(result, str):
            results["error"] += 1
            result_list.append("error")
        else:
            if isinstance(result, list) and len(result) == 0:
                results["empty"] += 1
                result_list.append("empty")
            else:
                results["ok"] += 1
                result_list.append("ok")
    gold["result"] = results
    gold["result_list"] = result_list
    write_json("gold_results.json", gold)


def confront(filename):
    data = load_json(filename)
    gold = load_json("gold_results.json")
    generated = data["generated"]
    results = {
        "ok": 0,
        "equals": 0,
        "equal_result": 0,
        "eq_in_error": 0,
        "eq_in_empty": 0,
        "different": 0,
        "diff_in_error": 0,
        "error": 0,
        "empty": 0
    }
    result_list = []
    errors = set()
    for i, result in enumerate(generated):
        if result == "equal":
            results["equals"] += 1
            result_list.append("equals")
        elif isinstance(result, bool) or isinstance(result, list):
            results["ok"] += 1
            if result == gold["gold"][i]:
                results["equals"] += 1
                results["equal_result"] += 1

                if isinstance(result, list) and len(result) == 0:
                    results["eq_in_empty"] += 1
                    result_list.append("equal_empty_result")
                else:
                    result_list.append("equal_result")
            else:
                results["different"] += 1
                result_list.append("different")
        elif isinstance(result, str):
            results["error"] += 1
            result_list.append("error")
            if "FILTER NOT EXISTS" in result:
                errors.add("FILTER NOT EXISTS")
            elif "MIN" in result:
                errors.add("MIN")
            elif "SPARQL query failed: QueryBadFormed" in result:
                errors.add("Bad Formed")
            else:
                errors.add(result)
            if result == gold["gold"][i]:
                results["eq_in_error"] += 1
            else:
                results["diff_in_error"] += 1
    print(json.dumps(results, indent=4))
    print("Errors: ", errors)
    data["results"] = result_list
    write_json(filename, data)


def new_confront(filename):
    data = load_json(filename)
    gold = load_json("gold_results.json")
    generated = get_equals(data["generated"])
    results = {
        "ok": 0,
        "equals": 0,
        "equal_result": 0,
        "eq_in_error": 0,
        "eq_in_empty": 0,
        "different": 0,
        "diff_in_error": 0,
        "error": 0,
        "empty": 0
    }
    result_list = []
    errors = set()
    for i, result in enumerate(generated):
        if result == gold["gold"][i]:
            results["equal_result"] += 1
            if isinstance(result, list) and len(result) == 0:
                results["eq_in_empty"] += 1
        else:
            if isinstance(result, bool) or isinstance(result, list):
                results["different"] += 1
            else:
                results["error"] += 1

    print(json.dumps(results, indent=4))
    print("Errors: ", errors)
    data["results"] = result_list
    write_json(filename, data)


if __name__ == '__main__':
    # save_gold_data()
    # confront("results_Llama.json")
    # confront("results_Mistral.json")
    # confront("results_cleaned_ft_T5_results.json")
    # confront("results_cleaned_nlp_7_shots_gpt_results.json")
    new_confront("hybrid.json")
    # new_confront("results_Llama.json")
    # new_confront("results_Mistral.json")
    # new_confront("results_cleaned_ft_T5_results.json")
    # new_confront("results_cleaned_nlp_7_shots_gpt_results.json")
