# DTS-SQL


## Overview
This repository hosts the code for the DTS-SQL paper, featuring state-of-the-art text-to-SQL models with 7B parameters. Our models demonstrate exceptional performance on the Spider and Spider-SYN datasets, setting new benchmarks in the field.

## Repository Contents

### Finetuning Scripts
- `schema_linking_generation_finetuning.ipynb`: Contains code for finetuning DeepSeek and Mistral models for text-to-SQL tasks.
- `sql_generation_finetuning.ipynb`: Dedicated to finetuning processes, specifically focusing on SQL generation.

### Inference Scripts
- `schema_linking_generation_inference.ipynb`: Script for schema linking generation using the finetuned models.
- `sql_generation_inference.ipynb`: Script for SQL generation at inference time using the finetuned models.

### Dataset Preparation
- `finetuning_dataset_creator.py`: Code for creating the finetuning dataset from the Spider dataset.

### Utilities
- `Utils` directory: Contains all necessary helper functions for formatting tables and creating the dataset.

### Results
- All of the results are stored in the results directory.

### Citation
@article{pourreza2024dts,
  title={DTS-SQL: Decomposed Text-to-SQL with Small Large Language Models},
  author={Pourreza, Mohammadreza and Rafiei, Davood},
  journal={arXiv preprint arXiv:2402.01117},
  year={2024}
}



