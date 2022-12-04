namespace Cliente.Models
{
    public class Programador : Funcionario
    {
        public Programador(string nome, string cargo, double salario) : base(nome, cargo, salario)
        {
            this.Salario = base.Salario * 1.18;
        }
    }
}