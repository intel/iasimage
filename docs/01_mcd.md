# Overview


iastool is a utility program running in host environment to create Intel Automotive Service (IAS) image files loaded by Intel Slim Bootloader.

The IAS image format consists of a header, a type specific header (optional), the image payload, a payload CRC, an RSA signature and a public key (modulus and exponent) at the end.

The image header consists a common (generic) and an optional (type specific) part.

The image payload contains the raw data or the original data file(s). It is possible to add a type-specific header (optional) containing information that is are only valid for the specific type of an image. CRC-32 checksum of the complete payload is added at the end of the payload data. To secure the image payload, an RSA signature with public key can be attached at the end of the image. Slim Bootloader loads and verifies the the IAS image using the attached signature.

iastool provides the following features:

## Combining:
  Add header information at the beginning of the data file(s) and calculate the header and data CRC checksums.

## Signing:
  Attache a generated RSA signature and the public key (from signing service) at the end of the image. The signature could be verified by providing the public key.

## Extracting:
  Extract payload files from the IAS image.

## Signing for test with a local key:
  Signing with a user provided RSA private key. This is for the development use.
