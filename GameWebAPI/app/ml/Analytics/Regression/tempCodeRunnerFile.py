# First split: train+temp and test 
# 0.7 train, 0.3 test+validation
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# Second split: validation and test
X_validation, X_test, y_validation, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) 
X_validation_scaled = scaler.transform(X_validation)
X_test_scaled = scaler.transform(X_test)