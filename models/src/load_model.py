import json
from pathlib import Path

import torch
from transformers import AutoTokenizer

from .joint_spert import JointSpert

from pathlib import Path

from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
)

label_map = {
    "L0":"O",
    "L1":"B-Ontvanger", "L2":"I-Ontvanger",
    "L3":"B-Besluitvormend_orgaan", "L4":"I-Besluitvormend_orgaan",
    "L5":"B-Rechtsobject", "L6":"I-Rechtsobject",
    "L7":"B-Wettelijke_actie", "L8":"I-Wettelijke_actie",
    "L9":"B-Wettelijke_grondslag", "L10":"I-Wettelijke_grondslag",
}

def load_ner_model(model_dir):

    model_dir = Path(model_dir)

    tokenizer = AutoTokenizer.from_pretrained(
        model_dir
    )

    model = AutoModelForTokenClassification.from_pretrained(
        model_dir
    )

    model.eval()

    return model, tokenizer


def load_nerre_model(model_dir):

    model_dir = Path(model_dir)

    cfg = json.load(
        open(model_dir / "config.json")
    )

    tokenizer = AutoTokenizer.from_pretrained(
        model_dir
    )

    model = JointSpert(
        encoder_name=cfg["base_model_name_or_path"],
        num_entity_labels=cfg["num_entity_labels"],
        num_rel_labels=cfg["num_rel_labels"],
        max_span_width=cfg["max_span_width"],
        width_emb_dim=cfg["width_emb_dim"],
        dropout=cfg["dropout"],
    )

    model.load_state_dict(
        torch.load(
            model_dir / "model.pt",
            map_location="cpu"
        )
    )

    model.eval()

    return model, tokenizer, cfg