
import getpass
import telnetlib

HOST = "192.168.42.70"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(b"victor\n")

tn.read_until(b"Password: ")
tn.write(b"cisco\n")

tn.read_until(b"R1>")
tn.write(b"enable\n")

tn.read_until(b"Password:")
tn.write(b"cisco\n")

tn.read_until(b"R1#")
tn.write(b"configure terminal\n")

# Crear Loopback 0
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"exit\n")

# Crear Loopback 1
tn.write(b"interface loopback 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"exit\n")

# Configurar OSPF
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"end\n")

tn.read_until(b"R1#")
tn.write(b"exit\n")

tn.close()
