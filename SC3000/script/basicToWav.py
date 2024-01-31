import basicparse
import wavparse
import argparse
import pathlib
import section
import bitparse


def canonicalName(fname):
    stem = pathlib.Path(fname).stem.upper()
    return ''.join(char for char in stem if char.isalnum()).ljust(16)[:16]


if __name__ == "__main__":
    remrate = 44100
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("outfile", nargs="?", default=None)
    parser.add_argument("--program_name")
    args = parser.parse_args()

    opt = {k: v for k, v in vars(args).items() if v is not None}

    if "program_name" not in opt:
        opt["program_name"] = canonicalName(args.infile)

    if args.outfile is None:
        args.outfile = pathlib.Path(args.infile).with_suffix(".wav")

    d = basicparse.readBasic(args.infile, opt)
    section.parseBytesSections(d["sections"], True, False)
    d["signal"] = bitparse.genSignal(d, remrate, True)
    wavparse.writeWav(str(args.outfile), d, opt)
