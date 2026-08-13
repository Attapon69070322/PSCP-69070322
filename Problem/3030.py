"""Saitama"""
import math as m
push_up = int(input())
sit_up = int(input())
look_up = int(input())
run = int(input())
pushday = int(input())
sitday = int(input())
runday = int(input())
lookday = int(input())

p = push_up / pushday
s = sit_up / sitday
l = look_up / lookday
r = run / runday

k = m.ceil(max(p ,s ,l ,r))
print(k)
