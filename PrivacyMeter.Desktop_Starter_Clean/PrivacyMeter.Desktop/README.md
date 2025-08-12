# Privacy Meter — Desktop MVP (WPF, .NET 8)

UI mínima para ver consultas DNS por proceso en Windows y marcar:
- **RED**: dominio rastreador conocido
- **YELLOW**: ráfaga de consultas del mismo proceso
- **GREEN**: normal

## Requisitos
- Windows 10/11
- .NET 8 SDK
- Visual Studio Code (si no ves eventos, ejecuta VS Code como Administrador)

## Ejecutar
```bash
dotnet restore
dotnet run
```
En la ventana, pulsa **Start** y navega en el navegador. Si un dominio coincide con la lista interna, verás **RED**.
