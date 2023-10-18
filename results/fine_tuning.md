### Fine-tuning experiments

#### Name: fine_tuned_tiny_bert

- pre-processing
    - max_length=384
    - stride=128

- post-processing
    - n_best=32
    - max_answer_length=128

- hyperparameters
    - batch_size=8
    - learning_rate=2e-5
    - num_train_epochs=3

- results
    - training time: 9min 50s
    - epoch 0: {'exact_match': 25.21286660359508, 'f1': 36.957914483680405}
    - epoch 1: {'exact_match': 29.829706717123937, 'f1': 41.99564183612771}
    - epoch 2: {'exact_match': 32.03405865657521, 'f1': 44.172691480744795}
