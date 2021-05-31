using System;
using System.Security.Cryptography;
using System.Windows;

namespace rsa_encryption
{
    public partial class GenerateKeyWindow : Window
    {
        private Action refreshAvailableKeys;
        public GenerateKeyWindow(Action refreshAvailableKeys)
        {
            InitializeComponent();
            InitializeComboBox();
            this.refreshAvailableKeys = refreshAvailableKeys;
        }

        private void InitializeComboBox()
        {
            foreach (var type in Enum.GetValues(typeof(KeySize)))
            {
                AvailableSizeOptions.Items.Add(type);
            }

            AvailableSizeOptions.SelectedIndex = 0;
        }
        
        private void GenerateKeysButton_OnClick(object sender, RoutedEventArgs e)
        {
            Console.WriteLine("Generating keys...");
            var rsa = new RSACryptoServiceProvider((int)KeySize.SIZE_2048);
            var publicKey = rsa.ToXmlString(false);
            var privateKey = rsa.ToXmlString(true);

            var fileName = $"{KeyName.Text}_PRIVATE";
            KeyStorage.SaveKeyToFile(fileName, privateKey);
            
            fileName = $"{KeyName.Text}_PUBLIC";
            KeyStorage.SaveKeyToFile(fileName, publicKey);

            refreshAvailableKeys.Invoke();
            Close();
        }
    }
}