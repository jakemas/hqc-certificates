DEPS_FILES := \
	X509-HQC-2026.asn \

# NOTE: example artifacts (HQC-*.crt/.pub/-seed.priv and their .txt
# pretty-prints) will be added to DEPS_FILES once a generator exists and
# the draft {::include}s them, mirroring lamps-wg/kyber-certificates.

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
