# Morphological compositional generalization

## Overview
This is the repo for Morphological Compositional Generalization project. For more project details, check the [Notion page](https://meteis.notion.site/Morphological-compositional-generalization-ba9a542988794c82b9236436be17a172?pvs=4).

## Evaluation Pipeline
Data is supposed to go through the following pipeline for evaluation:

Raw Data --> | Preprocess Data | --> | Prepare Data for Tasks | --> | Prepare Data for Evaluation | --> | Evaluate Model on Data | --> | Report Metrics |

These steps are done respectively with `preprocess_data.py`, `prepare_data_for_tasks.py` and `prepare_data_for_eval.py` scripts. Each pipeline step outputs data along with some metadata. Once the evaluation data is ready, it can be evaluated using the `evaluate_gpt.py` script (e.g. for GPT models) and metrics can be reported using the `report_metrics.py` script. Input data resides in the `data` folder, and outputs of the evaluation reside in `outputs` folder. 