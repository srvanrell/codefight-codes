def featureSelection1(Dataset, Labels, FeatureNames):
    n_examples = len(Dataset)
    n_features = len(FeatureNames)

    for feat in range(n_features):
        
