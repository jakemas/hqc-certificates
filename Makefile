DEPS_FILES := \
	X509-HQC-2026.asn \
	./example/HQC-128.crt \
	./example/HQC-128.crt.txt \
	./example/HQC-128-seed.priv \
	./example/HQC-128-seed.priv.txt \
	./example/HQC-128.pub \
	./example/HQC-128.pub.txt \
	./example/HQC-192.crt \
	./example/HQC-192.crt.txt \
	./example/HQC-192-seed.priv \
	./example/HQC-192-seed.priv.txt \
	./example/HQC-192.pub \
	./example/HQC-192.pub.txt \
	./example/HQC-256.crt \
	./example/HQC-256.crt.txt \
	./example/HQC-256-seed.priv \
	./example/HQC-256-seed.priv.txt \
	./example/HQC-256.pub \
	./example/HQC-256.pub.txt \

LIBDIR := lib
include $(LIBDIR)/main.mk

$(LIBDIR)/main.mk:
ifneq (,$(shell grep "path *= *$(LIBDIR)" .gitmodules 2>/dev/null))
	git submodule sync
	git submodule update $(CLONE_ARGS) --init
else
	git clone -q --depth 10 $(CLONE_ARGS) \
	    -b main https://github.com/martinthomson/i-d-template $(LIBDIR)
endif
