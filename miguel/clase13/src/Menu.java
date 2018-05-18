import java.util.Scanner;

public class Menu {

    public Menu() {
    }
    
    public void menu() {
	Scanner sc = new Scanner(System.in);
	Calculadora calc = new Calculadora();
	double a;
	double b;
	double resultado;
	while (true) {
	  System.out.println("Calculadora");
	  System.out.println("Dame a: ");
	  a = Double.parseDouble(sc.nextLine());
	  System.out.println("Dame b: ");
	  b = Double.parseDouble(sc.nextLine());
	  System.out.println("Dame una operación");
	  String operacion = sc.nextLine();
	  switch(operacion) {
	      case "+":
		  resultado = calc.suma(a, b);
		  System.out.println(String.format("La suma de %.2f, con %.2f, es: %.2f", a, b, resultado));
		  break;
	      case "-":
		  resultado = calc.resta(a, b);
		  System.out.println(String.format("La resta de %.2f, con %.2f, es: %.2f", a, b, resultado));
		  break;
	      case "*":
		  resultado = calc.multiplicacion(a, b);
		  System.out.println(String.format("La multiplicacion de %.2f, con %.2f, es: %.2f", a, b, resultado));
		  break;
	      case "/":
		  resultado = calc.division(a, b);
		  System.out.println(String.format("La division de %.2f, con %.2f, es: %.2f", a, b, resultado));
		  break;
	      default:
		  System.out.println("Operacion no permitida");
	  }
	  System.out.println("¿Desea terminar el programa? (si/no)");
	  String continua = sc.nextLine();
	  if (continua.equals("si")) {
	    break;
	  }
	}
    }

}