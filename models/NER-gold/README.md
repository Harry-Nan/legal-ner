# NER-gold

## Description

This model is a token-classification (NER) model trained on manually annotated (gold) legal sentences from administrative decisions.

The model extracts the following entity types:

* Besluitvormend_orgaan
* Ontvanger
* Rechtsobject
* Wettelijke_actie
* Wettelijke_grondslag

## Download

Download the model files from Google Drive:

**Google Drive:**
<https://drive.google.com/drive/folders/1as8i1J5sgiJOyYow7SLYeJmFQEz09fhg?usp=drive_link>

After downloading, extract the files into:

```text
models/NER-gold/
```

## Usage

```python
from src.load_ner import load_ner_model

model, tokenizer, ner_pipe = load_ner_model(
    "models/NER-gold"
)
```
