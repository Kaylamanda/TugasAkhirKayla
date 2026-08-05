
from energy import calculate_energy


def compare_subband_energy(LH, HL):
  
    energy_lh = calculate_energy(LH)
    energy_hl = calculate_energy(HL)

    return energy_lh, energy_hl


def select_adaptive_subband(LH, HL):
  
    energy_lh, energy_hl = compare_subband_energy(LH, HL)

    if energy_lh > energy_hl:

        return "LH", LH

    else:

        return "HL", HL


def get_selected_energy(LH, HL):

    energy_lh, energy_hl = compare_subband_energy(LH, HL)

    if energy_lh > energy_hl:

        return "LH", energy_lh

    else:

        return "HL", energy_hl


def adaptive_information(LH, HL):

    energy_lh, energy_hl = compare_subband_energy(LH, HL)

    print("=" * 45)
    print("ADAPTIVE SUBBAND SELECTION")
    print("=" * 45)

    print(f"Energi LH : {energy_lh:.2f}")
    print(f"Energi HL : {energy_hl:.2f}")

    if energy_lh > energy_hl:

        print("\nSubband Terpilih : LH")

    else:

        print("\nSubband Terpilih : HL")
