#
# Simple Makefile for a Prog8 program.
#

# Cross-platform removal command
ifeq ($(OS),Windows_NT)
    CLEAN = del /Q build\* 
    CP = copy
    RM = del /Q
    MD = mkdir
    MV = ren
else
    CLEAN = rm -f build/*
    CP = cp -p
    RM = rm -f
    MD = mkdir -p
    MV = mv
endif

PCC=prog8c
PCCARGSVM=-srcdirs src -asmlist -target virtual -out build

PROGS	= build/demo.p8ir
SRCS	= demo/demo.p8 src/args.p8

all: build $(PROGS)

build:
	$(MD) build/

build/demo.p8ir: $(SRCS)
	$(PCC) $(PCCARGSVM) $<

clean:
	$(RM) build/*

run:	all
	echo "RUN HERE"
	tools/p8r.py $(PROGS) one two three four five "six seven"

#
# end-of-file
#
