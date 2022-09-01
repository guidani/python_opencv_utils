import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from numpy import bitwise_and, bitwise_or, bitwise_xor, bitwise_not

def main():
    mouse_events = [j for j in dir(cv) if 'EVENT' in j]
    print(mouse_events)


if __name__ == "__main__":
    main()