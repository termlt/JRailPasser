import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtGui import QIcon


def main(amount=None, typee=int):
    # Creating the plot
    if typee == 1:
        mpl.rcParams["toolbar"] = "None"
        plt.style.use("fivethirtyeight")

        result_7_s = amount * 279
        result_14_s = amount * 445
        result_21_s = amount * 570

        x = np.array([7, 14, 21])
        y = np.array([int(result_7_s), int(result_14_s), int(result_21_s)])

        fig, ax = plt.subplots(num="JRailPasser")

        plt.xticks(ticks=x, labels=x)
        plt.yticks(ticks=y, labels=y)
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.title(f"Prices for Standard for {amount} people", fontweight="bold")
        plt.tight_layout()
        ax.bar(x, y, width=1, color="#444444")
        ax.yaxis.set_major_formatter("{x}$")

        plt.get_current_fig_manager().window.setWindowIcon(QIcon("favicon.ico"))
        plt.show()
    if typee == 2:
        mpl.rcParams["toolbar"] = "None"
        plt.style.use("fivethirtyeight")

        result_7_fc = amount * 373
        result_14_fc = amount * 604
        result_21_fc = amount * 786

        x = np.array([7, 14, 21])
        y = np.array([int(result_7_fc), int(result_14_fc), int(result_21_fc)])

        fig, ax = plt.subplots(num="JRailPasser")

        plt.xticks(ticks=x, labels=x)
        plt.yticks(ticks=y, labels=y)
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.title(f"Prices for First Class for {amount} people", fontweight="bold")
        plt.tight_layout()
        ax.bar(x, y, width=1, color="#faa20a")
        ax.yaxis.set_major_formatter("{x}$")

        plt.get_current_fig_manager().window.setWindowIcon(QIcon("favicon.ico"))
        plt.show()
    if typee == 3:
        mpl.rcParams["toolbar"] = "None"
        plt.style.use("fivethirtyeight")

        result_7_s = amount * 279
        result_14_s = amount * 445
        result_21_s = amount * 570
        result_7_fc = amount * 373
        result_14_fc = amount * 604
        result_21_fc = amount * 786

        x = np.array([7, 14, 21])
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

        fig, ax = plt.subplots(num="JRailPasser")

        plt.xticks(ticks=x, labels=x)
        plt.yticks(ticks=y, labels=y)
        plt.title(f"Prices for {amount} people", fontweight="bold")
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.tight_layout()
        ax.bar(x - 0.5, y[:3], width=1, color="#444444", label="Standard")
        ax.bar(x + 0.5, y[3:], width=1, color="#faa20a", label="First Class")

        ax.yaxis.set_major_formatter("{x}$")
        plt.legend()

        for i in range(0, 3):
            plt.gca().get_yticklabels()[i].set_color("#444444")
        for i in range(3, 6):
            plt.gca().get_yticklabels()[i].set_color("#faa20a")
        plt.get_current_fig_manager().window.setWindowIcon(QIcon("favicon.ico"))
        plt.show()
