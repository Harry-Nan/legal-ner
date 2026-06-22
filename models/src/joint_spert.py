import torch
import torch.nn as nn
from transformers import AutoModel


class JointSpert(nn.Module):
    def __init__(
        self,
        encoder_name,
        num_entity_labels,
        num_rel_labels,
        max_span_width=24,
        width_emb_dim=16,
        dropout=0.2,
    ):
        super().__init__()

        self.enc = AutoModel.from_pretrained(
            encoder_name
        )

        h = self.enc.config.hidden_size

        self.width_embeddings = nn.Embedding(
            max_span_width,
            width_emb_dim,
        )

        self.ent_mlp = nn.Sequential(
            nn.Linear(2 * h + width_emb_dim, h),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(h, num_entity_labels)
        )

        self.rel_mlp = nn.Sequential(
            nn.Linear(3 * h, h),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(h, num_rel_labels)
        )

    def _span_repr(self, hidden, span_sub_ix):
        reps = []
        H = hidden.size(-1)

        for (si, ei) in span_sub_ix:

            if si is None or ei is None:
                reps.append(
                    torch.zeros(
                        2 * H + self.width_embeddings.embedding_dim,
                        device=hidden.device
                    )
                )
                continue

            hs = hidden[0, si]
            he = hidden[0, ei]

            width = (
                torch.tensor(
                    min(
                        max(ei - si + 1, 1),
                        self.width_embeddings.num_embeddings
                    ),
                    device=hidden.device
                ) - 1
            )

            wemb = self.width_embeddings(width)

            reps.append(
                torch.cat([hs, he, wemb], dim=-1)
            )

        if len(reps) == 0:
            return torch.zeros(
                0,
                2 * H + self.width_embeddings.embedding_dim,
                device=hidden.device
            )

        return torch.stack(reps, dim=0)

    def forward(
        self,
        input_ids,
        attention_mask,
        token_type_ids=None,
        span_sub_ix=None,
        pair_sub_ix=None,
        entity_labels=None,
        pair_labels=None,
        return_hidden=False,
    ):
        out = self.enc(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
        )

        hidden = out.last_hidden_state

        span_repr = self._span_repr(
            hidden,
            span_sub_ix or []
        )

        ent_logits = (
            self.ent_mlp(span_repr)
            if span_repr.numel()
            else torch.zeros(
                0,
                self.ent_mlp[-1].out_features,
                device=hidden.device
            )
        )

        return {
            "ent_logits": ent_logits
        }