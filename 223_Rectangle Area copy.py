class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
            :type A: int
            :type B: int
            :type C: int
            :type D: int
            :type E: int
            :type F: int
            :type G: int
            :type H: int
            :rtype: int
            """
        
        nRec1Area = ( C - A ) * ( D - B )
        nRec2Area = ( G - E ) * ( H - F )
        NotOverlay = ( A > G ) or ( E > C ) or ( F > D ) or ( B > H )
        
        if NotOverlay :
            return nRec1Area + nRec2Area
        else :
            xArray = [ A, C, E, G ]
            yArray = [ B, D, F, H ]
            xArray.sort();
            yArray.sort();
            nRecOverlap = ( xArray[2] - xArray[1] ) * ( yArray[2] - yArray[1] )
            
            return nRec1Area + nRec2Area - nRecOverlap
