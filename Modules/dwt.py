
import pywt
import matplotlib.pyplot as plt

#Melakukan dekomposisi DWT Level-1.
def dwt_decompose(image, wavelet="haar"):

    LL, (LH, HL, HH) = pywt.dwt2(image, wavelet)

    return LL, LH, HL, HH

#Rekonstruksi citra menggunakan Inverse DWT.
def dwt_reconstruct(LL, LH, HL, HH, wavelet="haar"):
    
    reconstructed = pywt.idwt2(
        (LL, (LH, HL, HH)),
        wavelet
    )

    return reconstructed

#memperoleh seluruh subband
def get_subbands(image, wavelet="haar"):
   
    return dwt_decompose(image, wavelet)

# Menampilkan empat subband hasil DWT.
def show_subbands(LL, LH, HL, HH):

    fig, ax = plt.subplots(2, 2, figsize=(8,8))

    ax[0,0].imshow(LL, cmap="gray")
    ax[0,0].set_title("LL")

    ax[0,1].imshow(LH, cmap="gray")
    ax[0,1].set_title("LH")

    ax[1,0].imshow(HL, cmap="gray")
    ax[1,0].set_title("HL")

    ax[1,1].imshow(HH, cmap="gray")
    ax[1,1].set_title("HH")

    for a in ax.ravel():
        a.axis("off")

    plt.tight_layout()
    plt.show()

#  Menampilkan informasi ukuran masing-masing subband
def subband_information(LL, LH, HL, HH):
    print(f"LL : {LL.shape}")
    print(f"LH : {LH.shape}")
    print(f"HL : {HL.shape}")
    print(f"HH : {HH.shape}")
