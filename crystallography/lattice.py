#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Philippe Pinard (philippe.pinard@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2008 Philippe Pinard"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = ""
__svnDate__ = ""
__svnId__ = ""

# Standard library modules.
from math import sin, cos, pi

# Third party modules.

# Local modules.
from EBSDTools.mathTools.mathExtras import _acos, h
import EBSDTools.crystallography.reflectors as reflectors

class Lattice:
  def __init__(self, a, b, c, alpha, beta, gamma, atoms=None, reflectorsMaxIndice=2):
    """
      
      Inputs:
        a, b, c: lattice parameter (in $\AA$)
        alpha, beta, gamma: lattice angle in rad
    """
    
    self.a = float(a)
    self.b = float(b)
    self.c =  float(c)
    self.alpha =  float(alpha)
    self.beta =  float(beta)
    self.gamma =  float(gamma)
    
    self.__calculateReciprocalAngle()
    self.__calculateLatticeVolume()
    self.__calculateReciprocalBasis()
    self.__calculateReciprocalVolume()
    
    self.atoms = atoms
    
    if atoms != None:
      self.reflectors = reflectors.Reflectors(self, reflectorsMaxIndice)
    else:
      self.reflectors = None
  
  def __calculateReciprocalAngle(self):
    self.alpha_ = _acos((cos(self.beta)*cos(self.gamma) - cos(self.alpha)) / (sin(self.beta)*sin(self.gamma)))
    self.beta_ = _acos((cos(self.alpha)*cos(self.gamma) - cos(self.beta)) / (sin(self.alpha)*sin(self.gamma)))
    self.gamma_ = _acos((cos(self.alpha)*cos(self.beta) - cos(self.gamma)) / (sin(self.alpha)*sin(self.beta)))
  
  def __calculateLatticeVolume(self):
    self.volume = self.a*self.b*self.c*sin(self.alpha_)*sin(self.beta)*sin(self.gamma)
  
  def __calculateReciprocalBasis(self):
    self.a_ = self.b*self.c*sin(self.alpha) / self.volume
    self.b_ = self.a*self.c*sin(self.beta) / self.volume
    self.c_ = self.a*self.b*sin(self.gamma) / self.volume
  
  def __calculateReciprocalVolume(self):
    self.volume_ = 1.0 / self.volume
  
  def __call__(self):
    return {'a': self.a
            , 'b': self.b
            , 'c': self.c
            , 'a*': self.a_
            , 'b*': self.b_
            , 'c*': self.c_
            , 'alpha': self.alpha
            , 'beta': self.beta
            , 'gamma': self.gamma
            , 'alpha*': self.alpha_
            , 'beta*': self.beta_
            , 'gamma*': self.gamma_
            , 'V': self.volume
            , 'V*': self.volume_
            }
  def getReflectors(self):
    return self.reflectors
  
  def getAtomsPositions(self):
    return self.atoms.keys()

if __name__ == '__main__':
  pass
  