#import pytest
import sys
  
# append the path of the parent directory
sys.path.append("../app")

import api.udp_discovery

def test_udp_discovery():
    flashforge_discovery = api.udp_discovery.UDP_discovery()
    flashforge_discovery.scan_devices()
    devices = flashforge_discovery.get_devices()
    print(devices)

test_udp_discovery()
