from lsproxy.client import Lsproxy
from lsproxy.models import GetReferencesRequest, GetReferencedSymbolsRequest
from tqdm import tqdm
import random
import time
import argparse
def main(seed=None):
    if seed is not None:
        random.seed(seed)
    lsproxy = Lsproxy(timeout=600)
    files = lsproxy.list_files()
    files = [f for f in files if f.endswith(".py")]
    random.shuffle(files)
    start = time.time()
    for file in tqdm(files,smoothing=0):
        symbols = lsproxy.definitions_in_file(file)
        for symbol in symbols:
            req = GetReferencedSymbolsRequest(
                identifier_position=symbol.identifier_position,
            )
            try:
                referenced_symbols = lsproxy.find_referenced_symbols(req)
            except Exception as e:
                print(e)
                continue
    end = time.time()
    print(f"Time taken: {end - start}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, help="Random seed for shuffling files")
    args = parser.parse_args()
    main(args.seed)
