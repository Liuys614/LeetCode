public class Solution {
    public void SetZeroes(int[,] matrix) {
        // find first 0 position
        int nCol = -1;
        int nRow = -1;
        for( int i = 0; i < matrix.GetLength(0); i++ ){
            if( nCol!= -1 && nRow != -1 ) break;
            for( int j = 0; j < matrix.GetLength(1); j++ ){
                if( matrix[i,j] == 0 ){
                    nCol = i;
                    nRow = j;
                    break;
                }
            }
        }
        
        // Return while no 0 in matrix
        if( nCol== -1 && nRow == -1 ) return;
        
        // mark 0 position information to nCol and nRow
        for( int i = 0; i < matrix.GetLength(0); i++ ){
            if( i == nCol ){
                    continue;
            }
            for( int j = 0; j < matrix.GetLength(1); j++ ){
                if( j == nRow ){
                    continue;
                }
                if( matrix[i,j] == 0 ){
                    matrix[nCol,j] = 0;
                    matrix[i,nRow] = 0;
                }
            }
        }
        
        // mark 0 ( without nCol nRow )
        for( int i = 0; i < matrix.GetLength(0); i++ ){
            if( i == nCol ){
                    continue;
            }
            for( int j = 0; j < matrix.GetLength(1); j++ ){
                if( j == nRow ){
                    continue;
                }
                if( matrix[nCol,j] == 0 || matrix[i,nRow] == 0 ){
                    matrix[i,j] = 0;
                }
            }
        }
        
        // mark 0 on nCol nRow
        for( int i = 0; i < matrix.GetLength(0); i++ ){
            matrix[i,nRow] = 0;
        }
        for( int j = 0; j < matrix.GetLength(1); j++ ){
            matrix[nCol,j] = 0;
        }
    }
}
