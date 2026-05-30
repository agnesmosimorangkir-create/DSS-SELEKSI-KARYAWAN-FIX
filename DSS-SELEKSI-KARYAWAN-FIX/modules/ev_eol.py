
def calculate_ev_eol(df):

    p_s1 = 0.30
    p_s2 = 0.40
    p_s3 = 0.30

    df["EV"] = (
        df["Payoff_S1"] * p_s1
        + df["Payoff_S2"] * p_s2
        + df["Payoff_S3"] * p_s3
    )

    df["Rank_EV"] = df["EV"].rank(ascending=False, method="dense")

    ev_max = df["EV"].max()
    df["EOL"] = ev_max - df["EV"]

    return df
