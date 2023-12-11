

from keras.datasets import mnist

class SampleImage:
    def __init__(self, image, label):
        self.image = image
        self.label = label


class DataGenerator:

    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self) -> SampleImage:
        pass

    def __len__(self) -> int:
        pass

# Create a generator for MNIST data
class MNISTGenerator(DataGenerator):
    
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