## Sistemi di numerazione
```
312 (base 10)

   3       1       2
   2       1       0
10^2    10^1    10^0
 100      10       1

312 (base 10) = 2 * 1 + 1 * 10 + 3 * 100 = 2 + 10 + 300 = 312 (base 10)
```
```
312 (base 16)

   3       1       2    (base 16)
   2       1       0
16^2    16^1    16^0
 256      16       1

312 (base 16) = 3 * 256 + 1 * 16 + 1 * 2 = 768 + 16 + 2 = 786 (base 10)
```
```
1011 (base 2)

1     0     1     1
3     2     1     0
2^3   2^2   2^1   2^0
8     4     2     1
1011 (base 2) = 1*8 + 0*4 + 1*2 + 1*1 = 8 + 0 + 2 + 1 = 11 (base 10)
```


## Conversione da base 10 a base x
```
18 (base 10) -> base 2

18 / 2 = 9 resto 0
9  / 2 = 4 resto 1
4  / 2 = 2 resto 0
2  / 2 = 1 resto 0
1  / 2 = 0 resto 1     quoziente * divisore + resto = dividendo => 0 * 2 + 1 = 1

18 (base 10) -> 10010 (base 2)
```

```
18 (base 10) -> base 16

18 / 16 = 1 resto 2
1  / 16 = 0 resto 1

18 (base 10) -> 12 (base 16)
```
```
180 (base 10) -> base 16

180 / 16 = 11 resto 4
11  / 16 =  0 resto 11

180 (base 10) -> B4 (base 16)
```

## Calcoli indirizzi IP
```
ip:         
ip binario: 
maschera:    => 

network:        => 
broadcast:   => 

gateway1:    => 
gateway2:    => 

numero massimo host o sottoreti:
2^(32 - cidr) - 2 = 

network: xxx ottetti
host: xxx ottetti
```
```
ip:         192.168.25.30/25
ip binario: 11000000.10101000.00011001.0 0011110
maschera:   11111111.11111111.11111111.1 0000000 => 255.255.255.128

network:       11000000.10101000.00011001.0 0000000 => 192.168.25.0
broadcast:  11000000.10101000.00011001.0 1111111 => 192.168.25.127

gateway1:   11000000.10101000.00011001.0 0000001 => 192.168.25.1
gateway2:   11000000.10101000.00011001.0 1111110 => 192.168.25.126

numero massimo host o sottoreti:
2^(32 - cidr) - 2 = 2^(32 - 25) - 2 = 2^7 - 2 = 128 - 2 = 126

network: 3.125 ottetti
host: 0.875 ottetti
```

