using System;
using System.Collections.Generic;

namespace PrivacyMeter.Desktop.Services
{
    public enum RiskColor { Green, Yellow, Red }

    public static class Policy
    {
        static readonly string[] Trackers = new[]
        {
            "doubleclick.net","graph.facebook.com","app-measurement.com",
            "google-analytics.com","googletagmanager.com"
        };

        static readonly Dictionary<int, Queue<DateTime>> Burst = new();
        static readonly TimeSpan Window = TimeSpan.FromSeconds(30);
        const int Threshold = 20; // 20 consultas/30s = Amarillo

        public static RiskColor Evaluate(DateTime ts, int pid, string host)
        {
            if (IsTracker(host)) return RiskColor.Red;

            if (!Burst.TryGetValue(pid, out var q)) { q = new(); Burst[pid] = q; }
            q.Enqueue(ts);
            while (q.Count > 0 && ts - q.Peek() > Window) q.Dequeue();
            if (q.Count >= Threshold) return RiskColor.Yellow;

            return RiskColor.Green;
        }

        static bool IsTracker(string host)
        {
            foreach (var t in Trackers)
                if (host == t || host.EndsWith("." + t)) return true;
            return false;
        }
    }
}
