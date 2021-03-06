# Copyright (c) 2011-2013, ImageCat Inc.
#
# This program is free software: you can redistribute it and/or modify 
# it under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License 
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#


def Enum(*names):
    """
    create enumeration from list of strings 
    Created by Zoran Isailovski on ActiveState Recipe
    http://code.activestate.com/recipes/413486/    
    """
    ##assert names, "Empty enums are not supported" # <- Don't like empty enums? Uncomment!
    
    class EnumClass(object):
        """ Enumeration class """
        __slots__ = names
        def __iter__(self):        return iter(constants)
        def __len__(self):         return len(constants)
        def __getitem__(self, i):  return constants[i]
        def __repr__(self):        return 'Enum' + str(names)
        def __str__(self):         return 'enum ' + str(constants)

    class EnumValue(object):
        __slots__ = ('__value')
        def __init__(self, value): self.__value = value
        Value = property(lambda self: self.__value)
        EnumType = property(lambda self: EnumType)
        def __hash__(self):        return hash(self.__value)
        def __cmp__(self, other):
            # C fans might want to remove the following assertion
            # to make all enums comparable by ordinal value {;))
            assert self.EnumType is other.EnumType, "Only values from the same enum are comparable"                        
            return cmp(self.__value, other.__value)            
        def __invert__(self):      return constants[maximum - self.__value]
        def __nonzero__(self):     return bool(self.__value)
        def __repr__(self):        return str(names[self.__value])        

    maximum = len(names) - 1
    constants = [None] * len(names)
    for i, each in enumerate(names):
        val = EnumValue(i)
        setattr(EnumClass, each, val)
        constants[i] = val
    constants = tuple(constants)
    EnumType = EnumClass()
    return EnumType

def makeEnum(enum, value):
    if hasattr(enum, value):
        return getattr(enum, value)
    else:
        return None
