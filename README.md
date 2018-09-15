[![Build Status](https://travis-ci.com/intel/iasimage.svg?branch=master)](https://travis-ci.com/intel/iasimage)

iasimage
-----------

iasimage is a utility program for creating Intel Automotive Service (IAS) images, a binary file format understood by bootloaders to load and initialize Operating Systems or Hypervisors.

iasimage supports the following features:

* Create an image (including kernel cmdline, kernel, hypervisor binary etc.)
* Attach a signature to an IAS image
* Extract components from an IAS image

## Examples

### Create an IAS image
`iasimage create -o iasImage -i 0x30000 cmdline.txt bzImage initrd`

### Create a multi-file IAS image of type #3 with default page alignment:
`iasimage create -o iasImage -i 0x30000 cmdline.txt bzImage initrd acpi Firmware1.bin --page-aligned`

### Create a multi-file IAS image of type #3 given page alignment:
`iasimage create -i 0x40000 cmdLine.txt elf1.bin cmdLine2.txt elf2.bin -o test_image.img --page-aligned=2`

Default page alignment values for multi-file images are:

* for type #3 alignment is 5
* for type #4 alignment is 4
* for type #10 alignment is 2

### Sign an IAS image
`iasimage sign -o iasImage_signed -s rsa.sig -k pub_key.pem iasImage`

### Create a signed IAS image with a private key (for development purposes only).
`iasimage create -o iasImage -i 0x30300 -d priv_key.pem cmdline.txt bzImage initrd`

### Extract components from an IAS image
`iasimage extract iasImage`
