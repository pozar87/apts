from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

def test_zwo_cooled_backfocus_consistency():
    # Standard Pro models
    pro_models = [
        ZwoCamera.ZWO_ASI_2600MC_Pro(),
        ZwoCamera.ZWO_ASI_533MC_Pro(),
        ZwoCamera.ZWO_ASI_183MM_Pro(),
        ZwoCamera.ZWO_ASI_6200MM_Pro(),
        ZwoCamera.ZWO_ASI_2400MC_Pro(),
        ZwoCamera.ZWO_ASI_071MC_Pro(),
    ]

    # Duo models
    duo_models = [
        ZwoCamera.ZWO_ASI_2600MC_Duo(),
        ZwoCamera.ZWO_ASI_2600MM_Duo(),
    ]

    # Cool models (legacy)
    cool_models = [
        ZwoCamera.ZWO_ASI_1600MC_Cool(),
        ZwoCamera.ZWO_ASI_183MM_Cool(),
    ]

    # Legacy all-caps factory methods
    legacy_factories = [
        ZwoCamera.ZWO_ASI2600MC_PRO(),
        ZwoCamera.ZWO_ASI533MM_PRO(),
        ZwoCamera.ZWO_ASI6200MC_PRO(),
    ]

    all_tested = pro_models + duo_models + cool_models + legacy_factories

    for cam in all_tested:
        # Standard ZWO backfocus is 17.5mm for these series
        assert cam.backfocus.to("mm").magnitude == 17.5
        assert cam.optical_length.to("mm").magnitude == 17.5

def test_zwo_uncooled_planetary_remains_short():
    # ASI224MC is uncooled, optical length 12.5mm
    cam = ZwoCamera.ZWO_ASI_224MC()
    assert cam.optical_length.to("mm").magnitude == 12.5

def test_zwo_mini_remains_short():
    # Mini cameras are typically 12.5mm or 8.5mm depending on model
    cam = ZwoCamera.ZWO_ASI_120MM_Mini()
    assert cam.optical_length.to("mm").magnitude == 12.5
