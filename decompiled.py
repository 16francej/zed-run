#
#  Panoramix v4 Oct 2019 
#  Decompiled source of poly:0xA5F1Ea7DF861952863dF2e8d1312f7305dabf215
# 
#  Let's make the world open source 
# 
#
#  I failed with these: 
#  - unknown0c53c51c(?)
#  - unknown14a26f0d(?)
#  - safeTransferFrom(address _from, address _to, uint256 _tokenId)
#  - unknown763e9466(?)
#  - unknown805ab9d1(?)
#  - safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes _data)
#  - tokenURI(uint256 _tokenId)
#  All the rest is below.
#

const unknown18988376 = ('core_owners' << 168)
const unknown530d8098 = 0x636f72655f6f776e6572735f61646d696e000000000000000000000000000000
const unknown55f6e842 = 0x636f72655f636f6e7472616374735f61646d696e000000000000000000000000
const unknowna217fddf = 0
const unknownafaaed94 = 0x556e6e616d656420466f616c0000000000000000000000000000000000000000
const unknownbb4e5223 = ('core_contracts' << 144)

def storage:
  unknown248a9ca3 is mapping of struct at storage 0
  stor1 is mapping of uint8 at storage 1
  tokenOfOwnerByIndex is array of uint256 at storage 2
  tokenByIndex is array of struct at storage 3
  stor4 is mapping of uint256 at storage 4
  approved is mapping of addr at storage 5
  stor6 is mapping of uint8 at storage 6
  name is array of uint256 at storage 7
  symbol is array of uint256 at storage 8
  stor9 is array of struct at storage 9
  baseURI is array of uint256 at storage 10
  paused is uint8 at storage 11
  unknowned24911d is uint256 at storage 12
  nonce is mapping of uint256 at storage 13
  stor16 is uint256 at storage 16
  stor17 is uint256 at storage 17
  stor18 is uint256 at storage 18
  stor19 is addr at storage 19
  unknown3ef5d325 is mapping of struct at storage 20
  stor21 is mapping of uint8 at storage 21

def tokenExists(uint256 _tokenId): # not payable
  require calldata.size - 4 >= 32
  return bool(stor4[_tokenId])

def supportsInterface(bytes4 _interfaceId): # not payable
  require calldata.size - 4 >= 32
  return bool(stor1[Mask(32, 224, _interfaceId)])

def name(): # not payable
  return name[0 len name.length]

def getApproved(uint256 _tokenId): # not payable
  require calldata.size - 4 >= 32
  if not stor4[_tokenId]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  44,
                  0x734552433732313a20617070726f76656420717565727920666f72206e6f6e6578697374656e7420746f6b65,
                  mem[208 len 20]
  return approved[_tokenId]

def totalSupply(): # not payable
  return tokenByIndex.length

def unknown18da2f26(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return bool(stor21[_param1])

def unknown248a9ca3(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown248a9ca3[_param1].field_512

def getNonce(address _addr): # not payable
  require calldata.size - 4 >= 32
  return nonce[addr(_addr)]

def tokenOfOwnerByIndex(address _owner, uint256 _index): # not payable
  require calldata.size - 4 >= 64
  if _index >= tokenOfOwnerByIndex[addr(_owner)]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  34,
                  0xfe456e756d657261626c655365743a20696e646578206f7574206f6620626f756e64,
                  mem[198 len 30]
  return tokenOfOwnerByIndex[addr(_owner)][_index]

def unknown3ef5d325(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown3ef5d325[_param1].field_512

def tokenByIndex(uint256 _index): # not payable
  require calldata.size - 4 >= 32
  if _index >= tokenByIndex.length:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  34,
                  0x6e456e756d657261626c654d61703a20696e646578206f7574206f6620626f756e64,
                  mem[198 len 30]
  return tokenByIndex[_index].field_0

def paused(): # not payable
  return bool(paused)

def ownerOf(uint256 _tokenId): # not payable
  require calldata.size - 4 >= 32
  if not stor4[_tokenId]:
      revert with 0, 
                  32,
                  41,
                  0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                  mem[169 len 23],
                  mem[215 len 9]
  require stor4[_tokenId] - 1 < tokenByIndex.length
  return tokenByIndex[stor4[_tokenId] - 1].field_256

def baseURI(): # not payable
  return baseURI[0 len baseURI.length]

def balanceOf(address _owner): # not payable
  require calldata.size - 4 >= 32
  if not _owner:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  42,
                  0x6c4552433732313a2062616c616e636520717565727920666f7220746865207a65726f20616464726573,
                  mem[206 len 22]
  return tokenOfOwnerByIndex[addr(_owner)]

def unknown8f8b5cde(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown3ef5d325[_param1].field_0, 
         unknown3ef5d325[_param1].field_256,
         unknown3ef5d325[_param1].field_512,
         unknown3ef5d325[_param1].field_768,
         unknown3ef5d325[_param1].field_1024,
         unknown3ef5d325[_param1].field_1280,
         unknown3ef5d325[_param1].field_1536,
         unknown3ef5d325[_param1].field_1792,
         unknown3ef5d325[_param1].field_2048

def unknown9010d07c(uint256 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  if _param2 >= unknown248a9ca3[_param1].field_0:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  34,
                  0xfe456e756d657261626c655365743a20696e646578206f7574206f6620626f756e64,
                  mem[198 len 30]
  return unknown248a9ca3[_param1][_param2].field_0

def unknown91d14854(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  return bool(unknown248a9ca3[_param1][1][addr(_param2)].field_0)

def symbol(): # not payable
  return symbol[0 len symbol.length]

def unknownca15c873(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown248a9ca3[_param1].field_0

def isApprovedForAll(address _owner, address _operator): # not payable
  require calldata.size - 4 >= 64
  return bool(stor6[addr(_owner)][addr(_operator)])

def unknowned24911d(): # not payable
  return unknowned24911d

def unknownf66b48da(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown3ef5d325[_param1].field_1280, 
         unknown3ef5d325[_param1].field_512,
         unknown3ef5d325[_param1].field_768,
         unknown3ef5d325[_param1].field_256,
         unknown3ef5d325[_param1].field_1024,
         unknown3ef5d325[_param1].field_1536,
         unknown3ef5d325[_param1].field_1792,
         unknown3ef5d325[_param1].field_2048,
         unknown3ef5d325[_param1].field_0

#
#  Regular functions
#

def _fallback() payable: # default function
  revert

def nextTokenId(): # not payable
  if stor18 + tokenByIndex.length < tokenByIndex.length:
      revert with 0, 'SafeMath: addition overflow'
  return (stor18 + tokenByIndex.length)

def unknownfbf5cacd(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if caller != this.address:
      if not unknown248a9ca3['core_owners'][1][caller].field_0:
          revert with 0, 'nCore: unauthorized'
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3['core_owners'][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 'nCore: unauthorized'
  stor19 = _param1

def unknown6678268c(array _param1, array _param2, uint256 _param3): # not payable
  require calldata.size - 4 >= 96
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + _param1.length + 36 <= calldata.size
  require _param2 <= 4294967296
  require _param2 + 36 <= calldata.size
  require _param2.length <= 4294967296 and _param2 + _param2.length + 36 <= calldata.size
  unknowned24911d = sha3(sha3(0x29454950373132446f6d61696e28737472696e67206e616d652c737472696e672076657273696f6e2c6164647265737320766572696679696e67436f6e74726163742c627974657333322073616c74), sha3(_param1[all]), sha3(_param2[all]), this.address, _param3)

def unknown3ca49f02(uint256 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  if caller != this.address:
      if not unknown248a9ca3['core_owners'][1][caller].field_0:
          revert with 0, 'nCore: unauthorized'
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3['core_owners'][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 'nCore: unauthorized'
  if stor21[_param2]:
      revert with 0, 'Core: name already taken'
  stor21[_param2] = 1
  unknown3ef5d325[_param1].field_1792 = _param2
  log 0xa44db362: _param1, _param2

def setBaseURI(string _baseURI): # not payable
  require calldata.size - 4 >= 32
  require _baseURI <= 4294967296
  require _baseURI + 36 <= calldata.size
  require _baseURI.length <= 4294967296 and _baseURI + _baseURI.length + 36 <= calldata.size
  if caller != this.address:
      if not unknown248a9ca3['core_owners'][1][caller].field_0:
          revert with 0, 'nCore: unauthorized'
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3['core_owners'][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 'nCore: unauthorized'
  if _baseURI.length:
      baseURI[] = Array(len=_baseURI.length, data=_baseURI[all])
  else:
      baseURI.length = 0
      idx = 0
      while baseURI.length + 31 / 32 > idx:
          baseURI[idx] = 0
          idx = idx + 1
          continue 

def pause(): # not payable
  if caller != this.address:
      if not unknown248a9ca3['core_owners'][1][caller].field_0:
          revert with 0, 'nCore: unauthorized'
      if paused:
          revert with 0, 'Pausable: paused'
      paused = 1
      if caller != this.address:
          log Paused(address account=caller)
      else:
          mem[96] = calldata.size
          mem[128 len calldata.size] = call.data[0 len calldata.size]
          log Paused(address account=mem[calldata.size + 108 len 20])
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3['core_owners'][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 'nCore: unauthorized'
      if paused:
          revert with 0, 'Pausable: paused'
      paused = 1
      if caller != this.address:
          log Paused(address account=caller)
      else:
          mem[ceil32(calldata.size) + 128] = calldata.size
          mem[ceil32(calldata.size) + 160 len calldata.size] = call.data[0 len calldata.size]
          log Paused(address account=mem[calldata.size + ceil32(calldata.size) + 140 len 20])

def unpause(): # not payable
  if caller != this.address:
      if not unknown248a9ca3['core_owners'][1][caller].field_0:
          revert with 0, 'nCore: unauthorized'
      if not paused:
          revert with 0, 'Pausable: not paused'
      paused = 0
      if caller != this.address:
          log Unpaused(address account=caller)
      else:
          mem[96] = calldata.size
          mem[128 len calldata.size] = call.data[0 len calldata.size]
          log Unpaused(address account=mem[calldata.size + 108 len 20])
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3['core_owners'][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 'nCore: unauthorized'
      if not paused:
          revert with 0, 'Pausable: not paused'
      paused = 0
      if caller != this.address:
          log Unpaused(address account=caller)
      else:
          mem[ceil32(calldata.size) + 128] = calldata.size
          mem[ceil32(calldata.size) + 160 len calldata.size] = call.data[0 len calldata.size]
          log Unpaused(address account=mem[calldata.size + ceil32(calldata.size) + 140 len 20])

def unknown0c31824c(addr _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5, uint256 _param6, uint256 _param7, uint256 _param8, uint256 _param9, uint256 _param10): # not payable
  require calldata.size - 4 >= 320
  if caller != this.address:
      if not unknown248a9ca3['core_owners'][1][caller].field_0:
          revert with 0, 'nCore: unauthorized'
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3['core_owners'][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 'nCore: unauthorized'
  unknown3ef5d325[_param2].field_0 = _param1
  unknown3ef5d325[_param2].field_256 = _param6
  unknown3ef5d325[_param2].field_512 = _param4
  unknown3ef5d325[_param2].field_768 = _param5
  unknown3ef5d325[_param2].field_1024 = _param7
  unknown3ef5d325[_param2].field_1280 = _param3
  unknown3ef5d325[_param2].field_1536 = _param8
  unknown3ef5d325[_param2].field_1792 = _param9
  unknown3ef5d325[_param2].field_2048 = _param10

def setApprovalForAll(address _to, bool _approved): # not payable
  require calldata.size - 4 >= 64
  if caller != this.address:
      if _to == caller:
          revert with 0, 'ERC721: approve to caller'
      if caller != this.address:
          stor6[caller][addr(_to)] = uint8(_approved)
          log ApprovalForAll(
                address owner=_approved,
                address operator=caller,
                bool approved=_to)
      else:
          mem[96] = calldata.size
          mem[128 len calldata.size] = call.data[0 len calldata.size]
          stor6[mem[calldata.size + 108 len 20]][addr(_to)] = uint8(_approved)
          mem[ceil32(calldata.size) + 128] = calldata.size
          mem[ceil32(calldata.size) + 160 len calldata.size] = call.data[0 len calldata.size]
          log ApprovalForAll(
                address owner=_approved,
                address operator=mem[calldata.size + ceil32(calldata.size) + 140 len 20],
                bool approved=_to)
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if _to == mem[calldata.size + 108 len 20]:
          revert with 0, 'ERC721: approve to caller'
      if caller != this.address:
          stor6[caller][addr(_to)] = uint8(_approved)
          log ApprovalForAll(
                address owner=_approved,
                address operator=caller,
                bool approved=_to)
      else:
          mem[ceil32(calldata.size) + 128] = calldata.size
          mem[ceil32(calldata.size) + 160 len calldata.size] = call.data[0 len calldata.size]
          stor6[mem[calldata.size + ceil32(calldata.size) + 140 len 20]][addr(_to)] = uint8(_approved)
          mem[(2 * ceil32(calldata.size)) + 160] = calldata.size
          mem[(2 * ceil32(calldata.size)) + 192 len calldata.size] = call.data[0 len calldata.size]
          log ApprovalForAll(
                address owner=_approved,
                address operator=mem[calldata.size + (2 * ceil32(calldata.size)) + 172 len 20],
                bool approved=_to)

def unknown515fe4b3(array _param1, array _param2): # not payable
  require calldata.size - 4 >= 64
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + (32 * _param1.length) + 36 <= calldata.size
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  require _param2 <= 4294967296
  require _param2 + 36 <= calldata.size
  require _param2.length <= 4294967296 and _param2 + (32 * _param2.length) + 36 <= calldata.size
  mem[(32 * _param1.length) + 128] = _param2.length
  mem[(32 * _param1.length) + 160 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  mem[(32 * _param1.length) + (32 * _param2.length) + 160] = 0
  if caller != this.address:
      if not unknown248a9ca3['core_owners'][1][caller].field_0:
          revert with 0, 'nCore: unauthorized'
  else:
      mem[(32 * _param1.length) + (32 * _param2.length) + 160] = calldata.size
      mem[(32 * _param1.length) + (32 * _param2.length) + 192 len calldata.size] = call.data[0 len calldata.size]
      mem[(32 * _param1.length) + (32 * _param2.length) + calldata.size + 192] = 0
      if not unknown248a9ca3['core_owners'][1][addr(mem[calldata.size + (32 * _param1.length) + (32 * _param2.length) + 160])].field_0:
          revert with 0, 'nCore: unauthorized'
  idx = 0
  while idx < _param1.length:
      require idx < _param2.length
      if stor21[mem[(32 * idx) + (32 * _param1.length) + 160]]:
          revert with 0, 'Core: name already taken'
      require idx < _param2.length
      stor21[mem[(32 * idx) + (32 * _param1.length) + 160]] = 1
      require idx < _param2.length
      require idx < _param1.length
      mem[0] = mem[(32 * idx) + 128]
      mem[32] = 20
      unknown3ef5d325[mem[(32 * idx) + 128]].field_1792 = mem[(32 * idx) + (32 * _param1.length) + 160]
      idx = idx + 1
      continue 
  log 0x7dd02a33: _param1.length

def unknown20122c76(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if caller != this.address:
      if not unknown248a9ca3[0x636f72655f6f776e6572735f61646d696e000000000000000000000000000000][1][caller].field_0:
          revert with 0, 'nCore: unauthorized'
      if not unknown248a9ca3[_param1][1][addr(_param2)].field_0:
          unknown248a9ca3[_param1].field_0++
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0 = _param2
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_160 = 0
          unknown248a9ca3[_param1][1][addr(_param2)].field_0 = unknown248a9ca3[_param1].field_0
          if caller != this.address:
              log 0x2f878811: _param1, _param2, caller
          else:
              mem[96] = calldata.size
              mem[128 len calldata.size] = call.data[0 len calldata.size]
              log 0x2f878811: _param1, _param2, mem[calldata.size + 108 len 20]
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3[0x636f72655f6f776e6572735f61646d696e000000000000000000000000000000][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 'nCore: unauthorized'
      if not unknown248a9ca3[_param1][1][addr(_param2)].field_0:
          unknown248a9ca3[_param1].field_0++
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0 = _param2
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_160 = 0
          unknown248a9ca3[_param1][1][addr(_param2)].field_0 = unknown248a9ca3[_param1].field_0
          if caller != this.address:
              log 0x2f878811: _param1, _param2, caller
          else:
              mem[ceil32(calldata.size) + 128] = calldata.size
              mem[ceil32(calldata.size) + 160 len calldata.size] = call.data[0 len calldata.size]
              log 0x2f878811: _param1, _param2, mem[calldata.size + ceil32(calldata.size) + 140 len 20]

def unknown2f2ff15d(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if caller != this.address:
      if not unknown248a9ca3[unknown248a9ca3[_param1].field_512][1][caller].field_0:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      47,
                      0x64416363657373436f6e74726f6c3a2073656e646572206d75737420626520616e2061646d696e20746f206772616e,
                      mem[211 len 17]
      if not unknown248a9ca3[_param1][1][addr(_param2)].field_0:
          unknown248a9ca3[_param1].field_0++
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0 = _param2
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_160 = 0
          unknown248a9ca3[_param1][1][addr(_param2)].field_0 = unknown248a9ca3[_param1].field_0
          if caller != this.address:
              log 0x2f878811: _param1, _param2, caller
          else:
              mem[96] = calldata.size
              mem[128 len calldata.size] = call.data[0 len calldata.size]
              log 0x2f878811: _param1, _param2, mem[calldata.size + 108 len 20]
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3[unknown248a9ca3[_param1].field_512][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 
                      32,
                      47,
                      0x64416363657373436f6e74726f6c3a2073656e646572206d75737420626520616e2061646d696e20746f206772616e,
                      mem[ceil32(calldata.size) + 243 len 17]
      if not unknown248a9ca3[_param1][1][addr(_param2)].field_0:
          unknown248a9ca3[_param1].field_0++
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0 = _param2
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_160 = 0
          unknown248a9ca3[_param1][1][addr(_param2)].field_0 = unknown248a9ca3[_param1].field_0
          if caller != this.address:
              log 0x2f878811: _param1, _param2, caller
          else:
              mem[ceil32(calldata.size) + 128] = calldata.size
              mem[ceil32(calldata.size) + 160 len calldata.size] = call.data[0 len calldata.size]
              log 0x2f878811: _param1, _param2, mem[calldata.size + ceil32(calldata.size) + 140 len 20]

def unknown36568abe(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if caller != this.address:
      if _param2 != caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      47,
                      0x64416363657373436f6e74726f6c3a2063616e206f6e6c792072656e6f756e636520726f6c657320666f722073656c,
                      mem[211 len 17]
      if unknown248a9ca3[_param1][1][addr(_param2)].field_0:
          require unknown248a9ca3[_param1].field_0 - 1 < unknown248a9ca3[_param1].field_0
          require unknown248a9ca3[_param1][1][addr(_param2)].field_0 - 1 < unknown248a9ca3[_param1].field_0
          unknown248a9ca3[_param1][unknown248a9ca3[_param1][1][addr(_param2)].field_0].field_0 = unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0
          unknown248a9ca3[_param1][1][unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0].field_0 = unknown248a9ca3[_param1][1][addr(_param2)].field_0
          require unknown248a9ca3[_param1].field_0
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0 = 0
          unknown248a9ca3[_param1].field_0--
          unknown248a9ca3[_param1][1][addr(_param2)].field_0 = 0
          if caller != this.address:
              log 0xf6391f5c: _param1, _param2, caller
          else:
              mem[96] = calldata.size
              mem[128 len calldata.size] = call.data[0 len calldata.size]
              log 0xf6391f5c: _param1, _param2, mem[calldata.size + 108 len 20]
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if _param2 != mem[calldata.size + 108 len 20]:
          revert with 0, 
                      32,
                      47,
                      0x64416363657373436f6e74726f6c3a2063616e206f6e6c792072656e6f756e636520726f6c657320666f722073656c,
                      mem[ceil32(calldata.size) + 243 len 17]
      if unknown248a9ca3[_param1][1][addr(_param2)].field_0:
          require unknown248a9ca3[_param1].field_0 - 1 < unknown248a9ca3[_param1].field_0
          require unknown248a9ca3[_param1][1][addr(_param2)].field_0 - 1 < unknown248a9ca3[_param1].field_0
          unknown248a9ca3[_param1][unknown248a9ca3[_param1][1][addr(_param2)].field_0].field_0 = unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0
          unknown248a9ca3[_param1][1][unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0].field_0 = unknown248a9ca3[_param1][1][addr(_param2)].field_0
          require unknown248a9ca3[_param1].field_0
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0 = 0
          unknown248a9ca3[_param1].field_0--
          unknown248a9ca3[_param1][1][addr(_param2)].field_0 = 0
          if caller != this.address:
              log 0xf6391f5c: _param1, _param2, caller
          else:
              mem[ceil32(calldata.size) + 128] = calldata.size
              mem[ceil32(calldata.size) + 160 len calldata.size] = call.data[0 len calldata.size]
              log 0xf6391f5c: _param1, _param2, mem[calldata.size + ceil32(calldata.size) + 140 len 20]

def unknownd547741f(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if caller != this.address:
      if not unknown248a9ca3[unknown248a9ca3[_param1].field_512][1][caller].field_0:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      48,
                      0x416363657373436f6e74726f6c3a2073656e646572206d75737420626520616e2061646d696e20746f207265766f6b00,
                      mem[212 len 16]
      if unknown248a9ca3[_param1][1][addr(_param2)].field_0:
          require unknown248a9ca3[_param1].field_0 - 1 < unknown248a9ca3[_param1].field_0
          require unknown248a9ca3[_param1][1][addr(_param2)].field_0 - 1 < unknown248a9ca3[_param1].field_0
          unknown248a9ca3[_param1][unknown248a9ca3[_param1][1][addr(_param2)].field_0].field_0 = unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0
          unknown248a9ca3[_param1][1][unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0].field_0 = unknown248a9ca3[_param1][1][addr(_param2)].field_0
          require unknown248a9ca3[_param1].field_0
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0 = 0
          unknown248a9ca3[_param1].field_0--
          unknown248a9ca3[_param1][1][addr(_param2)].field_0 = 0
          if caller != this.address:
              log 0xf6391f5c: _param1, _param2, caller
          else:
              mem[96] = calldata.size
              mem[128 len calldata.size] = call.data[0 len calldata.size]
              log 0xf6391f5c: _param1, _param2, mem[calldata.size + 108 len 20]
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3[unknown248a9ca3[_param1].field_512][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 
                      32,
                      48,
                      0x416363657373436f6e74726f6c3a2073656e646572206d75737420626520616e2061646d696e20746f207265766f6b00,
                      mem[ceil32(calldata.size) + 244 len 16]
      if unknown248a9ca3[_param1][1][addr(_param2)].field_0:
          require unknown248a9ca3[_param1].field_0 - 1 < unknown248a9ca3[_param1].field_0
          require unknown248a9ca3[_param1][1][addr(_param2)].field_0 - 1 < unknown248a9ca3[_param1].field_0
          unknown248a9ca3[_param1][unknown248a9ca3[_param1][1][addr(_param2)].field_0].field_0 = unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0
          unknown248a9ca3[_param1][1][unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0].field_0 = unknown248a9ca3[_param1][1][addr(_param2)].field_0
          require unknown248a9ca3[_param1].field_0
          unknown248a9ca3[_param1][unknown248a9ca3[_param1].field_0].field_0 = 0
          unknown248a9ca3[_param1].field_0--
          unknown248a9ca3[_param1][1][addr(_param2)].field_0 = 0
          if caller != this.address:
              log 0xf6391f5c: _param1, _param2, caller
          else:
              mem[ceil32(calldata.size) + 128] = calldata.size
              mem[ceil32(calldata.size) + 160 len calldata.size] = call.data[0 len calldata.size]
              log 0xf6391f5c: _param1, _param2, mem[calldata.size + ceil32(calldata.size) + 140 len 20]

def approve(address _spender, uint256 _value): # not payable
  require calldata.size - 4 >= 64
  if not stor4[_value]:
      revert with 0, 
                  32,
                  41,
                  0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                  mem[169 len 23],
                  mem[215 len 9]
  require stor4[_value] - 1 < tokenByIndex.length
  if _spender == tokenByIndex[stor4[_value] - 1].field_256:
      revert with 0, 32, 33, 0x644552433732313a20617070726f76616c20746f2063757272656e74206f776e65, mem[293 len 31]
  if caller != this.address:
      if caller == tokenByIndex[stor4[_value] - 1].field_256:
          approved[_value] = _spender
          if not stor4[_value]:
              revert with 0, 
                          32,
                          41,
                          0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                          mem[265 len 23],
                          mem[311 len 9]
      else:
          if caller != this.address:
              if not stor6[stor3[stor4[_value] - 1].field_256][caller]:
                  revert with 0, 
                              32,
                              56,
                              0x524552433732313a20617070726f76652063616c6c6572206973206e6f74206f776e6572206e6f7220617070726f76656420666f7220616c,
                              mem[316 len 8]
              approved[_value] = _spender
              if not stor4[_value]:
                  revert with 0, 
                              32,
                              41,
                              0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                              mem[265 len 23],
                              mem[311 len 9]
          else:
              mem[192] = calldata.size
              mem[224 len calldata.size] = call.data[0 len calldata.size]
              if not stor6[stor3[stor4[_value] - 1].field_256][addr(mem[calldata.size + 192])]:
                  revert with 0, 
                              32,
                              56,
                              0x524552433732313a20617070726f76652063616c6c6572206973206e6f74206f776e6572206e6f7220617070726f76656420666f7220616c,
                              mem[ceil32(calldata.size) + 348 len 8]
              approved[_value] = _spender
              if not stor4[_value]:
                  revert with 0, 
                              32,
                              41,
                              0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                              mem[ceil32(calldata.size) + 297 len 23],
                              mem[ceil32(calldata.size) + 343 len 9]
  else:
      mem[192] = calldata.size
      mem[224 len calldata.size] = call.data[0 len calldata.size]
      if mem[calldata.size + 204 len 20] == tokenByIndex[stor4[_value] - 1].field_256:
          approved[_value] = _spender
          if not stor4[_value]:
              revert with 0, 
                          32,
                          41,
                          0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                          mem[ceil32(calldata.size) + 297 len 23],
                          mem[ceil32(calldata.size) + 343 len 9]
      else:
          if caller != this.address:
              if not stor6[stor3[stor4[_value] - 1].field_256][caller]:
                  revert with 0, 
                              32,
                              56,
                              0x524552433732313a20617070726f76652063616c6c6572206973206e6f74206f776e6572206e6f7220617070726f76656420666f7220616c,
                              mem[ceil32(calldata.size) + 348 len 8]
              approved[_value] = _spender
              if not stor4[_value]:
                  revert with 0, 
                              32,
                              41,
                              0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                              mem[ceil32(calldata.size) + 297 len 23],
                              mem[ceil32(calldata.size) + 343 len 9]
          else:
              mem[ceil32(calldata.size) + 224] = calldata.size
              mem[ceil32(calldata.size) + 256 len calldata.size] = call.data[0 len calldata.size]
              if not stor6[stor3[stor4[_value] - 1].field_256][addr(mem[calldata.size + ceil32(calldata.size) + 224])]:
                  revert with 0, 
                              32,
                              56,
                              0x524552433732313a20617070726f76652063616c6c6572206973206e6f74206f776e6572206e6f7220617070726f76656420666f7220616c,
                              mem[(2 * ceil32(calldata.size)) + 380 len 8]
              approved[_value] = _spender
              if not stor4[_value]:
                  revert with 0, 
                              32,
                              41,
                              0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                              mem[(2 * ceil32(calldata.size)) + 329 len 23],
                              mem[(2 * ceil32(calldata.size)) + 375 len 9]
  ('bool', ('stor', ('map', ('param', '_value'), ('name', 'stor4', 4))))
  require stor4[_value] - 1 < tokenByIndex.length
  log Approval(
        address owner=tokenByIndex[stor4[_value] - 1].field_256,
        address spender=_spender,
        uint256 value=_value)

def unknown382f217e(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if caller != this.address:
      if not unknown248a9ca3['core_owners'][1][caller].field_0:
          revert with 0, 'nCore: unauthorized'
      if not _param2:
          revert with 0, 'Core: address is null'
      if not stor4[_param1]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[169 len 23],
                      mem[215 len 9]
      require stor4[_param1] - 1 < tokenByIndex.length
      if not stor4[_param1]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[265 len 23],
                      mem[311 len 9]
      require stor4[_param1] - 1 < tokenByIndex.length
      if tokenByIndex[stor4[_param1] - 1].field_256 != tokenByIndex[stor4[_param1] - 1].field_256:
          revert with 0, 32, 41, 0x6e4552433732313a207472616e73666572206f6620746f6b656e2074686174206973206e6f74206f77, mem[397 len 23]
      if not _param2:
          revert with 0, 32, 36, 0x294552433732313a207472616e7366657220746f20746865207a65726f20616464726573, mem[392 len 28]
      if paused:
          revert with 0, 32, 43, 0x734552433732315061757361626c653a20746f6b656e207472616e73666572207768696c65207061757365, mem[399 len 21]
      approved[_param1] = 0
      if not stor4[_param1]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[361 len 23],
                      mem[407 len 9]
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3['core_owners'][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 'nCore: unauthorized'
      if not _param2:
          revert with 0, 'Core: address is null'
      if not stor4[_param1]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[ceil32(calldata.size) + 201 len 23],
                      mem[ceil32(calldata.size) + 247 len 9]
      require stor4[_param1] - 1 < tokenByIndex.length
      if not stor4[_param1]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[ceil32(calldata.size) + 297 len 23],
                      mem[ceil32(calldata.size) + 343 len 9]
      require stor4[_param1] - 1 < tokenByIndex.length
      if tokenByIndex[stor4[_param1] - 1].field_256 != tokenByIndex[stor4[_param1] - 1].field_256:
          revert with 0, 
                      32,
                      41,
                      0x6e4552433732313a207472616e73666572206f6620746f6b656e2074686174206973206e6f74206f77,
                      mem[ceil32(calldata.size) + 429 len 23]
      if not _param2:
          revert with 0, 
                      32,
                      36,
                      0x294552433732313a207472616e7366657220746f20746865207a65726f20616464726573,
                      mem[ceil32(calldata.size) + 424 len 28]
      if paused:
          revert with 0, 
                      32,
                      43,
                      0x734552433732315061757361626c653a20746f6b656e207472616e73666572207768696c65207061757365,
                      mem[ceil32(calldata.size) + 431 len 21]
      approved[_param1] = 0
      if not stor4[_param1]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[ceil32(calldata.size) + 393 len 23],
                      mem[ceil32(calldata.size) + 439 len 9]
  ('bool', ('stor', ('map', ('param', '_param1'), ('name', 'stor4', 4))))
  require stor4[_param1] - 1 < tokenByIndex.length
  log Approval(
        address owner=tokenByIndex[stor4[_param1] - 1].field_256,
        address spender=0,
        uint256 value=_param1)
  if tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256][1][_param1]:
      require tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256] - 1 < tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256]
      require tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256][1][_param1] - 1 < tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256]
      tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256][tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256][1][_param1]] = tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256][tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256]]
      tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256][1][tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256][tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256]]] = tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256][1][_param1]
      require tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256]
      tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256][tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256]] = 0
      tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256]--
      tokenOfOwnerByIndex[stor3[stor4[_param1] - 1].field_256][1][_param1] = 0
  if not tokenOfOwnerByIndex[addr(_param2)][1][_param1]:
      tokenOfOwnerByIndex[addr(_param2)]++
      tokenOfOwnerByIndex[addr(_param2)][tokenOfOwnerByIndex[addr(_param2)]] = _param1
      tokenOfOwnerByIndex[addr(_param2)][1][_param1] = tokenOfOwnerByIndex[addr(_param2)]
  if stor4[_param1]:
      require stor4[_param1] - 1 < tokenByIndex.length
      tokenByIndex[stor4[_param1] - 1].field_256 = _param2
      tokenByIndex[stor4[_param1] - 1].field_416 = 0
  else:
      tokenByIndex.length++
      tokenByIndex[tokenByIndex.length].field_0 = _param1
      tokenByIndex[tokenByIndex.length].field_256 = _param2
      tokenByIndex[tokenByIndex.length].field_416 = 0
      stor4[_param1] = tokenByIndex.length
  log Transfer(
        address from=tokenByIndex[stor4[_param1] - 1].field_256,
        address to=_param2,
        uint256 value=_param1)

def burn(uint256 _value): # not payable
  require calldata.size - 4 >= 32
  if paused:
      revert with 0, 'Pausable: paused'
  if not stor4[_value]:
      revert with 0, 'Core: token does not exist'
  if caller != this.address:
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[169 len 23],
                      mem[215 len 9]
      require stor4[_value] - 1 < tokenByIndex.length
      if tokenByIndex[stor4[_value] - 1].field_256 != caller:
          revert with 0, 'Core: not owner of token'
      stor18++
      unknown3ef5d325[_value].field_0 = 0
      unknown3ef5d325[_value].field_256 = 0
      unknown3ef5d325[_value].field_512 = 0
      unknown3ef5d325[_value].field_768 = 0
      unknown3ef5d325[_value].field_1024 = 0
      unknown3ef5d325[_value].field_1280 = 0
      unknown3ef5d325[_value].field_1536 = 0
      unknown3ef5d325[_value].field_1792 = 0
      unknown3ef5d325[_value].field_2048 = 0
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[265 len 23],
                      mem[311 len 9]
      require stor4[_value] - 1 < tokenByIndex.length
      if paused:
          revert with 0, 32, 43, 0x734552433732315061757361626c653a20746f6b656e207472616e73666572207768696c65207061757365, mem[399 len 21]
      approved[_value] = 0
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[361 len 23],
                      mem[407 len 9]
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[ceil32(calldata.size) + 201 len 23],
                      mem[ceil32(calldata.size) + 247 len 9]
      require stor4[_value] - 1 < tokenByIndex.length
      if tokenByIndex[stor4[_value] - 1].field_256 != mem[calldata.size + 108 len 20]:
          revert with 0, 'Core: not owner of token'
      stor18++
      unknown3ef5d325[_value].field_0 = 0
      unknown3ef5d325[_value].field_256 = 0
      unknown3ef5d325[_value].field_512 = 0
      unknown3ef5d325[_value].field_768 = 0
      unknown3ef5d325[_value].field_1024 = 0
      unknown3ef5d325[_value].field_1280 = 0
      unknown3ef5d325[_value].field_1536 = 0
      unknown3ef5d325[_value].field_1792 = 0
      unknown3ef5d325[_value].field_2048 = 0
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[ceil32(calldata.size) + 297 len 23],
                      mem[ceil32(calldata.size) + 343 len 9]
      require stor4[_value] - 1 < tokenByIndex.length
      if paused:
          revert with 0, 
                      32,
                      43,
                      0x734552433732315061757361626c653a20746f6b656e207472616e73666572207768696c65207061757365,
                      mem[ceil32(calldata.size) + 431 len 21]
      approved[_value] = 0
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[ceil32(calldata.size) + 393 len 23],
                      mem[ceil32(calldata.size) + 439 len 9]
  ('bool', ('stor', ('map', ('param', '_value'), ('name', 'stor4', 4))))
  require stor4[_value] - 1 < tokenByIndex.length
  log Approval(
        address owner=tokenByIndex[stor4[_value] - 1].field_256,
        address spender=0,
        uint256 value=_value)
  if Mask(255, 1, stor9[_value].field_0 and (256 * not stor9[_value].field_0) - 1):
      stor9[_value].field_0 = 0
      if 31 < stor9[_value].length:
          idx = 0
          while stor9[_value].length + 31 / 32 > idx:
              stor9[_value][idx].field_0 = 0
              idx = idx + 1
              continue 
  if tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256][1][_value]:
      require tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256] - 1 < tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256]
      require tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256][1][_value] - 1 < tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256]
      tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256][tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256][1][_value]] = tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256][tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256]]
      tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256][1][tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256][tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256]]] = tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256][1][_value]
      require tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256]
      tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256][tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256]] = 0
      tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256]--
      tokenOfOwnerByIndex[stor3[stor4[_value] - 1].field_256][1][_value] = 0
  if stor4[_value]:
      require tokenByIndex.length - 1 < tokenByIndex.length
      require stor4[_value] - 1 < tokenByIndex.length
      tokenByIndex[stor4[_value] - 1].field_0 = tokenByIndex[tokenByIndex.length - 1].field_0
      tokenByIndex[stor4[_value] - 1].field_256 = tokenByIndex[tokenByIndex.length - 1].field_256
      stor4[stor3[stor3.length - 1].field_0] = stor4[_value]
      require tokenByIndex.length
      tokenByIndex[tokenByIndex.length - 1].field_0 = 0
      tokenByIndex[tokenByIndex.length - 1].field_256 = 0
      tokenByIndex.length--
      stor4[_value] = 0
  log Transfer(
        address from=tokenByIndex[stor4[_value] - 1].field_256,
        address to=0,
        uint256 value=_value)

def transferFrom(address _from, address _to, uint256 _value): # not payable
  require calldata.size - 4 >= 96
  if caller != this.address:
      if not stor4[_value]:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      44,
                      0x734552433732313a206f70657261746f7220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[208 len 20]
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[169 len 23],
                      mem[215 len 9]
      require stor4[_value] - 1 < tokenByIndex.length
      if tokenByIndex[stor4[_value] - 1].field_256 != caller:
          if not stor4[_value]:
              revert with 0, 32, 44, 0x734552433732313a20617070726f76656420717565727920666f72206e6f6e6578697374656e7420746f6b65, mem[304 len 20]
          if approved[_value] != caller:
              if not stor6[stor3[stor4[_value] - 1].field_256][caller]:
                  revert with 0, 
                              32,
                              49,
                              0x6c4552433732313a207472616e736665722063616c6c6572206973206e6f74206f776e6572206e6f7220617070726f7665,
                              mem[309 len 15]
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[265 len 23],
                      mem[311 len 9]
      require stor4[_value] - 1 < tokenByIndex.length
      if tokenByIndex[stor4[_value] - 1].field_256 != _from:
          revert with 0, 32, 41, 0x6e4552433732313a207472616e73666572206f6620746f6b656e2074686174206973206e6f74206f77, mem[397 len 23]
      if not _to:
          revert with 0, 32, 36, 0x294552433732313a207472616e7366657220746f20746865207a65726f20616464726573, mem[392 len 28]
      if paused:
          revert with 0, 32, 43, 0x734552433732315061757361626c653a20746f6b656e207472616e73666572207768696c65207061757365, mem[399 len 21]
      approved[_value] = 0
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[361 len 23],
                      mem[407 len 9]
  else:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not stor4[_value]:
          revert with 0, 
                      32,
                      44,
                      0x734552433732313a206f70657261746f7220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[ceil32(calldata.size) + 240 len 20]
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[ceil32(calldata.size) + 201 len 23],
                      mem[ceil32(calldata.size) + 247 len 9]
      require stor4[_value] - 1 < tokenByIndex.length
      if mem[calldata.size + 108 len 20] != tokenByIndex[stor4[_value] - 1].field_256:
          if not stor4[_value]:
              revert with 0, 
                          32,
                          44,
                          0x734552433732313a20617070726f76656420717565727920666f72206e6f6e6578697374656e7420746f6b65,
                          mem[ceil32(calldata.size) + 336 len 20]
          if approved[_value] != mem[calldata.size + 108 len 20]:
              if not stor6[stor3[stor4[_value] - 1].field_256][addr(mem[calldata.size + 96])]:
                  revert with 0, 
                              32,
                              49,
                              0x6c4552433732313a207472616e736665722063616c6c6572206973206e6f74206f776e6572206e6f7220617070726f7665,
                              mem[ceil32(calldata.size) + 341 len 15]
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[ceil32(calldata.size) + 297 len 23],
                      mem[ceil32(calldata.size) + 343 len 9]
      require stor4[_value] - 1 < tokenByIndex.length
      if tokenByIndex[stor4[_value] - 1].field_256 != _from:
          revert with 0, 
                      32,
                      41,
                      0x6e4552433732313a207472616e73666572206f6620746f6b656e2074686174206973206e6f74206f77,
                      mem[ceil32(calldata.size) + 429 len 23]
      if not _to:
          revert with 0, 
                      32,
                      36,
                      0x294552433732313a207472616e7366657220746f20746865207a65726f20616464726573,
                      mem[ceil32(calldata.size) + 424 len 28]
      if paused:
          revert with 0, 
                      32,
                      43,
                      0x734552433732315061757361626c653a20746f6b656e207472616e73666572207768696c65207061757365,
                      mem[ceil32(calldata.size) + 431 len 21]
      approved[_value] = 0
      if not stor4[_value]:
          revert with 0, 
                      32,
                      41,
                      0x734552433732313a206f776e657220717565727920666f72206e6f6e6578697374656e7420746f6b65,
                      mem[ceil32(calldata.size) + 393 len 23],
                      mem[ceil32(calldata.size) + 439 len 9]
  ('bool', ('stor', ('map', ('param', '_value'), ('name', 'stor4', 4))))
  require stor4[_value] - 1 < tokenByIndex.length
  log Approval(
        address owner=tokenByIndex[stor4[_value] - 1].field_256,
        address spender=0,
        uint256 value=_value)
  if tokenOfOwnerByIndex[addr(_from)][1][_value]:
      require tokenOfOwnerByIndex[addr(_from)] - 1 < tokenOfOwnerByIndex[addr(_from)]
      require tokenOfOwnerByIndex[addr(_from)][1][_value] - 1 < tokenOfOwnerByIndex[addr(_from)]
      tokenOfOwnerByIndex[addr(_from)][tokenOfOwnerByIndex[addr(_from)][1][_value]] = tokenOfOwnerByIndex[addr(_from)][tokenOfOwnerByIndex[addr(_from)]]
      tokenOfOwnerByIndex[addr(_from)][1][tokenOfOwnerByIndex[addr(_from)][tokenOfOwnerByIndex[addr(_from)]]] = tokenOfOwnerByIndex[addr(_from)][1][_value]
      require tokenOfOwnerByIndex[addr(_from)]
      tokenOfOwnerByIndex[addr(_from)][tokenOfOwnerByIndex[addr(_from)]] = 0
      tokenOfOwnerByIndex[addr(_from)]--
      tokenOfOwnerByIndex[addr(_from)][1][_value] = 0
  if not tokenOfOwnerByIndex[addr(_to)][1][_value]:
      tokenOfOwnerByIndex[addr(_to)]++
      tokenOfOwnerByIndex[addr(_to)][tokenOfOwnerByIndex[addr(_to)]] = _value
      tokenOfOwnerByIndex[addr(_to)][1][_value] = tokenOfOwnerByIndex[addr(_to)]
  if stor4[_value]:
      require stor4[_value] - 1 < tokenByIndex.length
      tokenByIndex[stor4[_value] - 1].field_256 = _to
      tokenByIndex[stor4[_value] - 1].field_416 = 0
  else:
      tokenByIndex.length++
      tokenByIndex[tokenByIndex.length].field_0 = _value
      tokenByIndex[tokenByIndex.length].field_256 = _to
      tokenByIndex[tokenByIndex.length].field_416 = 0
      stor4[_value] = tokenByIndex.length
  log Transfer(
        address from=_from,
        address to=_to,
        uint256 value=_value)

def unknown185e159a(addr _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5): # not payable
  require calldata.size - 4 >= 160
  if this.address == caller:
      mem[96] = calldata.size
      mem[128 len calldata.size] = call.data[0 len calldata.size]
      if not unknown248a9ca3['core_contracts'][1][addr(mem[calldata.size + 96])].field_0:
          revert with 0, 'nCore: unauthorized'
      if paused:
          revert with 0, 'Pausable: paused'
      if _param2 < 1:
          revert with 0, 'Core: gen out of bounds'
      if _param2 > 10:
          revert with 0, 'Core: gen out of bounds'
      if stor21[_param4]:
          revert with 0, 'Core: name already taken'
      stor21[_param4] = 1
      if stor18 + tokenByIndex.length < tokenByIndex.length:
          revert with 0, 'SafeMath: addition overflow'
      require ext_code.size(stor19)
      static call stor19.0x3ef5d325 with:
              gas gas_remaining wei
             args _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(stor19)
      static call stor19.0x7866ed6e with:
              gas gas_remaining wei
             args _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      unknown3ef5d325[stor18 + stor3.length].field_0 = _param1
      unknown3ef5d325[stor18 + stor3.length].field_256 = _param2
      unknown3ef5d325[stor18 + stor3.length].field_512 = ext_call.return_data[0]
      unknown3ef5d325[stor18 + stor3.length].field_768 = block.timestamp
      unknown3ef5d325[stor18 + stor3.length].field_1024 = ext_call.return_data[0]
      if _param3 != 0x4d616c6500000000000000000000000000000000000000000000000000000000:
          unknown3ef5d325[stor18 + stor3.length].field_1280 = stor17
          unknown3ef5d325[stor18 + stor3.length].field_1536 = 0x46696c6c79000000000000000000000000000000000000000000000000000000
      else:
          unknown3ef5d325[stor18 + stor3.length].field_1280 = stor16
          unknown3ef5d325[stor18 + stor3.length].field_1536 = 0x436f6c7400000000000000000000000000000000000000000000000000000000
      unknown3ef5d325[stor18 + stor3.length].field_1792 = _param4
      unknown3ef5d325[stor18 + stor3.length].field_2048 = _param5
      if not _param1:
          revert with 0, 'ERC721: mint to the zero address'
      if stor4[stor18 + stor3.length]:
          revert with 0, 'ERC721: token already minted'
      if paused:
          revert with 0, 
                      32,
                      43,
                      0x734552433732315061757361626c653a20746f6b656e207472616e73666572207768696c65207061757365,
                      mem[ceil32(calldata.size) + 527 len 21]
      if not tokenOfOwnerByIndex[addr(_param1)][1][stor18 + stor3.length]:
          tokenOfOwnerByIndex[addr(_param1)]++
          tokenOfOwnerByIndex[addr(_param1)][tokenOfOwnerByIndex[addr(_param1)]] = stor18 + tokenByIndex.length
          tokenOfOwnerByIndex[addr(_param1)][1][stor18 + stor3.length] = tokenOfOwnerByIndex[addr(_param1)]
      if stor4[stor18 + stor3.length]:
          require stor4[stor18 + stor3.length] - 1 < tokenByIndex.length
          tokenByIndex[stor4[stor18 + tokenByIndex.length] - 1].field_256 = _param1
          tokenByIndex[stor4[stor18 + tokenByIndex.length] - 1].field_416 = 0
          log Transfer(
                address from=0,
                address to=_param1,
                uint256 value=stor18 + tokenByIndex.length)
          if not stor18 + tokenByIndex.length:
              if not stor4[stor18 + stor3.length]:
                  revert with 0, 
                              32,
                              44,
                              0x6e4552433732314d657461646174613a2055524920736574206f66206e6f6e6578697374656e7420746f6b65,
                              mem[ceil32(calldata.size) + 592 len 20]
              stor9[stor18 + stor3.length].field_0 = 0
              stor9[stor18 + stor3.length].field_1 = 1
              stor9[stor18 + stor3.length].field_248 = 48
              idx = 0
              while stor9[stor18 + stor3.length].length + 31 / 32 > idx:
                  stor9[stor18 + stor3.length][idx].field_0 = 0
                  idx = idx + 1
                  continue 
          else:
              s = 0
              idx = stor18 + tokenByIndex.length
              while idx:
                  s = s + 1
                  idx = idx / 10
                  continue 
              require s <= 18446744073709551615
              if s:
                  mem[ceil32(calldata.size) + 448 len s] = call.data[calldata.size len s]
              t = s - 1
              idx = stor18 + tokenByIndex.length
              while idx:
                  require t < s
                  mem[t + ceil32(calldata.size) + 448 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
                  t = t - 1
                  idx = idx / 10
                  continue 
              if not stor4[stor18 + stor3.length]:
                  revert with 0, 
                              32,
                              44,
                              0x6e4552433732314d657461646174613a2055524920736574206f66206e6f6e6578697374656e7420746f6b65,
                              mem[ceil32(calldata.size) + ceil32(s) + 560 len 20]
              if s:
                  stor9[stor18 + stor3.length][].field_0 = Array(len=s, data=mem[ceil32(calldata.size) + 448 len s])
              else:
                  stor9[stor18 + stor3.length].field_0 = 0
                  idx = 0
                  while stor9[stor18 + stor3.length].length + 31 / 32 > idx:
                      stor9[stor18 + stor3.length][idx].field_0 = 0
                      idx = idx + 1
                      continue 
      else:
          tokenByIndex.length++
          tokenByIndex[tokenByIndex.length].field_0 = stor18 + tokenByIndex.length
          tokenByIndex[tokenByIndex.length].field_256 = _param1
          tokenByIndex[tokenByIndex.length].field_416 = 0
          stor4[stor18 + stor3.length] = tokenByIndex.length
          log Transfer(
                address from=0,
                address to=_param1,
                uint256 value=stor18 + tokenByIndex.length)
          if not stor18 + tokenByIndex.length:
              if not stor4[stor18 + stor3.length]:
                  revert with 0, 
                              32,
                              44,
                              0x6e4552433732314d657461646174613a2055524920736574206f66206e6f6e6578697374656e7420746f6b65,
                              mem[ceil32(calldata.size) + 656 len 20]
              stor9[stor18 + stor3.length].field_0 = 0
              stor9[stor18 + stor3.length].field_1 = 1
              stor9[stor18 + stor3.length].field_248 = 48
              idx = 0
              while stor9[stor18 + stor3.length].length + 31 / 32 > idx:
                  stor9[stor18 + stor3.length][idx].field_0 = 0
                  idx = idx + 1
                  continue 
          else:
              s = 0
              idx = stor18 + tokenByIndex.length
              while idx:
                  s = s + 1
                  idx = idx / 10
                  continue 
              require s <= 18446744073709551615
              if s:
                  mem[ceil32(calldata.size) + 512 len s] = call.data[calldata.size len s]
              t = s - 1
              idx = stor18 + tokenByIndex.length
              while idx:
                  require t < s
                  mem[t + ceil32(calldata.size) + 512 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
                  t = t - 1
                  idx = idx / 10
                  continue 
              if not stor4[stor18 + stor3.length]:
                  revert with 0, 
                              32,
                              44,
                              0x6e4552433732314d657461646174613a2055524920736574206f66206e6f6e6578697374656e7420746f6b65,
                              mem[ceil32(calldata.size) + ceil32(s) + 624 len 20]
              if s:
                  stor9[stor18 + stor3.length][].field_0 = Array(len=s, data=mem[ceil32(calldata.size) + 512 len s])
              else:
                  stor9[stor18 + stor3.length].field_0 = 0
                  idx = 0
                  while stor9[stor18 + stor3.length].length + 31 / 32 > idx:
                      stor9[stor18 + stor3.length][idx].field_0 = 0
                      idx = idx + 1
                      continue 
  else:
      if not unknown248a9ca3['core_contracts'][1][caller].field_0:
          revert with 0, 'nCore: unauthorized'
      if paused:
          revert with 0, 'Pausable: paused'
      if _param2 < 1:
          revert with 0, 'Core: gen out of bounds'
      if _param2 > 10:
          revert with 0, 'Core: gen out of bounds'
      if stor21[_param4]:
          revert with 0, 'Core: name already taken'
      stor21[_param4] = 1
      if stor18 + tokenByIndex.length < tokenByIndex.length:
          revert with 0, 'SafeMath: addition overflow'
      require ext_code.size(stor19)
      static call stor19.0x3ef5d325 with:
              gas gas_remaining wei
             args _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(stor19)
      static call stor19.0x7866ed6e with:
              gas gas_remaining wei
             args _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[192] = block.timestamp
      mem[224] = ext_call.return_data[0]
      mem[320] = _param4
      mem[352] = _param5
      if _param3 != 0x4d616c6500000000000000000000000000000000000000000000000000000000:
          mem[256] = stor17
          mem[288] = 0x46696c6c79000000000000000000000000000000000000000000000000000000
          unknown3ef5d325[stor18 + stor3.length].field_0 = _param1
          unknown3ef5d325[stor18 + stor3.length].field_256 = _param2
          unknown3ef5d325[stor18 + stor3.length].field_512 = ext_call.return_data[0]
          unknown3ef5d325[stor18 + stor3.length].field_768 = block.timestamp
          unknown3ef5d325[stor18 + stor3.length].field_1024 = ext_call.return_data[0]
          unknown3ef5d325[stor18 + stor3.length].field_1280 = stor17
          unknown3ef5d325[stor18 + stor3.length].field_1536 = 0x46696c6c79000000000000000000000000000000000000000000000000000000
      else:
          mem[256] = stor16
          mem[288] = 0x436f6c7400000000000000000000000000000000000000000000000000000000
          unknown3ef5d325[stor18 + stor3.length].field_0 = _param1
          unknown3ef5d325[stor18 + stor3.length].field_256 = _param2
          unknown3ef5d325[stor18 + stor3.length].field_512 = ext_call.return_data[0]
          unknown3ef5d325[stor18 + stor3.length].field_768 = block.timestamp
          unknown3ef5d325[stor18 + stor3.length].field_1024 = ext_call.return_data[0]
          unknown3ef5d325[stor18 + stor3.length].field_1280 = stor16
          unknown3ef5d325[stor18 + stor3.length].field_1536 = 0x436f6c7400000000000000000000000000000000000000000000000000000000
      unknown3ef5d325[stor18 + stor3.length].field_1792 = _param4
      unknown3ef5d325[stor18 + stor3.length].field_2048 = _param5
      if not _param1:
          revert with 0, 'ERC721: mint to the zero address'
      if stor4[stor18 + stor3.length]:
          revert with 0, 'ERC721: token already minted'
      if paused:
          revert with 0, 32, 43, 0x734552433732315061757361626c653a20746f6b656e207472616e73666572207768696c65207061757365, mem[495 len 21]
      if not tokenOfOwnerByIndex[addr(_param1)][1][stor18 + stor3.length]:
          tokenOfOwnerByIndex[addr(_param1)]++
          tokenOfOwnerByIndex[addr(_param1)][tokenOfOwnerByIndex[addr(_param1)]] = stor18 + tokenByIndex.length
          tokenOfOwnerByIndex[addr(_param1)][1][stor18 + stor3.length] = tokenOfOwnerByIndex[addr(_param1)]
      if stor4[stor18 + stor3.length]:
          require stor4[stor18 + stor3.length] - 1 < tokenByIndex.length
          tokenByIndex[stor4[stor18 + tokenByIndex.length] - 1].field_256 = _param1
          tokenByIndex[stor4[stor18 + tokenByIndex.length] - 1].field_416 = 0
          log Transfer(
                address from=0,
                address to=_param1,
                uint256 value=stor18 + tokenByIndex.length)
          if not stor18 + tokenByIndex.length:
              if not stor4[stor18 + stor3.length]:
                  revert with 0, 32, 44, 0x6e4552433732314d657461646174613a2055524920736574206f66206e6f6e6578697374656e7420746f6b65, mem[560 len 20]
              stor9[stor18 + stor3.length].field_0 = 0
              stor9[stor18 + stor3.length].field_1 = 1
              stor9[stor18 + stor3.length].field_248 = 48
              idx = 0
              while stor9[stor18 + stor3.length].length + 31 / 32 > idx:
                  stor9[stor18 + stor3.length][idx].field_0 = 0
                  idx = idx + 1
                  continue 
          else:
              s = 0
              idx = stor18 + tokenByIndex.length
              while idx:
                  s = s + 1
                  idx = idx / 10
                  continue 
              require s <= 18446744073709551615
              mem[384] = s
              mem[64] = ceil32(s) + 416
              if s:
                  mem[416 len s] = call.data[calldata.size len s]
              t = s - 1
              idx = stor18 + tokenByIndex.length
              while idx:
                  require t < mem[384]
                  mem[t + 416 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
                  t = t - 1
                  idx = idx / 10
                  continue 
              if not stor4[stor18 + stor3.length]:
                  revert with 0, 
                              32,
                              44,
                              0x6e4552433732314d657461646174613a2055524920736574206f66206e6f6e6578697374656e7420746f6b65,
                              mem[mem[64] + 112 len 20]
              if mem[384]:
                  stor9[stor18 + stor3.length][].field_0 = Array(len=mem[384], data=mem[416 len mem[384]])
              else:
                  stor9[stor18 + stor3.length].field_0 = 0
                  idx = 0
                  while stor9[stor18 + stor3.length].length + 31 / 32 > idx:
                      stor9[stor18 + stor3.length][idx].field_0 = 0
                      idx = idx + 1
                      continue 
      else:
          mem[384] = stor18 + tokenByIndex.length
          mem[416] = _param1
          tokenByIndex.length++
          tokenByIndex[tokenByIndex.length].field_0 = stor18 + tokenByIndex.length
          tokenByIndex[tokenByIndex.length].field_256 = _param1
          tokenByIndex[tokenByIndex.length].field_416 = 0
          stor4[stor18 + stor3.length] = tokenByIndex.length
          log Transfer(
                address from=0,
                address to=_param1,
                uint256 value=stor18 + tokenByIndex.length)
          if not stor18 + tokenByIndex.length:
              if not stor4[stor18 + stor3.length]:
                  revert with 0, 32, 44, 0x6e4552433732314d657461646174613a2055524920736574206f66206e6f6e6578697374656e7420746f6b65, mem[624 len 20]
              stor9[stor18 + stor3.length].field_0 = 0
              stor9[stor18 + stor3.length].field_1 = 1
              stor9[stor18 + stor3.length].field_248 = 48
              idx = 0
              while stor9[stor18 + stor3.length].length + 31 / 32 > idx:
                  stor9[stor18 + stor3.length][idx].field_0 = 0
                  idx = idx + 1
                  continue 
          else:
              s = 0
              idx = stor18 + tokenByIndex.length
              while idx:
                  s = s + 1
                  idx = idx / 10
                  continue 
              require s <= 18446744073709551615
              mem[448] = s
              mem[64] = ceil32(s) + 480
              if s:
                  mem[480 len s] = call.data[calldata.size len s]
              t = s - 1
              idx = stor18 + tokenByIndex.length
              while idx:
                  require t < mem[448]
                  mem[t + 480 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
                  t = t - 1
                  idx = idx / 10
                  continue 
              if not stor4[stor18 + stor3.length]:
                  revert with 0, 
                              32,
                              44,
                              0x6e4552433732314d657461646174613a2055524920736574206f66206e6f6e6578697374656e7420746f6b65,
                              mem[mem[64] + 112 len 20]
              if mem[448]:
                  stor9[stor18 + stor3.length][].field_0 = Array(len=mem[448], data=mem[480 len mem[448]])
              else:
                  stor9[stor18 + stor3.length].field_0 = 0
                  idx = 0
                  while stor9[stor18 + stor3.length].length + 31 / 32 > idx:
                      stor9[stor18 + stor3.length][idx].field_0 = 0
                      idx = idx + 1
                      continue 
  log 0x8bb39788: addr(_param1), block.timestamp, stor18 + tokenByIndex.length
