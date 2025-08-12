using Microsoft.Diagnostics.Tracing;
using Microsoft.Diagnostics.Tracing.Session;

static class Program
{
    // GUID del proveedor DNS Client
    static readonly Guid DnsClientProvider = new("1c95126e-7eea-49a9-a3fe-a378b03ddb4d");

    // Lista corta de dominios de rastreo (empieza simple)
    static readonly string[] Trackers = new[]
    {
        "doubleclick.net",
        "graph.facebook.com",
        "app-measurement.com",
        "googletagmanager.com",
        "google-analytics.com"
    };

    static bool IsTracker(string host)
    {
        host = host.ToLowerInvariant();
        foreach (var t in Trackers)
        {
            if (host == t) return true;
            if (host.EndsWith("." + t)) return true;
        }
        return false;
    }

    static void Main()
    {
        Console.WriteLine("PrivacyMeter Console — DNS watcher (Ctrl+C para salir)");
        var sessionName = "PM_DnsSession_" + Guid.NewGuid().ToString("N");

        using var session = new TraceEventSession(sessionName);
        session.StopOnDispose = true;

        using var source = new ETWTraceEventSource(session.SessionName, TraceEventSourceType.Session);
        var parser = new DynamicTraceEventParser(source);
        parser.AddDynamicProvider(DnsClientProvider, TraceEventLevel.Informational);

        parser.All += (TraceEvent e) =>
        {
            // En distintas builds el campo puede ser QueryName o HostName
            var qname = (e.PayloadByName("QueryName") as string)
                        ?? (e.PayloadByName("HostName") as string)
                        ?? "";
            if (string.IsNullOrWhiteSpace(qname)) return;

            var pid = e.ProcessID;
            string color = IsTracker(qname) ? "RED" : "GREEN";
            if (color == "RED")
                Console.ForegroundColor = ConsoleColor.Red;
            else
                Console.ForegroundColor = ConsoleColor.Green;

            Console.WriteLine($"{DateTime.Now:HH:mm:ss} [{color}] pid:{pid} {qname}");
            Console.ResetColor();
        };

        session.EnableProvider(DnsClientProvider);
        // Nota: puede requerir ejecutar la terminal como Administrador en algunos equipos
        source.Process();
    }
}
