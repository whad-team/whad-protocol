WHAD Generic Service
====================

.. _generic_service:

The *Generic Service* provides a set of messages used for generic communication. These messages can be used
by any other service and provides dedicated features to report some information, to specify a status regarding
the hardware device, send debug and verbose information, etc.


Messages
--------

This section details 

CmdResult
~~~~~~~~~

The `CmdResult` message defined in `generic.proto` must be sent by a device to notify the host a command `result`, that
must be one of the `ResultCode` enumeration.

**This message must be sent each time a compatible device have processed an incoming command from the host.**


Progress
~~~~~~~~

The `Progress` message should be used to hold the percentage corresponding to the progress of an underlying operation.
Its `value` **must** be comprised between 0 and 100. 

DebugMsg
~~~~~~~~

The `DebugMsg` message allows the device to send debug information to the host. Each message **must** have a debug `level` and some `data` associated. 

VerboseMsg
~~~~~~~~~~

The `VerboseMsg` message allows the device to send a verbose message to the host. Each message **must** have some data
set.