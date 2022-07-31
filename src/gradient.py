import numpy as np
from PIL import Image
class Gradient():

    def get_gradient_2d(self, start, stop, width, height, is_horizontal):
        if is_horizontal:
            return np.tile(np.linspace(start, stop, width), (height, 1))
        else:
            return np.tile(np.linspace(start, stop, height), (width, 1)).T


    def get_gradient_3d(self, width, height, start_list, stop_list, is_horizontal_list):
        result = np.zeros((height, width, len(start_list)), dtype=float)

        for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
            result[:, :, i] = self.get_gradient_2d(start, stop, width, height, is_horizontal)

        return result

    def generate_gradient(self, width, height, start, stop):
        array = self.get_gradient_3d(width, height, start, stop, (False, False, True))
        return Image.fromarray(np.uint8(array))
