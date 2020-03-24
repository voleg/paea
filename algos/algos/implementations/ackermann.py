import logging

log = logging.getLogger(__name__)



def ackerman_naive(m,n):
     if m == 0:
          return (n + 1)
     elif n == 0:
          return ackerman_naive(m - 1, 1)
     else:
          return ackerman_naive(m - 1, ackerman_naive(m, n - 1))
