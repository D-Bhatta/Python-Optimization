import sys

# basic dict memory
# ob = {'x':1, 'y':2, 'z':3}
# print(sys.getsizeof(ob))
# # memory used is 
# # 240

# using slots

# class Point:
#     __slots__ = 'x', 'y', 'z'

#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

# ob = Point(1,2,3)
# print(sys.getsizeof(ob))
# memory used is 
# 64

# using slots eliminates dict and weakref 

# automating using slots

# import namedlist 

# Point = namedlist.namedlist('Point', ('x', 'y', 'z'))
# ob = Point(1,2,3)
# print(sys.getsizeof(ob))
# # memory used is 
# # 64

# tuples
# basic tuple memory size

# ob = (1,2,3)
# print(sys.getsizeof(ob))

# # memory used is 
# # 72

# using namedtuples

# from collections import namedtuple

# Point  = namedtuple('Point', ('x', 'y', 'z'))
# ob = Point(1,2,3)

# print(ob)
# print(sys.getsizeof(ob))

# # output
# # Point(x=1, y=2, z=3)
# # 72

# mutable tuples that remove cyclic garbage collection flags
# recordclass namedtuple

# import recordclass

# Point = recordclass.recordclass('Point', ('x', 'y', 'z'))
# ob = Point(1,2,3)

# print(ob)
# print(sys.getsizeof(ob))
# # output
# # Point(x=1, y=2, z=3)
# # 48

# recordclass data class
# using function

# import recordclass


# Point = recordclass.dataclass.make_dataclass('Point', ('x', 'y', 'z'))
# ob = Point(1,2,3)

# print(ob)
# print(sys.getsizeof(ob))
# # output
# # Point(x=1, y=2, z=3)
# # 40

# recordclass dataobject
# using inheritance

# from recordclass import dataobject

# class Point(dataobject):
#     x:int
#     y:int
#     z:int

# ob = Point(1,2,3)

# print(ob)
# print(sys.getsizeof(ob))
# # output
# # Point(x=1, y=2, z=3)
# # 40

# using numpy

# import numpy

# Point = numpy.dtype([('x', numpy.int32), ('y', numpy.int32), ('z', numpy.int32)])

# points = numpy.zeros(10, dtype=Point)

# print(points)
# print(sys.getsizeof(points))
# # output
# # [(0, 0, 0) (0, 0, 0) (0, 0, 0) (0, 0, 0) (0, 0, 0) (0, 0, 0) (0, 0, 0)
# #  (0, 0, 0) (0, 0, 0) (0, 0, 0)]
# # 216

