"""This module contains classes for generating data"""

from keras.datasets import mnist

class SampleImage:
    """This class represents a sample image with its label"""

    def __init__(self, image, label):
        self.image = image
        self.label = label


class DataGenerator:
    """This class represents an abstract generator of data"""

    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self) -> SampleImage:
        pass

    def __len__(self) -> int:
        pass

class MNISTGenerator(DataGenerator):
    """This class represents a generator of MNIST data"""

    def __init__(self):
        super().__init__()
        # Load MNIST data from keras
        (images, tags), (_, __)= mnist.load_data()
        self.images = images
        self.tags = tags

        self.index = 0
        self.length = len(images)

    def __next__(self) -> SampleImage:
        if self.index >= len(self.images):
            raise StopIteration
        image = self.images[self.index]
        tag = self.tags[self.index]
        self.index += 1
        return SampleImage(image=image, label=tag)

    def __len__(self) -> int:
        return self.length