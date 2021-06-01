using System;
using System.IO;
using System.Security.Cryptography;
using System.Windows;

namespace rsa_encryption
{
    public partial class KeyInfo : Window
    {
        public KeyInfo()
        {
            InitializeComponent();
            InitializeData();
        }

        private void InitializeData()
        {
            var keyPath = KeyStorage.Instance().GetKeyPath();
            KeyNameText.Text = "Nazwa: " + Path.GetFileName(keyPath);
            
            KeyCreationDateText.Text = "Stworzono: " + new FileInfo(keyPath).CreationTime.ToString();

            var rsa = new RSACryptoServiceProvider();
            rsa.FromXmlString(File.ReadAllText(keyPath));
            KeySizeText.Text = "Rozmiar: " + rsa.KeySize.ToString();
        }

        private void CopyButton_OnClick(object sender, RoutedEventArgs e)
        {
            var keyPath = KeyStorage.Instance().GetKeyPath();
            Clipboard.SetText(File.ReadAllText(keyPath));
            Close();
        }
    }
}