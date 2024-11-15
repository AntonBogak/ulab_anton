import numpy as np
import matplotlib.pyplot as plt

def horizontal_subplots(domain=(0, 2 * np.pi)):
    """
    PURPOSE: Plots two subplots side-by-side.
    Left subplot: h(x) = cos(x)
    Right subplot: k(x) = sin(x)
    
    INPUT:
    domain (tuple): The range of x values (start, end)
    """
    xf = np.linspace(domain[0], domain[1], 100)
    hf = np.cos(xf)
    kf = np.sin(xf)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left subplot: h(x) = cos(x)
    ax1.plot(xf, hf, color='blue', linestyle='--')
    ax1.set_title("h(x) = cos(x)")
    ax1.set_xlabel("X")
    ax1.set_ylabel("h(X)")

    # Right subplot: k(x) = sin(x)
    ax2.plot(xf, kf, color='red', linestyle=':')
    ax2.set_title("k(x) = sin(x)")
    ax2.set_xlabel("X")
    ax2.set_ylabel("k(X)")

    plt.suptitle("Side-by-Side Subplots of h(x) = cos(x) and k(x) = sin(x)", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


def vertical_subplots(domain=(0, 2 * np.pi)):
    """
    PURPOSE: Plots two subplots on top of each other.
    Top subplot: h(x) = cos(x)
    Bottom subplot: k(x) = sin(x)
    
    INPUT:
    domain (tuple): The range of x values (start, end)
    """
    xf = np.linspace(domain[0], domain[1], 100)
    hf = np.cos(xf)
    kf = np.sin(xf)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

    # Top subplot: h(x) = cos(x)
    ax1.plot(xf, hf, color='blue', linestyle='--')
    ax1.set_title("h(x) = cos(x)")
    ax1.set_xlabel("X")
    ax1.set_ylabel("h(X)")

    # Bottom subplot: k(x) = sin(x)
    ax2.plot(xf, kf, color='red', linestyle=':')
    ax2.set_title("k(x) = sin(x)")
    ax2.set_xlabel("X")
    ax2.set_ylabel("k(X)")

    plt.suptitle("Vertical Subplots of h(x) = cos(x) and k(x) = sin(x)", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()