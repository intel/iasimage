# Copyright (c) 2018 Intel Corporation. All right reserved.
# See LICENSE for terms.

BINDIR := /usr/bin

all: iasimage

install: iasimage
	install -D --mode=0755 iasimage ${INSTALL_ROOT}${BINDIR}/iasimage

check:
	

.PHONY: all check install

