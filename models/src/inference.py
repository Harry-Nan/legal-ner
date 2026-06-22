import torch
from transformers import pipeline

def predict_ner_entities(
    text,
    model,
    tokenizer,
    label_map=None
):

    ner_pipe = pipeline(
        "token-classification",
        model=model,
        tokenizer=tokenizer,
        aggregation_strategy="first"
    )

    preds = ner_pipe(text)

    if label_map:

        for p in preds:
            p["entity_group"] = label_map.get(
                p["entity_group"],
                p["entity_group"]
            )

    merged = []
    current = None

    for ent in preds:

        tag = ent["entity_group"]

        if tag.startswith("B-"):

            if current:
                merged.append(current)

            current = {
                "label": tag[2:],
                "text": ent["word"],
                "score": float(ent["score"])
            }

        elif tag.startswith("I-") and current:

            current["text"] += " " + ent["word"]

            current["score"] = max(
                current["score"],
                float(ent["score"])
            )

    if current:
        merged.append(current)

    return merged

def word_to_subword_bounds(
    tokenizer,
    words,
    max_length=256
):
    enc = tokenizer(
        words,
        is_split_into_words=True,
        return_tensors="pt",
        truncation=True,
        max_length=max_length
    )

    word_ids = enc.word_ids(0)

    first = {}
    last = {}

    for i, w in enumerate(word_ids):

        if w is None:
            continue

        if w not in first:
            first[w] = i

        last[w] = i

    return enc, first, last


def generate_candidate_spans(
    words,
    first,
    last,
    max_span_width=24
):
    candidates = []

    for s in range(len(words)):

        for e in range(
            s + 1,
            min(len(words), s + max_span_width) + 1
        ):

            si = first.get(s)
            ei = last.get(e - 1)

            if si is None or ei is None:
                continue

            candidates.append(
                {
                    "word_span": (s, e),
                    "subword_span": (si, ei)
                }
            )

    return candidates


def predict_entities(
    text,
    model,
    tokenizer,
    cfg,
    threshold=0.95
):

    id2label = {
        int(k): v
        for k, v in cfg["id2label"].items()
    }

    words = text.split()

    enc, first, last = word_to_subword_bounds(
        tokenizer,
        words
    )

    candidates = generate_candidate_spans(
        words,
        first,
        last,
        max_span_width=cfg["max_span_width"]
    )

    span_sub_ix = [
        c["subword_span"]
        for c in candidates
    ]

    with torch.no_grad():

        out = model(
            input_ids=enc["input_ids"],
            attention_mask=enc["attention_mask"],
            span_sub_ix=span_sub_ix
        )

    probs = torch.softmax(
        out["ent_logits"],
        dim=-1
    )

    results = []

    for cand, prob in zip(
        candidates,
        probs
    ):

        label_id = int(prob.argmax())
        score = float(prob.max())

        label = id2label[label_id]

        if label == "O":
            continue

        if score < threshold:
            continue

        s, e = cand["word_span"]

        results.append(
            {
                "label": label,
                "text": " ".join(words[s:e]),
                "score": score,
                "span": (s, e)
            }
        )

    return sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )