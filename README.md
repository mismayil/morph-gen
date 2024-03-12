# Morphological compositional generalization

## Overview
This is the repo for Morphological Compositional Generalization project. For more project details, check the [Notion page](https://meteis.notion.site/Morphological-compositional-generalization-ba9a542988794c82b9236436be17a172?pvs=4).

## Experiment Pipeline
Data is supposed to go through the following pipeline for evaluation:

1. Raw Data -->

2. Preprocess Data [`preprocess_data.py`] --> 

3. Prepare Data for Tasks [`prepare_data_for_tasks.py`] --> 

4. Prepare Data for Evaluation [`prepare_data_for_eval.py`] --> 

5. Evaluate Model on Data [`evaluate_gpt.py`] --> 

6. Report Metrics [`report_metrics.py`] --> 

7. Tabulate Results [`tabulate_results.py`] --> 

8. Plot Results [`plot_results.py`]

There are also corresponding bash scripts to automatically run pipeline steps for multiple languages, templates etc. Raw input data resides in the `data` folder. Input data and outputs of models reside in the `experiments/data` and `experiments/outputs` directories respectively.