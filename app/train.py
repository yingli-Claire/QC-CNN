import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import time
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
import os

def train_network(net = None, train_set = None, val_set = None, device = None, 
epochs = 10, bs = 20, optimizer = None, criterion = None):

    train_loader = DataLoader(train_set, batch_size=bs, shuffle=True)
    val_loader = DataLoader(val_set, batch_size=bs, shuffle=True)

    net = net.to(device)

    for epoch in range(epochs):
        t1 = time.time()
        net.train()
        tr_loss = 0

        y_trues = []
        y_preds = []

        for i, sampled_batch in enumerate(train_loader):

            data = sampled_batch['feature']
            y = sampled_batch['label'].squeeze()

            data = data.type(torch.FloatTensor)
            y = y.type(torch.LongTensor)

            data = data.to(device)
            y = y.to(device)

            optimizer.zero_grad()
            output = net(data)
            loss = criterion(output,y)
            loss.backward()
            optimizer.step()
            
            tr_loss = loss.data.cpu().numpy()

            y_trues += y.cpu().numpy().tolist()
            y_preds += output.data.cpu().numpy().argmax(axis=1).tolist()

        tr_acc = accuracy_score(y_trues, y_preds)
        tr_loss = tr_loss/(i+1)
        cnf_tr = confusion_matrix(y_trues, y_preds)

        net.eval()
        val_loss = 0

        y_trues = []
        y_preds = []

        for i, sampled_batch in enumerate(val_loader):
            data = sampled_batch['feature']
            y = sampled_batch['label'].squeeze()

            data = data.type(torch.FloatTensor)
            y = y.type(torch.LongTensor)

            data = data.to(device)
            y = y.to(device)

            with torch.no_grad():
                output = net(data)

            loss = criterion(output,y)
            val_loss = val_loss + loss.data.cpu().numpy()

            y_trues += y.cpu().numpy().tolist()
            y_preds += output.data.cpu().numpy().argmax(axis=1).tolist()

        val_acc = accuracy_score(y_trues, y_preds)
        val_loss = val_loss/(i+1)
        cnf_val = confusion_matrix(y_trues, y_preds)

        print('Time:{:.4f}, Epoch:{}, TR_Loss: {:.4f}, TR_Acc: {:.4f}, VAL_Loss: {:.4f}, VAL_Acc: {:.4f}'.format(time.time()-t1, epoch, tr_loss, tr_acc, val_loss, val_acc))
        #print(torch.cat((torch.tensor(cnf_tr), torch.tensor(cnf_val)), dim=1))
        
    


    # torch.save(net.state_dict(), outdir + '/' + file_prefix + '_model')
    # np.save(outdir + '/' + file_prefix + '_training_loss.npy', tr_losses)
    # np.save(outdir + '/' + file_prefix + '_validation_loss.npy', val_losses)
    # np.save(outdir + '/' + file_prefix + '_training_accuracy.npy', tr_accs)
    # np.save(outdir + '/' + file_prefix + '_validation_accuracy.npy', val_accs)
