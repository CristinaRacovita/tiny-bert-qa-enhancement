### Fine-tuning experiments

#### Name: fine_tuned_tiny_bert

- pre-processing
    - max_length=384
    - stride=128

- post-processing
    - n_best=20
    - max_answer_length=30

- hyperparameters
    - batch_size=8
    - learning_rate=2e-5
    - num_train_epochs=3

- results
    - training time: 4h 16min
    - epoch 0: {'exact_match': 26.3197729422895, 'f1': 38.04366149964173}
    - epoch 1: {'exact_match': 29.858088930936614, 'f1': 41.80600115478611}
    - epoch 2: {'exact_match': 31.09744560075686, 'f1': 43.15172932323862}
