public class Printer {
    
    public static String printerError(String s) {

      int num_bad = 0;
      
      for (int i = 0; i < s.length(); i++) {
        
        if (s.charAt(i) > 'm') {
          
          num_bad++;
          
        }
        
      }
      
      return num_bad + "/" + s.length();
      
    }
}
