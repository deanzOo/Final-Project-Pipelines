import torch.nn as nn

class Discriminator(nn.Module):
        def __init__(self, ngpu):
            super(Discriminator, self).__init__()
            self.ngpu = ngpu
            self.main = nn.Sequential(
                # input is (nc) x 64 x 64
                nn.Conv2d(3, 64, 4, 2, 1, bias=True),
                nn.LeakyReLU(0.2, inplace=True),
                # state size. (64) x 32 x 32
                nn.Conv2d(64, 64 * 2, 4, 2, 1, bias=True),
                nn.BatchNorm2d(64 * 2),
                nn.LeakyReLU(0.2, inplace=True),
                # state size. (64*2) x 16 x 16
                nn.Conv2d(64 * 2, 64 * 4, 4, 2, 1, bias=True),
                nn.BatchNorm2d(64 * 4),
                nn.LeakyReLU(0.2, inplace=True),
                # state size. (64*4) x 8 x 8
                nn.Conv2d(64 * 4, 64 * 8, 4, 2, 1, bias=True),
                nn.BatchNorm2d(64 * 8),
                nn.LeakyReLU(0.2, inplace=True),
                # state size. (64*8) x 4 x 4
                nn.Conv2d(64 * 8, 1, 4, 1, 0, bias=True),
                nn.Sigmoid()
            )

        def forward(self, input):
            return self.main(input)