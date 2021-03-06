# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: routing.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
from . import CasperMessage_pb2 as CasperMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='routing.proto',
  package='routing',
  syntax='proto3',
  serialized_options=b'\342?%\n!coop.rchain.comm.protocol.routing\020\001',
  serialized_pb=b'\n\rrouting.proto\x12\x07routing\x1a\x15scalapb/scalapb.proto\x1a\x13\x43\x61sperMessage.proto\"D\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0c\n\x04host\x18\x02 \x01(\x0c\x12\x10\n\x08tcp_port\x18\x03 \x01(\r\x12\x10\n\x08udp_port\x18\x04 \x01(\r\":\n\x06Header\x12\x1d\n\x06sender\x18\x01 \x01(\x0b\x32\r.routing.Node\x12\x11\n\tnetworkId\x18\x02 \x01(\t\"\x0b\n\tHeartbeat\"\x13\n\x11HeartbeatResponse\"\"\n\x11ProtocolHandshake\x12\r\n\x05nonce\x18\x01 \x01(\x0c\"*\n\x19ProtocolHandshakeResponse\x12\r\n\x05nonce\x18\x01 \x01(\x0c\")\n\x06Packet\x12\x0e\n\x06typeId\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"\x0c\n\nDisconnect\"\xb2\x02\n\x08Protocol\x12\x1f\n\x06header\x18\x01 \x01(\x0b\x32\x0f.routing.Header\x12\'\n\theartbeat\x18\x02 \x01(\x0b\x32\x12.routing.HeartbeatH\x00\x12\x38\n\x12protocol_handshake\x18\x03 \x01(\x0b\x32\x1a.routing.ProtocolHandshakeH\x00\x12I\n\x1bprotocol_handshake_response\x18\x04 \x01(\x0b\x32\".routing.ProtocolHandshakeResponseH\x00\x12!\n\x06packet\x18\x05 \x01(\x0b\x32\x0f.routing.PacketH\x00\x12)\n\ndisconnect\x18\x06 \x01(\x0b\x32\x13.routing.DisconnectH\x00\x42\t\n\x07message\"0\n\tTLRequest\x12#\n\x08protocol\x18\x01 \x01(\x0b\x32\x11.routing.Protocol\"$\n\x13InternalServerError\x12\r\n\x05\x65rror\x18\x01 \x01(\x0c\"&\n\x03\x41\x63k\x12\x1f\n\x06header\x18\x01 \x01(\x0b\x32\x0f.routing.Header\"q\n\nTLResponse\x12\x1b\n\x03\x61\x63k\x18\x01 \x01(\x0b\x32\x0c.routing.AckH\x00\x12;\n\x13internalServerError\x18\x02 \x01(\x0b\x32\x1c.routing.InternalServerErrorH\x00\x42\t\n\x07payload\"z\n\x0b\x43hunkHeader\x12\x1d\n\x06sender\x18\x01 \x01(\x0b\x32\r.routing.Node\x12\x0e\n\x06typeId\x18\x02 \x01(\t\x12\x12\n\ncompressed\x18\x03 \x01(\x08\x12\x15\n\rcontentLength\x18\x04 \x01(\x05\x12\x11\n\tnetworkId\x18\x05 \x01(\t\" \n\tChunkData\x12\x13\n\x0b\x63ontentData\x18\x01 \x01(\x0c\"^\n\x05\x43hunk\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x14.routing.ChunkHeaderH\x00\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x12.routing.ChunkDataH\x00\x42\t\n\x07\x63ontent2v\n\x0eTransportLayer\x12\x31\n\x04Send\x12\x12.routing.TLRequest\x1a\x13.routing.TLResponse\"\x00\x12\x31\n\x06Stream\x12\x0e.routing.Chunk\x1a\x13.routing.TLResponse\"\x00(\x01\x42(\xe2?%\n!coop.rchain.comm.protocol.routing\x10\x01\x62\x06proto3'
  ,
  dependencies=[scalapb_dot_scalapb__pb2.DESCRIPTOR,CasperMessage__pb2.DESCRIPTOR,])




_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='routing.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='routing.Node.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='routing.Node.host', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcp_port', full_name='routing.Node.tcp_port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='udp_port', full_name='routing.Node.udp_port', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=138,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='routing.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='routing.Header.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='networkId', full_name='routing.Header.networkId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=198,
)


_HEARTBEAT = _descriptor.Descriptor(
  name='Heartbeat',
  full_name='routing.Heartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=211,
)


_HEARTBEATRESPONSE = _descriptor.Descriptor(
  name='HeartbeatResponse',
  full_name='routing.HeartbeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=232,
)


_PROTOCOLHANDSHAKE = _descriptor.Descriptor(
  name='ProtocolHandshake',
  full_name='routing.ProtocolHandshake',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='routing.ProtocolHandshake.nonce', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=268,
)


_PROTOCOLHANDSHAKERESPONSE = _descriptor.Descriptor(
  name='ProtocolHandshakeResponse',
  full_name='routing.ProtocolHandshakeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='routing.ProtocolHandshakeResponse.nonce', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=312,
)


_PACKET = _descriptor.Descriptor(
  name='Packet',
  full_name='routing.Packet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='typeId', full_name='routing.Packet.typeId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='routing.Packet.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=355,
)


_DISCONNECT = _descriptor.Descriptor(
  name='Disconnect',
  full_name='routing.Disconnect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=369,
)


_PROTOCOL = _descriptor.Descriptor(
  name='Protocol',
  full_name='routing.Protocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='routing.Protocol.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heartbeat', full_name='routing.Protocol.heartbeat', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol_handshake', full_name='routing.Protocol.protocol_handshake', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol_handshake_response', full_name='routing.Protocol.protocol_handshake_response', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packet', full_name='routing.Protocol.packet', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disconnect', full_name='routing.Protocol.disconnect', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='routing.Protocol.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=372,
  serialized_end=678,
)


_TLREQUEST = _descriptor.Descriptor(
  name='TLRequest',
  full_name='routing.TLRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol', full_name='routing.TLRequest.protocol', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=728,
)


_INTERNALSERVERERROR = _descriptor.Descriptor(
  name='InternalServerError',
  full_name='routing.InternalServerError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='routing.InternalServerError.error', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=730,
  serialized_end=766,
)


_ACK = _descriptor.Descriptor(
  name='Ack',
  full_name='routing.Ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='routing.Ack.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=768,
  serialized_end=806,
)


_TLRESPONSE = _descriptor.Descriptor(
  name='TLResponse',
  full_name='routing.TLResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='routing.TLResponse.ack', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internalServerError', full_name='routing.TLResponse.internalServerError', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='routing.TLResponse.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=808,
  serialized_end=921,
)


_CHUNKHEADER = _descriptor.Descriptor(
  name='ChunkHeader',
  full_name='routing.ChunkHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='routing.ChunkHeader.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typeId', full_name='routing.ChunkHeader.typeId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compressed', full_name='routing.ChunkHeader.compressed', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contentLength', full_name='routing.ChunkHeader.contentLength', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='networkId', full_name='routing.ChunkHeader.networkId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=923,
  serialized_end=1045,
)


_CHUNKDATA = _descriptor.Descriptor(
  name='ChunkData',
  full_name='routing.ChunkData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contentData', full_name='routing.ChunkData.contentData', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1047,
  serialized_end=1079,
)


_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='routing.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='routing.Chunk.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='routing.Chunk.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content', full_name='routing.Chunk.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1081,
  serialized_end=1175,
)

_HEADER.fields_by_name['sender'].message_type = _NODE
_PROTOCOL.fields_by_name['header'].message_type = _HEADER
_PROTOCOL.fields_by_name['heartbeat'].message_type = _HEARTBEAT
_PROTOCOL.fields_by_name['protocol_handshake'].message_type = _PROTOCOLHANDSHAKE
_PROTOCOL.fields_by_name['protocol_handshake_response'].message_type = _PROTOCOLHANDSHAKERESPONSE
_PROTOCOL.fields_by_name['packet'].message_type = _PACKET
_PROTOCOL.fields_by_name['disconnect'].message_type = _DISCONNECT
_PROTOCOL.oneofs_by_name['message'].fields.append(
  _PROTOCOL.fields_by_name['heartbeat'])
_PROTOCOL.fields_by_name['heartbeat'].containing_oneof = _PROTOCOL.oneofs_by_name['message']
_PROTOCOL.oneofs_by_name['message'].fields.append(
  _PROTOCOL.fields_by_name['protocol_handshake'])
_PROTOCOL.fields_by_name['protocol_handshake'].containing_oneof = _PROTOCOL.oneofs_by_name['message']
_PROTOCOL.oneofs_by_name['message'].fields.append(
  _PROTOCOL.fields_by_name['protocol_handshake_response'])
_PROTOCOL.fields_by_name['protocol_handshake_response'].containing_oneof = _PROTOCOL.oneofs_by_name['message']
_PROTOCOL.oneofs_by_name['message'].fields.append(
  _PROTOCOL.fields_by_name['packet'])
_PROTOCOL.fields_by_name['packet'].containing_oneof = _PROTOCOL.oneofs_by_name['message']
_PROTOCOL.oneofs_by_name['message'].fields.append(
  _PROTOCOL.fields_by_name['disconnect'])
_PROTOCOL.fields_by_name['disconnect'].containing_oneof = _PROTOCOL.oneofs_by_name['message']
_TLREQUEST.fields_by_name['protocol'].message_type = _PROTOCOL
_ACK.fields_by_name['header'].message_type = _HEADER
_TLRESPONSE.fields_by_name['ack'].message_type = _ACK
_TLRESPONSE.fields_by_name['internalServerError'].message_type = _INTERNALSERVERERROR
_TLRESPONSE.oneofs_by_name['payload'].fields.append(
  _TLRESPONSE.fields_by_name['ack'])
_TLRESPONSE.fields_by_name['ack'].containing_oneof = _TLRESPONSE.oneofs_by_name['payload']
_TLRESPONSE.oneofs_by_name['payload'].fields.append(
  _TLRESPONSE.fields_by_name['internalServerError'])
_TLRESPONSE.fields_by_name['internalServerError'].containing_oneof = _TLRESPONSE.oneofs_by_name['payload']
_CHUNKHEADER.fields_by_name['sender'].message_type = _NODE
_CHUNK.fields_by_name['header'].message_type = _CHUNKHEADER
_CHUNK.fields_by_name['data'].message_type = _CHUNKDATA
_CHUNK.oneofs_by_name['content'].fields.append(
  _CHUNK.fields_by_name['header'])
_CHUNK.fields_by_name['header'].containing_oneof = _CHUNK.oneofs_by_name['content']
_CHUNK.oneofs_by_name['content'].fields.append(
  _CHUNK.fields_by_name['data'])
_CHUNK.fields_by_name['data'].containing_oneof = _CHUNK.oneofs_by_name['content']
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Heartbeat'] = _HEARTBEAT
DESCRIPTOR.message_types_by_name['HeartbeatResponse'] = _HEARTBEATRESPONSE
DESCRIPTOR.message_types_by_name['ProtocolHandshake'] = _PROTOCOLHANDSHAKE
DESCRIPTOR.message_types_by_name['ProtocolHandshakeResponse'] = _PROTOCOLHANDSHAKERESPONSE
DESCRIPTOR.message_types_by_name['Packet'] = _PACKET
DESCRIPTOR.message_types_by_name['Disconnect'] = _DISCONNECT
DESCRIPTOR.message_types_by_name['Protocol'] = _PROTOCOL
DESCRIPTOR.message_types_by_name['TLRequest'] = _TLREQUEST
DESCRIPTOR.message_types_by_name['InternalServerError'] = _INTERNALSERVERERROR
DESCRIPTOR.message_types_by_name['Ack'] = _ACK
DESCRIPTOR.message_types_by_name['TLResponse'] = _TLRESPONSE
DESCRIPTOR.message_types_by_name['ChunkHeader'] = _CHUNKHEADER
DESCRIPTOR.message_types_by_name['ChunkData'] = _CHUNKDATA
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.Node)
  })
_sym_db.RegisterMessage(Node)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.Header)
  })
_sym_db.RegisterMessage(Header)

Heartbeat = _reflection.GeneratedProtocolMessageType('Heartbeat', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEAT,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.Heartbeat)
  })
_sym_db.RegisterMessage(Heartbeat)

HeartbeatResponse = _reflection.GeneratedProtocolMessageType('HeartbeatResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATRESPONSE,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.HeartbeatResponse)
  })
_sym_db.RegisterMessage(HeartbeatResponse)

ProtocolHandshake = _reflection.GeneratedProtocolMessageType('ProtocolHandshake', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLHANDSHAKE,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.ProtocolHandshake)
  })
_sym_db.RegisterMessage(ProtocolHandshake)

ProtocolHandshakeResponse = _reflection.GeneratedProtocolMessageType('ProtocolHandshakeResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLHANDSHAKERESPONSE,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.ProtocolHandshakeResponse)
  })
_sym_db.RegisterMessage(ProtocolHandshakeResponse)

Packet = _reflection.GeneratedProtocolMessageType('Packet', (_message.Message,), {
  'DESCRIPTOR' : _PACKET,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.Packet)
  })
_sym_db.RegisterMessage(Packet)

Disconnect = _reflection.GeneratedProtocolMessageType('Disconnect', (_message.Message,), {
  'DESCRIPTOR' : _DISCONNECT,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.Disconnect)
  })
_sym_db.RegisterMessage(Disconnect)

Protocol = _reflection.GeneratedProtocolMessageType('Protocol', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOL,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.Protocol)
  })
_sym_db.RegisterMessage(Protocol)

TLRequest = _reflection.GeneratedProtocolMessageType('TLRequest', (_message.Message,), {
  'DESCRIPTOR' : _TLREQUEST,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.TLRequest)
  })
_sym_db.RegisterMessage(TLRequest)

InternalServerError = _reflection.GeneratedProtocolMessageType('InternalServerError', (_message.Message,), {
  'DESCRIPTOR' : _INTERNALSERVERERROR,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.InternalServerError)
  })
_sym_db.RegisterMessage(InternalServerError)

Ack = _reflection.GeneratedProtocolMessageType('Ack', (_message.Message,), {
  'DESCRIPTOR' : _ACK,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.Ack)
  })
_sym_db.RegisterMessage(Ack)

TLResponse = _reflection.GeneratedProtocolMessageType('TLResponse', (_message.Message,), {
  'DESCRIPTOR' : _TLRESPONSE,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.TLResponse)
  })
_sym_db.RegisterMessage(TLResponse)

ChunkHeader = _reflection.GeneratedProtocolMessageType('ChunkHeader', (_message.Message,), {
  'DESCRIPTOR' : _CHUNKHEADER,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.ChunkHeader)
  })
_sym_db.RegisterMessage(ChunkHeader)

ChunkData = _reflection.GeneratedProtocolMessageType('ChunkData', (_message.Message,), {
  'DESCRIPTOR' : _CHUNKDATA,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.ChunkData)
  })
_sym_db.RegisterMessage(ChunkData)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'routing_pb2'
  # @@protoc_insertion_point(class_scope:routing.Chunk)
  })
_sym_db.RegisterMessage(Chunk)


DESCRIPTOR._options = None

_TRANSPORTLAYER = _descriptor.ServiceDescriptor(
  name='TransportLayer',
  full_name='routing.TransportLayer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1177,
  serialized_end=1295,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='routing.TransportLayer.Send',
    index=0,
    containing_service=None,
    input_type=_TLREQUEST,
    output_type=_TLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Stream',
    full_name='routing.TransportLayer.Stream',
    index=1,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_TLRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSPORTLAYER)

DESCRIPTOR.services_by_name['TransportLayer'] = _TRANSPORTLAYER

# @@protoc_insertion_point(module_scope)
