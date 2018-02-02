public class Solution {
    public int[,] UpdateMatrix(int[,] matrix) {
        int nCol = matrix.GetLength(0);
        int nRow = matrix.GetLength(1);
        
        int[,] OutputArray = new int[ nCol, nRow ];
        
        // init OutputArray
        for( int i = 0; i < nCol; i++ ){
            for( int j = 0; j< nRow; j++ ){
                if( matrix[i,j] == 0 ){
                    OutputArray[i,j] = 0;
                }
                else{
                    OutputArray[i,j] = -1;
                }
            }
        }
        
        // fill matrix form 1 => max number
        int nStep = 0;
        while( isFinish( OutputArray ) == false ){
            ProcessMatrix( nStep, OutputArray );
            nStep++;
        }
        
        return OutputArray;
    }
    
    bool isFinish( int[,] matrix ){
        int nCol = matrix.GetLength(0);
        int nRow = matrix.GetLength(1);
        for( int i = 0; i < nCol; i++ ){
            for( int j = 0; j< nRow; j++ ){
                if( matrix[i,j] == -1 ){
                    return false;
                }
            }
        }
        return true;
    }

    void ProcessMatrix( int nStep, int[,] matrix ){
        int nCol = matrix.GetLength(0);
        int nRow = matrix.GetLength(1);
        
        for( int i = 0; i < nCol; i++ ){
            for( int j = 0; j< nRow; j++ ){
                if( matrix[i,j] != nStep ){
                    continue;    
                }
                
                // left adjacent
                if( i > 0 ){
                    if( matrix[i-1,j] == -1 ){
                        matrix[i-1,j] = nStep + 1;
                    }
                }
                
                // right adjacent
                if( i < nCol - 1 ){
                    if( matrix[i+1,j] == -1 ){
                        matrix[i+1,j] = nStep + 1;
                    }
                }
                
                // top adjacent
                if( j > 0 ){
                    if( matrix[i,j-1] == -1 ){
                        matrix[i,j-1] = nStep + 1;
                    }
                }
                
                // buttom adjacent
                if( j < nRow - 1 ){
                    if( matrix[i,j+1] == -1 ){
                        matrix[i,j+1] = nStep + 1;
                    }
                }
            }
        }
        
    }
}