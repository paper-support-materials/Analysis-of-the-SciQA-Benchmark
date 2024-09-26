import openai
from config import OPENAI_API_KEY





openai.api_key = OPENAI_API_KEY


def gpt_query(msg, context=None, adding="\n you must return only the Sparql query!"):
    if context is None:
        context = "You are a translator from natural language to Sparql using the provided examples."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": context},
            {"role": "user", "content": msg + adding}],
        temperature=0.5,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        timeout=30
    )
    return response['choices'][0]['message']['content']


if __name__ == '__main__':
    a=gpt_query('\n input (English text): Which model has achieved the highest F1 score on the HoC benchmark dataset?\n output (Sparql query): SELECT DISTINCT ?model ?model_lbl WHERE { ?metric a orkgc:Metric; rdfs:label ?metric_lbl. FILTER (str( ?metric_lbl) = "F1") { SELECT ?model ?model_lbl WHERE { ?dataset a orkgc:Dataset; rdfs:label ?dataset_lbl. FILTER (str( ?dataset_lbl) = "HoC") ?benchmark orkgp:HAS_DATASET ?dataset; orkgp:HAS_EVALUATION ?eval. ?eval orkgp:HAS_VALUE ?value; orkgp:HAS_METRIC ?metric. ?cont orkgp:HAS_BENCHMARK ?benchmark; orkgp:HAS_MODEL ?model. ?model rdfs:label ?model_lbl. } ORDER BY DESC( ?value) LIMIT 1 } } \n with this example what is the sparql query for:  Which model has achieved the highest Accuracy score on the Story Cloze Test benchmark dataset?')
    print(a)