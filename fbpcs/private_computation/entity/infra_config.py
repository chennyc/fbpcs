# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from dataclasses import dataclass
from enum import Enum

from dataclasses_json import dataclass_json
from fbpcs.private_computation.entity.private_computation_status import (
    PrivateComputationInstanceStatus,
)


class PrivateComputationRole(Enum):
    PUBLISHER = "PUBLISHER"
    PARTNER = "PARTNER"


@dataclass_json
@dataclass
class InfraConfig:
    """Stores metadata of infra config in a private computation instance

    Public attributes:

    Private attributes:

    """

    instance_id: str
    role: PrivateComputationRole
    status: PrivateComputationInstanceStatus
    status_update_ts: int