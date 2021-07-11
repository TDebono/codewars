public class XO {
  
  public static boolean getXO (String str) {
    
    str.toLowerCase();
    
    int numX = 0;
    int numO = 0;
    
    for (int i = 0; i < str.length(); i++) {
      
      char c = str.charAt(i);
      
      if (c == 'x') {
        numX++;
      } 
      else if (c == 'o') {
        numO++;
      }
      
    }
    
    return numX == numO;
    
  }
}
