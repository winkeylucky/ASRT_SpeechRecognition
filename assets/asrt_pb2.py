# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: asrt.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='asrt.proto',
    package='asrt',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\nasrt.proto\x12\x04\x61srt\"0\n\rSpeechRequest\x12\x1f\n\x08wav_data\x18\x01 \x01(\x0b\x32\r.asrt.WavData\"R\n\x0eSpeechResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\x12\x16\n\x0estatus_message\x18\x02 \x01(\t\x12\x13\n\x0bresult_data\x18\x03 \x03(\t\"\"\n\x0fLanguageRequest\x12\x0f\n\x07pinyins\x18\x01 \x03(\t\"P\n\x0cTextResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\x12\x16\n\x0estatus_message\x18\x02 \x01(\t\x12\x13\n\x0btext_result\x18\x03 \x01(\t\"U\n\x07WavData\x12\x0f\n\x07samples\x18\x01 \x01(\x0c\x12\x13\n\x0bsample_rate\x18\x02 \x01(\x05\x12\x10\n\x08\x63hannels\x18\x03 \x01(\x05\x12\x12\n\nbyte_width\x18\x04 \x01(\x05\x32\xec\x01\n\x0f\x41srtGrpcService\x12\x35\n\x06Speech\x12\x13.asrt.SpeechRequest\x1a\x14.asrt.SpeechResponse\"\x00\x12\x37\n\x08Language\x12\x15.asrt.LanguageRequest\x1a\x12.asrt.TextResponse\"\x00\x12\x30\n\x03\x41ll\x12\x13.asrt.SpeechRequest\x1a\x12.asrt.TextResponse\"\x00\x12\x37\n\x06Stream\x12\x13.asrt.SpeechRequest\x1a\x12.asrt.TextResponse\"\x00(\x01\x30\x01\x62\x06proto3'
)

_SPEECHREQUEST = _descriptor.Descriptor(
    name='SpeechRequest',
    full_name='asrt.SpeechRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='wav_data', full_name='asrt.SpeechRequest.wav_data', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_start=20,
    serialized_end=68,
)

_SPEECHRESPONSE = _descriptor.Descriptor(
    name='SpeechResponse',
    full_name='asrt.SpeechResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='status_code', full_name='asrt.SpeechResponse.status_code', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='status_message', full_name='asrt.SpeechResponse.status_message', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='result_data', full_name='asrt.SpeechResponse.result_data', index=2,
            number=3, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_end=152,
)

_LANGUAGEREQUEST = _descriptor.Descriptor(
    name='LanguageRequest',
    full_name='asrt.LanguageRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='pinyins', full_name='asrt.LanguageRequest.pinyins', index=0,
            number=1, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_start=154,
    serialized_end=188,
)

_TEXTRESPONSE = _descriptor.Descriptor(
    name='TextResponse',
    full_name='asrt.TextResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='status_code', full_name='asrt.TextResponse.status_code', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='status_message', full_name='asrt.TextResponse.status_message', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='text_result', full_name='asrt.TextResponse.text_result', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_start=190,
    serialized_end=270,
)

_WAVDATA = _descriptor.Descriptor(
    name='WavData',
    full_name='asrt.WavData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='samples', full_name='asrt.WavData.samples', index=0,
            number=1, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=b"",
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='sample_rate', full_name='asrt.WavData.sample_rate', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='channels', full_name='asrt.WavData.channels', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='byte_width', full_name='asrt.WavData.byte_width', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_start=272,
    serialized_end=357,
)

_SPEECHREQUEST.fields_by_name['wav_data'].message_type = _WAVDATA
DESCRIPTOR.message_types_by_name['SpeechRequest'] = _SPEECHREQUEST
DESCRIPTOR.message_types_by_name['SpeechResponse'] = _SPEECHRESPONSE
DESCRIPTOR.message_types_by_name['LanguageRequest'] = _LANGUAGEREQUEST
DESCRIPTOR.message_types_by_name['TextResponse'] = _TEXTRESPONSE
DESCRIPTOR.message_types_by_name['WavData'] = _WAVDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpeechRequest = _reflection.GeneratedProtocolMessageType('SpeechRequest', (_message.Message,), {
    'DESCRIPTOR': _SPEECHREQUEST,
    '__module__': 'asrt_pb2'
    # @@protoc_insertion_point(class_scope:asrt.SpeechRequest)
})
_sym_db.RegisterMessage(SpeechRequest)

SpeechResponse = _reflection.GeneratedProtocolMessageType('SpeechResponse', (_message.Message,), {
    'DESCRIPTOR': _SPEECHRESPONSE,
    '__module__': 'asrt_pb2'
    # @@protoc_insertion_point(class_scope:asrt.SpeechResponse)
})
_sym_db.RegisterMessage(SpeechResponse)

LanguageRequest = _reflection.GeneratedProtocolMessageType('LanguageRequest', (_message.Message,), {
    'DESCRIPTOR': _LANGUAGEREQUEST,
    '__module__': 'asrt_pb2'
    # @@protoc_insertion_point(class_scope:asrt.LanguageRequest)
})
_sym_db.RegisterMessage(LanguageRequest)

TextResponse = _reflection.GeneratedProtocolMessageType('TextResponse', (_message.Message,), {
    'DESCRIPTOR': _TEXTRESPONSE,
    '__module__': 'asrt_pb2'
    # @@protoc_insertion_point(class_scope:asrt.TextResponse)
})
_sym_db.RegisterMessage(TextResponse)

WavData = _reflection.GeneratedProtocolMessageType('WavData', (_message.Message,), {
    'DESCRIPTOR': _WAVDATA,
    '__module__': 'asrt_pb2'
    # @@protoc_insertion_point(class_scope:asrt.WavData)
})
_sym_db.RegisterMessage(WavData)

_ASRTGRPCSERVICE = _descriptor.ServiceDescriptor(
    name='AsrtGrpcService',
    full_name='asrt.AsrtGrpcService',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=360,
    serialized_end=596,
    methods=[
        _descriptor.MethodDescriptor(
            name='Speech',
            full_name='asrt.AsrtGrpcService.Speech',
            index=0,
            containing_service=None,
            input_type=_SPEECHREQUEST,
            output_type=_SPEECHRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='Language',
            full_name='asrt.AsrtGrpcService.Language',
            index=1,
            containing_service=None,
            input_type=_LANGUAGEREQUEST,
            output_type=_TEXTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='All',
            full_name='asrt.AsrtGrpcService.All',
            index=2,
            containing_service=None,
            input_type=_SPEECHREQUEST,
            output_type=_TEXTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='Stream',
            full_name='asrt.AsrtGrpcService.Stream',
            index=3,
            containing_service=None,
            input_type=_SPEECHREQUEST,
            output_type=_TEXTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_ASRTGRPCSERVICE)

DESCRIPTOR.services_by_name['AsrtGrpcService'] = _ASRTGRPCSERVICE

# @@protoc_insertion_point(module_scope)
