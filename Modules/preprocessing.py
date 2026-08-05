
import numpy as np
import pydicom
import matplotlib.pyplot as plt


def load_dicom(filepath):
    return pydicom.dcmread(filepath)


def get_pixel_array(dataset):
    return dataset.pixel_array


def normalize_image(image):
    image = image.astype(np.float32)

    image = (image - image.min()) / (image.max() - image.min())

    image = image * 255

    return image.astype(np.uint8)


def extract_metadata(dataset):

    metadata = {
    "Patient ID":
        str(getattr(dataset, "PatientID", "Unknown")),

    "Modality":
        str(getattr(dataset, "Modality", "Unknown")),

    "Slice Thickness":
        float(getattr(dataset, "SliceThickness", 0)),

    "Slice Location":
        float(getattr(dataset, "SliceLocation", 0)),

    "Pixel Spacing":
        list(getattr(dataset, "PixelSpacing", [])),
    }

    return metadata


def image_information(image):

    print(f"Shape      : {image.shape}")
    print(f"Datatype   : {image.dtype}")
    print(f"Minimum    : {image.min()}")
    print(f"Maximum    : {image.max()}")


def show_image(image,
               title="Image",
               cmap="gray"):

    plt.figure(figsize=(6,6))

    plt.imshow(image,
               cmap=cmap)

    plt.title(title)

    plt.axis("off")

    plt.show()
