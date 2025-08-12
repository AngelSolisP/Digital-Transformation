using System;
using System.Windows;
using PrivacyMeter.Desktop.ViewModels;

namespace PrivacyMeter.Desktop
{
    public partial class MainWindow : Window
    {
        private readonly MainViewModel _vm = new();
        public MainWindow()
        {
            InitializeComponent();
            DataContext = _vm;
            Grid.ItemsSource = _vm.Rows;
        }

        private void Start_Click(object sender, RoutedEventArgs e) => _vm.Start();
        private void Stop_Click(object sender, RoutedEventArgs e)  => _vm.Stop();

        protected override void OnClosed(EventArgs e)
        {
            _vm.Stop();
            base.OnClosed(e);
        }
    }
}
