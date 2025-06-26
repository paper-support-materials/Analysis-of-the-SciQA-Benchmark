import json
import time
from tqdm import tqdm
from SPARQLWrapper import SPARQLWrapper, JSON
import codecs
from files_utilities import *


# def run_sparql_query(query: str, endpoint: str = "https://sparql.dblp.org/sparql") -> list:
#     """
#     Runs a SPARQL query against the specified DBLP endpoint.
#
#     Args:
#         query (str): SPARQL query string.
#         endpoint (str): SPARQL endpoint URL.
#
#     Returns:
#         list: A list of query result dictionaries.
#     """
#     sparql = SPARQLWrapper(endpoint)
#     sparql.setQuery(query)
#     sparql.setReturnFormat(JSON)
#
#     try:
#         results = sparql.query().convert()
#         return results["results"]["bindings"]
#     except Exception as e:
#         print(f"SPARQL query failed: {e}")
#         return []


def run_sparql_query(query: str, endpoint: str = "https://sparql.dblp.org/sparql"):
    query = codecs.decode(query, 'unicode_escape')
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    try:
        response = sparql.query().convert()

        if "boolean" in response:
            # ASK query
            return response["boolean"]
        elif "results" in response:
            # SELECT query
            return response["results"]["bindings"]
        else:
            return "SPARQL query returned unexpected structure."

    except Exception as e:
        return f"SPARQL query failed: {e}"


def test_results(filename):
    results = {
        "gold": [],
        "generated": [],
        "empty": [],
        "equals": []
    }

    empty = 0
    equals = 0
    different = 0

    with open(filename, "r", encoding="utf-8") as j:
        data = json.load(j)

    queries = data["sparql"]
    g_queries = data["cleaned"]
    e_match = data["equals"]

    for i, query in enumerate(tqdm(queries)):

        try:
            if e_match[i]:
                equals += 1
                # res = run_sparql_query(query)
                # results["gold"].append(res)
                results["generated"].append("equal")
                # results["equals"].append(True)
                # if isinstance(res, bool):
                #     results["empty"].append(False)
                # else:
                #     results["empty"].append(len(res) == 0)
                #     if len(res) == 0:
                #         empty += 1
            else:
                # res = run_sparql_query(query)
                res_g = run_sparql_query(g_queries[i])
                time.sleep(0.5)
                # results["gold"].append(res)
                results["generated"].append(res_g)
                # if isinstance(res, bool):
                #     is_equal = res == res_g
                # else:
                #     is_equal = (res == res_g and len(res) > 0)
                # results["equals"].append(is_equal)
                # if isinstance(res_g, bool):
                #     results["empty"].append(False)
                # else:
                #     results["empty"].append(len(res_g) == 0)
                #     if len(res_g) == 0:
                #         empty += 1
                # if is_equal:
                #     equals += 1
                # else:
                #     different += 1
        except Exception as e:
            print(f"Error at index {i}: {e}")
            # results["gold"].append([])
            results["generated"].append([])
            # results["equals"].append(False)
            # results["empty"].append(True)
            empty += 1

        output_file = "results_" + filename
        with open(output_file, "w", encoding="utf-8") as jj:
            json.dump(results, jj, indent=2)

    print(f"Total queries: {len(queries)}")
    print(f"Equals: {equals}")
    # print(f"Different: {different}")
    # print(f"Empty: {empty}")

    output_file = "results_" + filename
    with open(output_file, "w", encoding="utf-8") as jj:
        json.dump(results, jj, indent=2)


def get_values_from_csv(filename):
    [header, data] = load_cvs(filename)
    new_data = {"questions": [], "sparql": [], "cleaned": [], "equals": []}
    print(header)
    for row in data:
        if len(row) > 3:
            new_data["questions"].append(row[0])
            new_data["sparql"].append(row[1])
            new_data["cleaned"].append(row[2])
            new_data["equals"].append(row[3] == "True")

    write_json("cleaned_"+filename.replace(".csv", ".json"), new_data)



if __name__ == '__main__':
    # test_results("Mistral.json")
    # get_values_from_csv("ft_T5_results.csv")
    # test_results("cleaned_ft_T5_results.json")
    get_values_from_csv("nlp_7_shots_gpt_results.csv")
    test_results("cleaned_nlp_7_shots_gpt_results.json")
