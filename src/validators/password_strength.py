#!/usr/bin/env python3
#
# Copyright (C) 2025 VyOS maintainers and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sys


if __name__ == '__main__':
    try:
        from vyos.utils.auth import (
            EPasswdStrength,
            evaluate_strength,
            WEAK_PASSWD_WARNING
        )
    except ImportError:
        print("Please install vyos.utils.auth")
        sys.exit(0)
    else:
        if len(sys.argv) != 2:
            sys.exit(1)

        check_result = evaluate_strength(sys.argv[1])

        if check_result['strength'] == EPasswdStrength.WEAK:
            err_list = [f'  - {e}' for e in check_result['errors']]
            print(WEAK_PASSWD_WARNING.replace(
                '@ERRORS@', '\n'.join(err_list)
            ))
            sys.exit(1)

        sys.exit(0)
