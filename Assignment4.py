import torch
import torch.nn as nn
import torch.nn.functional as F

class GrayscaleImageNet(nn.Module):
    def __init__(self):
        super(GrayscaleImageNet, self).__init__()
        # Fill in your code here

    def forward(self, x):
        # Input size: (batch_size, 1, 64, 64)
        # Fill in your code here
        pass

# Example usage:
if __name__ == "__main__":
    # Define the model
    model = GrayscaleImageNet()

    # Dummy input for testing (batch_size=8, 1 channel, 64x64 images)
    dummy_input = torch.randn(8, 1, 64, 64)

    # Forward pass
    output = model(dummy_input)
    print("Output shape:", output.shape)  # Should be (8, 5)
