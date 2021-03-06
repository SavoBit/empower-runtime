#!/usr/bin/env python3
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

"""List workers that can be loaded."""

import empower_core.command as command


def do_cmd(gargs, *_):
    """List workers that can be loaded."""

    _, data = command.connect(gargs, ('GET', '/api/v1/catalog'), 200)

    for entry in data.values():

        accum = []

        accum.append("name ")
        accum.append(entry['name'])
        accum.append("\n")

        accum.append("  desc: ")
        accum.append(entry['desc'])

        accum.append("\n  params:")

        for k, val in entry['params'].items():
            if k in ('service_id', 'project_id'):
                continue
            accum.append("\n    %s: %s" % (k, val['desc']))
            if 'default' in val:
                accum.append(" Default: %s." % val['default'])
            accum.append(" Type: %s." % val['type'])
            accum.append(" Mandatory: %s." % val['mandatory'])

        print(''.join(accum))
