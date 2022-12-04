namespace Cliente.Models
{
    public class Operador : Funcionario
    {
        public Operador(string nome, String cargo, double salario) : base(nome, cargo, salario)
        {
            this.Salario = base.Salario * 1.2;
        }
    }
}