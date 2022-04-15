DOMAIN = "apex"


def setup(hass, config):
    hass.states.set("apex.hello", "true")

    # Return boolean to indicate that initialization was successful.
    return True
