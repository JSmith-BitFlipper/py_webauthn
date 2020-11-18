
def get_verifier(extension_name):
    if extension_name == 'txAuthnSimple':
        return verify_txAuthnSimple

    raise KeyError("Verifier for extension `{}` does not exist!".
                   format(extension_name))

def verify_txAuthnSimple(client_data, expected_data):
    # Test the `txAuthSimple` extension equality, except for line breaks
    return client_data.replace('\n', '') == expected_data.replace('\n', '')
