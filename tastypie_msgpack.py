
from tastypie.serializers import Serializer as DefaultSerializer
import msgpack


class Serializer(DefaultSerializer):

    def __init__(self, *args, **kwargs):
        super(Serializer, self).__init__(*args, **kwargs)
        self.formats.append("msgpack")
        self.content_types["msgpack"] = "application/x-msgpack"

    def to_msgpack(self, data, options=None):
        return msgpack.packb(self.to_simple(data, options or {}))

    def from_msgpack(self, content):
        return msgpack.unpackb(content)
