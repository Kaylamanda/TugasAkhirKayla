
import numpy as np

from skimage.metrics import (
    peak_signal_noise_ratio,
    structural_similarity
)

#Menghitung Mean Squared Error (MSE)
def calculate_mse(original, stego):
   
    original = original.astype(np.float64)
    stego = stego.astype(np.float64)

    mse = np.mean((original - stego) ** 2)

    return mse

#Menghitung Peak Signal-to-Noise Ratio (PSNR).
def calculate_psnr(original, stego):

    psnr = peak_signal_noise_ratio(
        original,
        stego,
        data_range=255
    )

    return psnr

# Menghitung Structural Similarity Index (SSIM).
def calculate_ssim(original, stego):

    ssim = structural_similarity(
        original,
        stego,
        data_range=255
    )

    return ssim

# Menghitung Bit Error Rate (BER).
def calculate_ber(original_binary, extracted_binary):

    if len(original_binary) != len(extracted_binary):

        raise ValueError(
            "Panjang data biner tidak sama."
        )

    total_bits = len(original_binary)

    error_bits = sum(
        bit1 != bit2
        for bit1, bit2 in zip(
            original_binary,
            extracted_binary
        )
    )

    ber = error_bits / total_bits

    return ber


def evaluation_report(
    original_image,
    stego_image,
    original_binary=None,
    extracted_binary=None
):

    report = {}

    report["MSE"] = calculate_mse(
        original_image,
        stego_image
    )

    report["PSNR"] = calculate_psnr(
        original_image,
        stego_image
    )

    report["SSIM"] = calculate_ssim(
        original_image,
        stego_image
    )

    if (
        original_binary is not None
        and extracted_binary is not None
    ):

        report["BER"] = calculate_ber(
            original_binary,
            extracted_binary
        )

    return report


def print_report(report):
    """
    Menampilkan hasil evaluasi.
    """

    print("=" * 40)
    print("IMAGE QUALITY EVALUATION")
    print("=" * 40)

    for key, value in report.items():

        print(f"{key:<6}: {value:.6f}")
