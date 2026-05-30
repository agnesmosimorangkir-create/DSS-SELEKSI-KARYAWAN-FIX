
import numpy as np

def calculate_utility(df):

    df["Utility_S1"] = np.sqrt(df["Payoff_S1"])
    df["Utility_S2"] = np.sqrt(df["Payoff_S2"])
    df["Utility_S3"] = np.sqrt(df["Payoff_S3"])

    p_s1 = 0.30
    p_s2 = 0.40
    p_s3 = 0.30

    df["Expected_Utility"] = (
        df["Utility_S1"] * p_s1
        + df["Utility_S2"] * p_s2
        + df["Utility_S3"] * p_s3
    )

    return df
