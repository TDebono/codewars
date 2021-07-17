public class Kata {
  public static boolean betterThanAverage(int[] classPoints, int yourPoints) {
    
    int sum = 0;
    
    for (int num : classPoints) {
      
      sum += num;
      
    }
      
    return yourPoints > (sum / classPoints.length);
    
  }
}
