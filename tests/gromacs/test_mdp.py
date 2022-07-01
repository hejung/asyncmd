# This file is part of asyncmd.
#
# asyncmd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# asyncmd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with asyncmd. If not, see <https://www.gnu.org/licenses/>.
import pytest
from unittest.mock import AsyncMock


from asyncmd.gromacs import MDP


class Test_MDP:
    # NOTE: we are not testing any of the FLOAT,INT,STR params (yet)!
    def setup(self):
        # just an empty file
        empty_mdp_file = "tests/test_data/gromacs/empty.mdp"
        self.empty_mdp = MDP(original_file=empty_mdp_file)

    @pytest.mark.parametrize(["line", "beauty"],
                             [  # comment lines
                              (";", {}),
                              ("; comment", {}),
                              ("; comment =", {}),
                              ("; comment = comment", {}),
                              (";comment=comment", {}),
                              # empty options, but with key
                              ("ich-bin-ein-key = ", {"ich-bin-ein-key": []}),
                              # CHARMM-GUI (still uses old gmx mdp format)
                              ("ich_bin_ein_key = ", {"ich-bin-ein-key": []}),
                              # options with values
                              ("key = option", {"key": ["option"]}),
                              ("key=option", {"key": ["option"]}),
                              ("key = tilded~option", {"key": ["tilded~option"]}),
                              ("key = slashed/option", {"key": ["slashed/option"]}),
                              ("key = dotted.option", {"key": ["dotted.option"]}),
                              ("key = minus-option", {"key": ["minus-option"]}),
                              ]
                             )
    def test_parse_line(self, line, beauty):
        # here we test the parse_line and key_char replace funcs
        ret_dict = self.empty_mdp._parse_line(line=line)
        assert ret_dict == beauty
        for key, val in beauty.items():
            assert ret_dict[key] == val

    @pytest.mark.parametrize("line",
                             # these are all misformatted mdp lines
                             # (and should therfore raise ValueErrors)
                             ["not a valid mdp line",
                              "also not = a valid mdp line",
                              "still not ; a valid mdp line",
                              ]
                             )
    def test_parse_line_errs(self, line):
        with pytest.raises(ValueError):
            _ = self.empty_mdp._parse_line(line=line)

    @pytest.mark.skip("TODO!")
    def test_setitem_getitem_delitem(self):
        pass
