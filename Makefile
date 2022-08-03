PYTHON_OUTDIR = dist/python
NANOPB_OUTDIR = dist/nanopb

PROTO_SOURCES = $(shell find protocol -name "*.proto")

PYTHON_TARGETS = python/protocol/whad_pb2.py \
		 python/protocol/device_pb2.py \
		 python/protocol/generic_pb2.py \
		 python/protocol/ble/ble_pb2.py \
		 python/protocol/zigbee/zigbee_pb2.py

NANOPB_TARGETS = nanopb/protocol/whad.pb.c \
		 nanopb/protocol/whad.pb.h \
		 nanopb/protocol/generic.pb.c \
		 nanopb/protocol/generic.pb.h \
		 nanopb/protocol/device.pb.c \
		 nanopb/protocol/device.pb.h \
		 nanopb/protocol/ble/ble.pb.c \
		 nanopb/protocol/ble/ble.pb.h \
		 nanopb/protocol/zigbee/zigbee.pb.h \
		 nanopb/protocol/zigbee/zigbee.pb.c

all: python nanopb 

clean: clean_python clean_nanopb

clean_python:
	@echo "Remove python output directory ..."
	@rm $(PYTHON_OUTDIR) -rf

clean_nanopb:
	@echo "Remove nanopb output directory ..."
	@rm $(NANOPB_OUTDIR) -rf

python: clean_python
	@mkdir -p $(PYTHON_OUTDIR)
	protoc --experimental_allow_proto3_optional --python_out=$(PYTHON_OUTDIR) $(PROTO_SOURCES)

nanopb: clean_nanopb
	@mkdir -p $(NANOPB_OUTDIR)
	./nanopb/generator/protoc --experimental_allow_proto3_optional --nanopb_out=$(NANOPB_OUTDIR) $(PROTO_SOURCES)

