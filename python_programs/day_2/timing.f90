  INTEGER, PARAMETER :: N = 256
  REAL*8, DIMENSION(N,N)::A, B, C
  ! Timing
  INTEGER:: T1, T2, RATE
  ! Initialize
  A = 1.0
  B = 1.0
  !
  CALL SYSTEM_CLOCK(COUNT_RATE=RATE)
  CALL SYSTEM_CLOCK(COUNT=T1)
  C = MATMUL(A,B)
  CALL SYSTEM_CLOCK(COUNT=T2)
  PRINT '(A,F6.2)', 'MATMUL timing', DBLE(T2-T1)/RATE
  END
