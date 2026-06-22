# NER-silver-to-gold

## Description

This model is a token-classification (NER) model first trained on silver data and subsequently fine-tuned on gold data.

The model extracts the following entity types:

* Besluitvormend_orgaan
* Ontvanger
* Rechtsobject
* Wettelijke_actie
* Wettelijke_grondslag

## Download

Download the model files from Google Drive:

**Google Drive:**
<https://drive.google.com/drive/folders/1BCOd4kPv5_Xrpb-2c0jTManGdcMES96P?usp=sharing>

After downloading, extract the files into:

```text
models/NER-silver-to-gold/
```

## Usage

```python
from src.load_ner import load_ner_model

model, tokenizer, ner_pipe = load_ner_model(
    "models/NER-silver-to-gold"
)
```
