from Dataset import IMDBDataset
from Dataset import get_dataloader
import torch
from transformers import (
    RobertaForSequenceClassification,
    RobertaTokenizer,
    get_linear_schedule_with_warmup,
)
from torch import nn
from sklearn.metrics import classification_report
from tqdm import tqdm
import pandas as pd
import numpy as np

def load_model(path):
    tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
    model = RobertaForSequenceClassification.from_pretrained("roberta-base")
    model.load_state_dict(torch.load(path))
    return tokenizer,model

def tokenize_text(tokenizer, input_text, max_length):
    # Tokenize the input text using the tokenizer
    inputs = tokenizer.encode_plus(
        input_text,
        add_special_tokens=True,
        return_tensors="pt",
        max_length=max_length,
        truncation=True,
    )
    # Get the input_ids and attention_mask tensors
    return inputs["input_ids"].cuda(), inputs["attention_mask"].cuda()

def predict(text, model, tokenizer,max_length):
    input_ids, attention_mask = tokenize_text(tokenizer, text, max_length)
    outputs = model(input_ids,attention_mask)
    prediction = np.argmax(outputs.logits.detach().cpu().numpy())
    return prediction

def main():
    model_path = "best_model.pt"
    test_data_path = "IMDB_dataset/Test.csv"
    tokenizer,model = load_model(model_path)
    model.cuda()
    test_data = pd.read_csv(test_data_path)
    predictions = []
    labels = list(test_data["label"])
    for i in range(len(test_data)):
        text = test_data.loc[i,"text"]
        prediction = predict(text, model, tokenizer, max_length = 512)
        predictions.append(prediction)

    report = classification_report(labels, predictions, digits=4)
    print(report)

if __name__ == "__main__":
    main()
