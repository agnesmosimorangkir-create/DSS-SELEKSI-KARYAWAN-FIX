
def calculate_uncertainty(df):

    df["Maximax"] = df[["Payoff_S1","Payoff_S2","Payoff_S3"]].max(axis=1)
    df["Maximin"] = df[["Payoff_S1","Payoff_S2","Payoff_S3"]].min(axis=1)
    df["Laplace"] = (df["Payoff_S1"] + df["Payoff_S2"] + df["Payoff_S3"]) / 3

    alpha = 0.6
    df["Hurwicz"] = alpha * df["Maximax"] + (1 - alpha) * df["Maximin"]

    return df
