# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from .DeployServiceCommon_pb2 import (
    BlockInfo as DeployServiceCommon_pb2___BlockInfo,
    ContinuationsWithBlockInfo as DeployServiceCommon_pb2___ContinuationsWithBlockInfo,
    DataWithBlockInfo as DeployServiceCommon_pb2___DataWithBlockInfo,
    LightBlockInfo as DeployServiceCommon_pb2___LightBlockInfo,
)

from .ServiceError_pb2 import (
    ServiceError as ServiceError_pb2___ServiceError,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class DeployResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    result = ... # type: typing___Text

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        result : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> DeployResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"error",u"message",u"result"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",u"message",u"result"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"result",b"result"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"result",b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","result"]: ...

class BlockResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    @property
    def blockInfo(self) -> DeployServiceCommon_pb2___BlockInfo: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        blockInfo : typing___Optional[DeployServiceCommon_pb2___BlockInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> BlockResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",u"error",u"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",u"error",u"message"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo",u"error",b"error",u"message",b"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo",u"error",b"error",u"message",b"message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","blockInfo"]: ...

class VisualizeBlocksResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    content = ... # type: typing___Text

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        content : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> VisualizeBlocksResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"content",u"error",u"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"content",u"error",u"message"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"content",b"content",u"error",b"error",u"message",b"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"content",b"content",u"error",b"error",u"message",b"message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","content"]: ...

class MachineVerifyResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    content = ... # type: typing___Text

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        content : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> MachineVerifyResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"content",u"error",u"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"content",u"error",u"message"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"content",b"content",u"error",b"error",u"message",b"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"content",b"content",u"error",b"error",u"message",b"message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","content"]: ...

class BlockInfoResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    @property
    def blockInfo(self) -> DeployServiceCommon_pb2___LightBlockInfo: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        blockInfo : typing___Optional[DeployServiceCommon_pb2___LightBlockInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> BlockInfoResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",u"error",u"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",u"error",u"message"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo",u"error",b"error",u"message",b"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo",u"error",b"error",u"message",b"message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","blockInfo"]: ...

class ListeningNameDataResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    @property
    def payload(self) -> ListeningNameDataPayload: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        payload : typing___Optional[ListeningNameDataPayload] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> ListeningNameDataResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"error",u"message",u"payload"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",u"message",u"payload"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"payload",b"payload"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"payload",b"payload"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","payload"]: ...

class ListeningNameDataPayload(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    length = ... # type: builtin___int

    @property
    def blockInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DeployServiceCommon_pb2___DataWithBlockInfo]: ...

    def __init__(self,
        *,
        blockInfo : typing___Optional[typing___Iterable[DeployServiceCommon_pb2___DataWithBlockInfo]] = None,
        length : typing___Optional[builtin___int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> ListeningNameDataPayload: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",u"length"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo",u"length",b"length"]) -> None: ...

class ContinuationAtNameResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    @property
    def payload(self) -> ContinuationAtNamePayload: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        payload : typing___Optional[ContinuationAtNamePayload] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> ContinuationAtNameResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"error",u"message",u"payload"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",u"message",u"payload"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"payload",b"payload"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"payload",b"payload"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","payload"]: ...

class ContinuationAtNamePayload(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    length = ... # type: builtin___int

    @property
    def blockResults(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DeployServiceCommon_pb2___ContinuationsWithBlockInfo]: ...

    def __init__(self,
        *,
        blockResults : typing___Optional[typing___Iterable[DeployServiceCommon_pb2___ContinuationsWithBlockInfo]] = None,
        length : typing___Optional[builtin___int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> ContinuationAtNamePayload: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"blockResults",u"length"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"blockResults",b"blockResults",u"length",b"length"]) -> None: ...

class FindDeployResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    @property
    def blockInfo(self) -> DeployServiceCommon_pb2___LightBlockInfo: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        blockInfo : typing___Optional[DeployServiceCommon_pb2___LightBlockInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> FindDeployResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",u"error",u"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",u"error",u"message"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo",u"error",b"error",u"message",b"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo",u"error",b"error",u"message",b"message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","blockInfo"]: ...

class PrivateNamePreviewResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    @property
    def payload(self) -> PrivateNamePreviewPayload: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        payload : typing___Optional[PrivateNamePreviewPayload] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> PrivateNamePreviewResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"error",u"message",u"payload"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",u"message",u"payload"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"payload",b"payload"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"payload",b"payload"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","payload"]: ...

class PrivateNamePreviewPayload(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ids = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bytes]

    def __init__(self,
        *,
        ids : typing___Optional[typing___Iterable[builtin___bytes]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> PrivateNamePreviewPayload: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"ids"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"ids",b"ids"]) -> None: ...

class LastFinalizedBlockResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    @property
    def blockInfo(self) -> DeployServiceCommon_pb2___BlockInfo: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        blockInfo : typing___Optional[DeployServiceCommon_pb2___BlockInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> LastFinalizedBlockResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",u"error",u"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",u"error",u"message"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo",u"error",b"error",u"message",b"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockInfo",b"blockInfo",u"error",b"error",u"message",b"message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","blockInfo"]: ...

class IsFinalizedResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    isFinalized = ... # type: builtin___bool

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        isFinalized : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> IsFinalizedResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"error",u"isFinalized",u"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",u"isFinalized",u"message"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"error",b"error",u"isFinalized",b"isFinalized",u"message",b"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"isFinalized",b"isFinalized",u"message",b"message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","isFinalized"]: ...

class BondStatusResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    isBonded = ... # type: builtin___bool

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        isBonded : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> BondStatusResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"error",u"isBonded",u"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",u"isBonded",u"message"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"error",b"error",u"isBonded",b"isBonded",u"message",b"message"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"isBonded",b"isBonded",u"message",b"message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","isBonded"]: ...
