import train
dim = 1024
eps = 0
dim_word = 300
norm = 2

for method, margin, abs in [('cosine', 0.2, False), ('hierarchy', 0.05, True)]:
    for captions in ['processed', 'raw']:
        for cnn in ['relu', 'relu_oversample']:
            name = '_'.join([method, captions, cnn])
            train.trainer(data='f30k', margin=margin, saveto='snapshots/' + name + '.npz', batch_size=128, lrate=0.001, eps=eps, dim_word=dim_word, dim=dim, max_epochs=80, validFreq=300, name=name, norm=norm, abs=abs, cnn=cnn, method=method, captions=captions, diagonal_weight=2)
