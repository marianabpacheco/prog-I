public class Main {
    public static void main(String[] args) {
        Empregado empregado = new Empregado("Pedro");
        empregado.setSalario(1200.0);
        empregado.setTurno('n');
        empregado.aumentaSalario(20.00);
        empregado.calculaAdicionalNoturno();
        empregado.imprimeInformacoes();
    }
}