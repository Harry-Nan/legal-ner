# NERRE-gold

## Description

This model is a span-based classification (NERRE) model trained on manually annotated (gold) legal sentences from administrative decisions.

The model extracts the following entity types:

* Besluitvormend_orgaan
* Ontvanger
* Rechtsobject
* Wettelijke_actie
* Wettelijke_grondslag

## Download

Download the model files from Google Drive:

**Google Drive:**
<https://drive.google.com/drive/folders/1naTTwCMYHJVH_maKPEM5Jc7cuIFnNmy7?usp=sharing>

After downloading, extract the files into:

```text
models/NERRE-gold/
```

## Usage

```python
from src.load_model import load_nerre_model

model, tokenizer, cfg = load_nerre_model(
    "NERRE-gold"
)

```
