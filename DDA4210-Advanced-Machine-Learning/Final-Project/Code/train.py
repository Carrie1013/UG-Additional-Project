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


def training(train_dataloader,model,criterion,optimizer,scheduler):
    tr_loss = 0
    pbar = tqdm(total=len(train_dataloader))
    model.train()

    for step, data in enumerate(train_dataloader,1):
        optimizer.zero_grad()
        ids = data["ids"].cuda()
        mask = data["mask"].cuda()
        target = data["targets"].type(torch.LongTensor).cuda()
        token_type_ids = data['token_type_ids'].cuda()
        outputs = model(ids, mask, token_type_ids)
        loss = criterion(outputs.logits, target)    
        loss.backward()
        optimizer.step()
        scheduler.step()
        tr_loss += loss.item()
        avg_loss = tr_loss / step
    # Update the progress bar
        pbar.set_description(f"avg_loss: {avg_loss:.4f}")
        pbar.update(1)
    pbar.close()
    # Return the average loss over the entire dataset
    return tr_loss / len(train_dataloader)


def validation(val_dataloader,model):
    val_loss = 0
    pbar = tqdm(total=len(val_dataloader))
    model.eval()
    true_labels = []
    predicted_labels = []

    with torch.no_grad():
        for step, data in enumerate(val_dataloader,1):
            ids = data["ids"].cuda()
            mask = data["mask"].cuda()
            target = data["targets"].cuda()
            token_type_ids = data['token_type_ids'].cuda()
            outputs = model(ids, mask, token_type_ids)
            true_labels.extend(target.cpu())
            predicted_labels.extend(torch.argmax(outputs.logits, dim=1).cpu())
        
    report = classification_report(true_labels, predicted_labels, digits=4)

    return (report,
            torch.sum(torch.tensor(true_labels) == torch.tensor(predicted_labels))
            / len(true_labels),
        )
    
# obtain the tokenizer and the model
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
model = RobertaForSequenceClassification.from_pretrained("roberta-base")

#set the batch and load data
batch_size = 32
data_train = pd.read_csv("IMDB_dataset/Train.csv")
data_val = pd.read_csv("IMDB_dataset/Valid.csv")

train_dataloader = get_dataloader(data_train,tokenizer,batch_size)
val_dataloader = get_dataloader(data_val,tokenizer,batch_size)

#put model to cuda
device = 'cuda:0'
model.to(device)
# train
max_epoch = 10
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
scheduler = get_linear_schedule_with_warmup(
            optimizer,
            num_warmup_steps=int(0.1 * len(train_dataloader) / batch_size),
            num_training_steps=len(train_dataloader)
            * max_epoch
            // batch_size,
        )
criterion = torch.nn.CrossEntropyLoss()

best_accuracy = 0
for epoch in range(max_epoch):
    train_loss = training(train_dataloader,model,criterion,optimizer,scheduler)
    val_report, val_accuracy = validation(val_dataloader,model)
    if val_accuracy > best_accuracy:
        best_accuracy = val_accuracy
        torch.save(model.state_dict(), "best_model.pt")
    # Print the epoch number, training loss, and validation accuracy
    print(
        f"Epoch {epoch + 1}, train loss: {train_loss:.4f}, val accuracy: {val_accuracy:.4f}"
    )
    # Print the classification report for the validation dataset
    print(val_report)