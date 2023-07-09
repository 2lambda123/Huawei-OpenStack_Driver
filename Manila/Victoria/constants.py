# Copyright (c) 2014 Huawei Technologies Co., Ltd.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

PORT_LINKUP = "10"
STATUS_FS_HEALTH = "1"
STATUS_FS_FAULT = "2"
STATUS_FS_RUNNING = "27"
STATUS_SNAPSHOT_HEALTH = '1'
AD_JOIN_DOMAIN = '1'
AD_EXIT_DOMAIN = '0'
AD_JOIN_FAILED = '4'
STATUS_SERVICE_RUNNING = "2"
QOS_ACTIVE = '2'
QOS_INACTIVATED = '45'
MAX_FS_NUM_IN_QOS = 64
MAX_QUERY_COUNT = 100
SENSITIVE_KEYS = ['access_password']

CAPACITY_UNIT = 1024 * 1024 * 2
DEFAULT_WAIT_INTERVAL = 3
DEFAULT_TIMEOUT = 60
PWD_EXPIRED_OR_INITIAL = (3, 4)

SOCKET_TIMEOUT = 52
LOGIN_SOCKET_TIMEOUT = 4
QOS_NAME_PREFIX = 'OpenStack_'
TMP_PATH_SRC_PREFIX = "huawei_manila_tmp_path_src_"
TMP_PATH_DST_PREFIX = "huawei_manila_tmp_path_dst_"

ACCESS_NFS_RW = "1"
ACCESS_NFS_RO = "0"
ACCESS_CIFS_FULLCONTROL = "1"
ACCESS_CIFS_RO = "0"

ERROR_CONNECT_TO_SERVER = -403
ERROR_UNAUTHORIZED_TO_SERVER = -401
ERROR_BAD_STATUS_LINE = -400
ERROR_LOGICAL_PORT_EXIST = 1073813505
ERROR_USER_OR_GROUP_NOT_EXIST = 1077939723
REPLICATION_PAIR_NOT_EXIST = 1077937923
REPLICATION_CONNECTION_NOT_NORMAL = 1077938040
OBJECT_NOT_EXIST = 1077948996
AD_DOMAIN_NOT_EXIST = 1077939763
FILESYSTEM_NOT_EXIST = 1073752065
SHARE_NOT_EXIST = 1077939717
ERROR_HYPERMETRO_NOT_EXIST = 1077674242
SNAPSHOT_NOT_EXIST = 1073754118
SHARE_PATH_INVALID = 1077939729
LIF_ALREADY_EXISTS = 1077948993
RELOGIN_ERROR_PASS = 1077939726
ERROR_DEVICE_COMMUNICATE = 4294967297

RELOGIN_ERROR_CODE = (ERROR_CONNECT_TO_SERVER, ERROR_UNAUTHORIZED_TO_SERVER,
                      ERROR_BAD_STATUS_LINE, ERROR_DEVICE_COMMUNICATE)

PORT_TYPE_ETH = '1'
PORT_TYPE_BOND = '7'
PORT_TYPE_VLAN = '8'

ALLOC_TYPE_THIN_FLAG = "1"
ALLOC_TYPE_THICK_FLAG = "0"

ALLOC_TYPE_THIN = "Thin"
ALLOC_TYPE_THICK = "Thick"
THIN_PROVISIONING = "true"
THICK_PROVISIONING = "false"

FILE_SYSTEM_POOL_TYPE = '2'
DORADO_V6_POOL_TYPE = '0'

QOS_LOWER_LIMIT = ('MINIOPS', 'LATENCY', 'MINBANDWIDTH')
QOS_UPPER_LIMIT = ('MAXIOPS', 'MAXBANDWIDTH')
QOS_KEYS = QOS_LOWER_LIMIT + QOS_UPPER_LIMIT + ('IOTYPE',)
QOS_IO_TYPES = ('0', '1', '2')

LOCAL_RES_TYPES = (FILE_SYSTEM_TYPE,) = ('40',)

REPLICA_MODELS = (REPLICA_SYNC_MODEL,
                  REPLICA_ASYNC_MODEL) = ('1', '2')

REPLICA_SPEED_MODELS = (REPLICA_SPEED_LOW,
                        REPLICA_SPEED_MEDIUM,
                        REPLICA_SPEED_HIGH,
                        REPLICA_SPEED_HIGHEST) = ('1', '2', '3', '4')

REPLICA_HEALTH_STATUSES = (REPLICA_HEALTH_STATUS_NORMAL,
                           REPLICA_HEALTH_STATUS_FAULT,
                           REPLICA_HEALTH_STATUS_INVALID) = ('1', '2', '14')

REPLICATION_TYPES = (REMOTE_REPLICATION, LOCAL_REPLICATION) = ('0', '1')

REPLICA_DATA_STATUSES = (
    REPLICA_DATA_STATUS_SYNCHRONIZED,
    REPLICA_DATA_STATUS_COMPLETE,
    REPLICA_DATA_STATUS_INCOMPLETE) = ('1', '2', '5')

REPLICA_DATA_STATUS_IN_SYNC = (
    REPLICA_DATA_STATUS_SYNCHRONIZED,
    REPLICA_DATA_STATUS_COMPLETE)

REPLICA_RUNNING_STATUSES = (
    REPLICA_RUNNING_STATUS_NORMAL,
    REPLICA_RUNNING_STATUS_SYNCING,
    REPLICA_RUNNING_STATUS_SPLITTED,
    REPLICA_RUNNING_STATUS_TO_RECOVER,
    REPLICA_RUNNING_STATUS_INTERRUPTED,
    REPLICA_RUNNING_STATUS_INVALID) = (
    '1', '23', '26', '33', '34', '35')

REPLICA_SECONDARY_ACCESS_RIGHTS = (
    REPLICA_SECONDARY_ACCESS_DENIED,
    REPLICA_SECONDARY_RO,
    REPLICA_SECONDARY_RW) = ('1', '2', '3')

METRO_RUNNING_STATUSES = (
    METRO_RUNNING_STATUS_NORMAL,
    METRO_RUNNING_STATUS_SYNCING,
    METRO_RUNNING_STATUS_INVALID,
    METRO_RUNNING_STATUS_PAUSE,
    METRO_RUNNING_STATUS_FORCED_START,
    METRO_RUNNING_STATUS_ERROR,
    METRO_RUNNING_STATUS_TO_BE_SYNC) = (
    '1', '23', '35', '41', '93', '94', '100')

VALID_PRODUCTS = ('V3', 'V5', 'Dorado', 'V6')

AVAILABLE_FEATURE_STATUS = (1, 2)
VALID_NETWORK_TYPE = ('flat', 'vlan', 'vxlan', None)
SUPPORT_CLONE_PAIR_VERSION = "V600R003C00"
SUPPORT_CLONE_FS_SPLIT_VERSION = "615"
ACTION_START_SPLIT = 1
SNAPSHOT_ROLLBACK_RATE = "100"
SNAPSHOT_ROLLBACK_TIMEOUT = 60 * 60 * 24
SNAPSHOT_ROLLING_BACK = "1"
SNAPSHOT_ROLLBACK_COMPLETED = "0"

FILESYSTEM_MODES = ('0', '2')
RPC_CALL_TIMES = 2
RPC_CALL_INTERVAL = 1
