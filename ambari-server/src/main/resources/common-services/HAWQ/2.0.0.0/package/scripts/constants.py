"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os

MASTER = "master"
STANDBY = "standby"
SEGMENT = "segment"
START = "start"
INIT = "init"
STOP = "stop"

# Users
root_user = "root"
gpadmin_user = "gpadmin"
hawq_user = gpadmin_user
hawq_group = gpadmin_user
hawq_password = gpadmin_user

# Directories
hawq_home_dir = "/usr/local/hawq/"
hawq_config_dir = "/usr/local/hawq/etc/"
hawq_pid_dir = "/var/run/hawq/"
hawq_tmp_dir = '/tmp/hawq/'
hawq_user_home_dir = os.path.expanduser("~{0}".format(hawq_user))
limits_conf_dir = "/etc/security/limits.d"
sysctl_conf_dir = "/etc/sysctl.d"

# Files
hawq_slaves_file = os.path.join(hawq_config_dir, "slaves")
hawq_user_bashrc_file = os.path.join(hawq_user_home_dir, ".bashrc")
hawq_greenplum_path_file = os.path.join(hawq_home_dir, "greenplum_path.sh")
hawq_hosts_file = "/tmp/hawq_hosts"
hawq_check_file = os.path.join(hawq_config_dir, "gpcheck.cnf")
sysctl_suse_file = "/etc/sysctl.conf"
sysctl_backup_file = "/etc/sysctl.conf.backup.{0}"
hawq_sysctl_filename = "hawq_sysctl.conf"
hawq_sysctl_tmp_file = os.path.join(hawq_tmp_dir, hawq_sysctl_filename)
hawq_sysctl_file = os.path.join(sysctl_conf_dir, hawq_sysctl_filename)
postmaster_opts_filename = "postmaster.opts"
postmaster_pid_filename = "postmaster.pid"

# Smoke check table
smoke_check_table_name = "ambari_hawq_smoke_test"

# Timeouts
default_exec_timeout = 600
hawq_operation_exec_timeout = 900
