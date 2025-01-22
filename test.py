from lsproxy.client import Lsproxy
from lsproxy.models import GetReferencesRequest, GetReferencedSymbolsRequest
from tqdm import tqdm
import random
import time
def main():
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
    main()
