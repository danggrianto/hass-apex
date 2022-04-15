DOMAIN = "apex_fusion"


def setup(hass, config):
    hass.states.set("apex_fusion.hello", "true")

    # Return boolean to indicate that initialization was successful.
    return True
