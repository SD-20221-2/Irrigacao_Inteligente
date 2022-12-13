namespace Cliente.Models
{
    public class Funcionario
    {
        public Funcionario(string nome, string cargo, double salario)
        {
            Nome = nome;
            Cargo = cargo;
            Salario = salario;
        }

        public string Nome { get; set; }
        public string Cargo { get; set; }
        public double Salario { get; set; }
    }
}