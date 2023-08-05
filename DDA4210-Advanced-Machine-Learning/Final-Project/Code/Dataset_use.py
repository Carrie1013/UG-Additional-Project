from Dataset import IMDBDataset
from Dataset import get_dataloader
from transformers import BertTokenizer, BertModel
import pandas as pd


#device = 'cuda:0'
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
batch_size = 16
data_train = pd.read_csv("IMDB_dataset/Train.csv")
data_val = pd.read_csv("IMDB_dataset/Valid.csv")
train_dataloader = get_dataloader(data_train,tokenizer,batch_size)
test_dataloader = get_dataloader(data_val,tokenizer,batch_size)
for data in train_dataloader:
    # data contains: ids, mask, token_type_ids, targets(labels)
    print("input_ids:")
    print(data["ids"])



