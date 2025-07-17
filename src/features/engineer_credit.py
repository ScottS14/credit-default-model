

def engineer_credit(app_train, app_test):
    
    
    return app_train, app_test


if __name__ == "__main__":
    import pandas as pd

    app_train = pd.read_csv('../data/raw/application_train.csv')
    app_test = pd.read_csv('../data/raw/application_test.csv')

    print(f"Shape of application train dataset: {app_train.shape}")
    print(f"Shape of application test dataset: {app_test.shape}")

    app_train, app_test = engineer_credit(app_train, app_test)