pragma solidity ^0.6.0;

// Simple storage contract.
contract SimpleStorage {
    uint256 public storedData;

    function set(uint256 x) public returns (uint256) {
        storedData = x;
        return storedData;
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
