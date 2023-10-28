### Fine-tuning experiments

#### Name: fine_tuned_tiny_bert_8_2e-05 - baseline model

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

#### Name: fine_tuned_tiny_bert_pos_after - best model

- pre-processing
    - max_length=384
    - stride=128
- post-processing
    - n_best=32
    - max_answer_length=128

- hyperparameters
    - batch_size=8
    - learning_rate=0.0003
    - num_train_epochs=3

- results when pos tags were not added to the vocab
    - training time: 9min 50s
    - epoch 0: {'exact_match': 32.8287606433301, 'f1': 46.0489131858411}
    - epoch 1: {'exact_match': 37.4361400189214, 'f1': 51.114421969191}
    - epoch 2: {'exact_match': 39.1579943235572, 'f1': 52.5000254240588}

- results when pos tags were added as new tokens to the vocab
    - epoch 0: {'exact_match': 30.87038789025544, 'f1': 43.58574141571618}
    - epoch 1: {'exact_match': 34.91958372753075, 'f1': 48.854862771354234}
    - epoch 2: {'exact_match': 36.98202459791864, 'f1': 50.547132347328464}

- results when pos tags were added as new special tokens to the vocab
    - epoch 0: {'exact_match': 31.608325449385053, 'f1': 44.25390123627761}
    - epoch 1: {'exact_match': 36.707663197729424, 'f1': 49.93520420906771}
    - epoch 2: {'exact_match': 38.72280037842952, 'f1': 51.816550386903074}
