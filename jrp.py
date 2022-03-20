import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

s_7_days = 279
s_14_days = 445
s_21_days = 570

fc_7_days = 373
fc_14_days = 604
fc_21_days = 786


def main():
    # Passengers amount
    while True:
        try:
            amount = int(
                input(
                    """The Japan Rail Pass
Enter passengers amount: """
                )
            )
        except:
            print()
            continue
        else:
            print()
            break
    # Type of the ticket
    while True:
        try:
            typee = int(
                input(
                    """Please choose between 
1. Standard 
2. First class
3. Get both
"""
                )
            )
        except:
            print()
            continue
        else:
            print()
            break
    # Creating the plot
    if typee == 1:
        mpl.rcParams["toolbar"] = "None"
        plt.style.use("fivethirtyeight")

        result_7_s = amount * s_7_days
        result_14_s = amount * s_14_days
        result_21_s = amount * s_21_days
        y = np.array([int(result_7_s), int(result_14_s), int(result_21_s)])

        fig, ax = plt.subplots(num="Japan Rail Pass")
        x = np.array([7, 14, 21])
        plt.xticks(ticks=x, labels=x)
        plt.yticks(ticks=y, labels=y)
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.title(f"Prices for Standard for {amount} people", fontweight="bold")
        plt.tight_layout()
        ax.bar(x, y, width=1, color="#444444")
        ax.yaxis.set_major_formatter("{x}$")

        plt.savefig("result.png")
        print("Done.")
        plt.show()
    if typee == 2:
        mpl.rcParams["toolbar"] = "None"
        plt.style.use("fivethirtyeight")

        result_7_fc = amount * fc_7_days
        result_14_fc = amount * fc_14_days
        result_21_fc = amount * fc_21_days
        y = np.array([int(result_7_fc), int(result_14_fc), int(result_21_fc)])

        fig, ax = plt.subplots(num="Japan Rail Pass")
        x = np.array([7, 14, 21])
        plt.xticks(ticks=x, labels=x)
        plt.yticks(ticks=y, labels=y)
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.title(f"Prices for First Class for {amount} people", fontweight="bold")
        plt.tight_layout()
        ax.bar(x, y, width=1, color="#e5ae38")
        ax.yaxis.set_major_formatter("{x}$")

        plt.savefig("result.png")
        print("Done.")
        plt.show()
    if typee == 3:
        mpl.rcParams["toolbar"] = "None"
        plt.style.use("fivethirtyeight")

        result_7_s = amount * s_7_days
        result_14_s = amount * s_14_days
        result_21_s = amount * s_21_days
        result_7_fc = amount * fc_7_days
        result_14_fc = amount * fc_14_days
        result_21_fc = amount * fc_21_days
        y = np.array(
            [
                int(result_7_s),
                int(result_14_s),
                int(result_21_s),
                int(result_7_fc),
                int(result_14_fc),
                int(result_21_fc),
            ]
        )

        fig, ax = plt.subplots(num="Japan Rail Pass")
        x = np.array([7, 14, 21])
        plt.xticks(ticks=x, labels=x)
        plt.yticks(ticks=y, labels=y)
        plt.title(f"Prices for {amount} people", fontweight="bold")
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.tight_layout()
        ax.bar(x - 0.5, y[:3], width=1, color="#444444", label="Standard")
        ax.bar(x + 0.5, y[3:], width=1, color="#e5ae38", label="First Class")

        ax.yaxis.set_major_formatter("{x}$")
        plt.legend()

        for i in range(0, 3):
            plt.gca().get_yticklabels()[i].set_color("#444444")
        for i in range(3, 6):
            plt.gca().get_yticklabels()[i].set_color("#e5ae38")
        plt.savefig("result.png")
        print("Done.")
        plt.show()


if __name__ == "__main__":
    main()