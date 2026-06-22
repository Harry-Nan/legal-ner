# Pretrained Models

This directory contains the pretrained model checkpoints. Due to GitHub file-size limitations, model weights are hosted externally and must be downloaded separately.

## Available Models

### NER Models (Token Classification)

| Model              | Description                                           | Download    |
| ------------------ | ----------------------------------------------------- | ----------- |
| NER-gold           | Trained on manually annotated (gold) data             | https://drive.google.com/drive/folders/1as8i1J5sgiJOyYow7SLYeJmFQEz09fhg?usp=drive_link |
| NER-silver         | Trained on automatically annotated (silver) data      | https://drive.google.com/drive/folders/1_5MW4jLl0WJCSIaT8Bo7toFLUWCx3yTr?usp=drive_link |
| NER-silver-to-gold | Pretrained on silver data and fine-tuned on gold data | https://drive.google.com/drive/folders/1BCOd4kPv5_Xrpb-2c0jTManGdcMES96P?usp=drive_link |

### NERRE Models (Span Classification)

| Model                | Description                                           | Download    |
| -------------------- | ----------------------------------------------------- | ----------- |
| NERRE-gold           | Trained on manually annotated (gold) data             | https://drive.google.com/drive/folders/1naTTwCMYHJVH_maKPEM5Jc7cuIFnNmy7?usp=drive_link |
| NERRE-silver         | Trained on automatically annotated (silver) data      | https://drive.google.com/drive/folders/1yywYKSjvbNcH9c07bnZLAdBkrIQIJNB6?usp=drive_link |
| NERRE-silver-to-gold | Pretrained on silver data and fine-tuned on gold data | https://drive.google.com/drive/folders/1Zjcb85d4XN9p-fNGoArdUnMebTdS-Op0?usp=drive_link |

---

## Installation

Download the desired model and extract it into the corresponding folder.

Example:

```text
models/
├── NER-gold/
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── special_tokens_map.json
│   └── vocab.txt
│
├── NERRE-gold/
│   ├── config.json
│   ├── model.pt
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── special_tokens_map.json
│   └── vocab.txt
```

---

## Usage

---

## Usage

Example code for loading and running all NER and NERRE models is provided in:

```text
load_models.ipynb
```

---

## Model Types

### NER

The NER models perform token-level entity recognition using BIO tagging.

Entity types:

* Besluitvormend_orgaan
* Ontvanger
* Rechtsobject
* Wettelijke_actie
* Wettelijke_grondslag

### NERRE

The NERRE models perform span-level entity classification using a JointSpERT architecture.

Entity types:

* Besluitvormend_orgaan
* Ontvanger
* Rechtsobject
* Wettelijke_actie
* Wettelijke_grondslag

---
