import json
import zlib
import zstandard as zstd
from pathlib import Path


class ZlibSerializer:

    @classmethod
    def dumps(cls, data):
        return zlib.compress(json.dumps(data).encode())

    @classmethod
    def loads(cls, data):
        return json.loads(zlib.decompress(data).decode())


class ZstdSerializer:

    dict_data = zstd.ZstdCompressionDict(
        open(Path(__file__).parent / 'addok-zstd-dict', 'rb').read())
    compressor = zstd.ZstdCompressor(level=10, dict_data=dict_data)
    decompressor = zstd.ZstdDecompressor(dict_data=dict_data)


    @classmethod
    def dumps(cls, data):
        return cls.compressor.compress(json.dumps(data).encode())

    @classmethod
    def loads(cls, data):
        return json.loads(cls.decompressor.decompress(data).decode())
