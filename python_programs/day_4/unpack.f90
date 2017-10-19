SUBROUTINE UNPACK(N, SP, SQ)
  DOUBLE PRECISION SP(*), SQ(N, N)
  Cf2py intent(in) n, sp
  Cf2py intent(out) sq
  IJ = 1
  DO I=1, N
     DO J=1, I-1
        SQ(I, J) = SP(IJ)
        SQ(J, I) = SP(IJ)
        IJ = IJ + 1
     END DO
     SQ(I, I) = SP(IJ)
     IJ = IJ + 1
  END DO
  RETURN
END SUBROUTINE UNPACK
