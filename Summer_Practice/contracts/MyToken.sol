// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";

contract MyToken is ERC721, Pausable, Ownable, ERC721Burnable {
    constructor() ERC721("MyToken", "MTK") {}
    using Counters for Counters.Counter; // use it to increment or decrement items stock
      struct Generalstuff{ 
        uint256 price; // items' prices
        uint256 itemsavailable; // ensuring the items are in stocks
        string itemname; // name of the item
       // uint256 
      }
      mapping(uint256 => Generalstuff) public Generalstuff; //saving the strings
      //uint256 price public; // making the price public
      //string item public;  // making the items public
      //string itemsavailable; //making the sure that the quantity of item is public
    function purchase(address seller, uint256 tokenId) public payable{
        require(seller.msg.value>0); //making sure that they have enough money
        require(seller.msg.value> Generalstuff[tokenId].price);
        payable address seller.totransfer(msg.value); // sends the value 
        uint256 itemsavailable=-1; //decrement items

    }
    function supply(address seller, uint256 itemsavailable) public Generalstuff{
        require(uint256 itemsavailable != 0) //making sure if it is not equal to zero
        uint256 itemsavailable+=1 // replenish stocks
    }
    //function 
    /*function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }*/

    function safeMint(address to, uint256 tokenId) public onlyOwner {
        _safeMint(to, tokenId);
    }

    function _beforeTokenTransfer(address from, address to, uint256 tokenId, uint256 batchSize)
        internal
        whenNotPaused
        override
    {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
    }
}
