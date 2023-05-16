import numpy as np
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def knn_cross_val_fit(X, y, min_k=1, max_k=50, cv=5):
    """
    Automatically find the best K with cross validation, fit a KNN classifier, and test it.

    Parameters:
    X : array-like, shape (n_samples, n_features)
        Training data.
    y : array-like, shape (n_samples,)
        Target values.
    min_k : int, optional (default=1)
        Minimum number of neighbors to test.
    max_k : int, optional (default=50)
        Maximum number of neighbors to test.
    cv : int, optional (default=5)
        Number of cross-validation folds.

    Returns:
    knn : KNeighborsClassifier
        The KNN classifier with the best K value.
    """
    # Split the dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Prepare the grid search parameters
    param_grid = {'n_neighbors': np.arange(min_k, max_k + 1)}

    # Create KNN classifier
    knn = KNeighborsClassifier()

    # Perform grid search with cross-validation
    grid_search = GridSearchCV(knn, param_grid, cv=cv, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    # Get the best K value
    best_k = grid_search.best_params_['n_neighbors']
    print(f"Best K value: {best_k}")

    # Train the KNN classifier with the best K value
    knn_best = KNeighborsClassifier(n_neighbors=best_k)
    knn_best.fit(X_train, y_train)

    # Test the KNN classifier
    y_pred = knn_best.predict(X_test)
    print("Accuracy score:", accuracy_score(y_test, y_pred))
    print("\nClassification report:\n", classification_report(y_test, y_pred))
    print("\nConfusion matrix:\n", confusion_matrix(y_test, y_pred))

    return knn_best