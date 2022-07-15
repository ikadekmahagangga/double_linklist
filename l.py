class block:
   def __init__(objek, isiblock):
      objek.isiblock = isiblock
      objek.block_selanjutnya = None
      objek.block_sebelum = None

class dobel_linklist:
   def __init__(objek):
      objek.head = None
	
   def masuk(objek, blocknext):
      block_baru = block(blocknext)
      block_baru.block_selanjutnya = objek.head
      if objek.head is not None:
         objek.head.block_sebelum = block_baru
      objek.head = block_baru
	
   def keluar(objek, block):
      while (block is not None):
         print(block.isiblock),
         blockterakhir = block
         block = block.block_selanjutnya

output = dobel_linklist()
output.masuk(3)
output.masuk(6)
output.masuk(9)
output.keluar(output.head)
