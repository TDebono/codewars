/*
There is an array with some numbers. All numbers are equal except for one. Try to find it!

Kata.findUniq(new double[]{ 1, 1, 1, 2, 1, 1 }); // => 2
Kata.findUniq(new double[]{ 0, 0, 0.55, 0, 0 }); // => 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

*/


import java.util.Arrays;

public class Kata {
    public static double findUniq(double arr[]) {
            
      Arrays.sort(arr);
      double solution;
      
      if (arr[0] < arr[arr.length - 1] && arr[0] < arr[arr.length - 2]) {
        
        solution = arr[0];  
        
      } else {
        
        solution = arr[arr.length - 1];
        
      }
      
      return solution;
      
    }
  
}
