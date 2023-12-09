## Added

- None

## Changed

- Fix `ipcx.Client` requests failing due to closing transport (#30)
- `aiohttp.ClientSession` is now bound to the ipcx.Client class, and a helper method that is undocumented is introduced to aid with the creation of aiohttp.ClientSession (b27807d49325acd2e6c14da6129d573153bb33b6)
- Logic for obtaining the port if not set has been moved to a helper method called get_port, which will obtain the port by connecting to the multicast server if not found (b27807d49325acd2e6c14da6129d573153bb33b6)
- Updated examples provided

## Removed

- None