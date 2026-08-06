
from .embedding import (
    prepare_subband,
    binary_to_string
)

#Mengambil seluruh bit LSB dari subband.
def extract_lsb(subband):

    # Sama seperti proses embedding,
    # subband harus diubah menjadi integer terlebih dahulu.
    subband_int = prepare_subband(subband)

    flat = subband_int.flatten()

    binary_stream = "".join(
        str(abs(int(value)) & 1)
        for value in flat
    )

    return binary_stream

# Membaca header 32-bit untuk memperoleh panjang payload.
def read_length_header(binary_stream):
    
    if len(binary_stream) < 32:
        raise ValueError(
            "Binary stream lebih pendek dari header 32-bit."
        )

    header = binary_stream[:32]

    payload_length = int(header, 2)

    return payload_length

# Mengekstrak payload berdasarkan panjang yang tersimpan pada header.
def extract_payload(binary_stream):

    payload_length = read_length_header(binary_stream)

    end_index = 32 + payload_length

    if end_index > len(binary_stream):
        raise ValueError(
            "Binary stream tidak cukup panjang untuk payload."
        )

    payload = binary_stream[32:end_index]

    return payload

#Mengubah payload biner menjadi string.
def recover_message(payload):
    return binary_to_string(payload)

#Fungsi utama untuk mengekstrak metadata dari subband hasil embedding.
def extract_metadata(subband):

    binary_stream = extract_lsb(subband)

    payload = extract_payload(binary_stream)

    metadata = recover_message(payload)

    return metadata
