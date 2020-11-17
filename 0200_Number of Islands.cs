public class Solution {
    public int NumIslands(char[,] grid) {
        int nWidth = grid.GetLength(0);
        int nHeight = grid.GetLength(1);
        
        int nCount = 0;
        for( int i = 0; i < nWidth; i++ ){
            for( int j = 0; j < nHeight; j++ ){
                if( CheckAdjacentAndMark( i, j, grid) ){
                    nCount++;
                }
            }
        }
        
        return nCount;
    }
    
    bool CheckAdjacentAndMark( int x, int y, char[,] Grid ){
        if( IsUnSearchedIsland( x, y, Grid ) == false ){
            return false;
        }
        
        // mark current as searched
        Grid[ x, y ] = 'x';
        
        // check Up
        if( IsUnSearchedIsland( x, y - 1, Grid ) ){
            CheckAdjacentAndMark( x, y - 1, Grid );
        }

        // check Down
        if( IsUnSearchedIsland( x, y + 1, Grid ) ){
            CheckAdjacentAndMark( x, y + 1, Grid );
        }

        // check Left
        if( IsUnSearchedIsland( x - 1, y, Grid ) ){
            CheckAdjacentAndMark( x - 1, y, Grid );
        }

        // check Right
        if( IsUnSearchedIsland( x + 1, y, Grid ) ){
            CheckAdjacentAndMark( x + 1, y, Grid );
        }
        
        return true;
    }
    
    bool IsUnSearchedIsland( int x, int y , char[,] grid ){
        int nWidth = grid.GetLength(0);
        int nHeight = grid.GetLength(1);
        
        // Edge case
        if( x < 0 || x >= nWidth ){
            return false;
        }
        if( y < 0 || y >= nHeight ){
            return false;
        }

        // check is unsearched land
        if( grid[ x, y ] == '1' ){
            return true;
        }
        
        return false;
    }
    
}