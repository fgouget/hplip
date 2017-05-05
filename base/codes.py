#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2003-2015 HP Development Company, L.P.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# Author: Don Welch, Naga Samrat Chowdary Narla, Yashwant Sahu
#
#
# NOTE: This module is safe for 'from codes import *'
#


# GUI/Console modes
INTERACTIVE_MODE = 0 # -i
GUI_MODE = 1 # -u
NON_INTERACTIVE_MODE = 2 # -n
BROWSER_MODE = 3 # -w

# Supported UI toolkits
UI_TOOLKIT_QT3 = 0
UI_TOOLKIT_QT4 = 1
UI_TOOLKIT_QT5 = 2
UI_TOOLKIT_GTK = 3 # Not used

# device types (CUPS queue or SANE types)
DEVICE_TYPE_UNKNOWN = 0
DEVICE_TYPE_PRINTER = 1 # hp:
DEVICE_TYPE_SCANNER = 2 # hpaio:
DEVICE_TYPE_FAX = 3     # hpfax:
DEVICE_TYPE_COPIER = 4  # not used

# Error Codes generated by HPMUD or raise Error(code) or func return
# Add 5000 to code for event code
ERROR_SUCCESS = 0
ERROR_UNKNOWN_ERROR = 1
ERROR_DEVICE_NOT_FOUND = 2 # MUD: HPMUD_R_INVALID_DEVICE
ERROR_INVALID_DEVICE_ID = 3 # MUD: HPMUD_R_INVALID_DESCRIPTOR
ERROR_INVALID_DEVICE_URI = 4 # MUD: HPMUD_R_INVALID_URI
ERROR_DATA_LENGTH_EXCEEDS_MAX = 8 # MUD: HPMUD_R_INVALID_LENGTH
ERROR_DEVICE_IO_ERROR = 12 # MUD: HPMUD_R_IO_ERROR
ERROR_NO_PROBED_DEVICES_FOUND = 18
ERROR_DEVICE_BUSY = 21 # MUD: HPMUD_R_DEVICE_BUSY
ERROR_DEVICE_STATUS_NOT_AVAILABLE = 26
ERROR_INVALID_SERVICE_NAME = 28 # MUD: HPMUD_R_INVALID_SN
ERROR_ERROR_INVALID_CHANNEL_ID = 30 # MUD: HPMUD_R_INVALID_CHANNEL_ID
ERROR_CHANNEL_BUSY = 31 # MUD: HPMUD_R_INVALID_STATE
ERROR_DEVICE_DOES_NOT_SUPPORT_OPERATION = 34
ERROR_DEVICEOPEN_FAILED = 37 # MUD: HPMUD_R_INVALID_DEVICE_OPEN
ERROR_INVALID_DEVNODE = 38 # MUD: HPMUD_R_INVALID_DEVICE_NODE
ERROR_INVALID_HOSTNAME = 45 # MUD: HPMUD_R_INVALID_IP
ERROR_INVALID_PORT_NUMBER = 46 # MUD: HPMUD_R_INVALID_IP_PORT
ERROR_INVALID_TIMEOUT = 47 # MUD: HPMUD_R_INVALID_TIMEOUT
ERROR_DATFILE_ERROR = 48 # MUD: HPMUD_R_DATFILE_ERROR
ERROR_IO_TIMEOUT = 49 # MUD: HPMUD_R_IO_TIMEOUT
ERROR_FAX_INCOMPATIBLE_OPTIONS = 50
ERROR_FAX_INVALID_FAX_FILE = 51
ERROR_NO_CUPS_QUEUE_FOUND_FOR_DEVICE = 55
ERROR_FAX_FILE_NOT_FOUND = 57
ERROR_INVALID_ARGUMENT = 58
# --> add new codes here <--
ERROR_INTERNAL = 99
ERROR_FILE_NOT_FOUND = 101
ERROR_DIRECTORY_NOT_FOUND = 102
ERROR_NO_NETWORK = 103
ERROR_CHECKSUM_ERROR = 104
ERROR_GPG_CMD_NOT_FOUND = 105
ERROR_UNABLE_TO_RECV_KEYS = 106
ERROR_DIGITAL_SIGN_NOT_FOUND = 107
ERROR_FAILED_TO_DOWNLOAD_FILE = 107
ERROR_DIGITAL_SIGN_BAD = 108
ERROR_INCORRECT_PASSWORD = 109
ERROR_UNKNOWN_VALIDATION_ERROR = 110
ERROR_NO_SI_DEVICE = 111
ERROR_FAILED_TO_DISABLE_SI = 112



# If you add new codes, also add the appropriate description
# to g.py for exception description strings.
# Thank you, The Management


# Event and status codes
# These are used for the 'status-code' returned by DeviceQuery (STATUS_*)
# and by the event-code used by Event (EVENT_* + STATUS_*)

# If you add a new EVENT/STATUS code, please add the appropriate
# entry into the STATUS_TO_ERROR_STATE_MAP

STATUS_UNKNOWN = 0

EVENT_MIN_USER_EVENT = 500
EVENT_START_PRINT_JOB = 500 # sent by hp: backend
EVENT_END_PRINT_JOB = 501 # sent by hp: backend
EVENT_PRINT_FAILED_MISSING_PLUGIN = 502

ERROR_RUNNING_AS_ROOT = 503

EVENT_START_FAX_PRINT_JOB = 600 # sent by hpfax: backend
EVENT_END_FAX_PRINT_JOB = 601 # sent by hpfax: backend

EVENT_PRINTER_QUEUE_STOPPED = 700
EVENT_PRINTER_QUEUE_STARTED = 701
EVENT_PRINTER_QUEUE_REJECTING_JOBS = 702
EVENT_PRINTER_QUEUE_ACCEPTING_JOBS = 703
EVENT_PRINTER_QUEUE_SET_AS_DEFAULT = 704

EVENT_FAX_QUEUE_STOPPED = 800
EVENT_FAX_QUEUE_STARTED = 801
EVENT_FAX_QUEUE_REJECTING_JOBS = 802
EVENT_FAX_QUEUE_ACCEPTING_JOBS = 803
EVENT_FAX_QUEUE_SET_AS_DEFAULT = 804
EVENT_FAX_FAILED_MISSING_PLUGIN = 805

STATUS_PRINTER_BASE = 1000
STATUS_PRINTER_IDLE = 1000
STATUS_PRINTER_BUSY = 1001
STATUS_PRINTER_PRINTING = 1002
STATUS_PRINTER_TURNING_OFF = 1003
STATUS_PRINTER_REPORT_PRINTING = 1004
STATUS_PRINTER_CANCELING = 1005
STATUS_PRINTER_IO_STALL = 1006
STATUS_PRINTER_DRY_WAIT_TIME = 1007
STATUS_PRINTER_PEN_CHANGE = 1008
STATUS_PRINTER_OUT_OF_PAPER = 1009
STATUS_PRINTER_BANNER_EJECT = 1010
STATUS_PRINTER_BANNER_MISMATCH = 1011
STATUS_PRINTER_PHOTO_MISMATCH = 1012
STATUS_PRINTER_DUPLEX_MISMATCH = 1013
STATUS_PRINTER_MEDIA_JAM = 1014
STATUS_PRINTER_CARRIAGE_STALL = 1015
STATUS_PRINTER_PAPER_STALL = 1016
STATUS_PRINTER_PEN_FAILURE = 1017
STATUS_PRINTER_HARD_ERROR = 1018
STATUS_PRINTER_POWER_DOWN = 1019
STATUS_PRINTER_FRONT_PANEL_TEST = 1020
STATUS_PRINTER_CLEAN_OUT_TRAY_MISSING = 1021
STATUS_PRINTER_OUTPUT_BIN_FULL = 1022
STATUS_PRINTER_MEDIA_SIZE_MISMATCH = 1023
STATUS_PRINTER_MANUAL_DUPLEX_BLOCK = 1024
STATUS_PRINTER_SERVCE_STALL = 1025
STATUS_PRINTER_OUT_OF_INK = 1026 # Also used for out of toner
STATUS_PRINTER_LIO_ERROR = 1027
STATUS_PRINTER_PUMP_STALL = 1028
STATUS_PRINTER_TRAY_2_MISSING = 1029
STATUS_PRINTER_DUPLEXER_MISSING = 1030
STATUS_PRINTER_REAR_TRAY_MISSING = 1031
STATUS_PRINTER_PEN_NOT_LATCHED = 1032
STATUS_PRINTER_BATTERY_VERY_LOW = 1033
STATUS_PRINTER_SPITTOON_FULL = 1034
STATUS_PRINTER_OUTPUT_TRAY_CLOSED = 1035
STATUS_PRINTER_MANUAL_FEED_BLOCKED = 1036
STATUS_PRINTER_REAR_FEED_BLOCKED = 1037
STATUS_PRINTER_TRAY_2_OUT_OF_PAPER = 1038
STATUS_PRINTER_UNABLE_TO_LOAD_FROM_LOCKED_TRAY = 1039
STATUS_PRINTER_NON_HP_INK = 1040
STATUS_PRINTER_PEN_CALIBRATION_RESUME = 1041
STATUS_PRINTER_MEDIA_TYPE_MISMATCH = 1042
STATUS_PRINTER_CUSTOM_MEDIA_MISMATCH = 1043
STATUS_PRINTER_PEN_CLEANING = 1044
STATUS_PRINTER_PEN_CHECKING = 1045
STATUS_PRINTER_POWER_SAVE = 1046
STATUS_PRINTER_CARTRIDGE_WRONG = 1047
STATUS_PRINTER_CARTRIDGE_MISSING = 1048
STATUS_PRINTER_PRINTHEAD_MISSING = 1049

#Alert messages for Pentane products RQ 8888
STATUS_SCANNER_ADF_MISPICK = 1050
STATUS_PRINTER_PAPER_TOO_SHORT_TO_AUTODUPLEX = 1051
STATUS_PRINTER_TRAY_2_3_DOOR_OPEN = 1052
STATUS_PRINTER_INK_TOO_LOW_TO_PRIME = 1053
STATUS_PRINTER_VERY_LOW_ON_INK = 1054
STATUS_PRINTER_SERVICE_INK_CONTAINER_ALMOST_FULL =1055
STATUS_PRINTER_SERVICE_INK_CONTAINER_FULL=1056
STATUS_PRINTER_SERVICE_INK_CONTAINER_FULL_PROMPT=1057
STATUS_PRINTER_DUPLEX_MODULE_MISSING=1058
STATUS_PRINTER_PRINTHEAD_JAM=1059
STATUS_PRINTER_CLEAR_OUTPUT_AREA=1060
STATUS_PRINTER_RESEAT_DUPLEXER=1061
STATUS_MANUALLY_FEED=1062
STATUS_PRINTER_PRINTHEAD_FAILED = 1063
STATUS_PRINTER_PRINTHEAD_INCOMPATIBLE = 1064
STATUS_UNKNOWN_CODE = 1065
STATUS_PRINTER_STOPPED = 1066
STATUS_PRINTER_PAUSED = 1067
STATUS_INPUT_TRAY_MISSING = 1068


# derived codes
# set to AGENT_TYPE + base (base: 1500=ink, 1600=laser )
STATUS_PRINTER_LOW_INK_BASE = 1500
STATUS_PRINTER_LOW_BLACK_INK = 1501
STATUS_PRINTER_LOW_TRI_COLOR_INK = 1502
STATUS_PRINTER_LOW_PHOTO_INK = 1503
STATUS_PRINTER_LOW_CYAN_INK = 1504
STATUS_PRINTER_LOW_MAGENTA_INK = 1505
STATUS_PRINTER_LOW_YELLOW_INK = 1506
STATUS_PRINTER_LOW_PHOTO_CYAN_INK = 1507
STATUS_PRINTER_LOW_PHOTO_MAGENTA_INK = 1508
STATUS_PRINTER_LOW_PHOTO_YELLOW_INK = 1509
STATUS_PRINTER_LOW_PHOTO_GRAY_INK = 1510
STATUS_PRINTER_LOW_PHOTO_BLUE_INK = 1511

STATUS_PRINTER_LOW_TONER_BASE = 1600
STATUS_PRINTER_LOW_BLACK_TONER = 1601
STATUS_PRINTER_LOW_CYAN_TONER = 1604
STATUS_PRINTER_LOW_MAGENTA_TONER = 1605
STATUS_PRINTER_LOW_YELLOW_TONER = 1606
# end

# derived laserjet codes
STATUS_PRINTER_WARMING_UP = 1800
STATUS_PRINTER_LOW_PAPER = 1801
STATUS_PRINTER_DOOR_OPEN = 1802
STATUS_PRINTER_OFFLINE = 1803
STATUS_PRINTER_LOW_TONER = 1804
STATUS_PRINTER_NO_TONER = 1805
STATUS_PRINTER_SERVICE_REQUEST = 1806
STATUS_PRINTER_FUSER_ERROR = 1807
STATUS_PRINTER_EMPTY_TONER = 1808
STATUS_PRINTER_MEDIA_EMPTY_ERROR = 1809
#end

# other derived codes
STATUS_DEVICE_UNSUPPORTED = 1900
#end

# scan
EVENT_START_SCAN_JOB = 2000
EVENT_END_SCAN_JOB = 2001
EVENT_SCANNER_FAIL = 2002
EVENT_SCAN_FAILED_MISSING_PLUGIN = 2003
EVENT_SCAN_ADF_LOADED = 2004
EVENT_SCAN_TO_DESTINATION_NOTSET = 2005
EVENT_SCAN_WAITING_FOR_PC = 2006
EVENT_SCAN_ADF_JAM = 2007
EVENT_SCAN_ADF_DOOR_OPEN = 2008
EVENT_SCAN_CANCEL = 2009
EVENT_SIZE_WARNING = 2010
EVENT_SCAN_ADF_NO_DOCS = 2011
EVENT_SCAN_ADF_MISPICK = 2012
EVENT_SCAN_BUSY = 2013
#end

# fax
EVENT_START_FAX_JOB = 3000
EVENT_END_FAX_JOB = 3001
EVENT_FAX_JOB_FAIL = 3002
EVENT_FAX_JOB_CANCELED = 3003
STATUS_FAX_TX_ACTIVE = 3004
STATUS_FAX_RX_ACTIVE = 3005
EVENT_FAX_DIALING = 3006
EVENT_FAX_CONNECTING = 3007
EVENT_FAX_SEND_ERROR = 3008
EVENT_FAX_ERROR_STORAGE_FULL = 3009
EVENT_FAX_RECV_ERROR =  3010
EVENT_FAX_BLOCKING = 3011
#end

# copy
EVENT_START_COPY_JOB = 4000
EVENT_END_COPY_JOB = 4001
EVENT_COPY_JOB_FAIL = 4002
EVENT_COPY_JOB_CANCELED = 4003
#end

# Adding the ERROR_CODE_BASE to the above
# ERROR codes will produce a event/status code
# e.g., EVENT_ERROR_DEVICE_NOT_FOUND=2 -> 5002 status/event code
ERROR_CODE_BASE = 5000
EVENT_ERROR_SUCCESS = 5000
EVENT_ERROR_UNKNOWN_ERROR = 5001
EVENT_ERROR_DEVICE_NOT_FOUND = 5002
EVENT_ERROR_INVALID_DEVICE_ID = 5003
EVENT_ERROR_INVALID_DEVICE_URI = 5004
EVENT_ERROR_DATA_LENGTH_EXCEEDS_MAX = 5008
EVENT_ERROR_DEVICE_IO_ERROR = 5012
EVENT_ERROR_NO_PROBED_DEVICES_FOUND = 5018
EVENT_ERROR_DEVICE_BUSY = 5021
EVENT_ERROR_DEVICE_STATUS_NOT_AVAILABLE = 5026
EVENT_ERROR_INVALID_SERVICE_NAME = 5028
EVENT_ERROR_ERROR_INVALID_CHANNEL_ID = 5030
EVENT_ERROR_CHANNEL_BUSY = 5031
EVENT_ERROR_DEVICE_DOES_NOT_SUPPORT_OPERATION = 5034
EVENT_ERROR_DEVICEOPEN_FAILED_ONE_DEVICE_ONLY = 5037
EVENT_ERROR_DEVICEOPEN_FAILED_DEV_NODE_MOVED = 5038
# end

# diagnosis tool codes
EVENT_DIAGNOSE_PRINTQUEUE = 5502
#end

# pcard
EVENT_START_PCARD_JOB = 6000
EVENT_END_PCARD_JOB = 6001
EVENT_PCARD_JOB_FAIL = 6002
EVENT_PCARD_UNABLE_TO_MOUNT = 6003
EVENT_PCARD_FILES_TRANSFERED = 6004
# end

# maint
EVENT_START_MAINT_JOB = 6050 # used for polling control (if print not used)
EVENT_END_MAINT_JOB = 6051

EVENT_MAX_USER_EVENT = 7999
# end of user events
# start of internal events

# fax (internal events)
EVENT_FAX_MIN = 8000
EVENT_FAX_RENDER_COMPLETE = 8000
EVENT_FAX_WAITING = 8001 # Sent by hpssd to toolbox when fax is waiting
EVENT_FAX_ADDRESS_BOOK_UPDATED = 8002 # Sent by FAB to indicate that the dB has changed
EVENT_FAX_MAX = 8999
# end

# UI
EVENT_MIN_UI_EVENT = 9000
EVENT_CUPS_QUEUES_ADDED = 9000 # sent by hp-setup if queues added
EVENT_RAISE_DEVICE_MANAGER = 9001
#EVENT_JOB_STORAGE_UI_REQUEST = 9002 # sent by hplipjs CUPS filter for job storage UI
EVENT_HISTORY_UPDATE = 9003 # sent by hp-systray to hp-toolbox when a device's history changes
EVENT_USER_CONFIGURATION_CHANGED = 9004 # sent when ~/.hplip/hplip.conf has been changed by another app.
EVENT_SYS_CONFIGURATION_CHANGED = 9005 # sent when /etc/hp/hplip.conf has been changed by another app.
EVENT_DEVICE_UPDATE_REQUESTED = 9010
EVENT_DEVICE_UPDATE_REPLY = 9011
EVENT_DEVICE_START_POLLING = 9020
EVENT_DEVICE_STOP_POLLING = 9021
EVENT_POLLING_REQUEST = 9022
EVENT_DEVICE_UPDATE_ACTIVE = 9030
EVENT_DEVICE_UPDATE_INACTIVE = 9031
EVENT_DEVICE_UPDATE_BLIP = 9032
EVENT_SYSTEMTRAY_EXIT = 9040
EVENT_CUPS_QUEUES_REMOVED = 9041 # sent by hp-setup if queues removed
EVENT_MAX_UI_EVENT = 9999

EVENT_MAX_EVENT = 9999

# do not add any events > 100000 (PJL error code space)

# end of events


# Error states
ERROR_STATE_CLEAR = 0        # Show icon w/o overlay
ERROR_STATE_OK = 1           # Icon w/ "OK" overlay
ERROR_STATE_MAX_OK = 99
ERROR_STATE_WARNING = 100      # Icon w/ triangle "!" overlay
ERROR_STATE_ERROR = 101        # Icon w/ circle "X" overlay
ERROR_STATE_LOW_SUPPLIES = 102 # Icon w/ supplies overlay
ERROR_STATE_BUSY = 103         # Icon with busy overlay
ERROR_STATE_LOW_PAPER = 104    # Icon w/ paper low overlay
ERROR_STATE_PRINTING = 105
ERROR_STATE_SCANNING = 106
ERROR_STATE_PHOTOCARD = 107
ERROR_STATE_FAXING = 108
ERROR_STATE_COPYING = 109
ERROR_STATE_REFRESHING = 999
#end


# Map of status/event codes to UI states
STATUS_TO_ERROR_STATE_MAP = {
    STATUS_UNKNOWN : ERROR_STATE_CLEAR,
    EVENT_START_PRINT_JOB : ERROR_STATE_BUSY,
    EVENT_END_PRINT_JOB   : ERROR_STATE_OK,
    EVENT_START_FAX_PRINT_JOB : ERROR_STATE_BUSY,
    EVENT_END_FAX_PRINT_JOB : ERROR_STATE_FAXING,

    EVENT_PRINTER_QUEUE_STOPPED : ERROR_STATE_WARNING,
    EVENT_PRINTER_QUEUE_STARTED : ERROR_STATE_CLEAR,
    EVENT_PRINTER_QUEUE_REJECTING_JOBS : ERROR_STATE_WARNING,
    EVENT_PRINTER_QUEUE_ACCEPTING_JOBS : ERROR_STATE_CLEAR,
    EVENT_PRINTER_QUEUE_SET_AS_DEFAULT : ERROR_STATE_OK,

    EVENT_FAX_QUEUE_STOPPED : ERROR_STATE_WARNING,
    EVENT_FAX_QUEUE_STARTED : ERROR_STATE_CLEAR,
    EVENT_FAX_QUEUE_REJECTING_JOBS : ERROR_STATE_WARNING,
    EVENT_FAX_QUEUE_ACCEPTING_JOBS : ERROR_STATE_CLEAR,
    EVENT_FAX_QUEUE_SET_AS_DEFAULT : ERROR_STATE_OK,

    STATUS_PRINTER_IDLE : ERROR_STATE_CLEAR,
    STATUS_PRINTER_BUSY : ERROR_STATE_BUSY,
    STATUS_PRINTER_POWER_SAVE : ERROR_STATE_CLEAR,
    STATUS_PRINTER_PRINTING : ERROR_STATE_PRINTING,
    STATUS_PRINTER_TURNING_OFF : ERROR_STATE_BUSY,
    STATUS_PRINTER_REPORT_PRINTING : ERROR_STATE_PRINTING,
    STATUS_PRINTER_CANCELING : ERROR_STATE_BUSY,
    STATUS_PRINTER_IO_STALL : ERROR_STATE_ERROR,
    STATUS_PRINTER_DRY_WAIT_TIME : ERROR_STATE_PRINTING,
    STATUS_PRINTER_PEN_CHANGE : ERROR_STATE_WARNING,
    STATUS_PRINTER_OUT_OF_PAPER : ERROR_STATE_WARNING,
    STATUS_PRINTER_BANNER_EJECT : ERROR_STATE_WARNING,
    STATUS_PRINTER_BANNER_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_PHOTO_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_DUPLEX_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_MEDIA_JAM : ERROR_STATE_ERROR,
    STATUS_PRINTER_CARRIAGE_STALL : ERROR_STATE_ERROR,
    STATUS_PRINTER_PAPER_STALL : ERROR_STATE_ERROR,
    STATUS_PRINTER_PEN_FAILURE : ERROR_STATE_ERROR,
    STATUS_PRINTER_HARD_ERROR : ERROR_STATE_ERROR,
    STATUS_PRINTER_POWER_DOWN : ERROR_STATE_ERROR,
    STATUS_PRINTER_FRONT_PANEL_TEST : ERROR_STATE_ERROR,
    STATUS_PRINTER_CLEAN_OUT_TRAY_MISSING : ERROR_STATE_ERROR,
    STATUS_PRINTER_OUTPUT_BIN_FULL : ERROR_STATE_ERROR,
    STATUS_PRINTER_MEDIA_SIZE_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_MANUAL_DUPLEX_BLOCK : ERROR_STATE_ERROR,
    STATUS_PRINTER_SERVCE_STALL : ERROR_STATE_ERROR,
    STATUS_PRINTER_OUT_OF_INK : ERROR_STATE_ERROR,
    STATUS_PRINTER_LIO_ERROR : ERROR_STATE_ERROR,
    STATUS_PRINTER_PUMP_STALL : ERROR_STATE_ERROR,
    STATUS_PRINTER_TRAY_2_MISSING : ERROR_STATE_ERROR,
    STATUS_PRINTER_DUPLEXER_MISSING : ERROR_STATE_ERROR,
    STATUS_PRINTER_REAR_TRAY_MISSING : ERROR_STATE_ERROR,
    STATUS_PRINTER_PEN_NOT_LATCHED : ERROR_STATE_ERROR,
    STATUS_PRINTER_BATTERY_VERY_LOW : ERROR_STATE_WARNING,
    STATUS_PRINTER_SPITTOON_FULL : ERROR_STATE_ERROR,
    STATUS_PRINTER_OUTPUT_TRAY_CLOSED : ERROR_STATE_ERROR,
    STATUS_PRINTER_MANUAL_FEED_BLOCKED : ERROR_STATE_ERROR,
    STATUS_PRINTER_REAR_FEED_BLOCKED : ERROR_STATE_ERROR,
    STATUS_PRINTER_TRAY_2_OUT_OF_PAPER : ERROR_STATE_LOW_PAPER,
    STATUS_PRINTER_UNABLE_TO_LOAD_FROM_LOCKED_TRAY : ERROR_STATE_ERROR,
    STATUS_PRINTER_NON_HP_INK : ERROR_STATE_WARNING,
    STATUS_PRINTER_PEN_CALIBRATION_RESUME : ERROR_STATE_WARNING,
    STATUS_PRINTER_MEDIA_TYPE_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_CUSTOM_MEDIA_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_PEN_CLEANING : ERROR_STATE_WARNING,
    STATUS_PRINTER_PEN_CLEANING : ERROR_STATE_WARNING,
    STATUS_PRINTER_WARMING_UP : ERROR_STATE_BUSY,
    STATUS_PRINTER_LOW_PAPER : ERROR_STATE_LOW_PAPER,
    STATUS_PRINTER_DOOR_OPEN : ERROR_STATE_ERROR,
    STATUS_PRINTER_OFFLINE : ERROR_STATE_ERROR,
    STATUS_PRINTER_LOW_TONER : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_NO_TONER : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_SERVICE_REQUEST : ERROR_STATE_ERROR,
    STATUS_PRINTER_FUSER_ERROR : ERROR_STATE_ERROR,
    STATUS_DEVICE_UNSUPPORTED : ERROR_STATE_ERROR,
    STATUS_PRINTER_CARTRIDGE_MISSING : ERROR_STATE_ERROR,
    STATUS_PRINTER_CARTRIDGE_WRONG : ERROR_STATE_ERROR,
    STATUS_PRINTER_PRINTHEAD_MISSING : ERROR_STATE_ERROR,
    STATUS_PRINTER_EMPTY_TONER : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_MEDIA_EMPTY_ERROR : ERROR_STATE_ERROR,

    #Alert messages for Pentane products RQ 8888
    STATUS_SCANNER_ADF_MISPICK : ERROR_STATE_ERROR,
    STATUS_PRINTER_PAPER_TOO_SHORT_TO_AUTODUPLEX : ERROR_STATE_ERROR,
    STATUS_PRINTER_TRAY_2_3_DOOR_OPEN : ERROR_STATE_ERROR,
    STATUS_PRINTER_INK_TOO_LOW_TO_PRIME : ERROR_STATE_WARNING,
    STATUS_PRINTER_VERY_LOW_ON_INK : ERROR_STATE_OK,
    STATUS_PRINTER_SERVICE_INK_CONTAINER_ALMOST_FULL : ERROR_STATE_WARNING,
    STATUS_PRINTER_SERVICE_INK_CONTAINER_FULL: ERROR_STATE_WARNING,
    STATUS_PRINTER_SERVICE_INK_CONTAINER_FULL_PROMPT: ERROR_STATE_ERROR,
    STATUS_PRINTER_DUPLEX_MODULE_MISSING: ERROR_STATE_ERROR,
    STATUS_PRINTER_PRINTHEAD_JAM: ERROR_STATE_ERROR,
    STATUS_PRINTER_CLEAR_OUTPUT_AREA: ERROR_STATE_WARNING,
    STATUS_PRINTER_RESEAT_DUPLEXER: ERROR_STATE_WARNING,
    STATUS_MANUALLY_FEED: ERROR_STATE_WARNING,
    STATUS_UNKNOWN_CODE:ERROR_STATE_OK,
    STATUS_PRINTER_STOPPED:ERROR_STATE_ERROR,
    STATUS_PRINTER_PAUSED:ERROR_STATE_WARNING,
    STATUS_INPUT_TRAY_MISSING:ERROR_STATE_ERROR,


    # The following block are EVENTs because they are only
    # received as events from hpmud, hp backend, etc.
    # i.e., a device does not produce status codes in this range
    EVENT_ERROR_SUCCESS : ERROR_STATE_CLEAR,
    EVENT_ERROR_UNKNOWN_ERROR : ERROR_STATE_ERROR,
    EVENT_ERROR_DEVICE_NOT_FOUND : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_DEVICE_ID : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_DEVICE_URI : ERROR_STATE_ERROR,
    EVENT_ERROR_DATA_LENGTH_EXCEEDS_MAX : ERROR_STATE_WARNING,
    EVENT_ERROR_DEVICE_IO_ERROR : ERROR_STATE_ERROR,
    EVENT_ERROR_NO_PROBED_DEVICES_FOUND : ERROR_STATE_WARNING,
    EVENT_ERROR_DEVICE_BUSY : ERROR_STATE_BUSY,
    EVENT_ERROR_DEVICE_STATUS_NOT_AVAILABLE : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_SERVICE_NAME : ERROR_STATE_ERROR,
    EVENT_ERROR_ERROR_INVALID_CHANNEL_ID : ERROR_STATE_ERROR,
    EVENT_ERROR_CHANNEL_BUSY : ERROR_STATE_BUSY,
    EVENT_ERROR_DEVICE_DOES_NOT_SUPPORT_OPERATION : ERROR_STATE_ERROR,
    EVENT_ERROR_DEVICEOPEN_FAILED_ONE_DEVICE_ONLY : ERROR_STATE_ERROR,
    EVENT_ERROR_DEVICEOPEN_FAILED_DEV_NODE_MOVED : ERROR_STATE_ERROR,
    # Scan
    EVENT_START_SCAN_JOB : ERROR_STATE_SCANNING,
    EVENT_END_SCAN_JOB : ERROR_STATE_OK,
    EVENT_SCANNER_FAIL : ERROR_STATE_ERROR,
    EVENT_SCAN_ADF_DOOR_OPEN : ERROR_STATE_ERROR,
    EVENT_SCAN_ADF_JAM : ERROR_STATE_ERROR,
    EVENT_SCAN_WAITING_FOR_PC : ERROR_STATE_SCANNING,
    EVENT_SCAN_TO_DESTINATION_NOTSET : ERROR_STATE_ERROR,
    EVENT_SCAN_ADF_LOADED : ERROR_STATE_OK,
    EVENT_SCAN_CANCEL : ERROR_STATE_OK,
    EVENT_SIZE_WARNING : ERROR_STATE_WARNING,
    EVENT_SCAN_ADF_NO_DOCS : ERROR_STATE_OK,
    EVENT_SCAN_ADF_MISPICK : ERROR_STATE_WARNING,
    EVENT_SCAN_BUSY : ERROR_STATE_SCANNING,
    # Fax
    EVENT_FAX_DIALING : ERROR_STATE_BUSY,
    EVENT_FAX_CONNECTING : ERROR_STATE_BUSY,
    EVENT_START_FAX_JOB : ERROR_STATE_FAXING,
    STATUS_FAX_TX_ACTIVE : ERROR_STATE_FAXING,
    STATUS_FAX_RX_ACTIVE : ERROR_STATE_FAXING,
    EVENT_END_FAX_JOB : ERROR_STATE_OK,
    EVENT_FAX_JOB_FAIL : ERROR_STATE_ERROR,
    EVENT_FAX_JOB_CANCELED : ERROR_STATE_ERROR,
    EVENT_FAX_SEND_ERROR : ERROR_STATE_ERROR,
    EVENT_FAX_RECV_ERROR : ERROR_STATE_ERROR,
    EVENT_FAX_ERROR_STORAGE_FULL : ERROR_STATE_WARNING,
    EVENT_FAX_BLOCKING : ERROR_STATE_ERROR,
    # Copy
    EVENT_START_COPY_JOB : ERROR_STATE_COPYING,
    EVENT_END_COPY_JOB : ERROR_STATE_OK,
    EVENT_COPY_JOB_FAIL : ERROR_STATE_ERROR,
    EVENT_COPY_JOB_CANCELED : ERROR_STATE_ERROR,
    # PCard
    EVENT_START_PCARD_JOB : ERROR_STATE_PHOTOCARD,
    EVENT_END_PCARD_JOB : ERROR_STATE_CLEAR,
    EVENT_PCARD_JOB_FAIL : ERROR_STATE_ERROR,
    EVENT_PCARD_UNABLE_TO_MOUNT : ERROR_STATE_ERROR,
    EVENT_PCARD_FILES_TRANSFERED : ERROR_STATE_OK,

    # Low supplies
    STATUS_PRINTER_LOW_BLACK_INK : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_TRI_COLOR_INK : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_PHOTO_INK : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_CYAN_INK : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_MAGENTA_INK : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_YELLOW_INK : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_PHOTO_CYAN_INK : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_PHOTO_MAGENTA_INK : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_PHOTO_YELLOW_INK : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_PHOTO_GRAY_INK : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_PHOTO_BLUE_INK : ERROR_STATE_LOW_SUPPLIES,

    STATUS_PRINTER_LOW_BLACK_TONER : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_CYAN_TONER : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_MAGENTA_TONER : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_LOW_YELLOW_TONER : ERROR_STATE_LOW_SUPPLIES,
    # end

}


# Device states
DEVICE_STATE_NOT_FOUND = -1
DEVICE_STATE_FOUND = 0
DEVICE_STATE_JUST_FOUND = 1


# I/O states
IO_STATE_HP_OPEN = 0
IO_STATE_HP_READY = 1
IO_STATE_HP_NOT_AVAIL = 2
IO_STATE_NON_HP = 3

#
# Systray visibility setting
#
SYSTRAY_VISIBLE_SHOW_ALWAYS = 0
SYSTRAY_VISIBLE_HIDE_WHEN_INACTIVE = 1
SYSTRAY_VISIBLE_HIDE_ALWAYS = 2

#
# Systray messages setting
#
SYSTRAY_MESSAGES_SHOW_ALL = 0
SYSTRAY_MESSAGES_SHOW_ERRORS_AND_WARNINGS = 1
SYSTRAY_MESSAGES_SHOW_ERRORS_ONLY = 2
SYSTRAY_MESSAGES_SHOW_NONE = 3

#
# Defines for model query types and status query
#

# agent info

# 'kind'
AGENT_KIND_NONE = 0
AGENT_KIND_HEAD = 1 # InkJet head (no ink)
AGENT_KIND_SUPPLY = 2 # InkJet supply (ink tank)
AGENT_KIND_HEAD_AND_SUPPLY = 3 # InkJet (cartridge)
AGENT_KIND_TONER_CARTRIDGE = 4 # LaserJet
AGENT_KIND_MAINT_KIT = 5 # LaserJet "Maintenance kit (fuser)"
AGENT_KIND_ADF_KIT = 6 # LaserJet "Document feeder kit"
AGENT_KIND_DRUM_KIT = 7 # LaserJet
AGENT_KIND_TRANSFER_KIT = 8 # LaserJet
AGENT_KIND_INT_BATTERY = 9 # Mobile deskjet (DJ450, etc)
AGENT_KIND_UNKNOWN = 0x3e # (62)

# 'type'
AGENT_TYPE_NONE = 0
AGENT_TYPE_BLACK = 1
AGENT_TYPE_CMY = 2 # Tricolor
AGENT_TYPE_KCM = 3 # Photo
AGENT_TYPE_CYAN = 4
AGENT_TYPE_MAGENTA = 5
AGENT_TYPE_YELLOW = 6
AGENT_TYPE_CYAN_LOW = 7
AGENT_TYPE_MAGENTA_LOW = 8
AGENT_TYPE_YELLOW_LOW = 9
AGENT_TYPE_GGK = 10 # 2 shades of grey and black
AGENT_TYPE_BLUE = 11
AGENT_TYPE_KCMY_CM = 12 # K/C/M/Y/LM/LC (02 pen set head)
AGENT_TYPE_LC_LM = 13 # light cyan and light magenta
#AGENT_TYPE_Y_M = 14 # yellow and magenta (B9180)
#AGENT_TYPE_C_K = 15 # cyan and black (B9180)
AGENT_TYPE_K_Y = 14 # black and yellow (for LJ Pro)
AGENT_TYPE_C_M = 15 # cyan and magenta (for LJ Pro)
AGENT_TYPE_LG_PK = 16 # light grey and photo black
AGENT_TYPE_LG = 17 # light grey
AGENT_TYPE_G = 18 # grey
AGENT_TYPE_PG = 19 # photo grey
AGENT_TYPE_PHOTO_BLACK = 20 # photo black
AGENT_TYPE_MATTE_BLACK = 21 # matte black
AGENT_TYPE_LC = 22 #light cyan
AGENT_TYPE_LM = 23 #light magenta
AGENT_TYPE_DG = 24 #dark gray
AGENT_TYPE_BLACK_B8800 = 39 # For PS B8800
AGENT_TYPE_WHITE = 0x20 # For ISO 10180 compatibility
AGENT_TYPE_RED = 0x21 # For ISO 10180 compatibility
AGENT_TYPE_UNSPECIFIED = 0x3e # (62) Used for kind = 5, 6, 7, 8, or 9
AGENT_TYPE_ERROR = 0x3f # (63)

# 'health'
AGENT_HEALTH_OK = 0
AGENT_HEALTH_MISINSTALLED = 1 # supply/cart
AGENT_HEALTH_FAIR_MODERATE = 1 # head
AGENT_HEALTH_INCORRECT = 2
AGENT_HEALTH_FAILED = 3
AGENT_HEALTH_OVERTEMP = 4 # Battery
AGENT_HEALTH_CHARGING = 5 # Battery
AGENT_HEALTH_DISCHARGING = 6 # Battery
AGENT_HEALTH_UNKNOWN = 0xff

# 'level'
AGENT_LEVEL_TRIGGER_SUFFICIENT_0 = 0
AGENT_LEVEL_TRIGGER_SUFFICIENT_1 = 1
AGENT_LEVEL_TRIGGER_SUFFICIENT_2 = 2
AGENT_LEVEL_TRIGGER_SUFFICIENT_3 = 3
AGENT_LEVEL_TRIGGER_SUFFICIENT_4 = 4
AGENT_LEVEL_TRIGGER_MAY_BE_LOW = 5
AGENT_LEVEL_TRIGGER_PROBABLY_OUT = 6
AGENT_LEVEL_TRIGGER_ALMOST_DEFINITELY_OUT = 7
AGENT_LEVEL_UNKNOWN = 0xff

# "Computed" configurations (2-pen products)
AGENT_CONFIG_NONE = 0
AGENT_CONFIG_BLACK_ONLY = 1
AGENT_CONFIG_PHOTO_ONLY = 2
AGENT_CONFIG_COLOR_ONLY = 3
AGENT_CONFIG_GREY_ONLY = 4
AGENT_CONFIG_COLOR_AND_BLACK = 5
AGENT_CONFIG_COLOR_AND_PHOTO = 6
AGENT_CONFIG_COLOR_AND_GREY = 7
AGENT_CONFIG_INVALID = 99

# align-types
ALIGN_TYPE_UNSUPPORTED = -1
ALIGN_TYPE_NONE = 0
ALIGN_TYPE_AUTO = 1
ALIGN_TYPE_8XX = 2
ALIGN_TYPE_9XX = 3
ALIGN_TYPE_LIDIL_0_3_8 = 4
ALIGN_TYPE_LIDIL_0_4_3 = 5
ALIGN_TYPE_LIDIL_AIO = 6
ALIGN_TYPE_LIDIL_VIP = 7
ALIGN_TYPE_DESKJET_450 = 8
ALIGN_TYPE_9XX_NO_EDGE_ALIGN = 9
ALIGN_TYPE_LBOW = 10
ALIGN_TYPE_LIDIL_0_5_4 = 11
ALIGN_TYPE_OJ_PRO = 12 # OJ Pro L7xxx
ALIGN_TYPE_AIO = 13 # AiO Non-LIDIL (OJ J4500/J4600)
ALIGN_TYPE_LIDIL_DJ_D1600 = 14
ALIGN_TYPE_LEDM = 15
ALIGN_TYPE_LEDM_MANUAL = 16
ALIGN_TYPE_LEDM_FF_CC_0 = 17

# clean-types
CLEAN_TYPE_UNSUPPORTED = -1
CLEAN_TYPE_NONE = 0
CLEAN_TYPE_PCL = 1
CLEAN_TYPE_LIDIL = 2
CLEAN_TYPE_PCL_WITH_PRINTOUT = 3
CLEAN_TYPE_LEDM = 4

# color-cal-types
COLOR_CAL_TYPE_UNSUPPORTED = -1
COLOR_CAL_TYPE_NONE = 0
COLOR_CAL_TYPE_DESKJET_450 = 1
COLOR_CAL_TYPE_MALIBU_CRICK = 2
COLOR_CAL_TYPE_STRINGRAY_LONGBOW_TORNADO = 3
COLOR_CAL_TYPE_CONNERY = 4
COLOR_CAL_TYPE_COUSTEAU = 5
COLOR_CAL_TYPE_CARRIER = 6
COLOR_CAL_TYPE_TYPHOON = 7

# status-types
STATUS_TYPE_NONE = 0
STATUS_TYPE_VSTATUS = 1
STATUS_TYPE_S = 2
STATUS_TYPE_LJ = 3
#STATUS_TYPE_S_W_BATTERY = 4 # DEPRECATED
#STATUS_TYPE_S_SNMP = 5 # DEPRECATED
STATUS_TYPE_LJ_XML = 6
#STATUS_TYPE_S_LIDIL = 7 # DEPRECATED
STATUS_TYPE_PJL = 8
STATUS_TYPE_PML_AND_PJL = 9 # Same as types 3(tbx)+8(hp:)
STATUS_TYPE_LEDM = 10 # Low-end Data Model
STATUS_TYPE_LEDM_FF_CC_0 = 11  #Low-end Data Model over FF/CC/0 USB channel
STATUS_TYPE_IPP = 12

# status-battery-check
STATUS_BATTERY_CHECK_NONE = 0
STATUS_BATTERY_CHECK_STD = 1 # Deskjet 450/460 (PML or dyn. counters)
STATUS_BATTERY_CHECK_PML = 2 # Officejet H470 (PML)

# status-dynamic-counters
STATUS_DYNAMIC_COUNTERS_NONE = 0
STATUS_DYNAMIC_COUNTERS_PCL = 1
STATUS_DYNAMIC_COUNTERS_PML_SNMP = 2
STATUS_DYNAMIC_COUNTERS_LIDIL_0_5_4 = 3 # Deskjet D4100

# tech-types
TECH_TYPE_NONE = 0
TECH_TYPE_MONO_INK = 1
TECH_TYPE_COLOR_INK = 2
TECH_TYPE_MONO_LASER = 3
TECH_TYPE_COLOR_LASER = 4
TECH_TYPE_COLOR_EDGELINE = 5

# support-type
SUPPORT_TYPE_NONE = 0
SUPPORT_TYPE_HPIJS = 1
SUPPORT_TYPE_HPLIP = 2

# fax-types
FAX_TYPE_NOT_SUPPORTED = -1
FAX_TYPE_NONE = 0
FAX_TYPE_BLACK_SEND_EARLY_OPEN = 1 # newer models
FAX_TYPE_BLACK_SEND_LATE_OPEN = 2 # older models
FAX_TYPE_BLACK_AND_COLOR_SEND = 3 # future/OZ
FAX_TYPE_SOAP = 4
FAX_TYPE_MARVELL = 5
FAX_TYPE_LEDM = 6
FAX_TYPE_LEDMSOAP = 7

# pcard-types
PCARD_TYPE_NONE = 0
PCARD_TYPE_MLC = 1
PCARD_TYPE_USB_MASS_STORAGE = 2

# scan-types
SCAN_TYPE_DIGITAL_SENDER = -2
SCAN_TYPE_NOT_SUPPORTED = -1
SCAN_TYPE_NONE = 0
SCAN_TYPE_SCL = 1
SCAN_TYPE_PML = 2
SCAN_TYPE_SOAP = 3
SCAN_TYPE_MARVEL = 4
SCAN_TYPE_SOAP2 = 5
SCAN_TYPE_SCL_DUPLEX = 6
SCAN_TYPE_LEDM = 7
SCAN_TYPE_MARVEL2 = 8

# scan-src
SCAN_SRC_NONE = 0x0
SCAN_SRC_FLATBED = 0x1
SCAN_SRC_SCROLLFED = 0x2
SCAN_SRC_CAMERA = 0x4

# copy-types
COPY_TYPE_NOT_SUPPORTED = -1
COPY_TYPE_NONE = 0
COPY_TYPE_DEVICE = 1 # LaserJet MFP PML
COPY_TYPE_SCAN_TO_PRINT = 2
COPY_TYPE_AIO_DEVICE = 3 # Inkjet AiO PML

# 'top_door' (lid)
TOP_DOOR_NOT_PRESENT = 0
TOP_DOOR_CLOSED = 1
TOP_DOOR_OPEN = 2

# 'supply_door'
SUPPLY_DOOR_NOT_PRESENT = 0
SUPPLY_DOOR_CLOSED = 1
SUPPLY_DOOR_OPEN = 2

# 'media_path'
MEDIA_PATH_NOT_PRESENT = 0 # S:00 means banner not present
MEDIA_PATH_CUT_SHEET = 1 # S:01 means banner present/engaged
MEDIA_PATH_BANNER = 2
MEDIA_PATH_PHOTO = 3

# 'photo_tray'(S:03 photo/hagaki)
PHOTO_TRAY_NOT_PRESENT = 0
PHOTO_TRAY_NOT_ENGAGED = 1
PHOTO_TRAY_ENGAGED = 2

# 'duplexer' (S:02 cleanout)
DUPLEXER_NOT_PRESENT = 0
DUPLEXER_DOOR_CLOSED = 1
DUPLEXER_DOOR_OPEN = 2

# 'in_tray1' & 'in_tray2'
IN_TRAY_NOT_PRESENT = 0
IN_TRAY_PRESENT = 1 # for !S:02, test for > IN_TRAY_NOT_PRESENT
IN_TRAY_DEFAULT = 2 # S:02 only
IN_TRAY_LOCKED = 3 # S:02 only

# 'io-support'
IO_SUPPORT_PARALLEL = 0x1
IO_SUPPORT_USB = 0x2
IO_SUPPORT_NETWORK = 0x4
IO_SUPPORT_WIRELESS = 0x8
IO_SUPPORT_BLUETOOTH = 0x10

# User friendly model categories
MODEL_TYPE2_UNSUPPORTED = 0
MODEL_TYPE2_DESKJET = 1
MODEL_TYPE2_DESKJET_AIO = 2
MODEL_TYPE2_PHOTOSMART = 3
MODEL_TYPE2_OFFICEJET = 4
MODEL_TYPE2_PSC = 5
MODEL_TYPE2_LASERJET = 6
MODEL_TYPE2_COLOR_LASERJET = 7
MODEL_TYPE2_BIJ = 8
MODEL_TYPE2_EDGELINE = 9
MODEL_TYPE2_APOLLO = 10
MODEL_TYPE2_SCANJET = 11 # not supported
MODEL_TYPE2_DESIGNJET = 12
MODEL_TYPE2_OTHER = 13 # No specific "sub-brand" (e.g., 910, cp1610)

MONITOR_TYPE_UNSUPPORTED = -1
MONITOR_TYPE_NONE = 0
MONITOR_TYPE_STD = 1

# 'io-mode' and 'io-mfp-mode'
IO_MODE_UNI = 0
IO_MODE_RAW = 1
#IO_MODE_NOT_USED = 2
IO_MODE_DOT4 = 3
IO_MODE_DOT4_PHOENIX = 4
IO_MODE_DOT4_BRIDGE = 5
IO_MODE_MLC_GUSHER = 6
IO_MODE_MLC_MISER = 7

# plugin
PLUGIN_NONE = 0
PLUGIN_REQUIRED = 1
PLUGIN_OPTIONAL = 2


#Plugin installation status values
PLUGIN_FILES_CORRUPTED = '-2'
PLUGIN_VERSION_MISMATCH = '-1'
PLUGIN_NOT_INSTALLED = '0'
PLUGIN_INSTALLED = '1'

# plugin-reason
PLUGIN_REASON_NONE = 0x0
PLUGIN_REASON_PRINTING_SUPPORT = 0x1
PLUGIN_REASON_FASTER_PRINTING = 0x2
PLUGIN_REASON_BETTER_PRINTING_PQ = 0x4
PLUGIN_REASON_PRINTING_FEATURES = 0x8
PLUGIN_REASON_RESERVED_10 = 0x10
PLUGIN_REASON_RESERVED_20 = 0x20
PLUGIN_REASON_SCANNING_SUPPORT = 0x40
PLUGIN_REASON_FASTER_SCANNING = 0x80
PLUGIN_REASON_BETTER_SCANNING_IQ = 0x100
PLUGIN_REASON_RESERVED_200 = 0x200
PLUGIN_REASON_RESERVED_400 = 0x400
PLUGIN_REASON_FAXING_SUPPORT = 0x800
PLUGIN_REASON_FAX_FEATURES = 0x1000
PLUGIN_REASON_RESERVED_2000 = 0x2000
PLUGIN_REASON_IO_SUPPORT = 0x4000
PLUGIN_REASON_UI_FEATURES = 0x8000
PLUGIN_REASON_OTHER_FEATURES = 0x10000
PLUGIN_REASON_RESERVED_20000 = 0x20000
PLUGIN_REASON_RESERVED_40000 = 0x40000

# embedded web server
EWS_NOT_SUPPORTED = -1
EWS_NONE = 0
EWS_PRESENT = 1

# panel check
PANEL_CHECK_TYPE_NONE = 0
PANEL_CHECK_TYPE_CHECK = 1

# pq diag
PQ_DIAG_TYPE_UNSUPPORTED = -1
PQ_DIAG_TYPE_NONE = 0
PQ_DIAG_TYPE_1 = 1
PQ_DIAG_TYPE_2 = 2

# line feed cal
LINEFEED_CAL_TYPE_UNSUPPORTED = -1
LINEFEED_CAL_TYPE_NONE = 0
LINEFEED_CAL_TYPE_OJ_K550 = 1
LINEFEED_CAL_TYPE_OJ_PRO_L7XXX = 2

# power-settings
POWER_SETTINGS_NONE = 0
POWER_SETTINGS_EPML = 1 # DJ450/DJ460
POWER_SETTINGS_PML = 2 # OJ H470

# Paper types (for hp-toolbox paper prompts)
PAPER_TYPE_PLAIN = 0
PAPER_TYPE_HP_ADV_PHOTO = 1

# job-storage
JOB_STORAGE_DISABLE = 0
JOB_STORAGE_ENABLE = 1

JOB_STORAGE_TYPE_OFF = 0
JOB_STORAGE_TYPE_PROOF_AND_HOLD = 1
JOB_STORAGE_TYPE_PERSONAL = 2
JOB_STORAGE_TYPE_QUICK_COPY = 3
JOB_STORAGE_TYPE_STORE = 4

JOB_STORAGE_EXISTING_JOB_REPLACE = 0
JOB_STORAGE_EXISTING_JOB_APPEND_1_99 = 1

JOB_STORAGE_HOLD_TYPE_PUBLIC = 0
JOB_STORAGE_HOLD_TYPE_PRIVATE = 1

# WIfi Config
WIFI_CONFIG_UNSUPPORTED = -1
WIFI_CONFIG_NONE = 0
WIFI_CONFIG_USB_XML = 1
WIFI_CONFIG_DEFAULT = 2
WIFI_CONFIG_LEDM = 3

# support-released
SUPPORT_UNRELEASED = 0
SUPPORT_RELEASED = 1

#USB-Autoplugin-installation
EVENT_AUTO_CONFIGURE = 900

# Queue diagnosis codes
QUEUES_CONFIG_ERROR = 1
QUEUES_PAUSED = 2
QUEUES_INCORRECT_PPD = 3
QUEUES_USER_GROUPS_ERROR = 4
QUEUES_MSG_SENDING = 5
QUEUES_SMART_INSTALL_ENABLED = 6

