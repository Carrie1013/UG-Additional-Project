from torch.utils.data import DataLoader, Dataset
import torch
import pandas as pd


class IMDBDataset(Dataset):
    def __init__(self,data,tokenizer,max_len):
        super().__init__()
        self.tokenizer = tokenizer
        self.max_len = max_len
        self.data = data
        self.texts = data["text"]
        self.labels = data["label"]
        
    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        label = self.labels[index]
        inputs = self.tokenizer.encode_plus(
            self.texts[index],
            None,
            add_special_tokens=True,
            max_length=self.max_len,
            pad_to_max_length=True,
            return_token_type_ids=True
        )
        ids = inputs['input_ids']
        mask = inputs['attention_mask']
        token_type_ids = inputs["token_type_ids"]


        return {
            'ids': torch.tensor(ids, dtype=torch.long),
            'mask': torch.tensor(mask, dtype=torch.long),
            'token_type_ids': torch.tensor(token_type_ids, dtype=torch.long),
            'targets': torch.tensor(label, dtype=torch.float)
        }


def get_dataloader(data,tokenizer,batch_size):
    dataloader = DataLoader(IMDBDataset(data,tokenizer,512),
                    batch_size=batch_size,
                    shuffle=True)
    return dataloader