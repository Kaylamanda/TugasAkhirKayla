
"""
Modul untuk proses penyisipan metadata menggunakan
Least Significant Bit (LSB) pada koefisien DWT.

Alur:
String
    ↓
Binary
    ↓
Header 32-bit
    ↓
Capacity Check
    ↓
Scaling Koefisien DWT
    ↓
LSB Embedding
    ↓
Restore Koefisien DWT
"""

import numpy as np

#  Mengubah string menjadi deretan bit biner.
def string_to_binary(message):

    binary = "".join(
        format(ord(char), "08b")
        for char in message
    )

    return binary

#    Mengubah deretan bit menjadi string.
def binary_to_string(binary):

    chars = []

    for i in range(0, len(binary), 8):

        byte = binary[i:i + 8]

        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))

    return "".join(chars)

# Menambahkan header 32-bit yang berisi panjang pesan dalam satuan bit.
def add_length_header(binary_message):

    message_length = len(binary_message)

    header = format(message_length, "032b")

    return header + binary_message

# Mengubah string menjadi payload siap disisipkan (header + binary).
def prepare_payload(message):

    binary = string_to_binary(message)

    payload = add_length_header(binary)

    return payload

#Memeriksa apakah payload dapat disisipkan ke dalam subband.
def capacity_check(payload, subband):

    capacity = subband.size

    required = len(payload)

    if required > capacity:

        raise ValueError(
            f"Payload terlalu besar ({required} bit) "
            f"untuk kapasitas subband ({capacity} bit)."
        )

    return {
        "capacity": capacity,
        "required": required,
        "remaining": capacity - required
    }

#Mengubah koefisien DWT float menjadi integer menggunakan faktor skala.
def prepare_subband(subband, scale=1000):

    return np.round(
        subband * scale
    ).astype(np.int32)

#Mengembalikan koefisien integer menjadi float.
def restore_subband(subband_int, scale=1000):

    return (
        subband_int.astype(np.float64)
        / scale
    )

#Menyisipkan payload ke LSB koefisien subband.
def embed_lsb(subband, payload):

    embedded = subband.copy()

    flat = embedded.flatten()

    for i, bit in enumerate(payload):

        value = int(flat[i])

        # Bilangan positif
        if value >= 0:

            value = (
                (value & ~1)
                | int(bit)
            )

        # Bilangan negatif
        else:

            sign = -1

            value = abs(value)

            value = (
                (value & ~1)
                | int(bit)
            )

            value *= sign

        flat[i] = value

    embedded = flat.reshape(subband.shape)

    return embedded
