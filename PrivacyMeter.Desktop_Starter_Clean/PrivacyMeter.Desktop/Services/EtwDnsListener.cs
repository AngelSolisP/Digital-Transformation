// Services/EtwDnsListener.cs
using System;
using System.Threading.Tasks;
using Microsoft.Diagnostics.Tracing;
using Microsoft.Diagnostics.Tracing.Session;
using Microsoft.Diagnostics.Tracing.Parsers; // para source.Dynamic

namespace PrivacyMeter.Desktop.Services
{
    public sealed class EtwDnsListener : IDisposable
    {
        private TraceEventSession? _session;
        private Task? _task;
        private volatile bool _running;

        // DNS Client provider: {1c95126e-7eea-49a9-a3fe-a378b03ddb4d}
        private static readonly Guid DnsClientProvider = new("1c95126e-7eea-49a9-a3fe-a378b03ddb4d");

        public event Action<DateTime,int,string>? OnDns; // ts, pid, domain

        public void Start()
        {
            if (_running) return;
            _running = true;

            var sessionName = "PM_DnsWpf_" + Guid.NewGuid().ToString("N");
            _session = new TraceEventSession(sessionName) { StopOnDispose = true };

            _task = Task.Run(() =>
            {
                using var source = new ETWTraceEventSource(_session!.SessionName, TraceEventSourceType.Session);

                // Parser dinámico: escucha TODO y filtramos en el handler
                source.Dynamic.All += (TraceEvent e) =>
                {
                    if (!_running) return;

                    // En distintas builds puede ser QueryName o HostName
                    var qname = (e.PayloadByName("QueryName") as string)
                                ?? (e.PayloadByName("HostName") as string)
                                ?? string.Empty;
                    if (string.IsNullOrWhiteSpace(qname)) return;

                    OnDns?.Invoke(DateTime.Now, e.ProcessID, qname.ToLowerInvariant());
                };

                // Habilita el proveedor DNS Client (nivel Informational, sin keywords específicos)
                _session.EnableProvider(DnsClientProvider, TraceEventLevel.Informational, 0);

                try { source.Process(); } catch { /* se cierra al Dispose */ }
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
