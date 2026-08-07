
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def show_image(image, title="Image", cmap="gray", figsize=(6, 6)):

    plt.figure(figsize=figsize)
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.show()


def show_difference(original, stego, figsize=(6, 6)):

    difference = np.abs(
        original.astype(np.float64)
        - stego.astype(np.float64)
    )

    plt.figure(figsize=figsize)
    plt.imshow(difference, cmap="gray", min=0, vmax=1)
    plt.title("Difference Image")
    plt.axis("off")
    plt.show()

    return difference


def print_metadata(metadata):
    
    print("=" * 40)
    print("METADATA")
    print("=" * 40)
    print(metadata)
    print("=" * 40)


def save_image(image, filename, output_path):

    os.makedirs(output_path, exist_ok=True)

    filepath = os.path.join(
        output_path,
        filename
    )

    plt.imsave(
        filepath,
        image,
        cmap="gray"
    )

    return filepath


def save_metrics(report, filename, output_path):

    os.makedirs(output_path, exist_ok=True)

    filepath = os.path.join(
        output_path,
        filename
    )

    df = pd.DataFrame([report])

    df.to_csv(
        filepath,
        index=False
    )

    return filepath


def print_energy(energies):

    print("=" * 40)
    print("SUBBAND ENERGY")
    print("=" * 40)

    for name, value in energies.items():

        print(f"{name:<5}: {value:.6f}")


def print_capacity(info):

    print("=" * 40)
    print("PAYLOAD INFORMATION")
    print("=" * 40)

    print(f"Capacity  : {info['capacity']} bit")
    print(f"Payload   : {info['required']} bit")
    print(f"Remaining : {info['remaining']} bit")

def print_metadata_summary(metadata, payload=None):

    print("=" * 50)
    print("METADATA SUMMARY")
    print("=" * 50)

    print(f"Number of Metadata Fields : {len(metadata)}")

    metadata_string = str(metadata)

    print(f"Metadata Characters       : {len(metadata_string)}")
    print(f"Metadata Bytes            : {len(metadata_string.encode('utf-8'))}")

    if payload is not None:
        print(f"Payload Length            : {len(payload)} bits")

    print("\nMetadata Fields")
    print("-" * 50)

    for key, value in metadata.items():

        print(f"{key:<30}: {value}")

    print("=" * 50)

def print_difference_statistics(difference):

    changed_pixels = np.count_nonzero(difference)

    total_pixels = difference.size

    percentage = (
        changed_pixels / total_pixels
    ) * 100

    print("=" * 50)
    print("DIFFERENCE STATISTICS")
    print("=" * 50)

    print(f"Changed Pixels     : {changed_pixels}")
    print(f"Total Pixels       : {total_pixels}")
    print(f"Percentage Changed : {percentage:.4f}%")
    print(f"Maximum Difference : {difference.max()}")
    print(f"Mean Difference    : {difference.mean():.6f}")

    print("=" * 50)

def show_difference_overlay(
    original,
    difference,
    alpha=0.5,
    figsize=(6,6)
):

    plt.figure(figsize=figsize)

    plt.imshow(original,
               cmap="gray")

    plt.imshow(
        difference,
        cmap="Reds",
        alpha=alpha
    )

    plt.title("Difference Overlay")

    plt.axis("off")

    plt.show()

def print_experiment_insight(df):

    print("=" * 60)
    print("EXPERIMENT INSIGHT")
    print("=" * 60)

    # Experiment Summary

    print(f"Images Tested         : {len(df)}")
    print(f"Successful Embedding  : {(df['Status'] == 'Success').sum()}")
    print(f"Failed Embedding      : {(df['Status'] != 'Success').sum()}")

    print()

    # Image Quality

    print(f"Average PSNR (dB)     : {df['PSNR (dB)'].mean():.4f}")
    print(f"Average SSIM          : {df['SSIM'].mean():.6f}")
    print(f"Average BER           : {df['BER'].mean():.6f}")

    print()

    # Payload Information

    print(f"Average Payload (bit) : {df['Payload Length (bits)'].mean():.0f}")
    print(f"Average Capacity(bit) : {df['Capacity (bits)'].mean():.0f}")
    print(f"Average Utilization   : {df['Capacity Utilization (%)'].mean():.2f}%")

    print()

    # Adaptive Subband

    print("Selected Subband Distribution")
    print(df["Selected Subband"].value_counts())

    print("=" * 60)

    return pd.DataFrame([insight])
