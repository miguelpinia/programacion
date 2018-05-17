import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Calculadora miCalcu = new Calculadora();
        Scanner sc = new Scanner(System.in);
        double a = 0;
        double b = 0;
        System.out.println("Mi calculadora");
        System.out.println("Dame a");
        a = Double.parseDouble(sc.nextLine());
        System.out.println("Dame b");
        b = Double.parseDouble(sc.nextLine());
        System.out.println("La suma es: "
                           + miCalcu.suma(a, b));
        System.out.println("La resta es: "
                           + miCalcu.resta(a, b));
        System.out.println("La multiplicación es: "
                           + miCalcu.multiplicacion(a, b));
        System.out.println("La división es: "
                           + miCalcu.division(a, b));
    }
}
