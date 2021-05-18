import torch

from mmedit.models.backbones.sr_backbones.ttsr_net import (CSFI2, CSFI3, SFE,
                                                           MergeFeatures)


def test_sfe():
    inputs = torch.rand(2, 3, 48, 48)
    sfe = SFE(3, 64, 16, 1.)
    outputs = sfe(inputs)
    assert outputs.shape == (2, 64, 48, 48)


def test_csfi():
    inputs1 = torch.rand(2, 16, 24, 24)
    inputs2 = torch.rand(2, 16, 48, 48)
    inputs4 = torch.rand(2, 16, 96, 96)

    csfi2 = CSFI2(mid_channels=16)
    out1, out2 = csfi2(inputs1, inputs2)
    assert out1.shape == (2, 16, 24, 24)
    assert out2.shape == (2, 16, 48, 48)

    csfi3 = CSFI3(mid_channels=16)
    out1, out2, out4 = csfi3(inputs1, inputs2, inputs4)
    assert out1.shape == (2, 16, 24, 24)
    assert out2.shape == (2, 16, 48, 48)
    assert out4.shape == (2, 16, 96, 96)


def test_merge_features():
    inputs1 = torch.rand(2, 16, 24, 24)
    inputs2 = torch.rand(2, 16, 48, 48)
    inputs4 = torch.rand(2, 16, 96, 96)

    merge_features = MergeFeatures(mid_channels=16, out_channels=3)
    out = merge_features(inputs1, inputs2, inputs4)
    assert out.shape == (2, 3, 96, 96)