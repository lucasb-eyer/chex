# Copyright 2020 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Pytypes for arrays and scalars."""

from typing import Any, Iterable, Mapping, Tuple, Union
import jax
import jax.numpy as jnp
import numpy as np

Array = jnp.ndarray
ArrayBatched = jax.interpreters.batching.BatchTracer
ArrayNumpy = np.ndarray
ArraySharded = jax.interpreters.pxla.ShardedDeviceArray
# Use this type for type annotation. For instance checking,  use
# `isinstance(x, jax.DeviceArray)`.
# `jax.interpreters.xla._DeviceArray` appears in jax > 0.2.5
if hasattr(jax.interpreters.xla, '_DeviceArray'):
  ArrayDevice = jax.interpreters.xla._DeviceArray  # pylint:disable=protected-access
else:
  ArrayDevice = jax.interpreters.xla.DeviceArray

Scalar = Union[float, int]
Numeric = Union[Array, Scalar]
PRNGKey = Array
PyTreeDef = type(jax.tree_structure(None))
Shape = Tuple[int, ...]

CpuDevice = jax.lib.xla_extension.CpuDevice
GpuDevice = jax.lib.xla_extension.GpuDevice
TpuDevice = jax.lib.xla_extension.TpuDevice
Device = Union[CpuDevice, GpuDevice, TpuDevice]

# As of 06/2020 pytype doesn't support recursive types (see b/109648354)
# pytype: disable=not-supported-yet
ArrayTree = Union[Array, Iterable['ArrayTree'], Mapping[Any, 'ArrayTree']]

ArrayDType = jax.numpy.lax_numpy._ScalarMeta  # pylint: disable=protected-access
