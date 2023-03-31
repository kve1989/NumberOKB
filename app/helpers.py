"""
Здесь храним функции-хелперы
"""

import hashlib
from datetime import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID


def generateFilename(filename):
    f_name = filename.rsplit('.', 1)
    f_name[0] = hashlib.md5((f_name[0] + datetime.now().strftime("%d-%m-%y_%H-%M")).encode('utf-8')).hexdigest()
    return '.'.join(f_name)

def parseCertificate(file):
    with open(file, "rb") as f:
        cert = x509.load_der_x509_certificate(f.read())

    parsedCertificate = {
        'dateStart': cert.not_valid_before,
        'dateEnd': cert.not_valid_after,
        'serial_number': str(cert.serial_number),
        'commonName': cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value,
        'givenName': cert.subject.get_attributes_for_oid(NameOID.GIVEN_NAME)[0].value,
        'surname': cert.subject.get_attributes_for_oid(NameOID.SURNAME)[0].value,
        'issuer': cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
    }

    return parsedCertificate