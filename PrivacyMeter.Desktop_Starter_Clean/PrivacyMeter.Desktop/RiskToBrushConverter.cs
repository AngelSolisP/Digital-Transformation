using System;
using System.Globalization;
using System.Windows.Data;
using System.Windows.Media;
using PrivacyMeter.Desktop.Services;

namespace PrivacyMeter.Desktop
{
    public sealed class RiskToBrush : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            return (RiskColor)value switch
            {
                RiskColor.Red => Brushes.IndianRed,
                RiskColor.Yellow => Brushes.Goldenrod,
                _ => Brushes.SeaGreen
            };
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
            => Binding.DoNothing;
    }
}
