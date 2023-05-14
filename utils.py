import numpy as np 
import matplotlib.pyplot as plt

def plot_fcd(ref, ureg, reg, syn, s, title):

    #print(f'{ref.shape}, {ureg.shape}, {reg.shape} ')

    fig = plt.figure(figsize=(16, 16))
    fig.suptitle(title, fontsize=14)
    #fig.subplots_adjust(hspace=1, wspace=1)

    ax1 = fig.add_subplot(2, 4, 1)
    ax1.axis("off")
    ax1.imshow(ref[:, :, 255-s], cmap="gray")

    ax2 = fig.add_subplot(2, 4, 2)
    ax2.axis("off")
    ax2.imshow(ureg[:, :, s], cmap="gray")

    ax3 = fig.add_subplot(2, 4, 3)
    ax3.axis("off")
    ax3.imshow(reg[:, :, s], cmap="gray")

    ax4 = fig.add_subplot(2, 4, 4)
    ax4.axis("off")
    ax4.imshow(syn[:, :, s], cmap="gray")

    ax5 = fig.add_subplot(2, 4, 5)
    ax5.axis("off")
    ax5.imshow(ref[:, :, s], cmap="gray")

    ax6 = fig.add_subplot(2, 4, 6)
    ax6.axis("off")
    ax6.imshow(np.where(ureg[:, :, s]==1, ureg[:, :, s], ref[:, :, 255-s]), cmap="gray")

    ax7 = fig.add_subplot(2, 4, 7)
    ax7.axis("off")
    ax7.imshow(np.where(reg[:, :, s]==1, reg[:, :, s], ref[:, :, 255-s]))

    ax8 = fig.add_subplot(2, 4, 8)
    ax8.axis("off")
    ax8.imshow(np.where(syn[:, :, s]==1, reg[:, :, s], ref[:, :, 255-s]))

    fig.tight_layout()
    plt.show()

def plot_unreg(img, msk, s, offset=False):

    fig = plt.figure(figsize=(16, 16))
    fig.suptitle(f'Slice = {s}', fontsize=14)
    #fig.subplots_adjust(hspace=1, wspace=1)

    ax1 = fig.add_subplot(1, 3, 1)
    ax1.axis("off")
    #ax1.imshow(img[:, :, img.shape[2]-s-1], cmap="gray")

    ax2 = fig.add_subplot(1, 3, 2)
    ax2.axis("off")
    ax2.imshow(msk[:, :, s], cmap="gray")

    ax3 = fig.add_subplot(1, 3, 3)
    ax3.axis("off")

    if offset:
        ax1.imshow(img[:, :, img.shape[2]-s-1], cmap="gray")
        ax3.imshow(img[:, :, img.shape[2]-s-1], cmap="gray")
        ax3.imshow(msk[:, :, s], cmap='gray', alpha=0.2)
    else:
        ax1.imshow(img[:, :, s], cmap="gray")
        ax3.imshow(img[:, :, s], cmap="gray")
        ax3.imshow(msk[:, :, s], cmap='gray', alpha=0.2)

    fig.tight_layout()
    plt.show()

def plot_reg(img, msk, s):

    fig = plt.figure(figsize=(16, 16))
    fig.suptitle(f'Slice = {s}', fontsize=14)
    #fig.subplots_adjust(hspace=1, wspace=1)

    ax1 = fig.add_subplot(1, 3, 1)
    ax1.axis("off")
    ax1.imshow(img[:, :, img.shape[2]-s-1], cmap="gray")

    ax2 = fig.add_subplot(1, 3, 2)
    ax2.axis("off")
    ax2.imshow(msk[:, :, s], cmap="gray")

    ax2 = fig.add_subplot(1, 3, 3)
    ax2.axis("off")
    ax2.imshow(img[:, :, img.shape[2]-s-1], cmap="gray")
    ax2.imshow(msk[:, :, s], cmap='gray', alpha=0.5)

    fig.tight_layout()
    plt.show()

def plot_rfx(ref, urfx, refx, s, title):

    #print(f'{ref.shape}, {urfx.shape}, {refx.shape} ')

    fig = plt.figure(figsize=(16, 16))
    fig.suptitle(title, fontsize=14)
    #fig.subplots_adjust(hspace=1, wspace=1)

    ax1 = fig.add_subplot(2, 3, 1)
    ax1.axis("off")
    ax1.imshow(ref[:, :, 255-s], cmap="gray")

    ax2 = fig.add_subplot(2, 3, 2)
    ax2.axis("off")
    ax2.imshow(urfx[:, :, s], cmap="gray")

    ax3 = fig.add_subplot(2, 3, 3)
    ax3.axis("off")
    ax3.imshow(refx[:, :, s], cmap="gray")

    ax4 = fig.add_subplot(2, 3, 4)
    ax4.axis("off")
    ax4.imshow(ref[:, :, 255-s], cmap="gray")

    ax5 = fig.add_subplot(2, 3, 5)
    ax5.axis("off")
    ax5.imshow(np.where(urfx[:, :, s]==1, urfx[:, :, s], ref[:, :, 255-s]), cmap="gray")

    ax6 = fig.add_subplot(2, 3, 6)
    ax6.axis("off")
    ax6.imshow(np.where(refx[:, :, s]==1, refx[:, :, s], ref[:, :, 255-s]), cmap="gray")

    # ax7 = fig.add_subplot(2, 4, 7)
    # ax7.axis("off")
    # ax7.imshow(np.where(refx[:, :, s]==1, refx[:, :, s], ref[:, :, 255-s]))

    # ax8 = fig.add_subplot(2, 4, 8)
    # ax8.axis("off")
    # ax8.imshow(np.where(syn[:, :, s]==1, refx[:, :, s], ref[:, :, 255-s]))

    fig.tight_layout()
    plt.show()

def plot_flipped(ref, flip, s, title):

    #print(f'{ref.shape}, {urfx.shape}, {refx.shape} ')

    fig = plt.figure(figsize=(16, 16))
    fig.suptitle(title, fontsize=14)
    #fig.subplots_adjust(hspace=1, wspace=1)

    ax1 = fig.add_subplot(1, 3, 1)
    ax1.axis("off")
    ax1.imshow(ref[:, :, s], cmap="gray")

    ax2 = fig.add_subplot(1, 3, 2)
    ax2.axis("off")
    ax2.imshow(flip[:, :, s], cmap="gray")

    ax3 = fig.add_subplot(1, 3, 3)
    ax3.axis("off")
    ax3.imshow(np.where(flip[:, :, s]==1, flip[:, :, s], ref[:, :, s]), cmap="gray")

    # ax4 = fig.add_subplot(2, 3, 4)
    # ax4.axis("off")
    # ax4.imshow(ref[:, :, 255-s], cmap="gray")

    # ax5 = fig.add_subplot(2, 3, 5)
    # ax5.axis("off")
    # ax5.imshow(np.where(urfx[:, :, s]==1, urfx[:, :, s], ref[:, :, 255-s]), cmap="gray")

    # ax6 = fig.add_subplot(2, 3, 6)
    # ax6.axis("off")
    # ax6.imshow(np.where(refx[:, :, s]==1, refx[:, :, s], ref[:, :, 255-s]), cmap="gray")

    # ax7 = fig.add_subplot(2, 4, 7)
    # ax7.axis("off")
    # ax7.imshow(np.where(refx[:, :, s]==1, refx[:, :, s], ref[:, :, 255-s]))

    # ax8 = fig.add_subplot(2, 4, 8)
    # ax8.axis("off")
    # ax8.imshow(np.where(syn[:, :, s]==1, refx[:, :, s], ref[:, :, 255-s]))

    fig.tight_layout()
    plt.show()


def plot_single(img, s, title, overlay=None, fn=''):

    fig = plt.figure(figsize=(16, 16))
    #fig.suptitle(f'{s}', fontsize=14)

    ax1 = fig.add_subplot(1, 1, 1)
    ax1.axis("off")

    if overlay is None:
        ax1.imshow(img[:, :, s], cmap="gray")
        ax1.figure.savefig(fn, dpi=300, format='pdf', 
                    bbox_inches='tight', facecolor='auto', edgecolor='auto',
        )
    else:
        ax1.imshow(img[:, :, s], cmap="gray")
        ax1.imshow(overlay[:, :, s], cmap='gray', alpha=0.5)
        ax1.figure.savefig(fn, dpi=300, format='pdf', 
                    bbox_inches='tight', facecolor='auto', edgecolor='auto',
        )

    fig.tight_layout()
    plt.show()