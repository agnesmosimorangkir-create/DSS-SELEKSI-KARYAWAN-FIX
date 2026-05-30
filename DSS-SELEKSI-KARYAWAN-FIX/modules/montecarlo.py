
import numpy as np
import pandas as pd

def run_monte_carlo(df, n_simulation=1000):

    winners = []

    for _ in range(n_simulation):

        probs = np.random.dirichlet([3, 4, 3])

        ev_sim = (
            df["Payoff_S1"] * probs[0]
            + df["Payoff_S2"] * probs[1]
            + df["Payoff_S3"] * probs[2]
        )

        winner = df.loc[ev_sim.idxmax(), "ID_Kandidat"]
        winners.append(winner)

    result = pd.Series(winners).value_counts().reset_index()
    result.columns = ["ID_Kandidat", "Jumlah_Menang"]
    result["Persentase"] = result["Jumlah_Menang"] / n_simulation * 100

    return result
