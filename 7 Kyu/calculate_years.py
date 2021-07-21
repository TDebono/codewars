public class Money {
  public static int calculateYears(double principal, double interest,  double tax, double desired) {
    
    int num_years = 0;
    
    if (principal == desired) {
      num_years = 0;
    }
    
    else if (principal < desired) {
      
      while (principal <= desired) {
      
      double interest_amount = principal * interest;
      double tax_amount = interest_amount * tax;
      
      principal *= (1 + interest);
      principal -= tax_amount;
      
      num_years++;
      
      }
    }
    
    return num_years;
    
  }
}