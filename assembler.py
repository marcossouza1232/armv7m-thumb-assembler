comando = input('comando:')
partes = comando.split(' ')
if ( partes[0] == 'movw' ):
	imm16 = int(partes[2], 16)
	str16 = '{:016b}'.format(imm16)
	imm4 = str16[0:4]
	i = str16[4]
	imm3 = str16[5:8]
	imm8 = str16[8:]
	Rd = '{:04b}'.format(int(partes[1],10))
	instruction = '11110' + i + '100100' + imm4 + '0' + imm3 + Rd + imm8
	hexins = '{:08x}'.format(int(instruction,2))
	hexinsp = list(hexins)
	hexinsp[0:2] = hexins[2:4]
	hexinsp[2:4] = hexins[0:2]
	hexinsp[4:6] = hexins[6:]
	hexinsp[6:] = hexins[4:6]
	print(''.join(hexinsp))
elif ( partes[0] == 'movt' ):
	imm16 = int(partes[2], 16)
	str16 = '{:016b}'.format(imm16)
	imm4 = str16[0:4]
	i = str16[4]
	imm3 = str16[5:8]
	imm8 = str16[8:]
	Rd = '{:04b}'.format(int(partes[1],10))
	instruction = '11110' + i + '101100' + imm4 + '0' + imm3 + Rd + imm8
	hexins = '{:08x}'.format(int(instruction,2))
	hexinsp = list(hexins)
	hexinsp[0:2] = hexins[2:4]
	hexinsp[2:4] = hexins[0:2]
	hexinsp[4:6] = hexins[6:]
	hexinsp[6:] = hexins[4:6]
	print(''.join(hexinsp))
elif ( partes[0] == 'mov' ):
	Rm = '{:04b}'.format(int(partes[2],10))
	Rd = '{:03b}'.format(int(partes[1],10))
	instruction = '010001100' + Rm + Rd
	hexins = '{:04x}'.format(int(instruction,2))
	hexinsp = list(hexins)
	hexinsp[0:2] = hexins[2:4]
	hexinsp[2:4] = hexins[0:2]
	print(''.join(hexinsp))
elif ( partes[0] == 'sub' ):
	Rdn = '{:03b}'.format(int(partes[1],10))
	imm8 = '{:08b}'.format(int(partes[2],16))
	instruction = '00111' + Rdn + imm8
	hexins = '{:04x}'.format(int(instruction,2))
	hexinsp = list(hexins)
	hexinsp[0:2] = hexins[2:4]
	hexinsp[2:4] = hexins[0:2]
	print(''.join(hexinsp))
elif ( partes[0] == 'cmp' ):
	Rm = '{:03b}'.format(int(partes[2],10))
	Rn = '{:03b}'.format(int(partes[1],10))
	instruction = '0100001010' + Rm + Rn
	hexins = '{:04x}'.format(int(instruction,2))
	hexinsp = list(hexins)
	hexinsp[0:2] = hexins[2:4]
	hexinsp[2:4] = hexins[0:2]
	print(''.join(hexinsp))
elif ( partes[0] == 'str' ):
	Rt = '{:03b}'.format(int(partes[1],10))
	Rn = '{:03b}'.format(int(partes[2],10))
	instruction = '0110000000' + Rn + Rt
	hexins = '{:04x}'.format(int(instruction,2))
	hexinsp = list(hexins)
	hexinsp[0:2] = hexins[2:4]
	hexinsp[2:4] = hexins[0:2]
	print(''.join(hexinsp))
elif ( partes[0] == 'b' ):
	present_ins = int(input('end ins atual'), 16)
	ins = int(input('end instruction alvo'), 16)
	offset = ins - present_ins - 4
	if ( offset < 0 ):
		offset *= -1
		bits = list('{:012b}'.format(offset)[-12:])
		for i in range(len(bits)):
			if ( bits[i] == '0' ):
				bits[i] = '1'
			else:
				bits[i] = '0'
		offset = int(''.join(bits), 2) + 1
		offset = int('{:011b}'.format(offset)[-12:-1],2)
	instruction = '11100' + '{:011b}'.format(offset)
	hexins = '{:04x}'.format(int(instruction,2))
	hexinsp = list(hexins)
	hexinsp[0:2] = hexins[2:4]
	hexinsp[2:4] = hexins[0:2]
	print(''.join(hexinsp))
elif ( partes[0] == 'beq' ):
	present_ins = int(input('end ins atual'), 16)
	ins = int(input('end instruction alvo'), 16)
	offset = ins - present_ins - 4
	if ( offset < 0 ):
		offset *= -1
		bits = list('{:09b}'.format(offset)[-9:])
		for i in range(len(bits)):
			if ( bits[i] == '0' ):
				bits[i] = '1'
			else:
				bits[i] = '0'
		offset = int(''.join(bits), 2) + 1
		offset = int('{:011b}'.format(offset)[-9:-1],2)
	cond = '0000'
	instruction = '1101' + cond + '{:08b}'.format(offset)
	hexins = '{:04x}'.format(int(instruction,2))
	hexinsp = list(hexins)
	hexinsp[0:2] = hexins[2:4]
	hexinsp[2:4] = hexins[0:2]
	print(''.join(hexinsp))
elif ( partes[0] == 'bge' ):
	present_ins = int(input('end ins atual'), 16)
	ins = int(input('end instruction alvo'), 16)
	offset = ins - present_ins - 4
	if ( offset < 0 ):
		offset *= -1
		bits = list('{:09b}'.format(offset)[-9:])
		for i in range(len(bits)):
			if ( bits[i] == '0' ):
				bits[i] = '1'
			else:
				bits[i] = '0'
		offset = int(''.join(bits), 2) + 1
		offset = int('{:011b}'.format(offset)[-9:-1],2)
	cond = '1010'
	instruction = '1101' + cond + '{:08b}'.format(offset)
	hexins = '{:04x}'.format(int(instruction,2))
	hexinsp = list(hexins)
	hexinsp[0:2] = hexins[2:4]
	hexinsp[2:4] = hexins[0:2]
	print(''.join(hexinsp))
elif ( partes[0] == 'ldr' ):
	Rt = '{:03b}'.format(int(partes[1],10))
	Rn = '{:03b}'.format(int(partes[2],10))
	instruction = '0110100000' + Rn + Rt
	hexins = '{:04x}'.format(int(instruction,2))
	hexinsp = list(hexins)
	hexinsp[0:2] = hexins[2:4]
	hexinsp[2:4] = hexins[0:2]
	print(''.join(hexinsp))
