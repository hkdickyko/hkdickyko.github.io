from math import sin, cos, asin, atan, atan2, sqrt, pi, degrees
import array

try:
    import utime as time
except ImportError:
    import time

class D3D:

  def __init__(self, timediff=None):
    pass

  def getAngleXYZ(self, acceleration, magnetic):
    AccX, AccY, AccZ = acceleration
    magX, magY, magZ = magnetic
    
    A_norm = float(sqrt(AccX * AccX + AccY * AccY + AccZ * AccZ))
    pitch = float(asin(-AccX/A_norm)) 
    roll = float(asin(AccY/(cos(pitch)*A_norm))) 
    yaw = float(0.0)
    
    M_norm = float(sqrt(magX * magX + magY * magY + magZ * magZ))
    m_x = float(magX / M_norm)
    m_y = float(magY / M_norm)
    m_z = float(magZ / M_norm)

    M_y = float((m_y*cos(roll))) + float((m_x*sin(roll)*sin(pitch))) - float((m_z*sin(roll)*cos(pitch)))
    M_x = float((m_x*cos(pitch)) + (m_z*sin(pitch)));
    M_z = float((-m_x*cos(roll)*sin(pitch))) + float((m_y*sin(roll))) + float((m_z*cos(roll)*cos(pitch)))

    accurate = float(sqrt(M_x*M_x + M_y*M_y + M_z*M_z))

    if M_y>=0.0:
       yaw = float(atan2(M_y, M_x))
       
    if M_y<0.0:
      yaw = 2*pi+float(atan2(M_y, M_x))
    
    return (roll, pitch, yaw, accurate)

  def getDegrees(self, xyz):
     x, y, z = xyz
     return degrees(x), degrees(y), degrees(z)

class Kalman:
    
  def __init__(self, timediff=None):
    self.q_angle = 0.001
    self.q_bias = 0.003
    self.R = 0.03
    self.angle = 0.0
    self.bias = 0.0
    self.rate = 0.0
    self.P = array.array('d', [0.0, 0.0, 0.0, 0.0])
    self.P[0] = 0.0
    self.P[1] = 0.0
    self.P[2] = 0.0
    self.P[3] = 0.0
    
  def getAngle(self, newAngle, newRate, dt):
    self.rate = float(newRate - self.bias)
    self.angle = self.angle + float(dt*self.rate)
    self.P[0] = self.P[0] + float(dt*self.P[3] - self.P[1] - self.P[2] + self.q_angle)
    self.P[1] = self.P[1] - float(dt*self.P[3])
    self.P[2] = self.P[2] - float(dt*self.P[3])
    self.P[3] = self.P[3] + float(self.q_bias*dt)
    y = float(newAngle-self.angle)
    S = self.P[0] + self.R
    K = array.array('f', [0.0, 0.0])
    K[0] = float(self.P[0]/S)
    K[1] = float(self.P[2]/S)
    self.angle = self.angle + float(K[0]*y)
    self.bias = self.bias + float(K[1]*y)
    P00_temp = self.P[0]
    P01_temp = self.P[1]
    self.P[0] = self.P[0] - float(K[0]*P00_temp)
    self.P[1] = self.P[1] - float(K[0]*P01_temp)
    self.P[2] = self.P[2] - float(K[1]*P00_temp)
    self.P[3] = self.P[3] - float(K[1]*P01_temp)
    return self.angle

  def setAngle(self, angle):
    self.angle = angle
    
  def getRate(self):
      return self.rate
      
  def setQAngle(self, angle):
    self.q_angle = angle
      
  def setQBias(self, bias):
    self.q_bias = bias
    
  def setR(self, R):
    self.R = R

  def getQAngle(self):
    return self.q_angle
      
  def getQBias(self):
    return self.q_bias
    
  def getR(self):
    return self.R
