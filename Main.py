'''
Created on 20 ago. 2019

@author: pabli
'''
import struct
import ctypes

"""
typedef struct {
    unsigned long dni;       => 4 bytes     => L
    char nomyap[100];        => 100 bytes   => s
    float saldo;             => 4 bytes     => f   
    char sexo;               => 1 byte      => c 
    char estado;             => 1 byte      => c
}t_cliente;

Total 110, en realidad es 112 por padding
"""


if __name__ == '__main__':
    pass
    