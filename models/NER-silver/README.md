# NER-silver

## Description

This model is a token-classification (NER) model trained on automatically annotated (silver) legal sentences from administrative decisions.

The model extracts the following entity types:

* Besluitvormend_orgaan
* Ontvanger
* Rechtsobject
* Wettelijke_actie
* Wettelijke_grondslag

## Download

Download the model files from Google Drive:

**Google Drive:**
<https://drive.google.com/drive/folders/1_5MW4jLl0WJCSIaT8Bo7toFLUWCx3yTr?usp=sharing>

After downloading, extract the files into:

```text
models/NER-silver/
```

## Usage

```python
from src.load_ner import load_ner_model

model, tokenizer, ner_pipe = load_ner_model(
    "models/NER-silver"
)
```
