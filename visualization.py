
import matplotlib.pyplot as plt
import database


def show_bmi_graph():
    records = database.get_records()

    if not records:
        print("No BMI records available to display.")
        return

    # Extract names and BMI values
    names = [record[1] for record in records]
    bmi_values = [record[4] for record in records]

    # Create BMI graph
    plt.figure(figsize=(10, 5))

    plt.plot(
        range(len(bmi_values)),
        bmi_values,
        marker="o",
        linewidth=2
    )

    plt.xticks(
        range(len(names)),
        names,
        rotation=45
    )

    plt.xlabel("Name")
    plt.ylabel("BMI Value")
    plt.title("BMI History Visualization")

    plt.axhline(y=18.5, linestyle="--", label="Underweight Limit")
    plt.axhline(y=25, linestyle="--", label="Normal Limit")
    plt.axhline(y=30, linestyle="--", label="Overweight Limit")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    show_bmi_graph()
