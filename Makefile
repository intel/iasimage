# Copyright (c) 2018 Intel Corporation. All right reserved.
# See LICENSE for terms.

BINDIR := /usr/bin

all: iasimage

install: iasimage check
	install -D --mode=0755 iasimage ${INSTALL_ROOT}${BINDIR}/iasimage

check:
	python tests/test_iasimage.py
	./iasimage -V

.PHONY: all check install

