/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.7-dev */

#ifndef PB_UNIFYING_PROTOCOL_UNIFYING_UNIFYING_PB_H_INCLUDED
#define PB_UNIFYING_PROTOCOL_UNIFYING_UNIFYING_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

/* Enum definitions */
typedef enum _unifying_UnifyingCommand { /* *
 Low-level commands */
    /* Set Node address. */
    unifying_UnifyingCommand_SetNodeAddress = 0, 
    /* Sniff packets. */
    unifying_UnifyingCommand_Sniff = 1, 
    /* Jam packets. */
    unifying_UnifyingCommand_Jam = 2, 
    /* Send packets. */
    unifying_UnifyingCommand_Send = 3, 
    unifying_UnifyingCommand_SendRaw = 4, 
    /* Logitech Dongle (ESB PRX) mode. */
    unifying_UnifyingCommand_LogitechDongleMode = 5, 
    /* Logitech Keyboard (PTX) mode. */
    unifying_UnifyingCommand_LogitechKeyboardMode = 6, 
    /* Logitech Mouse (PTX) mode. */
    unifying_UnifyingCommand_LogitechMouseMode = 7, 
    /* Start and Stop commands shared with node-related mode. */
    unifying_UnifyingCommand_Start = 8, 
    unifying_UnifyingCommand_Stop = 9 
} unifying_UnifyingCommand;

/* Struct definitions */
/* *
 StartCmd

 Enable node-related modes. */
typedef struct _unifying_StartCmd { 
    char dummy_field;
} unifying_StartCmd;

/* *
 StopCmd

 Disable node-related modes. */
typedef struct _unifying_StopCmd { 
    char dummy_field;
} unifying_StopCmd;

typedef struct _unifying_JamCmd { 
    uint32_t channel;
} unifying_JamCmd;

typedef struct _unifying_Jammed { 
    uint32_t timestamp;
} unifying_Jammed;

/* *
 LogitechDongleMode

 Enable Logitech Dongle (ESB PRX) mode. */
typedef struct _unifying_LogitechDongleModeCmd { 
    uint32_t channel;
} unifying_LogitechDongleModeCmd;

/* *
 LogitechKeyboardMode

 Enable Logitech Keyboard (ESB PTX) mode. */
typedef struct _unifying_LogitechKeyboardModeCmd { 
    uint32_t channel;
} unifying_LogitechKeyboardModeCmd;

/* *
 LogitechMouseMode

 Enable Logitech Mouse (ESB PTX) mode. */
typedef struct _unifying_LogitechMouseModeCmd { 
    uint32_t channel;
} unifying_LogitechMouseModeCmd;

typedef PB_BYTES_ARRAY_T(5) unifying_PduReceived_address_t;
typedef PB_BYTES_ARRAY_T(255) unifying_PduReceived_pdu_t;
typedef struct _unifying_PduReceived { 
    uint32_t channel;
    bool has_rssi;
    int32_t rssi;
    bool has_timestamp;
    uint32_t timestamp;
    bool has_crc_validity;
    bool crc_validity;
    bool has_address;
    unifying_PduReceived_address_t address;
    unifying_PduReceived_pdu_t pdu;
} unifying_PduReceived;

typedef PB_BYTES_ARRAY_T(5) unifying_RawPduReceived_address_t;
typedef PB_BYTES_ARRAY_T(255) unifying_RawPduReceived_pdu_t;
typedef struct _unifying_RawPduReceived { 
    uint32_t channel;
    bool has_rssi;
    int32_t rssi;
    bool has_timestamp;
    uint32_t timestamp;
    bool has_crc_validity;
    bool crc_validity;
    bool has_address;
    unifying_RawPduReceived_address_t address;
    unifying_RawPduReceived_pdu_t pdu;
} unifying_RawPduReceived;

typedef PB_BYTES_ARRAY_T(255) unifying_SendCmd_pdu_t;
/* *
 SendCmd

 Transmit Logitech Unifying packets on a single channel. */
typedef struct _unifying_SendCmd { 
    uint32_t channel;
    unifying_SendCmd_pdu_t pdu;
} unifying_SendCmd;

typedef PB_BYTES_ARRAY_T(255) unifying_SendRawCmd_pdu_t;
typedef struct _unifying_SendRawCmd { 
    uint32_t channel;
    unifying_SendRawCmd_pdu_t pdu;
} unifying_SendRawCmd;

typedef PB_BYTES_ARRAY_T(5) unifying_SetNodeAddressCmd_address_t;
typedef struct _unifying_SetNodeAddressCmd { 
    unifying_SetNodeAddressCmd_address_t address;
} unifying_SetNodeAddressCmd;

typedef PB_BYTES_ARRAY_T(5) unifying_SniffCmd_address_t;
typedef struct _unifying_SniffCmd { 
    /* Channel can be specified, the device will only
listen on this specific channel. */
    uint32_t channel; /* special value: 0xFF (autofind) */
    unifying_SniffCmd_address_t address;
    bool show_acknowledgements;
} unifying_SniffCmd;

typedef struct _unifying_Message { 
    pb_size_t which_msg;
    union {
        /* Messages */
        unifying_SetNodeAddressCmd set_node_addr;
        unifying_SniffCmd sniff;
        unifying_JamCmd jam;
        unifying_SendCmd send;
        unifying_SendRawCmd send_raw;
        unifying_LogitechDongleModeCmd dongle;
        unifying_LogitechKeyboardModeCmd keyboard;
        unifying_LogitechKeyboardModeCmd mouse;
        unifying_StartCmd start;
        unifying_StopCmd stop;
        /* Notifications */
        unifying_Jammed jammed;
        unifying_RawPduReceived raw_pdu;
        unifying_PduReceived pdu;
    } msg;
} unifying_Message;


/* Helper constants for enums */
#define _unifying_UnifyingCommand_MIN unifying_UnifyingCommand_SetNodeAddress
#define _unifying_UnifyingCommand_MAX unifying_UnifyingCommand_Stop
#define _unifying_UnifyingCommand_ARRAYSIZE ((unifying_UnifyingCommand)(unifying_UnifyingCommand_Stop+1))


#ifdef __cplusplus
extern "C" {
#endif

/* Initializer values for message structs */
#define unifying_SetNodeAddressCmd_init_default  {{0, {0}}}
#define unifying_SniffCmd_init_default           {0, {0, {0}}, 0}
#define unifying_JamCmd_init_default             {0}
#define unifying_SendCmd_init_default            {0, {0, {0}}}
#define unifying_SendRawCmd_init_default         {0, {0, {0}}}
#define unifying_LogitechDongleModeCmd_init_default {0}
#define unifying_LogitechKeyboardModeCmd_init_default {0}
#define unifying_LogitechMouseModeCmd_init_default {0}
#define unifying_StartCmd_init_default           {0}
#define unifying_StopCmd_init_default            {0}
#define unifying_Jammed_init_default             {0}
#define unifying_RawPduReceived_init_default     {0, false, 0, false, 0, false, 0, false, {0, {0}}, {0, {0}}}
#define unifying_PduReceived_init_default        {0, false, 0, false, 0, false, 0, false, {0, {0}}, {0, {0}}}
#define unifying_Message_init_default            {0, {unifying_SetNodeAddressCmd_init_default}}
#define unifying_SetNodeAddressCmd_init_zero     {{0, {0}}}
#define unifying_SniffCmd_init_zero              {0, {0, {0}}, 0}
#define unifying_JamCmd_init_zero                {0}
#define unifying_SendCmd_init_zero               {0, {0, {0}}}
#define unifying_SendRawCmd_init_zero            {0, {0, {0}}}
#define unifying_LogitechDongleModeCmd_init_zero {0}
#define unifying_LogitechKeyboardModeCmd_init_zero {0}
#define unifying_LogitechMouseModeCmd_init_zero  {0}
#define unifying_StartCmd_init_zero              {0}
#define unifying_StopCmd_init_zero               {0}
#define unifying_Jammed_init_zero                {0}
#define unifying_RawPduReceived_init_zero        {0, false, 0, false, 0, false, 0, false, {0, {0}}, {0, {0}}}
#define unifying_PduReceived_init_zero           {0, false, 0, false, 0, false, 0, false, {0, {0}}, {0, {0}}}
#define unifying_Message_init_zero               {0, {unifying_SetNodeAddressCmd_init_zero}}

/* Field tags (for use in manual encoding/decoding) */
#define unifying_JamCmd_channel_tag              1
#define unifying_Jammed_timestamp_tag            1
#define unifying_LogitechDongleModeCmd_channel_tag 1
#define unifying_LogitechKeyboardModeCmd_channel_tag 1
#define unifying_LogitechMouseModeCmd_channel_tag 1
#define unifying_PduReceived_channel_tag         1
#define unifying_PduReceived_rssi_tag            2
#define unifying_PduReceived_timestamp_tag       3
#define unifying_PduReceived_crc_validity_tag    4
#define unifying_PduReceived_address_tag         5
#define unifying_PduReceived_pdu_tag             6
#define unifying_RawPduReceived_channel_tag      1
#define unifying_RawPduReceived_rssi_tag         2
#define unifying_RawPduReceived_timestamp_tag    3
#define unifying_RawPduReceived_crc_validity_tag 4
#define unifying_RawPduReceived_address_tag      5
#define unifying_RawPduReceived_pdu_tag          6
#define unifying_SendCmd_channel_tag             1
#define unifying_SendCmd_pdu_tag                 2
#define unifying_SendRawCmd_channel_tag          1
#define unifying_SendRawCmd_pdu_tag              2
#define unifying_SetNodeAddressCmd_address_tag   1
#define unifying_SniffCmd_channel_tag            1
#define unifying_SniffCmd_address_tag            2
#define unifying_SniffCmd_show_acknowledgements_tag 3
#define unifying_Message_set_node_addr_tag       1
#define unifying_Message_sniff_tag               2
#define unifying_Message_jam_tag                 3
#define unifying_Message_send_tag                4
#define unifying_Message_send_raw_tag            5
#define unifying_Message_dongle_tag              6
#define unifying_Message_keyboard_tag            7
#define unifying_Message_mouse_tag               8
#define unifying_Message_start_tag               9
#define unifying_Message_stop_tag                10
#define unifying_Message_jammed_tag              11
#define unifying_Message_raw_pdu_tag             12
#define unifying_Message_pdu_tag                 13

/* Struct field encoding specification for nanopb */
#define unifying_SetNodeAddressCmd_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, BYTES,    address,           1)
#define unifying_SetNodeAddressCmd_CALLBACK NULL
#define unifying_SetNodeAddressCmd_DEFAULT NULL

#define unifying_SniffCmd_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   channel,           1) \
X(a, STATIC,   SINGULAR, BYTES,    address,           2) \
X(a, STATIC,   SINGULAR, BOOL,     show_acknowledgements,   3)
#define unifying_SniffCmd_CALLBACK NULL
#define unifying_SniffCmd_DEFAULT NULL

#define unifying_JamCmd_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   channel,           1)
#define unifying_JamCmd_CALLBACK NULL
#define unifying_JamCmd_DEFAULT NULL

#define unifying_SendCmd_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   channel,           1) \
X(a, STATIC,   SINGULAR, BYTES,    pdu,               2)
#define unifying_SendCmd_CALLBACK NULL
#define unifying_SendCmd_DEFAULT NULL

#define unifying_SendRawCmd_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   channel,           1) \
X(a, STATIC,   SINGULAR, BYTES,    pdu,               2)
#define unifying_SendRawCmd_CALLBACK NULL
#define unifying_SendRawCmd_DEFAULT NULL

#define unifying_LogitechDongleModeCmd_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   channel,           1)
#define unifying_LogitechDongleModeCmd_CALLBACK NULL
#define unifying_LogitechDongleModeCmd_DEFAULT NULL

#define unifying_LogitechKeyboardModeCmd_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   channel,           1)
#define unifying_LogitechKeyboardModeCmd_CALLBACK NULL
#define unifying_LogitechKeyboardModeCmd_DEFAULT NULL

#define unifying_LogitechMouseModeCmd_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   channel,           1)
#define unifying_LogitechMouseModeCmd_CALLBACK NULL
#define unifying_LogitechMouseModeCmd_DEFAULT NULL

#define unifying_StartCmd_FIELDLIST(X, a) \

#define unifying_StartCmd_CALLBACK NULL
#define unifying_StartCmd_DEFAULT NULL

#define unifying_StopCmd_FIELDLIST(X, a) \

#define unifying_StopCmd_CALLBACK NULL
#define unifying_StopCmd_DEFAULT NULL

#define unifying_Jammed_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   timestamp,         1)
#define unifying_Jammed_CALLBACK NULL
#define unifying_Jammed_DEFAULT NULL

#define unifying_RawPduReceived_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   channel,           1) \
X(a, STATIC,   OPTIONAL, INT32,    rssi,              2) \
X(a, STATIC,   OPTIONAL, UINT32,   timestamp,         3) \
X(a, STATIC,   OPTIONAL, BOOL,     crc_validity,      4) \
X(a, STATIC,   OPTIONAL, BYTES,    address,           5) \
X(a, STATIC,   SINGULAR, BYTES,    pdu,               6)
#define unifying_RawPduReceived_CALLBACK NULL
#define unifying_RawPduReceived_DEFAULT NULL

#define unifying_PduReceived_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   channel,           1) \
X(a, STATIC,   OPTIONAL, INT32,    rssi,              2) \
X(a, STATIC,   OPTIONAL, UINT32,   timestamp,         3) \
X(a, STATIC,   OPTIONAL, BOOL,     crc_validity,      4) \
X(a, STATIC,   OPTIONAL, BYTES,    address,           5) \
X(a, STATIC,   SINGULAR, BYTES,    pdu,               6)
#define unifying_PduReceived_CALLBACK NULL
#define unifying_PduReceived_DEFAULT NULL

#define unifying_Message_FIELDLIST(X, a) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,set_node_addr,msg.set_node_addr),   1) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,sniff,msg.sniff),   2) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,jam,msg.jam),   3) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,send,msg.send),   4) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,send_raw,msg.send_raw),   5) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,dongle,msg.dongle),   6) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,keyboard,msg.keyboard),   7) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,mouse,msg.mouse),   8) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,start,msg.start),   9) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,stop,msg.stop),  10) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,jammed,msg.jammed),  11) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,raw_pdu,msg.raw_pdu),  12) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,pdu,msg.pdu),  13)
#define unifying_Message_CALLBACK NULL
#define unifying_Message_DEFAULT NULL
#define unifying_Message_msg_set_node_addr_MSGTYPE unifying_SetNodeAddressCmd
#define unifying_Message_msg_sniff_MSGTYPE unifying_SniffCmd
#define unifying_Message_msg_jam_MSGTYPE unifying_JamCmd
#define unifying_Message_msg_send_MSGTYPE unifying_SendCmd
#define unifying_Message_msg_send_raw_MSGTYPE unifying_SendRawCmd
#define unifying_Message_msg_dongle_MSGTYPE unifying_LogitechDongleModeCmd
#define unifying_Message_msg_keyboard_MSGTYPE unifying_LogitechKeyboardModeCmd
#define unifying_Message_msg_mouse_MSGTYPE unifying_LogitechKeyboardModeCmd
#define unifying_Message_msg_start_MSGTYPE unifying_StartCmd
#define unifying_Message_msg_stop_MSGTYPE unifying_StopCmd
#define unifying_Message_msg_jammed_MSGTYPE unifying_Jammed
#define unifying_Message_msg_raw_pdu_MSGTYPE unifying_RawPduReceived
#define unifying_Message_msg_pdu_MSGTYPE unifying_PduReceived

extern const pb_msgdesc_t unifying_SetNodeAddressCmd_msg;
extern const pb_msgdesc_t unifying_SniffCmd_msg;
extern const pb_msgdesc_t unifying_JamCmd_msg;
extern const pb_msgdesc_t unifying_SendCmd_msg;
extern const pb_msgdesc_t unifying_SendRawCmd_msg;
extern const pb_msgdesc_t unifying_LogitechDongleModeCmd_msg;
extern const pb_msgdesc_t unifying_LogitechKeyboardModeCmd_msg;
extern const pb_msgdesc_t unifying_LogitechMouseModeCmd_msg;
extern const pb_msgdesc_t unifying_StartCmd_msg;
extern const pb_msgdesc_t unifying_StopCmd_msg;
extern const pb_msgdesc_t unifying_Jammed_msg;
extern const pb_msgdesc_t unifying_RawPduReceived_msg;
extern const pb_msgdesc_t unifying_PduReceived_msg;
extern const pb_msgdesc_t unifying_Message_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define unifying_SetNodeAddressCmd_fields &unifying_SetNodeAddressCmd_msg
#define unifying_SniffCmd_fields &unifying_SniffCmd_msg
#define unifying_JamCmd_fields &unifying_JamCmd_msg
#define unifying_SendCmd_fields &unifying_SendCmd_msg
#define unifying_SendRawCmd_fields &unifying_SendRawCmd_msg
#define unifying_LogitechDongleModeCmd_fields &unifying_LogitechDongleModeCmd_msg
#define unifying_LogitechKeyboardModeCmd_fields &unifying_LogitechKeyboardModeCmd_msg
#define unifying_LogitechMouseModeCmd_fields &unifying_LogitechMouseModeCmd_msg
#define unifying_StartCmd_fields &unifying_StartCmd_msg
#define unifying_StopCmd_fields &unifying_StopCmd_msg
#define unifying_Jammed_fields &unifying_Jammed_msg
#define unifying_RawPduReceived_fields &unifying_RawPduReceived_msg
#define unifying_PduReceived_fields &unifying_PduReceived_msg
#define unifying_Message_fields &unifying_Message_msg

/* Maximum encoded size of messages (where known) */
#define unifying_JamCmd_size                     6
#define unifying_Jammed_size                     6
#define unifying_LogitechDongleModeCmd_size      6
#define unifying_LogitechKeyboardModeCmd_size    6
#define unifying_LogitechMouseModeCmd_size       6
#define unifying_Message_size                    293
#define unifying_PduReceived_size                290
#define unifying_RawPduReceived_size             290
#define unifying_SendCmd_size                    264
#define unifying_SendRawCmd_size                 264
#define unifying_SetNodeAddressCmd_size          7
#define unifying_SniffCmd_size                   15
#define unifying_StartCmd_size                   0
#define unifying_StopCmd_size                    0

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
