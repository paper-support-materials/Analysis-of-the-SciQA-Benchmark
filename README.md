# Exploring Large Language Models for Scientific Question Answering via Natural Language to SPARQL Translation


This repository contains all the code and data referenced in the paper titled "Exploring Large Language Models for Scientific Question Answering via Natural Language to SPARQL Translation" 
\- ACM Transactions on Intelligent Systems and Technology, August 2025, ACM (Association for Computing Machinery), [DOI: 10.1145/3757923](http://dx.doi.org/10.1145/3757923) - authored by 

Antonello Meloni<sup>1</sup> and Diego Reforgiato Recupero<sup>1</sup>, 
Francesco Osborne<sup>2,3</sup>, 
Angelo Antonio Salatino<sup>3</sup> and Enrico Motta<sup>3</sup>,
Sahar Vahdati<sup>4</sup>,
Jens Lehmann<sup>4,5</sup>

1. Department of Mathematics and Computer Science, University of Cagliari, IT
2. University of Milan-Bicocca, IT
3. Knowledge Media Institute, The Open University, UK
4. ScaDS.AI - TU Dresden, DE
5. Amazon, DE


## Table of Content

- [Exploring Large Language Models for Scientific Question Answering via Natural Language to SPARQL Translation](#exploring-large-language-models-for-scientific-question-answering-via-natural-language-to-sparql-translation)
  - [Table of Content](#table-of-content)
  - [Abstract](#abstract)
  - [More info](#more-info)
    - [Models employed](#models-employed)
      - [T5-base](#t5-base)
      - [GPT-2-large](#gpt-2-large)
      - [Dolly-v2-3b](#dolly-v2-3b)
      - [GPT-3.5 Turbo](#gpt-35-turbo)
      - [Mistral-7B](#mistral-7b)
      - [Llama3.1-8B](#llama31-8b)
  - [Structure of the repository](#structure-of-the-repository)
  - [How to cite](#how-to-cite)

## Abstract

Translating scientific questions expressed in natural language into SPARQL queries that can be executed over knowledge graphs remains a significant challenge in the field of question answering. Recently, several prominent benchmarks, notably SciQA and DBLP-QuAD, have emerged to evaluate performance in this domain. In this paper, we provide a comprehensive analysis of the performance of language models on these benchmarks, assessing various optimization strategies. Our results indicate that the combined use of fine-tuning and prompting techniques, especially when incorporating strategic few-shot selection, produces excellent results on both benchmarks. These findings underscore an urgent need for more challenging benchmarks to better assess model capabilities. We identify key insights, common error patterns, and potential opportunities for transfer learning, and we discuss their implications for optimizing the performance of large language models in knowledge graph-based question answering tasks.

## More info

Answering scientific questions using large language models (LLMs) is a growing area of research. In our work, we explored how well these models can translate everyday scientific questions into SPARQL, a language used to query knowledge graphs (structured databases of information). We tested several modern models using two well-known benchmarks, SciQA and DBLP-QuAD. By combining techniques like fine-tuning and smart prompt design (known as few-shot prompting), we achieved strong results. However, we also found that the current benchmarks may be too easy for today’s advanced models. This suggests a need for more difficult tests to truly measure progress. We also identified common mistakes the models make and discussed how lessons from one domain can help improve performance in others. 

### Models employed

#### T5-base  
**Description:** T5-base is a transformer-based language model developed by Google. It is designed for versatility across a wide range of natural language processing tasks and, despite being smaller than other T5 variants, delivers strong performance in diverse applications.  
**Model:** [https://huggingface.co/t5-base](https://huggingface.co/t5-base)  

#### GPT-2-large  
**Description:** GPT-2-large is a transformer-based language model developed by OpenAI. It is characterized by a large number of parameters and strong capabilities in generating coherent, contextually relevant text from natural language prompts.  
**Model:** [https://huggingface.co/gpt2-large](https://huggingface.co/gpt2-large)  

#### Dolly-v2-3b  
**Description:** Dolly-v2-3b is a transformer-based language model released by Databricks. It is trained for natural language understanding and generation tasks and demonstrates solid performance on a variety of language-based applications.  
**Model:** [https://huggingface.co/databricks/dolly-v2-3b](https://huggingface.co/databricks/dolly-v2-3b)  

#### GPT-3.5 Turbo  
**Description:** GPT-3.5 Turbo is an advanced transformer-based language model developed by OpenAI. It offers large-scale capabilities and is optimized for both high-quality natural language generation and efficient deployment across diverse tasks.  
**Model:** [https://platform.openai.com/docs/models/gpt-3-5](https://platform.openai.com/docs/models/gpt-3-5)  

#### Mistral-7B  
**Description:** Mistral-7B is a transformer-based language model developed by Mistral AI. It is optimized for efficiency and strong performance on a broad range of language understanding and generation tasks, achieving competitive results with a relatively small parameter size.  
**Model:** [https://huggingface.co/mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)  

#### Llama3.1-8B  
**Description:** Llama3.1-8B is a transformer-based language model from the Llama 3 family developed by Meta AI. It is designed to balance high performance and computational efficiency, making it well-suited for fine-tuning in domain-specific applications.  
**Model:** [https://huggingface.co/meta-llama/Meta-Llama-3.1-8B](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B)  



## Structure of the repository

Folder ```code``` contains the codebase we used to perform our experiments.

Folder ```test_data``` contains the prompts for the large language models.

Folder ```execution_tests``` contains the codebase and the results of the execution evaluations.

## How to cite

[![ACM Digital Library](https://img.shields.io/badge/ACM-Digital%20Library-red)](https://doi.org/10.1145/3757923)

If you use this work in your research, please cite it as follows:

**BibTeX**
```bibtex
@article{10.1145/3757923,
  author    = {Meloni, Antonello and Reforgiato Recupero, Diego and Osborne, Francesco and Salatino, Angelo and Motta, Enrico and Vahadati, Sahar and Lehmann, Jens},
  title     = {Exploring Large Language Models for Scientific Question Answering via Natural Language to SPARQL Translation},
  year      = {2025},
  publisher = {Association for Computing Machinery},
  address   = {New York, NY, USA},
  issn      = {2157-6904},
  url       = {https://doi.org/10.1145/3757923},
  doi       = {10.1145/3757923},
  journal   = {ACM Trans. Intell. Syst. Technol.},
  month     = aug,
  keywords  = {Knowledge graphs, Question answering, Language models, Fine-tuning, Few-shot learning}
}


