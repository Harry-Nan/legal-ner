# NERRE-silver-to-gold

## Description

This model is a span-based classification (NERRE) model first trained on silver data and subsequently fine-tuned on gold data.

The model extracts the following entity types:

* Besluitvormend_orgaan
* Ontvanger
* Rechtsobject
* Wettelijke_actie
* Wettelijke_grondslag

## Download

Download the model files from Google Drive:

**Google Drive:**
<https://drive.google.com/drive/folders/1Zjcb85d4XN9p-fNGoArdUnMebTdS-Op0?usp=sharing>

After downloading, extract the files into:

```text
models/NERRE-silver-to-gold/
```

## Usage

```python
from src.load_model import load_nerre_model

model, tokenizer, cfg = load_nerre_model(
    "NERRE-silver-to-gold"
)

```
