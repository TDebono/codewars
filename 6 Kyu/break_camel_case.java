class Solution {
  
  public static String camelCase(String input) {
    
    String output = "";
    String[] splits = input.split("(?<=[a-z])(?=[A-Z])");
    
    for (String i : splits) {
      
      output += i + " ";
      
    }
    
    return output.substring(0, output.length() - 1);
    
  }
}
