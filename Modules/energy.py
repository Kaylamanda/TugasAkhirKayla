
import numpy as np
import pandas as pd

#  Menghitung energi suatu subband
def calculate_energy(subband):
    return np.sum(np.square(subband))


def calculate_all_energies(LL, LH, HL, HH):
    energies = {
        "LL": calculate_energy(LL),
        "LH": calculate_energy(LH),
        "HL": calculate_energy(HL),
        "HH": calculate_energy(HH),
    }

    return energies


def print_energies(energies):
    print("=" * 40)
    print("SUBBAND ENERGIES")
    print("=" * 40)

    for key, value in energies.items():
        print(f"{key} : {value:.2f}")


def energy_dataframe(energies):
    return pd.DataFrame(
        energies.items(),
        columns=["Subband", "Energy"]
    )


def highest_energy_subband(energies):
    return max(energies, key=energies.get)


def lowest_energy_subband(energies):
    return min(energies, key=energies.get)
