using System;
using System.Collections.ObjectModel;
using PrivacyMeter.Desktop.Services;

namespace PrivacyMeter.Desktop.ViewModels
{
    public sealed class MainViewModel
    {
        public sealed class Row
        {
            public DateTime Time { get; init; }
            public string Process { get; init; } = string.Empty;
            public int Pid { get; init; }
            public string Domain { get; init; } = string.Empty;
            public RiskColor Color { get; init; }
            public string Note => Color switch
            { RiskColor.Red => "Tracker", RiskColor.Yellow => "Burst", _ => "OK" };
        }

        private readonly EtwDnsListener _listener = new();
        public ObservableCollection<Row> Rows { get; } = new();

        public void Start()
        {
            _listener.OnDns += HandleDns;
            _listener.Start();
        }

        public void Stop()
        {
            _listener.OnDns -= HandleDns;
            _listener.Stop();
        }

        void HandleDns(DateTime ts, int pid, string host)
        {
            var color = Policy.Evaluate(ts, pid, host);
            var proc = TryName(pid);

            App.Current.Dispatcher.Invoke(() =>
            {
                Rows.Insert(0, new Row { Time = ts, Process = proc, Pid = pid, Domain = host, Color = color });
                if (Rows.Count > 500) Rows.RemoveAt(Rows.Count - 1);
            });
        }

        static string TryName(int pid)
        {
            try { return System.Diagnostics.Process.GetProcessById(pid).ProcessName; }
            catch { return $"pid:{pid}"; }
        }
    }
}
