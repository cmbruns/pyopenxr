xr.utils
========

High-level utilities and abstractions for OpenXR integration.

The ``xr.utils`` module provides ergonomic helpers and glue code that complement the low-level OpenXR API exposed in ``xr``. While ``xr`` aims to mirror the native OpenXR specification as closely as possible, ``xr.utils`` offers higher-level constructs that simplify common workflows such as matrix manipulation, swapchain management, and pose utilities.

.. warning::
   The API surface of ``xr.utils`` is provisional and may evolve more rapidly than the stable ``xr`` namespace. Use with awareness of potential changes.

Contents
--------

.. automodule:: xr.utils
   :members:
   :undoc-members:
   :show-inheritance:

Related Modules
---------------

- :mod:`xr` — Core OpenXR bindings
- :mod:`xr.ext` — Extension modules for OpenXR (e.g., ``XR_KHR_opengl_enable``)
