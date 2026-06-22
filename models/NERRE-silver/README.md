# NERRE-silver

## Description

This model is a span-based classification (NERRE) model trained on automatically annotated (silver) legal sentences from administrative decisions.

The model extracts the following entity types:

* Besluitvormend_orgaan
* Ontvanger
* Rechtsobject
* Wettelijke_actie
* Wettelijke_grondslag

## Download

Download the model files from Google Drive:

**Google Drive:**
<https://drive.google.com/drive/folders/1yywYKSjvbNcH9c07bnZLAdBkrIQIJNB6?usp=sharing>

After downloading, extract the files into:

```text
models/NERRE-silver/
```

## Usage

```python
from src.load_model import load_nerre_model

model, tokenizer, cfg = load_nerre_model(
    "NERRE-silver"
)

```
