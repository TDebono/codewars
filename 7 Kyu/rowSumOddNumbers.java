class RowSumOddNumbers {
    public static int rowSumOddNumbers(int n) {
        
      int sum = 0;
      int start = 1;
      int multiple = 0;
      int end = 0;
      int[] arr = new int[n];
      
      if (n == 1) {
        
        sum = start;
        
      } else if (n > 1) {
        
        for (int k = n; k >= 2; k--) {
          
          multiple += k;
          
        }
        
        end = 1 + multiple * 2;
          
        for (int j = 0; j <= n - 1; j++) {
          
          arr[j] = end - 2 * j;
          
        }
        
        for (int s : arr) {
          sum += s;
        }
        
        
      }
      
      return sum;
      
    }
}