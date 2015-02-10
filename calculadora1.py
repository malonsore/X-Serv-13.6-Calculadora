#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import operator 

operations = {
    'sumar': {'func': operator.add, 'char': '+'},
    'multiplicar': {'func': operator.mul, 'char': '*'},
    'dividir': {'func': operator.div, 'char': '/'},
    'restar': {'func': operator.sub, 'char': '-'}
}
inputs = sys.argv;
_operator=inputs[1]
operando1=inputs[2]
operando2=inputs[3]

if len(inputs) != 4:
    print
    sys.exit("Usage: $ python calculadora.py operation operando1 operando2")

try:
    result=operations[_operator]['func'](int(operando1), int(operando2))
    
    print operando1, operations[_operator]['char'], operando2, '=' , result
    
except KeyError:
    print "Error operation: " + _operator 
except ValueError:
    print "Error Value : Use integer numbers"  
except ZeroDivisionError:
    print "Imposible dividir por cero"
