// Services/EtwDnsListener.cs
using System;
using System.Threading.Tasks;
using Microsoft.Diagnostics.Tracing;
using Microsoft.Diagnostics.Tracing.Session;
using Microsoft.Diagnostics.Tracing.Parsers; // <-- IMPORTANTE

namespace PrivacyMeter.Desktop.Services
{
    public sealed class EtwDnsListener : IDisposable
    {
        private TraceEventSession? _session;
        private Task? _task;
        private volatile bool _running;

        // DNS Client provider: {1c95126e-7eea-49a9-a3fe-a378b03ddb4d}
        private static readonly Guid DnsClientProvider = new("1c95126e-7eea-49a9-a3fe-a378b03ddb4d");

        public event Action<DateTime, int, string>? OnDns; // ts, pid, domain

        public void Start()
        {
            if (_running) return;
            _running = true;

            var sessionName = "PM_DnsWpf_" + Guid.NewGuid().ToString("N");
            _session = new TraceEventSession(sessionName) { StopOnDispose = true };

            _task = Task.Run(() =>
            {
                using var source = new ETWTraceEventSource(_session!.SessionName, TraceEventSourceType.Session);

                // Parser dinámico para el proveedor DNS Client
                var parser = new DynamicTraceEventParser(source);
                parser.AddDynamicProvider(DnsClientProvider, TraceEventLevel.Informational);

                parser.All += (TraceEvent e) =>
                {
                    if (!_running) return;

                    // En distintas builds el campo puede llamarse QueryName o HostName
                    var qname = (e.PayloadByName("QueryName") as string)
                                ?? (e.PayloadByName("HostName") as string)
                                ?? string.Empty;
                    if (string.IsNullOrWhiteSpace(qname)) return;

                    OnDns?.Invoke(DateTime.Now, e.ProcessID, qname.ToLowerInvariant());
                };

                _session.EnableProvider(DnsClientProvider);

                try
                {
                    source.Process(); // bloquea hasta Dispose()
                }
                catch
                {
                    // swallow al cerrar la sesión
                }
            });
        }

        public void Stop()
        {
            _running = false;
            _session?.Dispose();
            _task?.Wait(500);
        }

        public void Dispose() => Stop();
    }
}
