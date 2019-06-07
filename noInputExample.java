/* My name is _____.
I go to __________. 
I am ____ years old. 
My favorite thing to do is ________. 
My favorite subjects are _______________. 
Rohan and Sai are awesome.
*/
class Main {
    static String name = "Rohan";
    static String school = "Corvallis High School";
    static int age = 15;
    static String favoriteThing = "eating";
    static String subjectOne = "Biology";
    static String subjectTwo = "Computer Science";
    static String subjectThree = "Chemsitry";
    static String description = "BETTER THAN AWESOME!";
  
    static void printStatements(){
      System.out.println("");
      System.out.println("My name is Sai.");
      System.out.println("I go to Corvallis High School");
      System.out.println("I am 15 years old.");
      System.out.println("My favorite thing to do is sleeping.");
      System.out.println("My favtoite subjects are Math, Computer Science, and Chemistry");
      System.out.println("Rohan and Sai are AWESOME!");
    }
  
    static void printTemplate(){
      System.out.println("");
      System.out.println("My name is " + name);
      System.out.println("I go to " + school);
      System.out.println("I am " + age + " years old.");
      System.out.println("My favorite thing to do is " + favoriteThing);
      System.out.println("My favtoite subjects are " + subjectOne + ", " + subjectTwo + ", and " + subjectThree + ".");
      System.out.println("Rohan and Sai are " + description);
    }
  
    public static void main(String[] args){
      printStatements();
      printTemplate();
    }
  }