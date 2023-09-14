import cv2
import numpy as np
import copy

class ImageDehazer:
    def __init__(self, airlight_estimation_window_size=15, boundary_constraint_window_size=3, 
                 C0=20, C1=300, regularize_lambda=0.1, sigma=0.5, delta=0.85, 
                 show_haze_transmission_map=True):
        # Initialize the dehazing parameters
        self.airlight_estimation_window_size = airlight_estimation_window_size
        self.boundary_constraint_window_size = boundary_constraint_window_size
        self.C0 = C0
        self.C1 = C1
        self.regularize_lambda = regularize_lambda
        self.sigma = sigma
        self.delta = delta
        self.show_haze_transmission_map = show_haze_transmission_map
        self._A = []  # List to store estimated airlight values
        self._transmission = []  # List to store haze transmission maps

    def _estimate_airlight(self, haze_img):
        # Estimate atmospheric light (airlight) from the hazy image
        if len(haze_img.shape) == 3:
            for ch in range(haze_img.shape[2]):
                kernel = np.ones((self.airlight_estimation_window_size, 
                                  self.airlight_estimation_window_size), np.uint8)
                min_img = cv2.erode(haze_img[:, :, ch], kernel)
                self._A.append(int(min_img.max()))
        else:
            kernel = np.ones((self.airlight_estimation_window_size, 
                              self.airlight_estimation_window_size), np.uint8)
            min_img = cv2.erode(haze_img, kernel)
            self._A.append(int(min_img.max()))

    def _boundary_constraint(self, haze_img):
        # Apply boundary constraints to the haze transmission map
        if len(haze_img.shape) == 3:
            t_b = np.maximum((self._A[0] - haze_img[:, :, 0].astype(float)) / 
                             (self._A[0] - self.C0),
                             (haze_img[:, :, 0].astype(float) - self._A[0]) / 
                             (self.C1 - self._A[0]))
            t_g = np.maximum((self._A[1] - haze_img[:, :, 1].astype(float)) / 
                             (self._A[1] - self.C0),
                             (haze_img[:, :, 1].astype(float) - self._A[1]) / 
                             (self.C1 - self._A[1]))
            t_r = np.maximum((self._A[2] - haze_img[:, :, 2].astype(float)) / 
                             (self._A[2] - self.C0),
                             (haze_img[:, :, 2].astype(float) - self._A[2]) / 
                             (self.C1 - self._A[2]))
            max_val = np.maximum(t_b, t_g, t_r)
            self._transmission = np.minimum(max_val, 1)
        else:
            self._transmission = np.maximum((self._A[0] - haze_img.astype(float)) / 
                                            (self._A[0] - self.C0),
                                            (haze_img.astype(float) - self._A[0]) / 
                                            (self.C1 - self._A[0]))
            self._transmission = np.minimum(self._transmission, 1)
        
        kernel = np.ones((self.boundary_constraint_window_size, 
                          self.boundary_constraint_window_size), float)
        self._transmission = cv2.morphologyEx(self._transmission, cv2.MORPH_CLOSE, kernel=kernel)

    # Other methods like load_filter_bank, calculate_weighting_function, circular_conv_filt,
    # psf2otf, and remove_haze can remain the same as in your original code.
    
    def remove_haze(self, haze_img):
        # Remove haze from the input hazy image
        self._estimate_airlight(haze_img)
        self._boundary_constraint(haze_img)
        # Call other methods to calculate transmission and remove haze
        # ...
        haze_corrected_img = self._remove_haze(haze_img)
        haze_transmission_map = self._transmission
        return haze_corrected_img, haze_transmission_map

def remove_haze(haze_img, airlight_estimation_window_size=15, boundary_constraint_window_size=3, 
                C0=20, C1=300, regularize_lambda=0.1, sigma=0.5, delta=0.85, 
                show_haze_transmission_map=True):
    # Convenience function to remove haze from an image using ImageDehazer
    dehazer = ImageDehazer(airlight_estimation_window_size=airlight_estimation_window_size,
                           boundary_constraint_window_size=boundary_constraint_window_size, 
                           C0=C0, C1=C1, regularize_lambda=regularize_lambda, 
                           sigma=sigma, delta=delta, 
                           show_haze_transmission_map=show_haze_transmission_map)
    haze_corrected_img, haze_transmission_map = dehazer.remove_haze(haze_img)
    return haze_corrected_img, haze_transmission_map
