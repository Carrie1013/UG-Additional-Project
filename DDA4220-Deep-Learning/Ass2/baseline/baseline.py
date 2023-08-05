import torch
import pandas as pd
import numpy as np
from torch import nn
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader, Dataset
from torchtext.data import get_tokenizer
from torchtext.vocab import GloVe

GLOVE_DIM = 100
GLOVE = GloVe(name='6B', dim=GLOVE_DIM)

train = pd.read_csv("./nlp-getting-started/train.csv").values.tolist()
test = pd.read_csv("./nlp-getting-started/test.csv").values.tolist()
split = 0.7*len(train)
train_data = train[:int(split)]
val_data = train[int(split):]

class twitterDataset(Dataset):
    def __init__(self, data):
        super().__init__()
        self.tokenizer = get_tokenizer("basic_english")
        self.data = data
        self.length = len(data)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        sentence = self.tokenizer(self.data[index][3])
        x = GLOVE.get_vecs_by_tokens(sentence)
        label = int(self.data[index][4])
        return x, label

def get_dataloader():
    def collate_fn(batch):
        x, y = zip(*batch)
        x_pad = pad_sequence(x, batch_first=True)
        y = torch.Tensor(y)
        return x_pad, y
    
    train_dataloader = DataLoader(twitterDataset(train_data),
                    batch_size=32,
                    shuffle=True,
                    collate_fn=collate_fn)
    val_dataloader = DataLoader(twitterDataset(val_data),
                    batch_size=32,
                    shuffle=True,
                    collate_fn=collate_fn)
    test_dataloader = DataLoader(twitterDataset(test),
                    batch_size = 32, 
                    shuffle=False,
                    collate_fn=collate_fn)

    return train_dataloader, val_dataloader, test_dataloader

class RNN(torch.nn.Module):
    def __init__(self, hidden_units=64, dropout_rate=0.5):
        super().__init__()
        self.drop = nn.Dropout(dropout_rate)
        self.rnn = nn.GRU(GLOVE_DIM, hidden_units, 1, batch_first=True)
        self.linear = nn.Linear(hidden_units, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x: torch.Tensor):
        emb = self.drop(x)
        output, _ = self.rnn(emb)
        output = output[:, -1]
        output = self.linear(output)
        output = self.sigmoid(output)
        return output

device = 'cpu'
train_dataloader, val_dataloader, test_dataloader = get_dataloader()
model = RNN().to(device)

# trian process
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
citerion = torch.nn.BCELoss()
for epoch in range(10):
    loss_sum = 0
    dataset_len = len(train_dataloader.dataset)

    for x, y in train_dataloader:
        batchsize = y.shape[0]
        x = x.to(device)
        y = y.to(device)
        hat_y = model(x)
        hat_y = hat_y.squeeze(-1)
        loss = citerion(hat_y, y)

        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 0.5)
        optimizer.step()
        loss_sum += loss * batchsize

    print(f'Epoch {epoch}. loss: {loss_sum / dataset_len}')

torch.save(model.state_dict(), 'rnn.pth')

# validation process
accuracy = 0
dataset_len = len(val_dataloader.dataset)
model.eval()
for x, y in val_dataloader:
    x = x.to(device)
    y = y.to(device)
    with torch.no_grad():
        hat_y = model(x)
    hat_y.squeeze_(1)
    predictions = torch.where(hat_y > 0.5, 1, 0)
    score = torch.sum(torch.where(predictions == y, 1, 0))
    accuracy += score.item()
accuracy /= dataset_len

print(f'Validation Accuracy: {accuracy}')