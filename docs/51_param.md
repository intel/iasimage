# Parameter {#params}


## Command line options {#cli}

Usage:
./iasimage MODE [OPTION] FILE

Mode     | Description
---------|-------------
create   | Create ias image
extract  | Extract files from ias image
sign     | Sign ias image with provided RSA signature and public key (signature is verified with the key)


Option                 | Short Option | Argument  | Description
---------------------- | ------------ | --------------- | -----------
create mode:           |              |                 | -
 \-\-image-type        | -i           | uint            | Image type (see `iasimage create -h` for more information)
 \-\-output            | -o           | file (optional) | Output image (default: iasImage)
 \-\-devkey            | -d           | file (optional) | Private key for internal (development phase) signing. RSA signature and public key will be generated and added at the end of image
 \-\-page-aligned[=NUM]| -p           | uint (optional) | Add padding bytes to align input files to 4KB (page) boundary. Start to align at file <NUM>. Defaults: type #3: NUM=5; #4: NUM=4
sign mode:             |              |                 | -
 \-\-output            | -o           | file (optional) | Output image (default: iasImage, file with added RSA signature and optionally public key)
 \-\-signature         | -s           | file            | RSA signature
 \-\-key               | -k           | file (optional) | Public key
common options:        |              |                 | -
 \-\-verbose           | -v[vvv ...]  |                 | Verbosity
other options:         |              |                 | -
 \-\-help              | -h           |                 | Help
 \-\-version           | -r           |                 | Tool version
