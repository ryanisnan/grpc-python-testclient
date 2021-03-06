# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: matches.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='matches.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rmatches.proto\"-\n\nScaleScore\x12\x10\n\x08scale_id\x18\x01 \x01(\x05\x12\r\n\x05score\x18\x02 \x01(\x02\"8\n\x13\x43\x61reerHistoryRating\x12\x11\n\tcareer_id\x18\x01 \x01(\x05\x12\x0e\n\x06rating\x18\x02 \x01(\x02\"/\n\x0b\x43\x61reerMatch\x12\x11\n\tcareer_id\x18\x01 \x01(\x05\x12\r\n\x05score\x18\x02 \x01(\x02\"o\n\x14\x43\x61reerMatchesRequest\x12!\n\x0cscale_scores\x18\x01 \x03(\x0b\x32\x0b.ScaleScore\x12\x34\n\x16\x63\x61reer_history_ratings\x18\x02 \x03(\x0b\x32\x14.CareerHistoryRating\"6\n\x15\x43\x61reerMatchesResponse\x12\x1d\n\x07matches\x18\x01 \x03(\x0b\x32\x0c.CareerMatch2U\n\x14\x43\x61reerMatchesService\x12=\n\nGetMatches\x12\x15.CareerMatchesRequest\x1a\x16.CareerMatchesResponse\"\x00\x62\x06proto3')
)




_SCALESCORE = _descriptor.Descriptor(
  name='ScaleScore',
  full_name='ScaleScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scale_id', full_name='ScaleScore.scale_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='ScaleScore.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=62,
)


_CAREERHISTORYRATING = _descriptor.Descriptor(
  name='CareerHistoryRating',
  full_name='CareerHistoryRating',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='career_id', full_name='CareerHistoryRating.career_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rating', full_name='CareerHistoryRating.rating', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=120,
)


_CAREERMATCH = _descriptor.Descriptor(
  name='CareerMatch',
  full_name='CareerMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='career_id', full_name='CareerMatch.career_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='CareerMatch.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=169,
)


_CAREERMATCHESREQUEST = _descriptor.Descriptor(
  name='CareerMatchesRequest',
  full_name='CareerMatchesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scale_scores', full_name='CareerMatchesRequest.scale_scores', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='career_history_ratings', full_name='CareerMatchesRequest.career_history_ratings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=282,
)


_CAREERMATCHESRESPONSE = _descriptor.Descriptor(
  name='CareerMatchesResponse',
  full_name='CareerMatchesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='matches', full_name='CareerMatchesResponse.matches', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=338,
)

_CAREERMATCHESREQUEST.fields_by_name['scale_scores'].message_type = _SCALESCORE
_CAREERMATCHESREQUEST.fields_by_name['career_history_ratings'].message_type = _CAREERHISTORYRATING
_CAREERMATCHESRESPONSE.fields_by_name['matches'].message_type = _CAREERMATCH
DESCRIPTOR.message_types_by_name['ScaleScore'] = _SCALESCORE
DESCRIPTOR.message_types_by_name['CareerHistoryRating'] = _CAREERHISTORYRATING
DESCRIPTOR.message_types_by_name['CareerMatch'] = _CAREERMATCH
DESCRIPTOR.message_types_by_name['CareerMatchesRequest'] = _CAREERMATCHESREQUEST
DESCRIPTOR.message_types_by_name['CareerMatchesResponse'] = _CAREERMATCHESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScaleScore = _reflection.GeneratedProtocolMessageType('ScaleScore', (_message.Message,), dict(
  DESCRIPTOR = _SCALESCORE,
  __module__ = 'matches_pb2'
  # @@protoc_insertion_point(class_scope:ScaleScore)
  ))
_sym_db.RegisterMessage(ScaleScore)

CareerHistoryRating = _reflection.GeneratedProtocolMessageType('CareerHistoryRating', (_message.Message,), dict(
  DESCRIPTOR = _CAREERHISTORYRATING,
  __module__ = 'matches_pb2'
  # @@protoc_insertion_point(class_scope:CareerHistoryRating)
  ))
_sym_db.RegisterMessage(CareerHistoryRating)

CareerMatch = _reflection.GeneratedProtocolMessageType('CareerMatch', (_message.Message,), dict(
  DESCRIPTOR = _CAREERMATCH,
  __module__ = 'matches_pb2'
  # @@protoc_insertion_point(class_scope:CareerMatch)
  ))
_sym_db.RegisterMessage(CareerMatch)

CareerMatchesRequest = _reflection.GeneratedProtocolMessageType('CareerMatchesRequest', (_message.Message,), dict(
  DESCRIPTOR = _CAREERMATCHESREQUEST,
  __module__ = 'matches_pb2'
  # @@protoc_insertion_point(class_scope:CareerMatchesRequest)
  ))
_sym_db.RegisterMessage(CareerMatchesRequest)

CareerMatchesResponse = _reflection.GeneratedProtocolMessageType('CareerMatchesResponse', (_message.Message,), dict(
  DESCRIPTOR = _CAREERMATCHESRESPONSE,
  __module__ = 'matches_pb2'
  # @@protoc_insertion_point(class_scope:CareerMatchesResponse)
  ))
_sym_db.RegisterMessage(CareerMatchesResponse)



_CAREERMATCHESSERVICE = _descriptor.ServiceDescriptor(
  name='CareerMatchesService',
  full_name='CareerMatchesService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=340,
  serialized_end=425,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMatches',
    full_name='CareerMatchesService.GetMatches',
    index=0,
    containing_service=None,
    input_type=_CAREERMATCHESREQUEST,
    output_type=_CAREERMATCHESRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CAREERMATCHESSERVICE)

DESCRIPTOR.services_by_name['CareerMatchesService'] = _CAREERMATCHESSERVICE

# @@protoc_insertion_point(module_scope)
