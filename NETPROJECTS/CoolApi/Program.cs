using CoolApi;
using Microsoft.OpenApi.Models;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    options.SwaggerDoc("v1", new OpenApiInfo
    {
        Version = "v1",
        Title = "Lavender API",
        Description = "Lavender's  API items",
        TermsOfService = new Uri("https://lavender.com/terms"),
        Contact = new OpenApiContact
        {
            Name = "Lavender's Contact",
            Url = new Uri("https://lavender.com/contact")
        },
        License = new OpenApiLicense
        {
            Name = "Lavender's License",
            Url = new Uri("https://lavender.com/license")
        }
    });
});
builder.Services.AddCors(p => p.AddPolicy("corsapp", builder =>
{
    builder.WithOrigins("*").AllowAnyMethod().AllowAnyHeader();
}));
var app = builder.Build();

app.MapGet("/user/details", () => new Student {Age = 40, Name = "Ven"}).WithTags("Lavender");
app.MapGet("/user/{age}",(int age) => new Student { Age = age, Name = "Ven" }).WithTags("Lavender");
app.MapPost("/user/student", (Student Winnie) => Winnie).WithTags("Lavender");
app.UseSwagger();
app.UseSwaggerUI();
app.UseCors("corsapp");
app.Run();
