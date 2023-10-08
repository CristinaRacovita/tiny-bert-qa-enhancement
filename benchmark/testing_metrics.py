from sklearn.metrics import f1_score, accuracy_score
from sklearn.model_selection import cross_val_score

def compute_evaluation_metrics(y_true, y_predicted):
    # Returns F1 and Exact Match Metrics
    return f1_score(y_true, y_predicted, average="micro"), accuracy_score(
        y_true, y_predicted
    )

def cross_validation(model, x, y, k):
    scores = cross_val_score(model, x, y, cv=k)
    print(f"{scores.mean()} accuracy with a standard deviation of {scores.std()}")

    return scores
