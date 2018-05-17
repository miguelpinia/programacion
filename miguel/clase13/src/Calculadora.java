public class Calculadora {

    public Calculadora() {
    }

    public double suma(double a, double b) {
        double resultado = a + b;
        return resultado;
    }

    public double resta(double a, double b) {
        double resultado = a - b;
        return resultado;
    }

    public double multiplicacion(double a, double b) {
        double resultado = a * b;
        return resultado;
    }

    public double division(double a, double b) {
        if (b != 0) {
            double resultado = a / b;
            return resultado;
        }
        return 0;
    }
}
