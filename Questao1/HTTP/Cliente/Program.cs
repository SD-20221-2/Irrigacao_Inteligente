using Cliente.Models;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.Urls.Add("http://localhost:3000");

app.MapGet("/{Nome}/{Cargo}/{Salario}", (string Nome, string Cargo, int Salario) =>
{
    if (Cargo == "Programador")
    {
        Programador Programador = new Programador(Nome, Cargo, Salario);

        return Results.Ok(Programador);
    }
    if (Cargo == "Operador")
    {
        Operador Operador = new Operador(Nome, Cargo, Salario);

        return Results.Ok(Operador);
    }


    return Results.BadRequest();
});

app.Run();