import pytest
import sys
  
# append the path of the parent directory
sys.path.append("../app")

import api.packets

def test_move_xyz():
    print("Testing move_xyz")
    command = api.packets.FlashForgeCommands()
    result = command.move_xyz(1,1,1)
    assert result == "~G1 X1 Y1 Z1\r"

    result = command.move_xyz(1,1)
    assert result == "~G1 X1 Y1\r"

    result = command.move_xyz(1)
    assert result == "~G1 X1\r"

    result = command.move_xyz(x=1,z=1)
    assert result == "~G1 X1 Z1\r"

    with pytest.raises(ValueError):
        result = command.move_xyz()

